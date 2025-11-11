"""
State Machine Executor (Everything Combined)
Create a state machine executor similar to your on_fail() method
"""
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class ExecutorState:
    IDLE = 'idle'
    RUNNING = 'running'
    SUCCESS = 'success'
    FAILED = 'failed'

class ServiceExecutor:
    """
    State machine that:
    - Runs a service operation
    - Transitions between states
    - Handles failures gracefully (nested exceptions)
    - Cleans up artifacts
    - Logs all errors
    - Does NOT propagate exceptions (for test isolation)
    """
    def __init__(self, service_name):
        self.service_name = service_name
        self.state = ExecutorState.IDLE
        self.artifacts = []
        self.errors = []

    def run(self, operation):
        """
        Execute operation.
        Transition to SUCCESS or FAILED.
        Return True on success, False on failure.
        """
        self.state = ExecutorState.RUNNING
        try:
            result = operation()
            return self._on_success(result)
        except Exception as e:
            return self._on_fail(e)

    def _on_success(self, result):
        """Handle successful execution"""
        logger.info(f"{self.service_name} succeeded")
        self.state = ExecutorState.SUCCESS
        try:
            self._cleanup_artifacts()
        except Exception as e:
            logger.warning(f"Cleanup failed but ignoring: {e}")
        return True

    def _on_fail(self, error):
        """
        Handle failed execution.
        Requirements:
        - Log the error
        - Attempt artifact cleanup (may fail)
        - Attempt to stop gracefully (may fail)
        - Always mark as failed
        - Always return False
        - NEVER raise (for test isolation)
        """
        pass  # YOUR CODE HERE - Use nested exceptions!

    def _cleanup_artifacts(self):
        """Clean up temporary files (may fail)"""
        if not self.artifacts:
            return
        # Simulate cleanup that might fail
        for artifact in self.artifacts:
            if artifact == "corrupted":
                raise IOError("Corrupted artifact")
            logger.debug(f"Cleaned up {artifact}")
        self.artifacts.clear()

    def _stop(self):
        """Stop the executor (may fail)"""
        if self.state == ExecutorState.RUNNING:
            raise RuntimeError("Cannot stop while running")
        logger.info("Executor stopped")

# Test cases:
def test_graceful_failure():
    executor = ServiceExecutor("test-service")
    executor.artifacts = ["temp.txt", "corrupted", "data.log"]

    def failing_operation():
        raise ValueError("Operation failed")

    result = executor.run(failing_operation)

    # Should return False, not raise
    assert result is False
    assert executor.state == ExecutorState.FAILED
    print("✅ Test passed: Handled failure gracefully")

def test_cleanup_failure():
    executor = ServiceExecutor("test-service")
    executor.artifacts = ["corrupted"]  # Will fail cleanup

    def failing_operation():
        raise ValueError("Operation failed")

    result = executor.run(failing_operation)

    # Should still mark as failed even if cleanup fails
    assert result is False
    assert executor.state == ExecutorState.FAILED
    print("✅ Test passed: Handled cleanup failure")

# Run tests:
test_graceful_failure()
test_cleanup_failure()