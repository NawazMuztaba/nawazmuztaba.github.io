# Public Guard Demonstrator — Standalone Educational Reconstruction

This is **not** the private AgentCheck V2 implementation. It is a small, independently written Python standard-library example of **Guard-before-protected-operation** behavior.

No LLM calls, remote APIs, real accounts, external identity system, actual payroll or secrets are involved. It uses an in-memory SQLite service containing only invented handbook and payroll fixtures.

## Run locally (Python 3.11+)

From this directory:

    python guard_demo.py --scenario normal
    python guard_demo.py --scenario injected-fixture
    python guard_demo.py --scenario forced-denial
    python guard_demo.py --scenario cross-tenant
    python -m unittest -v test_guard_demo.py

**Expected forced-denial values:** guard_decision = DENY; actual_handler_invoked = false; reads_after = 0; synthetic_payroll_reads = 0.

The injected-fixture scenario only demonstrates that an attacker-written paragraph is **data returned by a test service**. It does **not** put that text into a real language model; do not interpret it as a prompt-injection attack blocked in this public example.

Eight stdlib tests cover allowed operations, forbidden payroll, cross-tenant requests, a fake injected document, replay, forged app context, malformed tool names and the kill switch.

## Security limitations

The context is an in-process programmatic reference, not real user authentication. Trusted Python code could bypass this dispatcher and read the local service directly. This example does not provide secure sandboxing, real agent tool connectors, external auditing or a production policy engine.

The private AgentCheck V2 experiment used Qwen/Ollama, a separate Guard adapter and synthetic Watch; those private source files are not distributed by this public demo. No broad open-source license is granted by viewing the example.