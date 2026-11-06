# Portfolio V2 — Controlled Implementation and Release Plan

**Status:** Implementation not yet authorized. Owner approved art direction A and requested design/continuity documentation. These are proposed steps, not completed work.

## Milestones
| Gate | Task | Exit |
|---|---|---|
| P0 | Continuity handoff and design evidence stored in GitHub | Documentation branch + reviewed draft PR; no main changes |
| P1 | Content truth/evidence reconciliation | Roles, dates, certs, metric provenance, links and resume consent signed off |
| P2 | Design components and visual prototype | Header, hero, globe, cards, timeline, skills, credentials, contact and mobile; owner screenshots approval |
| P3 | Static implementation on a NEW feature branch | HTML/CSS/JS modules, versioned assets, static fallback, accessible interactions |
| P4 | Desktop and mobile QA | Test matrix + Lighthouse/DevTools + visual comparisons + keyboard/motion/fallback checks; no misleading claims |
| P5 | Docs and release review | Preview PR with scoped diff, review checklist, owner explicit merge approval |
| P6 | Production rollout | Merge specific reviewed PR, verify GitHub Pages deploy and links, capture date/commit and rollback path |

## Safe repository procedure
- Repository: NawazMuztaba/nawazmuztaba.github.io (PUBLIC).
- Existing main homepage remains live until owner authorizes a replacement. Do not delete the repo, history or branches.
- AgentCheck public case-study subtree projects/agentcheck-v2/** remains UNMODIFIED. Private repository NawazMuztaba/apex-permitlab not to be published or modified for this website.
- Existing open PR #2 is deferred; do not merge, close or mutate it without new owner instruction.
- Current docs branch docs/portfolio-v2-continuity-20261107 contains this handoff only. It is NOT an implementation branch.
- When authorized, create a fresh scoped implementation branch off current main, keep PR small, do not auto-merge. Review deployment settings and use a safe preview method; GitHub Pages generally serves selected published branch/workflow only, so a PR alone is NOT automatically a live preview.
- Existing deleted resumes must NOT be restored from git history. Only post the latest OWNER-APPROVED resume PDF after privacy review.
- Before change, record git SHA and simple rollback instructions (revert merge or restore verified previous homepage commit).

## Proposed component architecture
```text
index.html                         # semantic SEO-ready layout
assets/css/tokens.css              # colors, typography, spacing and states
assets/css/main.css                # layout and responsive styling
assets/js/main.js                  # progressive navigation and affordances
assets/js/globe.js                 # lazy 3D, pause, fallback, context loss
assets/img/globe-fallback.webp     # optimized static fallback
assets/img/og-portfolio.webp      # social sharing preview
assets/img/projects/              # reviewed project illustrations
assets/resume/                     # owner-approved PDF ONLY
docs/portfolio-v2/                # design and development continuity
projects/agentcheck-v2/           # preserved as-is
```
No new paid API, analytics backend, framework, or form service is essential.

## Content truth gate
Use CONTENT_AUDIT.md. For unverified certifications/metrics/roles either obtain proof or remove/generalize claims. Specific unresolveds: SafeAeon official job title, Sentinel-X dates, completion status, certificates CEH/eJPT, updated SOC alert counts, sample rates/results, repository links, and approved resume binary. Never use illustrative mockup dates.

## Accessibility and performance gate
- WCAG 2.2 AA-guided review: meaningful headings, anchor semantics, keyboard menu, visible focus, correct form status, accessible links, text contrast, reduced-motion and pause controls.
- Browser matrix: recent Chrome, Edge, Firefox; iPhone Safari if available; multiple screen widths. Include keyboard-only and touch tests.
- Performance measurements from actual build, not speculative Lighthouse scores; ensure globe does not block LCP.
- Inert links, missing thumbnails, mismatched README copy, broken downloads, and inaccessible contact flows are release blockers.
- No fixed percentages like "skill 88%" or unmeasured "ATS score ~90%".

## Phase 3 first tasks
1. Read START_HERE.md and each sibling spec; inspect latest main and existing PR #2 read-only.
2. Verify images exist and download exact concept images using the hashes in VISUAL_REFERENCES.md; if not present in GitHub, arrange explicit upload by owner. Preserve actual PNGs before finalizing visual design.
3. Produce clean component-level UX specs and a safe content inventory spreadsheet/table; separate owner facts and external verification.
4. Prepare an accessible *static* hero prototype with globe fallback; next review should explicitly show desktop and 390px mobile variants.
5. Only after approval, implement scoped branches/PRs. Never publish based solely on a design approval.

## Acceptance / definition of done
A recruiter can scan role and strongest projects immediately; case study links are accurate; resume download works; no false claims; mobile supports full navigation; all interactive controls accessible; quality targets measured and logged; owner approves screenshots/PR; public AgentCheck content unchanged; site deploy green; documented rollback exists.
