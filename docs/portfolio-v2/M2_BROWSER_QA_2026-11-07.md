# APEX Portfolio 2.0 — M2 Actual Browser QA Evidence
**Date:** 2026-11-07 (Asia/Kolkata)
**Status:** PARTIAL BROWSER QA; release gate remains HOLD.

## Actual runs / evidence
- [First Chromium QA run #42319812304](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42319812304) — completed (failing due existing layout overflow). Includes screenshots/JSON artifact.
- [Diagnostic Chromium run #42320063636](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42320063636) — completed (failing due existing layout overflow + intermittent pixel diffs). Includes richer overflow diagnostics.
- [Navigation-fix regression run #42320507654](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42320507654) — **IN PROGRESS when this record was authored; no final pass result claimed**.
- QA and GitHub workflow reside only in review [draft PR #8](https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/8), which targets the V2 prototype branch **not** `main`.

## Test design and scope
The test starts a local HTTP server on a GitHub Actions Ubuntu runner, launches actual headless Chromium/Playwright, loads the actual preview HTML/CSS/JS, and checks viewports 320, 360, 390, 480, 740, 768, 900, 901, 1010, 1024, 1280, 1366, 1440 and 1920px. It compares screenshots using baseline CSS from prototype commit `26bd33d879be44fd5cf52ff42b74748b5cd0b0d1` against the review branch. The CSS-only comparison **intentionally blocks Three.js and freezes animation** for deterministic layout comparison; a separate runtime smoke attempts to load the real Three.js/CDN and canvas. Do not confuse CSS-only screenshots with proof of a visually working globe.

## First confirmed browser facts
- **14 viewport widths were exercised** in actual Chromium.
- Mobile 390px: menu opens; Escape closes; Escape returns focus; clicking Work anchor closes menu — **4/4 scripted interaction assertions passed**.
- Real globe smoke at 1440px: **Three.js loaded**, `#tc` canvas visible, **no JavaScript page errors or captured console errors**; screenshot artifact saved. This is **not** a measured FPS/visual-quality/accessibility pass.
- First CSS-only baseline/candidate screenshot comparison reported no pixel differences at all 14 widths. The second run reported intermittent pixel differences at 360, 480, 740, 1024 and 1366px (without source changes to the active elements). Do **not** claim stable pixel-identical rendering across repeated runs. Updated test records changed-pixel fractions to distinguish minor rendering noise from substantial differences.
- Original globe source remained unchanged in review branch: blob `1be0c45a592aa54aa78bf42682964a0d11303977`.

## Confirmed pre-existing responsive defects from diagnostic run
| Viewport | Baseline scroll width | Candidate scroll width | Actual offending element | Diagnosis |
|---|---:|---:|---|---|
| 320px | 330 | 330 | `.menu-button` right edge 330px | Mobile header too wide |
| 768px | 786 | 786 | `.site-nav` right edge 786px | Desktop nav too wide for tablet |
| 901px | 923 | 923 | `.original-globe` right edge 923px | Fixed 460px original visual overhangs right-aligned desktop grid |

These are **existing prototype defects**, not caused by dead CSS removal in PR #8. The original and candidate CSS yielded identical widths in the diagnostic run.

## Action already taken but not yet browser-verified
PR #8 now includes a **navigation-only** adjustment: compact header at <=360px, collapsible tablet navigation from 741–900px, and corresponding `ui.js` resize threshold 900px. Original globe materials, geometry, animation loop, layout rules and active globe JS are untouched. The follow-up CI run is required to prove whether 320px and 768px overflow are fixed; do not claim they are fixed from source inspection alone.

## 901px globe decision gate
**No edit has been applied to this issue.** The owner locked the original globe design and requires approval before globe modifications. A possible minimal CSS-only solution is to scale the visual wrapper slightly at 901–960px or to postpone two-column composition until enough width exists; these alternatives may shift the visual appearance and must be reviewed with the owner. Never silently clip orbit rings or recolor/rebuild the globe.

## Outstanding quality gates
- Review the final outcome and `report.json` from run #42320507654; distinguish true regressions from intentionally changed navigation and rendering jitter.
- Inspect actual 390px/900px/901px/1440px screenshots manually (artifacts uploaded) before claiming visual acceptance.
- Approve and verify a reversible 901px responsive globe-layout fix.
- Test 200% zoom, assistive technology, mobile Safari, Firefox/Edge, actual FPS, WebGL fallback and Core Web Vitals.
- Review all public credentials, resume links and contact behavior on the existing live site separately.
- **Do not merge PR #8 or PR #4 and do not change `main` without owner release approval.**
