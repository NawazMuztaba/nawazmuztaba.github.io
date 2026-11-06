# Original 3D Globe — Exact Restoration (Review Branch)

**Purpose:** Restore the owner's ORIGINAL working globe from the uploaded legacy `index.html` into the approved Portfolio V2 premium homepage with the smallest integration surface.

## What has been preserved exactly
- Original 185-line `function initThreeJS(){...}` from owner's supplied original 1,164-line document, unchanged.
- Original Three.js `r128` global build, same version referenced by old homepage.
- Canvas `340×340`, original scene geometry, colors, opacities, node counts, orbit speeds, satellite motion, and frame-based animation.
- All original render objects: dense green wireframe icosphere, inner wire core, solid dark occlusion sphere, 48 nodes, 22 curved arcs, particle shells, 3 orbital rings, 2 orbiting satellite points, and latitude/longitude markings.
- Original three CSS halo rings, dimensions 360/400/440px and 30/48/68s rotations.

**Original function SHA256** (UTF-8, no trailing newlines): `cb92ccf9f7ce14fff1e5237a87d4586afaf4ce1051f3cf3fa7a3db23c77ae1a9`. The text is a byte-for-byte copy of that function inside `original-globe.js`.

## Only required integration adaptations
1. `index.html`: remove the V2.2 `globe.js` module and its import map; load the original `three.min.js` r128 build, and `original-globe.js`.
2. `index.html`: replace only the right-side hero globe markup with the canvas `id="tc"`, the original three `cring` nodes, and a responsive positioning shell.
3. `styles.css`: append scoped rules for centering and scaling the original exact 340px display and 440px outer ring within Portfolio V2. At narrower widths the *entire unchanged globe* is scaled (0.80 or 0.67), not internally remodeled.
4. `original-globe.js`: append a minimal `DOMContentLoaded` adapter to invoke the untouched original function when the page is parsed, with error reporting if the external Three.js script is blocked.

## What is deliberately not imported from the old page
- The old boot animation and fictional security logs, outdated resume links, unverified certification text, Matrix rainfall, skill claims, and old entire-page styling.
- The original globe does **not** contain geographic Earth continents. It is the precise abstract wireframe/orbital sphere the owner previously liked. Do not claim it renders a realistic Earth.
- The original globe doesn't have a built-in Pause button and continuously calls `requestAnimationFrame`. This preserves original behavior but means real-browser FPS, background-tab behavior and reduced-motion accessibility must be assessed separately. Do not label performance as proven.
- Third-party Three.js r128 is an archived version; parity is prioritized here. Separate upgrade/rewrite only after owner approves this faithful integration.

## Review steps
1. Open branch `feat/portfolio-v2-original-globe-20261107` in `NawazMuztaba/nawazmuztaba.github.io`.
2. Download branch ZIP, extract; open Command Prompt *inside* `portfolio-v2-preview`.
3. Run `python -m http.server 8000` then open `http://localhost:8000/`.
4. With server running, verify original globe with green wireframe, continuously changing red/cyan signals, 3 CSS rings and no extraneous V2.2 overlays.
5. Check at 1440×900 and 390×844, browser console, animation smoothness, content overlap and project links. Screenshot for owner approval.

## Validation
- Connector read-back confirmed exact 185-line original function exists within `original-globe.js`.
- 14/14 static integration checks passed. **No direct real-browser/fps verification performed in this current chat session**.
- Do not merge any PR into main without owner explicitly approving after reviewing the actual webpage.
- Root site and public AgentCheck files remain untouched.
