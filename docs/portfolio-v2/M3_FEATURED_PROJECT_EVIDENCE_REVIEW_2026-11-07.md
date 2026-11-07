# Portfolio V2 — M3 Featured Projects: Repository-to-Claim Review
**Checkpoint:** 2026-11-07 | **Scope:** Source-content audit only; NO live execution of assessment/scanning tools, no target contact, and no release approval.

## Goal
Ensure a technical hiring manager can click a project and see evidence that matches the portfolio's wording. Source inspection is **not** proof that the code runs successfully in a clean environment, that its claimed outputs were achieved, or that any external testing was authorized.

## Evidence matrix
| Work | Source inspected | Supported by code presence | Not established by this inspection |
|---|---|---|---|
| AgentCheck V2 Alpha | Public `projects/agentcheck-v2/index.html` on portfolio `main`; portfolio handoff | Public bounded local/synthetic technical case study is available | Production deployment, full public source, generalized prevention of agent attacks |
| Intelligent SOC Automation | `NawazMuztaba/intelligent-soc-automation` `README.md` blob `9cc8fcecf2aed4fbedb91f811e62d51218f4a8ff`; `adapters/log_adapter.py`, `detectors/ssh_bruteforce_detector.py`, `dashboard/api.py`; public tree `a54baec64ce7c3b62a6ebece8853ef3fd7372cd7` | Source implements log-tail/Redis publishing, threshold-based SSH alerting, API structures, Python detectors, and a React UI tree | Real-world operational coverage, production SIEM operation, verified detection statistics, current end-to-end local boot, security effectiveness |
| Sentinel-X | `NawazMuztaba/Sentinel-X` `README.md` blob `87ff7577c9e3e9b55a19c92041564c8789b0827b`; `sentinelx.py`, reporting and red-team orchestrator; public tree `be7f45130870d9c33d93690fcd34ff6ba0a6a5fb` | Python assessment-pipeline and module files exist, including discovery, classification, risk scoring, TLS review, report generation and red-team orchestration | Enterprise/production readiness, “1000+ assets”, “23 successful exploits”, speed/benchmark tables, alleged client outcome, safe/portable clean install, external authorization |

## Specific professional-credibility defects
1. **Sentinel-X README contains claims not demonstrated by source inspection.** It calls the project “production-grade” and “enterprise,” displays illustrative “1,247 assets” and “23 successful exploits,” uses performance tables, and attributes a purported enterprise-client testimonial to a “Red Team Lead.” No independently verifiable benchmark or named testimonial authorization was established here. Do **not** carry those numbers or quotation into Portfolio V2.
2. **Sentinel-X setup appears environment-specific.** The entry script resolves its modules under `Path.home() / "SentinelX"`, while the red-team orchestrator manually inserts `/home/kali/SentinelX` into `sys.path`. A fresh clone in a different location may not work as described, but that must be tested in an isolated environment before labeling the repo broken.
3. **Sentinel-X includes committed reports/JSON with third-party domain names** visible in public paths under `recon/` (e.g., example files naming major brands and universities). No actual authorization or consent status was established; conduct a privacy/authorization review of the generated artifacts before republishing or promoting claims. **Do not reproduce potentially sensitive contents in the portfolio or this report.**
4. **Intelligent SOC Automation README has broader “real-time/complete SOC” positioning** than source inspection can verify. The present portfolio's “simulated log monitoring” framing is more defensible. Test with documented synthetic logs and report precise observed effects before adding metrics.
5. **Sentinel-X README installation snippet uses `YOURUSERNAME`** rather than the actual repo path. This can confuse a recruiter. Fix in a separate, scoped repo-specific PR after validating setup rather than silently modifying unrelated projects.
6. **No execution or independent QA performed on either project in this audit.** Presence of a Python file, sample report or markdown checklist is not validation of production capabilities.

## Proposed evidence-first card copy (DRAFT — NOT PUBLISHED)
**AgentCheck V2 Alpha — “Authorization before agent tool execution.”**  
A bounded local study of untrusted document content, AI-agent tool requests, and a model-independent application Guard. Explore the synthetic cases and decision evidence in the public technical report. **Caveat:** not a production-certified agent-security gateway.

**Intelligent SOC Automation — “From log input to structured alerts.”**  
A Python/Redis prototype that ingests local log samples, applies rule-based detectors for authentication, scanning and web-pattern events, and publishes alert data for a Flask/React interface. **Caveat:** simulated/local; outcomes and performance should be demonstrated before numeric claims.

**Sentinel-X — “Security assessment workflow prototype.”**  
A modular Python project exploring asset discovery, classification, risk prioritization, TLS analysis and reporting. **Caveat:** avoid claiming production-grade exploitation or measured real-world business impact without independently reviewed evidence.

These text proposals are constrained by observed repository code, but the owner must review wording and what is safe to make public before publishing.

## Defensible demos to produce next
- SOC Automation: clean local setup, Redis startup, synthetic SSH/password-failure log input, observed alert, Flask/React dashboard capture, README that states dependencies and limits.
- Sentinel-X: entirely owner-controlled or explicitly authorized lab/synthetic domain; document which modules execute; fix hardcoded filesystem paths; clarify safe testing mode, output provenance, claims, and sample data licensing/authorization. **Do not scan third-party domains as a “demo.”**
- AgentCheck: preserve existing public case-study caveats and the private-repository boundary; do not conflate separate model behavior and Guard forced-call denial.

## Release gates and owner decisions
- The original globe and its visual design remain locked. This document does not change any implementation.
- The current public homepage `main` has unrelated existing credibility/404 contact defects already recorded in [M0/M1 audit](./M0_M1_AUDIT_2026-11-07.md). Those require separate authorization to repair.
- Exact official SafeAeon employment title, graduation completion, DP-900 credential URL, safe public contact channels and approved resume remain to be confirmed before finalized Portfolio V2 claims.
- Next safely scoped implementation should improve the project evidence/navigation path **after** the responsive cleanup is browser-validated and separately reviewed. Do not merge PR #4 or PR #8 or publish without explicit release approval.
