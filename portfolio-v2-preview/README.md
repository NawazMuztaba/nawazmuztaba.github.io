# Portfolio V2 — Phase 3 Interactive Prototype

**Status:** REVIEW ONLY. Prototype built on feature branch \`feat/portfolio-v2-prototype-20261107\` and not yet released. Main/root \`index.html\`, \`projects/agentcheck-v2/**\`, and older PR #2 are unchanged. Approved design direction: **A — Cybersecurity × Premium Engineering**. Design requirements/handoff: [docs-only PR #3](https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/3).

## How to preview locally
Clone/download this feature branch. From the repository root, start a local HTTP server:

\`\`\`sh
python -m http.server 8000
\`\`\`

Then visit **http://localhost:8000/portfolio-v2-preview/**. Do **not** open the HTML using a \`file://\` URL: local modules/textures may not load correctly under browser security rules.

This branch is not configured as the production GitHub Pages publishing source; a draft PR is not a public interactive preview by itself.

## Implemented in this scoped prototype
- Premium navy/cyan/emerald design; semantic hero; credible copy; three verifiable public project links.
- Responsive navigation with keyboard Escape and outside-click closing.
- Responsive desktop/touch layout; accessible links; reduced-motion styling.
- Real Three.js **r187 (0.187.0)** WebGL2 globe on desktop: textured geographic Earth, latitude/longitude lines, orbit rings, illustrative network points, arcs, moving pulses and optional mouse drag.
- Pause/resume button, tab/in-view pause, pixel-ratio cap, responsive canvas resizing, disposal on pagehide, context-loss fallback, and static SVG Earth fallback.
- No fabricated skill percentages, fake certifications, fake attack logs or misleading form submission confirmations.
- Owner's current resume is **not copied publicly**; the temporary call-to-action is a genuine \`mailto:\` "Request resume".

## Important limitations / release blockers
1. **Browser visual test has not yet been performed** for WebGL, SVG texture compatibility, actual FPS or layout screenshot. Static syntax/file checks are not substitutes for real browser testing.
2. Performance and WCAG acceptance testing remain pending across browsers, 390px and other viewports, keyboard navigation, low-end devices, reduced motion, and offline CDN cases.
3. A stable CDN serves the pinned Three.js module; when absent the static fallback remains visible. Consider self-hosting after size and licensing review.
4. Globe visual is **illustrative**, not live network telemetry or SOC incident data; exact similarity to the concept art is not guaranteed before screenshot iteration.
5. Official SafeAeon job title, project dates, credentials and numerical metrics still need verification. This draft uses cautious descriptions and omits questionable numbers.
6. The current GitHub Pages homepage remains unchanged. The public AgentCheck study is a bounded demo; full private source is not included.
7. Resume link must point to an owner-approved PDF only after privacy check. The prototype intentionally does not expose existing obsolete PDFs.
8. Project metrics and certification details omitted until evidence is approved. Both SOC Automation and Sentinel-X linked repositories were publicly checked.
9. Animated connections/hotspot interaction modes described as future options are **not implemented** in this initial version. Globe here uses animated illustrative pulses, not clickable security dossiers.
10. The original concept PNG reference hashes are documented in PR #3 but binary files require separate owner-controlled durable upload.

## Asset provenance
- \`assets/earth-texture.svg\` and \`assets/globe-fallback.svg\` are generated from [Natural Earth 1:110m land vector geography](https://github.com/nvkelso/natural-earth-vector), which is **public domain**.
- Globe source: Three.js \`0.187.0\`, MIT licensed, loaded as an ECMAScript module from jsDelivr.
- All project and service content is authored for this user's portfolio prototype; no client/customer data is included.

## QA checklist before any merge
- [ ] Desktop screenshot at 1440 × 900 visually reviewed against approved concept A
- [ ] 390 × 844 mobile screenshot; no horizontal clipping
- [ ] Globe rendered and rotating in a real browser with clear continents
- [ ] Pause/resume, pointer drag, reduced-motion, and off-screen pause verified
- [ ] Keyboard navigation/mobile menu/focus checks
- [ ] Browser console free of unexpected exceptions; WebGL fallback tested
- [ ] Links and contact actions tested; resume action replaced only with owner consent
- [ ] Updated content independently verified; no private sources leaked
- [ ] LCP/INP/CLS/transfer size and GPU profile measured
- [ ] Owner approves prototype and review PR before any main-branch replacement
