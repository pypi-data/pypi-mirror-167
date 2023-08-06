"""This module implements the Aug class."""
from uuid import UUID
from random import getrandbits

from rook.logger import logger
from rook.processor.error import Error
from rook.processor.namespaces.container_namespace import ContainerNamespace
from rook.processor.namespaces.stack_namespace import StackNamespace
from rook.processor.namespaces.python_utils_namespace import PythonUtilsNamespace
from rook.processor.namespaces.trace_namespace import TraceNamespace
from rook.processor.namespaces.process_state_namespace import ProcessStateNamespace
from rook.user_warnings import UserWarnings

from rook.exceptions import RookRuleMaxExecutionTimeReached, RookRuleRateLimited, RookGlobalRuleRateLimited
from rook.augs.aug_rate_limiter import AugRateLimiter
from rook.config import RateLimiter
import rook.utils as utils


class Aug(object):
    """The Aug class is the skeleton that holds together all the components that define a modification to the application.

    This class brings together the following elements:
    - location - specifies when to run the modification.
    - condition - specifies an optional filter as to when to run the modification.
    - action - specifies the modification to preform.
    """

    TRACE_NAMESPACE_INSTANCE = TraceNamespace()
    UTILS_NAMESPACE_INSTANCE = PythonUtilsNamespace()
    STATE_NAMESPACE_INSTANCE = ProcessStateNamespace()

    def __init__(self, aug_id, condition, action, global_rate_limit=AugRateLimiter(None, None),
                 max_aug_execution_time_ns=0, rate_limits_ns=None):
        """Build an Aug object from the individual elements."""
        self.aug_id = aug_id
        self._condition = condition
        self._action = action
        self._max_aug_time = max_aug_execution_time_ns
        self._enabled = True
        self._executed = False
        self._has_been_rate_limited = False
        self._global_rate_limiter = global_rate_limit

        if rate_limits_ns:
            self._rate_limiter = AugRateLimiter(rate_limits_ns[0], rate_limits_ns[1])
        else:
            self._rate_limiter = AugRateLimiter(None, None)

    def execute(self, frame_namespace, extracted, output):
        """Called by the trigger service to run the extractor, condition and action."""
        if not self._enabled:
            return

        if output.is_user_messages_queue_full():
            output.send_output_queue_full_warning(self.aug_id)
            return

        now_ns = utils.get_most_accurate_time_stamp_nano_seconds()
        rate_limits_keys = self._allow(now_ns)

        if self._enforce_rate_limits(rate_limits_keys):
            return

        try:
            namespace = ContainerNamespace({
                'frame': frame_namespace,
                'stack': StackNamespace(frame_namespace),
                'extracted': ContainerNamespace(extracted),
                'store': ContainerNamespace(),
                'utils': Aug.UTILS_NAMESPACE_INSTANCE,
                'trace': Aug.TRACE_NAMESPACE_INSTANCE,
                'state': Aug.STATE_NAMESPACE_INSTANCE,
            })

            if not self._condition or self._condition.evaluate(namespace, extracted):
                msg_id = UUID(int=getrandbits(128), version=4).hex

                if self._executed:
                    logger.debug("Executing aug-\t%s (msg ID %s)", self.aug_id, msg_id)
                else:
                    logger.info("Executing aug for the first time-\t%s (msg ID %s)", self.aug_id, msg_id)
                    self._executed = True

                self._action.execute(self.aug_id, msg_id, namespace, output)
        finally:
            duration = max(utils.get_most_accurate_time_stamp_nano_seconds() - now_ns, RateLimiter.MIN_RATE_LIMIT_VALUE_NS)

            if 0 < self._max_aug_time < duration:
                UserWarnings.set_error(Error(exc=RookRuleMaxExecutionTimeReached()))
                self._enabled = False

            self._record_rate_limits(rate_limits_keys, duration)

    def _allow(self, now_ns):
        return self._rate_limiter.allow(now_ns), self._global_rate_limiter.allow(now_ns)

    def _enforce_rate_limits(self, rate_limits_keys):
        if rate_limits_keys[0] is None:
            if not self._has_been_rate_limited:
                UserWarnings.send_warning(Error(exc=RookRuleRateLimited()))
                self._has_been_rate_limited = True
            return True

        if rate_limits_keys[1] is None:
            if not self._has_been_rate_limited:
                UserWarnings.send_warning(Error(exc=RookGlobalRuleRateLimited()))
                self._has_been_rate_limited = True
            return True

        return False

    def _record_rate_limits(self, rate_limits_keys, duration):
        self._rate_limiter.record(rate_limits_keys[0], duration)
        self._global_rate_limiter.record(rate_limits_keys[1], duration)
