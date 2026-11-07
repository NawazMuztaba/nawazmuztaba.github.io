# APEX Portfolio 2.0 — Original Globe Prototype
**Status: REVIEW ONLY — NOT RELEASED**  
**Updated:** 2026-11-07  
**Owner's approved current direction:** premium dark cybersecurity portfolio with the original green/red/cyan animated wireframe globe, on the **right of the hero at desktop widths**.

## Read this first
The source of truth is the **latest owner-decision/recovery section** at `docs/portfolio-v2/START_HERE.md` in [documentation PR #3](https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/3), plus the [M0/M1 source audit](https://github.com/NawazMuztaba/nawazmuztaba.github.io/blob/docs/portfolio-v2-continuity-20261107/docs/portfolio-v2/M0_M1_AUDIT_2026-11-07.md).

**Active prototype:** `feat/portfolio-v2-prototype-20261107`, tracked in [draft PR #4](https://github.com/NawazMuztaba/nawazmuztaba.github.io/pull/4) targeting `main`. Work in any narrower review branch remains separate until it is reviewed and intentionally merged. The live GitHub Pages homepage has **not** been replaced by V2.

Previous V2.1/V2.2 geographic-Earth prototypes, Globe V3 and the Obsidian Aurora palette were **rejected or superseded for the active hero**. Do not follow stale globe instructions in older design/engineering files over the later recovery record.

## Run this version locally
Download/clone the **current branch** rather than reusing an old ZIP.

From the repository root:
```bash
python -m http.server 8000
```
Open **http://localhost:8000/portfolio-v2-preview/**.

Alternatively, start the server from within `portfolio-v2-preview/` and open **http://localhost:8000/**.

A local HTTP server is preferred to opening `index.html` directly as a `file://` URL. The original globe requires the browser to load a pinned external Three.js script from cdnjs. If that request fails or WebGL is unsupported, the 3D animation may not appear.

## Actual active implementation (source-verified; runtime QA pending)
| Area | Files / behavior |
|---|---|
| Portfolio layout and contents | `index.html`: hero, selected work, professional experience, technical capabilities, about/education, contact and footer |
| Visual system | `styles.css`: navy/cyan/emerald site theme plus preserved original globe ring styling and recovered desktop hero grid |
| Navigation | `ui.js`: responsive menu, close on nav link / outside pointer / Escape, reset on resize |
| **Active original globe** | `original-globe.js` and HTML `#tc` canvas; Three.js **r128** global build loaded by `index.html` |
| Older *inactive* experiment | `globe.js` is the superseded V2.2 geographic-Earth implementation; **it is not imported or executed** by the current `index.html` |
| Historical assets | `assets/earth-texture.svg` and `assets/globe-fallback.svg` were made for the old geographic Earth; current hero does **not** render them |

### The approved globe is locked
- Original code source: `portfolio-v2-preview/original-globe.js`.
- Original globe blob SHA at this checkpoint: `1be0c45a592aa54aa78bf42682964a0d11303977`.
- Exact original material colors: green `#00FF41`, red `#FF2244`, cyan `#00E5FF`, dark core `#010801`.
- Original 340 × 340 WebGL canvas, original animated wireframe layers, nodes, arcs, particles, satellite motion and surrounding three HTML/CSS rings.
- Current desktop hero layout places copy on the left and the original globe on the right above 900px. At narrower widths, the layout stacks.
- **Do not recolor, redesign, or change globe geometry/motion without explicit owner approval.** Preserve a recoverable source checkpoint.

### What is *not* implemented in the active globe
The original source starts an ongoing `requestAnimationFrame` loop and does **not** currently expose a working pause/resume button, tab-visibility suspension, WebGL resource disposal, or a fully equivalent reduced-motion fallback. Its original green globe also does **not** implement geographic Earth rendering, pointer drag, an atmosphere shader, or the V2.2 radar/pedestal controls.

The CSS disables decorative ring animations for reduced-motion preferences, but **that does not pause the WebGL loop**. Without Three.js/WebGL there is currently no active static art fallback in the hero. These are assessment/remediation items, **not completed accessibility/performance features**.

## Current content and evidence restrictions
- Featured order: **AgentCheck V2 Alpha**, **Intelligent SOC Automation**, **Sentinel-X**.
- AgentCheck public technical case study is a **bounded local/synthetic research demonstration**. The full private source repository `NawazMuztaba/apex-permitlab` stays private; do not imply production-certified protection or general immunity to prompt injection.
- Some biography, official employment-title, degree-completion, certificate and project evidence details remain under review. Do not manufacture outcomes, metrics, job titles, earned credentials or operational claims.
- An approved/current resume PDF has **not** been published in this prototype; `Request resume` uses a `mailto:` action.
- Confirm the portfolio contact information with the owner before publication. A `mailto:` action is **not** a confirmed sent message.
- Do not copy customer logs, private security artifacts or personal secrets into public HTML.

## Source clean-up scope (separate review work)
Obsolete styling for `.globe-stage`, `.globe-fallback`, old radar sweep, pedestal and V2.2 Earth visuals should be treated as **legacy only**. Removing confirmed unused CSS must not change the original `.legacy-hero`, `.original-globe`, `.cring`, `#tc`, animation function or responsive positioning. Keep the superseded `globe.js` and assets until a separately reviewed deletion/archival decision.

## Required QA before any release
These are **not pass claims**; they are still required:
- [ ] Review genuine Chrome/Edge screenshots at desktop 1440 × 900 and 1280px; confirm text-left/globe-right without overlap
- [ ] Review 320px / 360px / 390px / 480px / 740px / 768px / 900px / 901px / 1010px / 1024px / 1366px / 1920px responsive layouts, no horizontal overflow
- [ ] Verify keyboard-only navigation, focus order, mobile menu, Escape, link behavior and 200% zoom
- [ ] Verify actual WebGL rendering, browser console, tab visibility, CPU/GPU cost and relevant FPS measurements
- [ ] Verify reduced-motion behavior: CSS ring pause exists; ongoing WebGL animation remains a known limitation
- [ ] Verify three featured project links and the public AgentCheck case-study link; check final content for supported claims
- [ ] Test offline/blocked CDN and WebGL-unavailable behavior; design a fallback before production release
- [ ] Verify mobile Safari / Firefox where available and measure LCP, INP, CLS and transfer size
- [ ] Obtain owner approval for meaningful visual changes and explicit permission before merging PR #4 to `main`

## Release guardrails
Do **not** directly change `main`, touch `projects/agentcheck-v2/**`, merge PR #4, reintroduce Obsidian Aurora, expose private AgentCheck source, or publish obsolete resume PDFs without separate approval. The current prototype base commit `26bd33d879be44fd5cf52ff42b74748b5cd0b0d1` is a rollback checkpoint. Code review and browser testing must happen before any release decision.
