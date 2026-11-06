"""Eight stdlib tests for the PUBLIC, fictional Guard example."""
import unittest

from guard_demo import (
    ContextError, GuardedDispatcher, SyntheticService, ToolRequest, run_scenario,
)


class GuardDemoTests(unittest.TestCase):
    def test_allowed_handbook_read_commits_effect(self):
        result = run_scenario("normal")
        self.assertEqual(result["guard_decision"], "ALLOW")
        self.assertEqual(result["reads_after"], 1)
        self.assertTrue(result["actual_handler_invoked"])
        self.assertFalse(result["real_model_invoked"])

    def test_injected_fixture_is_only_data(self):
        result = run_scenario("injected-fixture")
        self.assertEqual(result["guard_decision"], "ALLOW")
        self.assertTrue(result["untrusted_document_text_present"])
        self.assertEqual(result["synthetic_payroll_reads"], 0)

    def test_forced_forbidden_payroll_never_runs(self):
        result = run_scenario("forced-denial")
        self.assertEqual(result["guard_decision"], "DENY")
        self.assertFalse(result["actual_handler_invoked"])
        self.assertEqual(result["reads_after"], 0)
        self.assertEqual(result["synthetic_payroll_reads"], 0)

    def test_cross_tenant_is_denied(self):
        result = run_scenario("cross-tenant")
        self.assertEqual(result["guard_decision"], "DENY")
        self.assertEqual(result["reads_after"], 0)

    def test_consumed_context_replay_is_rejected(self):
        service = SyntheticService()
        try:
            guard = GuardedDispatcher(service)
            ctx = guard.issue_context()
            req = ToolRequest("read-document", "handbook", "lab")
            guard.execute(req, ctx)
            with self.assertRaises(ContextError):
                guard.execute(req, ctx)
            self.assertEqual(service.read_count(), 1)
        finally:
            service.close()

    def test_lookalike_forged_context_is_rejected(self):
        service = SyntheticService()
        try:
            guard = GuardedDispatcher(service)
            ctx = guard.issue_context()
            forged = type(ctx)(ctx.run_id, ctx.nonce)
            with self.assertRaises(ContextError):
                guard.execute(ToolRequest("read-document", "handbook", "lab"), forged)
            self.assertEqual(service.read_count(), 0)
        finally:
            service.close()

    def test_malformed_request_is_rejected(self):
        service = SyntheticService()
        try:
            guard = GuardedDispatcher(service)
            with self.assertRaises(ValueError):
                guard.execute(
                    ToolRequest("../read", "handbook", "lab"), guard.issue_context()
                )
            self.assertEqual(service.read_count(), 0)
        finally:
            service.close()

    def test_kill_switch_denies_even_valid_handbook(self):
        service = SyntheticService()
        try:
            guard = GuardedDispatcher(service, deny_all=True)
            outcome = guard.execute(
                ToolRequest("read-document", "handbook", "lab"), guard.issue_context()
            )
            self.assertEqual(outcome["guard_decision"], "DENY")
            self.assertEqual(service.read_count(), 0)
        finally:
            service.close()


if __name__ == "__main__":
    unittest.main()
