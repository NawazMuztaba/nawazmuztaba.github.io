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
