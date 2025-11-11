# def on_fail(self):
#     """
#     Handle actions after transitioning to the 'failed' state.
#     This logs and records the failure but does NOT raise,
#     so the overall test run won't fail due to a single service execution error.
#     """
#     try:
#         logger.warning(f"In {inspect.currentframe().f_code.co_name}: "
#                        "Attempting to stop the state machine gracefully because service execution failed.")
#         self._move_artifacts()
#         self._generate_and_purge_allure_report()
#     except Exception as e:
#         logger.error(f"Failed to handle execution failure: {e}")
#         # record the error for later inspection but do not raise
#         self.fetcher_error = getattr(self, "fetcher_error", None) or str(e)
#     finally:
#         # Record validation/fetcher errors (if present) for post-test analysis
#         if hasattr(self, "validation_error") and self.validation_error:
#             logger.error(f"Final failure reason: {self.validation_error}")
#         if hasattr(self, "fetcher_error") and self.fetcher_error:
#             logger.error(f"Fetcher error: {self.fetcher_error}")
#
#         # Mark internal state as failed and stop the state machine gracefully
#         logger.info("Marking state machine as failed but NOT raising an exception to avoid failing the whole test run.")
#         self.failed = True
#         try:
#             # Best-effort graceful stop; ignore errors here
#             self.stop()
#         except Exception as stop_exc:
#             logger.debug(f"Error while stopping executor after failure: {stop_exc}")
#
#         return False
#
# """
# from contextlib import suppress
#
# finally:
# logger.info("Marking state machine as failed...")
# self.failed = True
# with suppress(Exception):
#     self.stop()
# return False
# """

