# APEX Portfolio 2.0 — START HERE / Canonical Handoff
**Last documented:** 2026-11-07 (Asia/Kolkata). **Owner-approved design:** A — Cybersecurity × Premium Engineering. **Stage:** Phase 2 approved; Phase 3 V2.2 code prototype created in separate PR #4 and undergoing owner visual review. **Status:** DOCUMENTATION ONLY / DO NOT MERGE docs PR #3 or prototype PR #4 without explicit owner release approval.

## One-paragraph product definition
Evolve the existing GitHub Pages site at https://nawazmuztaba.github.io/ into a polished, credible, fast and accessible global cybersecurity portfolio for Nawaz Muztaba. Preserve its recognizable animated Three.js globe, but upgrade its visual fidelity and performance. Position the owner around real SOC operations, detection automation, and bounded AI-agent security research; showcase AgentCheck V2 Alpha, Intelligent SOC Automation, and Sentinel-X. Do not delete the repository or automatically publish a redesign.

## Source of truth
- Site repository: https://github.com/NawazMuztaba/nawazmuztaba.github.io (PUBLIC).
- Unchanged live homepage: https://nawazmuztaba.github.io/.
- Published AgentCheck V2 technical study: https://nawazmuztaba.github.io/projects/agentcheck-v2/ (MUST remain untouched during portfolio work).
- Public project subdirectory: https://github.com/NawazMuztaba/nawazmuztaba.github.io/tree/main/projects/agentcheck-v2.
- **Source development repo:** NawazMuztaba/apex-permitlab remains PRIVATE; never present the public educational demo as the complete private source.
- Deferred older homepage PR #2: https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/2 — leave OPEN/UNMERGED; its proposed homepage is outdated relative to this approved design.
- This design-handoff documentation branch: docs/portfolio-v2-continuity-20261107. Main branch intentionally unchanged.
- The original homepage on main is a 1,165-line single-file HTML/CSS/JS site, including a neon-green spinning Three.js icosphere, matrix canvas, boot animation, skill radar, project cards, contact form and old resume links.

## Read in order
1. DESIGN_SYSTEM.md — precise design direction and visual decisions.
2. WIREFRAMES.md — desktop/mobile content ordering, layouts, and component behavior.
3. GLOBE_SPEC.md — realistic rendering, accessibility, fallback and performance safeguards.
4. CONTENT_AUDIT.md — verified vs owner-provided vs disputed claims; release blockers.
5. IMPLEMENTATION_PLAN.md — safe GitHub workflow, milestones, acceptance tests, and next actions.
6. VISUAL_REFERENCES.md — two approved ChatGPT-generated concept visuals, their filenames, dimensions and checksums. IMPORTANT: at handoff time the exact PNG binaries are NOT yet stored in GitHub.

