# APEX Portfolio 2.0 — M3 Evidence-First Showcase Implementation Review
**Checkpoint:** 2026-11-07 (Asia/Kolkata)  
**Release decision:** HOLD for review. Prototype PR #9 only; no production publication.

## Locked baseline
- Portfolio V2 prototype branch: `feat/portfolio-v2-prototype-20261107`.
- PR #8 merged **into prototype only** at `dd7ea30285f7a651d967ddc5b9e938b306cc05ae`. Source baseline for M3.
- Original globe JS blob SHA: `1be0c45a592aa54aa78bf42682964a0d11303977`. Never alter its color/geometry/rotation or approved responsive fit without explicit owner decision.
- Existing live `main` still at `35e627bfa69c161717bebb31d19c62ea5c7162a2` when M3 started. PR #4 remains open/draft and unmerged.

## M3 development review
- [Draft PR #9 — evidence-first selected-work cards](https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/9) from `feat/portfolio-v2-m3-evidence-showcase-20261107` to the **prototype branch**, NOT `main`.
- `portfolio-v2-preview/index.html`: replace generic descriptions with clear problem framing, actual implementation, evidence-to-inspect, scope/limitations and more precise public link labels. Exactly three project articles, with accessible `aria-labelledby`/headings and definition-list evidence groups.
- `portfolio-v2-preview/styles.css`: appended M3 work-section-only styling. A balanced 3-column (large screens), 2-column (tablets), 1-column (phones) grid; more legible text and clear scan hierarchy. All preexisting CSS before the M3 block preserved verbatim.
- `qa/portfolio-v2/m3_showcase_qa.py` and `.github/workflows/portfolio-v2-m3-review.yml`: headless Chromium comparison against the exact M2 merge, project links and content assertions, 20 viewport widths, hero geometry protection, navigation checks, runtime Three.js smoke and screenshot artifacts.
- No modification to `original-globe.js`, `ui.js`, `globe.js`, old case-study page, `main`, resumes or private AgentCheck source. No use of actual third-party scanning targets.

## Source-to-claim mapping
| Portfolio card | Code/public source inspected | Support and caveats |
|---|---|---|
| AgentCheck V2 Alpha | Published `projects/agentcheck-v2/index.html` on live site (blob `5aa11e0844f02c47086a7b7d0cbc62f03ec792c5`) | The study describes bounded local/synthetic model/Guard interaction and separately denied forced-call test. Does not prove production immunity. Full private implementation stays private |
| Intelligent SOC Automation | Public repo `NawazMuztaba/intelligent-soc-automation`, `adapters/log_adapter.py`, `detectors/ssh_bruteforce_detector.py`, `detectors/web_attack_detector.py`, `dashboard/api.py`, `dashboard/ui/src/Dashboard.js` | Python/Redis log pipeline, rule-based detectors, Flask and React code exist. Clean environment execution, performance and operational detection outcomes unverified |
| Sentinel-X | Public repo `NawazMuztaba/Sentinel-X`: `sentinelx.py`, `modules/asset_discovery/risk_scoring.py`, `modules/tls_analysis/tls_analyzer.py`, `modules/reporting/unified_report.py` | Python modules for discovery, scoring, TLS and reporting exist. No independent proof for README's aggressive numerical benchmarks, enterprise readiness or client testimonial; no such numbers published on card |

See the [M3 source audit](./M3_FEATURED_PROJECT_EVIDENCE_REVIEW_2026-11-07.md) for complete caveats. Source presence alone is **not** an executed or validated demonstration.

## QA / release gates
- First two CI attempts identified **test-harness assumptions** only (the M2 baseline lacked the new `project-summary` element; bounding-rectangle key was wrong). They do not prove a live page defect.
- Latest QA: [GitHub Actions run #42323398234](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42323398234), **pending final verification** when this record was written. Don't claim PASS without final logs.
- Review actual mobile/tablet/desktop project-card screenshots with owner; review exact links; ensure no overflow, loss of hero layout or unexpected interactive regressions.
- Before production: verify official SafeAeon role, actual graduation status, owner-approved contact/resume, earned credentials and links, independent customer/privacy review of exposed Sentinel-X artifacts, accessibility and Core Web Vitals. Do not infer these from M3 automation.
- **Never merge PR #9 or PR #4 into `main` without separate explicit owner approval.** If M3 passes and owner accepts, merge PR #9 **into prototype only** as a separate decision.

## Next scope after M3 cards
- Credential verification and a precise education/experience narrative.
- Evidence-rich deeper case studies or demo screenshots only after real reproducible results and safe publication review.
- Continue manual browser aesthetics, keyboard/screen-reader, mobile Safari, WebGL fallback and performance checks before public release.

## Verified M3 browser QA — SUCCESS
- [GitHub Actions run #42323398234](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42323398234) completed **SUCCESS** on M3 review commit `7ef4a3d1a8a641d79251b0ab8479bca21fefa2c7`.
- Actual headless Chromium browser checked **20 viewport widths**, baseline-versus-candidate hero geometry, no horizontal page overflow, card counts/semantics/links, intended 3/2/1 responsive grid, text-size and card-link bounds. Zero reported failures.
- Mobile navigation assertions passed at 390px and tablet assertions passed at 768px (open, Escape closes, focus returned). Original globe smoke: Three.js loaded, canvas visible, no captured browser console/page errors; original globe source SHA still `1be0c45a592aa54aa78bf42682964a0d11303977`.
- [Screenshot and JSON evidence artifact](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42323398234/artifacts/13553814237) was uploaded (13 files). **These screenshots have not received owner manual visual sign-off.**
- Contrast spot-checks against solid endpoints of project-card gradient backgrounds: new text colors ranged **7.81:1–12.93:1** (calculated for selected text/surface pairs, **not** a full WCAG conformance assessment).
- **Release decision remains HOLD** until owner visual review, contact/credentials/employment claim verification, and wider accessibility/performance review. PR #9 is draft and unmerged into prototype; PR #4 unmerged into `main`.
