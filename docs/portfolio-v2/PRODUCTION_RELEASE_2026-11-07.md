# Portfolio V2 — Production Release and Live Verification
**Date:** 2026-11-07 (Asia/Kolkata)  
**Status: DEPLOYED AND LIVE.** This status is based on merged production code and fresh HTTP 200 checks against the public domain.

## Release
- Owner explicitly requested immediate public launch of the new design at `https://nawazmuztaba.github.io/`.
- [Production PR #11](https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/11) merged into `main` at commit **`75eed9c961dfe43de0a79c52b21e1be321928862`**.
- Previous production main baseline was `35e627bfa69c161717bebb31d19c62ea5c7162a2`. Keep this SHA as emergency rollback reference. Revert safely via a PR; avoid rewriting main history.
- PR #11 changed exactly five files:
  1. root `index.html` promoted from tested prototype, updated production title/footer/canonical meta
  2. root `styles.css` — Git blob `de8c5194b13a6aa2c2aef543723e7bd65f93bd39`
  3. root `ui.js` — Git blob `9120861924a183b1b19a4155f16dea0e1ffb8f16`
  4. root `original-globe.js` — approved, byte-exact Git blob `1be0c45a592aa54aa78bf42682964a0d11303977`
  5. root `assets/Nawaz_Muztaba_Resume.pdf` — owner-original Git blob `1fd52b57cc228cddb2e85079c5bd9cc933b7753e`; SHA-256 `94725e11537ad488169299a0cd5351c64134402dae06ee877e7897b80c8ae221`
- Existing public `projects/agentcheck-v2/**` remained untouched. No private PermitLab code published.
- Older prototype draft PR #4 was closed **without merging** as superseded by #11. Its branch and Git history remain available for reference.

## Direct live HTTP verification, fresh requests
- `https://nawazmuztaba.github.io/` — HTTP **200**, title **Nawaz Muztaba | Cybersecurity Engineering**, meta canonical/OG URL correct, page text contains new hero “I investigate threats. I build safer systems.” and both resume buttons. Previous root title “Nawaz Muztaba | Penetration Tester” no longer present in returned HTML.
- `https://nawazmuztaba.github.io/styles.css` — HTTP **200** `text/css`
- `https://nawazmuztaba.github.io/ui.js` — HTTP **200** `application/javascript`
- `https://nawazmuztaba.github.io/original-globe.js` — HTTP **200** `application/javascript`
- `https://nawazmuztaba.github.io/assets/Nawaz_Muztaba_Resume.pdf` — HTTP **200** `application/pdf`
- Underlying prototype headless Chromium run [#42327524454](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42327524454) passed M4 19 viewport checks, navigation, visible WebGL canvas, PDF HTTP/download/new-tab navigation. Original PDF SHA was verified twice on actual browser downloads there. Production HTTP checks confirm deploy paths, but are **not** separate production real-device/browser performance tests.

## Known release follow-ups (non-blocking for first preview launch)
- User's PDF was deliberately preserved **without editing**; existing last skill line is clipped and its AgentCheck embedded link is not the preferred case-study route. Request owner's updated original PDF before changing PDF bytes.
- The site presents internship/SOC employment and CGPA as reflected in the owner's latest resume. HR conversion status, degree award and formal credential URL verifications remain outstanding for future public content polish; do not silently invent or amplify claims.
- Reduced motion handling of original WebGL loop, non-WebGL fallback, manual mobile Safari/Firefox and actual Core Web Vitals/FPS remain unmeasured. Do not label these as passed.
- If a user still sees old content, request a browser hard refresh and try a private window; GitHub Pages and browser caching can lag the merge.
- Future improvements should go through new scoped PRs targeting `main`, with standard source tests and approval. Avoid merging the stale PR #4.

**Live URL:** https://nawazmuztaba.github.io/