## NON-NEGOTIABLE guardrails
1. Keep main, GitHub Pages, projects/agentcheck-v2/** and existing PR #2 unchanged without explicit owner authorization.
2. User approved visual direction A and later authorized a first interactive globe prototype; this is **not** approval to merge, replace the live homepage, or work on private APEX source.
3. NEVER invent certifications (CEH/eJPT), internships/job titles, salary/availability, attack outcomes, client details, skill percentages, CVSS numbers, or test outcomes.
4. AgentCheck: in observed indirect prompt-injection run the Qwen model did NOT request forbidden tool; separate model-independent forced forbidden request WAS denied before protected SQLite service execution. Never conflate.
5. Public project is a bounded synthetic/local demo, NOT a production-certified gateway or full open-source AgentCheck.
6. Website must be clear to a recruiter in seconds; visual beauty must not delay navigation, text, resume or contact access.
7. No client-sensitive logs, credentials, personal secrets, private repo code, internal reports or metrics that identify third-party clients.
8. New homepage implementation only on dedicated branch and reviewed PR; mobile, keyboard, motion, broken-link and performance testing mandatory before merge.

## Authoritative working choices
- Hero: "Nawaz Muztaba" + "I investigate threats. I build safer systems."
- Positioning: SOC Operations / AI Security / Security Engineering.
- Main CTA: Explore Projects; secondary: View Resume. Portfolio is professional, not "hacker cosplay".
- Selected work order: AgentCheck V2 Alpha, Intelligent SOC Automation, Sentinel-X.
- Experience: SafeAeon (SOC, March 2026–Present, role title to verify) and Vaishnav Technologies (VAPT, Jan–Mar 2025, location to verify).
- FortiSIEM marked **learning / training** until experience is demonstrated.
- No unverified percentage skill bars, inflated claims, fictitious boot logs, false send-message confirmation or "ATS 90%" scores.
- Use static GitHub Pages + HTML/CSS/JS + progressively enhanced Three.js rather than adding a paid backend.
- Palette: #07111D backdrop, #112536 surfaces, #F0F6FA primary text, #31E5E2 cyan, #19D99A emerald.
- Strongest visual signature: recognizable luminous cyan/emerald Earth, sparse fine network arcs, thin orbital rings, floating security labels; premium, restrained, cinematic dark aesthetic.


## NOVEMBER 7, 2026 — ACTIVE IMPLEMENTATION CHECKPOINT (V2.2)
- The first feature prototype exists in **draft PR #4**: https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/4
- Feature branch: `feat/portfolio-v2-prototype-20261107`. Review files in `portfolio-v2-preview/` (index.html, styles.css, ui.js, globe.js, assets/).
- Owner **rejected initial V2.1 globe visual** as too dim, flat and generic, and requested a detailed cinematic recognizable Earth resembling the approved concept PNG, plus strong cyan/emerald glow, fast red radar orbits like old legacy homepage, pulses, network nodes, holographic pedestal and a slightly smaller sphere.
- **V2.2 code has been pushed to that PR branch**: shader-brightened geographic Earth, atmospheric Fresnel glow, 3 red fast signal paths + 2 cyan/green paths, animated pulses, CSS radar sweep, glowing base and mobile fallback; pause control stops WebGL and CSS radar.
- **19/19 static source checks passed**. **Real browser screenshots, WebGL shader compilation, layout, actual FPS and quality checks are still PENDING**. Never report V2.2 visually approved or released without owner feedback and browser evidence.
- The old downloaded feature-branch ZIP on the owner's Windows PC is STALE and does not update automatically. To review: download latest ZIP from feature branch, extract, open Command Prompt *inside* `portfolio-v2-preview`, run `python -m http.server 8000`, visit `http://localhost:8000/`. From the repository root use `http://localhost:8000/portfolio-v2-preview/`.
- Next assistant: ask for / inspect a **fresh V2.2 browser screenshot**, then do targeted visual fixes if the Earth, halo or red radar still look wrong. Preserve main/AgentCheck path and don't merge.

## NEXT CHAT — copy this exactly
Act as Principal Cybersecurity Portfolio Architect, Technical UX Lead, and Release QA Owner for APEX Portfolio 2.0. First read all documentation in GitHub repository NawazMuztaba/nawazmuztaba.github.io at branch docs/portfolio-v2-continuity-20261107, starting with docs/portfolio-v2/START_HERE.md, then read the other linked files. Inspect current main and PR #2 read-only; reconcile changes since last audit, don't rely on memories alone. Preserve approved Direction A — Premium Cybersecurity Engineering with a refined, luminous interactive 3D globe. Explicitly identify verified facts, unverified content, and visual-reference limitations. Continue from Phase 3 V2.2 prototype in draft PR #4: inspect current globe.js/styles.css and the owner's updated screenshot before any further styling. Do not change main or the AgentCheck study; do not merge or deploy anything without my explicit release approval. Work in small professional steps and leave durable GitHub documentation for the next handoff.

## 2026-11-07 — LATEST OWNER DECISION: RESTORE ORIGINAL GLOBE (PR #6)
- Owner rejected Globe V2.2/V3 visuals and requested **exact original globe code from the uploaded legacy HTML**, placed within premium Portfolio V2. **This supersedes V2.2/V3 globe design for the active implementation.**
- **Draft PR #6:** https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/6 targets `feat/portfolio-v2-prototype-20261107`, not main.
- Feature branch: `feat/portfolio-v2-original-globe-20261107`.
- Four changed files all under `portfolio-v2-preview/`: original-globe.js, index.html, styles.css, ORIGINAL_GLOBE_INTEGRATION.md.
- Exact legacy 185-line `initThreeJS()` copied byte-for-byte (function SHA-256: `cb92ccf9f7ce14fff1e5237a87d4586afaf4ce1051f3cf3fa7a3db23c77ae1a9`). Original THREE r128 CDN, 340x340 canvas, 3 rotating HTML rings 360/400/440, green wireframe, red/cyan satellite motion and original speeds preserved. Scaled only as a unit for mobile.
- 14/14 static integration checks passed, **no actual browser or FPS measurement in this turn**; await owner's local screenshot before any merge. Original frame loop has no pause/reduced-motion feature: faithful recreation, not a performance optimization claim.
- To preview: download branch ZIP, extract, open `portfolio-v2-preview`, run `python -m http.server 8000`, browse `http://localhost:8000/`.
- Important: owner's old globe is an **abstract wireframe cyber sphere**, not detailed geographic Earth. Do not insert V3 flat picture or V2.2 Earth shader into PR #6 unless owner changes direction.
- Main and published AgentCheck untouched. Keep draft PR #2, #3, #4, #5, #6 unmerged unless explicitly authorized.

## 2026-11-07 — LATEST: Obsidian Aurora reversible experiment (DRAFT PR #7)
- Owner approved a limited **Version A** test: fix right-side hero positioning and try premium colors, but preserve ability to revert to the original.
- **Draft PR #7** https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/7 targets original-globe feature branch (PR #6), NOT main. Experiment branch: `feat/portfolio-v2-obsidian-aurora-20261107`.
- Corrected malformed HTML: the `<div class="hero-visual">` had been accidentally placed inside `<ul class="skill-strip">` and leftover V2 markup remained. Two sibling hero grid items now render intro left and globe right at desktop widths over 900px; smaller devices intentionally stack.
- Original globe dynamics kept intact: animation block byte-identical, original node counts, geometry and 340px renderer unchanged. Only materials updated to Emerald 0x34e2a8, Cyan 0x49ddf5, Coral Red 0xff4d6d, Obsidian Core 0x040b14, Ice primary nodes 0xa7fff0; outer CSS rings color-tuned.
- 15/15 source checks passed. Real browser visual impression/FPS NOT yet tested or approved. User should download a NEW ZIP from PR #7 head branch and run local Python HTTP server from `portfolio-v2-preview`.
- **Rollback:** Original unchanged colors remain in PR #6; if user dislikes palette, restore PR #6 original-globe.js material values while KEEPING valid HTML/layout from PR #7. Do NOT simply revert PR #7 wholesale, because PR #6 HTML was malformed.
- GitHub main, public case study and previous PRs untouched; DO NOT merge anything until explicit release approval.


## 2026-11-07 — RECOVERY AFTER ACCIDENTAL MERGE (current decision, supersedes Aurora)
- User accidentally merged **PR #6** into prototype branch `feat/portfolio-v2-prototype-20261107`. PR #6 was the exact *original* green wireframe globe; its HTML still had malformed hero markup.
- **PR #7 Obsidian Aurora was never merged** (despite user concern) and was **closed unmerged** upon user rejection.
- On the existing prototype branch `feat/portfolio-v2-prototype-20261107`, corrected hero HTML **in place** and added a responsive grid layout override that positions original globe to the **right side on desktop**. Original hero copy was recovered verbatim from branch `feat/globe-v3-fidelity-20261107` (created before PR #6) to avoid invented content.
- **Globe JS untouched**: `portfolio-v2-preview/original-globe.js` blob SHA `1be0c45a592aa54aa78bf42682964a0d11303977`. Exact legacy colors: green `0x00ff41`, red `0xff2244`, cyan `0x00e5ff`, dark core `0x010801`. Original renderer size, particle counts, arcs, satellite movements and animation speeds unchanged.
- Recovery commits to prototype branch: HTML `2a0a96a7615d60aa0c24c001310d49b66dffef8f`; CSS `26bd33d879be44fd5cf52ff42b74748b5cd0b0d1`.
- Verification: 16/16 static checks passed: balanced HTML, original palette unchanged, correct right-column CSS, no stray markup, old orbit timings, PR #7 closed, old site/case-study main untouched. **Actual desktop browser display/FPS not yet measured.**
- PR #4 (prototype toward `main`) remains open/draft. Do not merge PR #4 into main without explicit release approval. User should download a **new ZIP** from prototype branch and serve inside `portfolio-v2-preview`: `python -m http.server 8000` → `http://localhost:8000/`. Do not download stale ZIPs or use Obsidian Aurora branch.
- Owner current choice: **original green globe** with fixed right-side desktop placement. Do not reintroduce Obsidian Aurora unless explicitly requested.

## 2026-11-07 — M0/M1 AUDIT COMPLETED; M2 LEGACY CLEANUP IN DRAFT PR #8 (NOT MERGED)
- [Verified M0/M1 source-audit and prioritized backlog](./M0_M1_AUDIT_2026-11-07.md) was committed to this documentation branch. It reconciled current `main`, the V2 prototype, existing PRs, the original globe source SHA, draft content and outstanding release blockers. It is **static/source evidence only**.
- A narrowly scoped implementation review was created: **draft PR #8**, https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/8. It targets `feat/portfolio-v2-prototype-20261107` (NOT `main`) from `fix/portfolio-v2-legacy-cleanup-20261107`. **PR #8 is not merged.** It is not a production release and does not change PR #4 until intentionally merged into the prototype.
- PR #8 modifies **only** `portfolio-v2-preview/README.md` and `portfolio-v2-preview/styles.css`. The README accurately describes the restored original green globe, real limitations and release gates. CSS cleanup removes the currently unused geographic-Earth/radar/fallback/pedestal styling and 14 obsolete responsive selectors. The removed rules referenced classes absent from the active preview HTML.
- **No changes to** `original-globe.js`, `index.html`, `ui.js`, `globe.js`, `main` or `projects/agentcheck-v2/**`. Original globe blob SHA on PR #8 remains `1be0c45a592aa54aa78bf42682964a0d11303977` with original colors/dynamics intact. The original-globe restoration CSS block and subsequent owner-requested right-column recovery rules were verified byte-identical before/after source cleanup.
- GitHub compare verified PR #8 was 2 commits ahead of original prototype checkpoint `26bd33d879be44fd5cf52ff42b74748b5cd0b0d1` and changed only the two reviewed files. CSS braces/comments were balanced, original critical selectors remained, and old selectors were absent after cleanup. **No live browser visual comparison, performance test, WebGL runtime test, or accessibility pass was performed.**
- **Next step:** perform actual 1440px/390px/900px/901px local browser screenshots and navigation/regression checks against original prototype; then review whether to merge **PR #8 into prototype only**. Keep PR #4 and main on hold until the larger portfolio review and explicit release permission. Prioritize credentials/experience verification, evidence-first projects, globe motion/fallback assessment with approval, and complete production QA.

## 2026-11-07 — M2 Chromium QA — responsive defects confirmed
- Detailed evidence, viewport measurements, GitHub Actions runs and owner approval gate: [M2_BROWSER_QA_2026-11-07.md](./M2_BROWSER_QA_2026-11-07.md).
- **Actual Chromium testing is now in place in draft PR #8**, with a GitHub Actions workflow and 14-width viewport screenshots. First two runs verified mobile menu keyboard behavior and Three.js canvas startup, but failed due pre-existing horizontal overflow at 320px (+10), 768px (+18), and 901px (+22), shared by prototype baseline and candidate.
- PR #8 now includes a narrow-mobile and tablet navigation-only correction in `styles.css` and `ui.js`; **final post-fix browser validation was still running** when this handoff was recorded: https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42320507654.
- **901px globe overflow intentionally NOT fixed**: original 460px visual wrapper overhangs 22px; any responsive scaling/repositioning of the approved original globe requires owner approval. Do not clip or recolor the asset.
- Globe source unchanged SHA `1be0c45a592aa54aa78bf42682964a0d11303977`. PR #8 is OPEN DRAFT/UNMERGED, PR #4 OPEN DRAFT/UNMERGED, `main` and AgentCheck study protected. Do not infer a browser pass from green source checks or one clean screenshot capture.

## 2026-11-07 — M3 project-evidence review (next milestone prepared)
- [M3 featured-project repository-to-claim review](./M3_FEATURED_PROJECT_EVIDENCE_REVIEW_2026-11-07.md) saved on docs branch. Source inspection covered public AgentCheck case study, Intelligent SOC Automation and Sentinel-X repositories.
- **Source-inspection findings:** the SOC automation project contains Redis log-adapter, detector and Flask/React code; its measured operational performance remains unverified. Sentinel-X contains Python discovery, assessment and reporting modules, but its public README makes high-confidence “production-grade” and numeric/client-impact claims without verified supporting evidence in this audit. Its code includes environment-specific hardcoded paths; its public repository also includes domain-named report artifacts that warrant authorization/privacy review. No live scans or project execution were performed.
- **No public claims or linked repositories changed.** Draft owner-review candidate wording is included for future M3 content work. Do not publish unverified outcomes or expose private implementation.
- **Responsive QA update:** Owner approved a small CSS-only globe fit at 901–960px; Chromium then identified a second 961px boundary overflow. The PR #8 branch now has a narrow follow-on 961–1000px fit, preserving original JavaScript SHA and materials. Regression matrix expanded to 19 viewports; read the latest run result before claiming a complete pass: https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42321681408. The globe’s source and the live website remain untouched. PR #8 and PR #4 remain draft/unmerged.

## 2026-11-07 — FINAL RESPONSIVE BROWSER QA VERIFIED
- [GitHub Actions run #42321681408](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42321681408) concluded **SUCCESS** on code-review commit `ef923898bda60efc476c1bdad72088e4d5f94943`. Tested 19 viewport widths, all seven mobile/tablet menu interactions, a Three.js/canvas runtime smoke and error-capture checks; zero reported failures. The approved CSS-only narrow desktop original-globe fit passed automated checks at the 901/960/961/980/1000/1001 boundaries.
- Detailed measured evidence and remaining caveats: [M2_BROWSER_QA_2026-11-07.md](./M2_BROWSER_QA_2026-11-07.md). Passing headless Chromium **is not** a full accessibility, real-device, FPS, visual aesthetic, WebGL-fallback or cross-browser sign-off.
- **Next milestone M3:** Evidence-first project content. Public Sentinel-X README includes unverified aggressive claims and domain-named reports that warrant a separate safe-claims/authorization review; Intelligent SOC Automation has inspectable code but needs an independently reproducible local demo before numeric metrics. See [M3_FEATURED_PROJECT_EVIDENCE_REVIEW_2026-11-07.md](./M3_FEATURED_PROJECT_EVIDENCE_REVIEW_2026-11-07.md).
- PR #8 remains a **DRAFT** into the prototype branch, **not merged**; PR #4 remains **DRAFT** into `main`, **not merged**; original globe JavaScript still SHA `1be0c45a592aa54aa78bf42682964a0d11303977`. No production changes or release authorization.

## 2026-11-07 — M3 PROJECT SHOWCASE REVIEW (PR #9)
- **Owner merged PR #8 into the prototype** (verified GitHub) on 2026-11-07 at `dd7ea30285f7a651d967ddc5b9e938b306cc05ae`. The prior chronological notes calling #8 draft are now historical, superseded by this confirmation. `main` was still `35e627bfa69c161717bebb31d19c62ea5c7162a2`; PR #4 remains open/draft/unmerged.
- **New M3 draft PR #9:** https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/9, from `feat/portfolio-v2-m3-evidence-showcase-20261107` into `feat/portfolio-v2-prototype-20261107` **only**. M3 improves three selected-work cards with evidence-first narratives, implementation facts, scope boundaries and responsive 3/2/1-card layout; no production change, private source publication or resume/credential update.
- **Original globe protected:** source blob `1be0c45a592aa54aa78bf42682964a0d11303977` unchanged; original hero/right-column and existing CSS preserved before the scoped M3 Work-section rules.
- **Evidence review and traceability:** [M3_FEATURED_PROJECT_EVIDENCE_REVIEW_2026-11-07.md](./M3_FEATURED_PROJECT_EVIDENCE_REVIEW_2026-11-07.md) and [M3_IMPLEMENTATION_REVIEW_2026-11-07.md](./M3_IMPLEMENTATION_REVIEW_2026-11-07.md). Sentinel-X README aggressive benchmarks/client claims are not reproduced; SOC tooling claims are restricted to actual public code presence; AgentCheck remains bounded synthetic case study.
- **Browser QA:** M3-specific 20-width Chromium and navigation/hero/globe test with screenshots in [run #42323398234](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42323398234). Initial CI attempts exposed and corrected two test-harness errors (baseline summary missing; link rectangle key). **Verify final run outcome before declaring the milestone passing.** Draft PR #9 remains unmerged; PR #4/main is on hold. Owner visual sign-off, full a11y/FPS, credible employment and credential review remain outstanding.

## 2026-11-07 — M3 CHROMIUM QA SUCCESS ON DRAFT PR #9
- [GitHub Actions run #42323398234](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42323398234) **SUCCESS**: 20 viewport widths, no recorded failures, correct responsive 3/2/1 project grid, protected hero geometry, navigation Escape/focus (390/768), Three.js + canvas smoke without captured JS errors. The approved original globe file blob remains `1be0c45a592aa54aa78bf42682964a0d11303977`.
- [13-file screenshot/JSON QA artifact](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42323398234/artifacts/13553814237) available for manual review. Detailed source mapping and caveats in [M3_IMPLEMENTATION_REVIEW_2026-11-07.md](./M3_IMPLEMENTATION_REVIEW_2026-11-07.md).
- PR #9 is still DRAFT into the *prototype branch*, not merged; PR #4 remains DRAFT into `main`; no deployment. Manual visual approval, official employment title, graduation, certifications, approved resume and full accessibility/performance are outstanding before launch.


## 2026-11-07 — M4 OWNER RESUME REVIEW & CHROMIUM PASS
- Owner reports **PR #9 merged**. Verified GitHub merge `ef27f795a63cc3e86e2fe8ce7d7d0f64c89adbff` into `feat/portfolio-v2-prototype-20261107`. PR #4 remains open/draft into `main` and unmerged; production main still unchanged when M4 began.
- M4 review PR **#10**, https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/10, from `feat/portfolio-v2-m4-identity-20261107` into the **prototype branch only**; OPEN DRAFT / UNMERGED when documented.
- Owner uploaded newest `Nawaz_Muztaba_Resume.pdf` to this chat as the professional content source. Its **bytes are not committed anywhere to public GitHub**, nor is a public resume link introduced yet. The uploader may need to reattach the PDF in a fresh conversation. Editorial summary and exact publication/privacy issues: [M4_RESUME_INTEGRATION_REVIEW_2026-11-07.md](./M4_RESUME_INTEGRATION_REVIEW_2026-11-07.md). That source has a personal phone number and a clipped final skill; avoid committing or serving exact PDF without disclosure decision and re-export.
- M4 draft uses owner's latest resume title `SOC Analyst` at SafeAeon rather than stale intern descriptor, and presents KQL/Defender as working knowledge, FortiSIEM as learning and LPU CGPA 7.5/10 (resume-listed). Previous official offer documented an internship; **conversion to a regular employee remains unverified**, so must be settled before public release. The resume lists five training/credential entries, but no unverified public certification badges were created.
- **Verified final M4 QA:** [GitHub Actions #42325218872](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42325218872), conclusion **SUCCESS** on `121dfab88e5b746a02b898ebcc4d6e46e58d5fff`, with 19 viewport widths, no reported test failures, preserved hero/work layout, mobile/tablet menu checks and visible original globe Three.js smoke. [Review screenshots and JSON](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42325218872/artifacts/13554703412).
- Original globe JavaScript remains `1be0c45a592aa54aa78bf42682964a0d11303977`. PR #10 is a safe review-branch candidate only; manual design approval, resume PDF publication choice, issuer verification, work-status confirmation, and full release QA remain pending.


## 2026-11-07 — M4.2 ORIGINAL RESUME UPLOADED VERBATIM (NOT YET DEPLOYED)
- The owner explicitly corrected the goal: **do not generate/rewrite a new resume; host their already uploaded resume** so visitors can click **View Resume** or **Download PDF** in the portfolio. The owner separately approved publishing the personal phone number in that PDF.
- The exact uploaded 1-page `Nawaz_Muztaba_Resume.pdf` (329220 bytes, SHA-256 `94725e11537ad488169299a0cd5351c64134402dae06ee877e7897b80c8ae221`) was transferred as a binary Git blob on **M4 PR #10 review branch** into `portfolio-v2-preview/assets/Nawaz_Muztaba_Resume.pdf`; Git blob `1fd52b57cc228cddb2e85079c5bd9cc933b7753e` exactly matched the original. Original content was **not modified**. The earlier unwanted generator was deleted from branch; no net generator file in PR.
- Preview HTML now includes **View resume** in navigation and hero (target `_blank`) and **Download PDF** in hero using a same-origin `download` attribute; they target `./assets/Nawaz_Muztaba_Resume.pdf`. No `main` changes; PR #4 remains draft/unmerged.
- [M4.2 implementation and deployment caveats](./M4_RESUME_VIEW_DOWNLOAD_IMPLEMENTATION_2026-11-07.md) documents exact hash, path, tests and release mapping. Note: a future root-index deployment must copy/move the PDF to root `/assets/` **or** change hrefs to the tested final path. Preview relative paths cannot simply be copied to root without assets.
- [Verified first Chromium PDF run #42326829430](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42326829430) PASSED: original SHA-256 served over HTTP as `application/pdf` at 5 tested widths; actual browser download SHA matched on 390px and 1440px; M4 19-width suite also PASSED. Follow-on View-popup navigation check is being tested separately; consult latest PR run before claiming popup test is green.
- The source PDF has pre-existing clipped skill text and a noncanonical AgentCheck link. Owner requested keeping the **original unchanged**, so these were not silently corrected. Future edited PDF requires a new explicit request.
- Original globe JS still SHA `1be0c45a592aa54aa78bf42682964a0d11303977`. **Do not merge PR #4 or publish the portfolio without explicit release approval.**

## 2026-11-07 — PORTFOLIO V2 LIVE ON THE ROOT DOMAIN
- User explicitly ordered immediate public launch at `nawazmuztaba.github.io`. **Production PR #11 MERGED** into `main`, commit `75eed9c961dfe43de0a79c52b21e1be321928862`. New root `index.html` serves Portfolio V2; CSS, UI, original globe JS, and original PDF are now served from root-level assets. The original globe source SHA is unchanged: `1be0c45a592aa54aa78bf42682964a0d11303977`. The resume PDF SHA256 remains `94725e11537ad488169299a0cd5351c64134402dae06ee877e7897b80c8ae221`.
- **FRESH LIVE HTTP CHECK PASS**: homepage HTTP 200/new “Nawaz Muztaba | Cybersecurity Engineering” title and hero; `/styles.css` 200 text/css; `/ui.js` and `/original-globe.js` 200 application/javascript; `/assets/Nawaz_Muztaba_Resume.pdf` 200 application/pdf. Full evidence and rollback: [PRODUCTION_RELEASE_2026-11-07.md](./PRODUCTION_RELEASE_2026-11-07.md).
- Older draft PR #4 was **closed without merging** as superseded by PR #11. Do not reopen/merge it just to launch the homepage; the new portfolio is already live. The development prototype branch is retained for historical comparison.
- Original owner resume is published **unchanged** by explicit user direction, including phone number. Previously observed clipped last skill line and embedded AgentCheck link are known defects, not silently fixed. HR conversion/degree/credential evidence and broader manual Safari/a11y/performance checks are future scope.
- Any further production edits must use a **new scoped PR into main** with updated QA. Baseline before release: `35e627bfa69c161717bebb31d19c62ea5c7162a2`; avoid force pushes.

