# Globe V2 — Engineering Specification

**Status:** Approved visual intent, NOT implemented or measured. This is an implementation contract and starting hypothesis, not a claim of achieved performance.

## Objective and reference
The existing homepage's moving neon-green globe is the user's favorite feature. Preserve its recognizably rotating 3D personality while transitioning to the approved premium direction: luminous cyan/emerald **recognizable Earth**, restrained sparse connection arcs, thin orbital rings, subtle atmosphere and small labels representing detection, AI-agent security and authorization. Do not display invented live incident data or claim the animation is a real SIEM dashboard.

Visual reference binaries and SHA-256 hashes are indexed in VISUAL_REFERENCES.md. The original artwork is a static concept—not a 3D model or ready-to-run source.

## Visual layers / starting budgets (tune through testing)
1. Sphere: landmass/ocean map with recognizable geography; low-gloss deep navy water, luminous cyan and emerald land outlines or points, gentle atmosphere halo.
2. Orbit rings: 2–3 fine, low-opacity tilted orbit paths.
3. Network points: approximately 8–24 illustrative nodes with 6–14 sparse arcs; avoid hundreds of expensive animated meshes.
4. Subtle halo and minimal particle field. Each visible component has a purpose, avoids unbounded transparency/postprocessing.
5. Labels: "Detection", "AI Security", "SOC Operations", "Authorization" if space permits. HTML callouts recommended so they can be accessible and responsive.
6. The hero text and both CTAs must remain fully readable and independently rendered in HTML. Globe must NEVER be required to understand the homepage.

## Technology
- Static GitHub Pages; HTML/CSS/JavaScript progressive enhancement.
- Use a reviewed, pinned, maintained Three.js version and correct module loading; do not blindly carry over existing Three.js r128 CDN script.
- Canvas container responsive to CSS; use ResizeObserver to synchronize camera aspect and renderer viewport.
- Use static optimized image first (no layout shift); lazy start WebGL after main content is visible or near viewport.
- Check support; gracefully leave static fallback if browser/device unsupported or initializing fails. Log harmless diagnostic info only during development.
- Caps: begin with devicePixelRatio <= 1.5 for renderer drawing-buffer dimensions, dynamic quality fallback based on actual profiling. Do not promise identical visual fidelity across all devices.
- requestAnimationFrame loop only if canvas intersects viewport, tab visible, motion allowed, and user has not pressed Pause. Pause when offscreen or tab hidden. Clean up listeners, geometries, materials, textures and renderer when done.
- Recover or gracefully fallback from lost WebGL context.
- Mobile default: optimized static recognizable globe (optional lower-cost WebGL after deliberate user opt-in and device testing); retain consistent composition.
- Optional pointer drag on desktop; keyboard-accessible equivalent controls or avoid making drag the only interaction.
- Provide a visible "Pause globe animation" button for persistent decorative animation; reduced-motion preferences disable automatic movement.

## Testing and measurable targets (NOT results)
- Performance: seek 60 FPS on selected desktop hardware, measure rather than assume. Frame timing, GPU load, resource transfer, first paint, memory, and effect of canvas on LCP must be tested.
- Core Web Vitals: target LCP <=2.5s, INP <=200ms, CLS <=0.1 at appropriate measurement percentiles.
- Initial globe artwork goal <=300KB compressed if practical, excluding Three.js code; verify size after asset build.
- Breakpoints: 1440 / 1366 / 1024 / 768 / 390 / 360 px and 200% text zoom.
- Usability: no page-blocking boot; no broken fallback; focus-visible on controls; no horizontal scrolling; buttons clickable without waiting for animation.
- Accessibility: reduced motion, keyboard operation, suitable text contrast, semantic controls, decorative canvas marked appropriately, no critical inaccessible image-only information.
- Reliability: page still readable if JS disabled, CDN inaccessible or GPU unsupported. Verify slow network and low-power modes.

## Fail-fast acceptance checks
- Desktop screenshot materially resembles approved concept **composition** while retaining text accessibility; avoid claiming pixel-perfect match to generated PNG.
- 3D effect can pause, resize, resume and degrade without runtime exceptions.
- Static fallback is branded and visually polished.
- No third-party telemetry without explicit review; no API tokens or customer data.
- Owner sees before/after comparisons and approves visual changes before any production merge.
