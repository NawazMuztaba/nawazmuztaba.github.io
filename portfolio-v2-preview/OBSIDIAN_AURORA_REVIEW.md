# Obsidian Aurora — Portfolio V2 experiment

**Review status:** DRAFT / HOLD. This is a reversible variant built on the original-globe branch. It is **not a live-site change** and does not authorize a merge.

## Why this variant exists
The previous original-globe integration accidentally inserted the canvas into the technology `<ul>` and left broken HTML. The browser therefore placed the globe below the hero rather than right of the text. The owner approved fixing the layout **and** trying Obsidian Aurora colors, provided the exact original version remains available to revert to.

## Changes made
1. `index.html`: repaired balanced, semantic hero markup. Two sibling grid children: `.hero-copy` on the left and `.hero-visual.legacy-hero` on the right. Restored fourth skill tag FortiSIEM (learning). Deleted corrupted leftover markup. Project cards and other content unchanged.
2. `styles.css`: desktop widths over 900px use a 55/45-ish grid; heading font scales appropriately. At 900px and below, content stacks intentionally. Original 340px canvas, 360/400/440px rings and animation timing retained. Outer ring colors adjusted and a cheap radial glow added without postprocessing.
3. `original-globe.js`: **only material colors and a provenance comment** changed. Geometry, counts, transforms, per-frame motion, renderer size, orbit speeds and sprite sizes are unchanged.

| Element | Original | Experimental |
|---|---|---|
| Emerald structures | `0x00ff41` | `0x34e2a8` |
| Red radar/satellite | `0xff2244` | `0xff4d6d` |
| Cyan satellite/ring | `0x00e5ff` | `0x49ddf5` |
| Dark center | `0x010801` | `0x040b14` |
| Main bright node | Original green | Ice-aqua `0xa7fff0` |
| Outer CSS rings | Original neon green faint | Emerald/cyan low opacity |

## Rollback
- **Original untouched:** branch `feat/portfolio-v2-original-globe-20261107`, draft PR #6.
- **Experiment:** branch `feat/portfolio-v2-obsidian-aurora-20261107`, its own draft PR targeting original branch.
- If owner dislikes colors, use original branch/PR #6 as reference and retain ONLY the corrected HTML/layout CSS; do **not** merge the experimental palette. An exact reversion should restore original material values while keeping the structural correction. No content is lost.

## Evidence & known limits
- 15/15 static checks passed (balanced HTML tree, JS syntax, CSS braces, old animation block equality, responsive rules, correct link scopes, no old PDF links).
- **Not yet confirmed:** real browser appearance, colorimetry, frames per second, touch/mobile visual, keyboard and reduced-motion behavior. The original renderer has an uninterrupted requestAnimationFrame loop; this experiment does not claim to fix historical FPS drops.
- The original Three.js r128 and 340px renderer are retained to maximize behavioral parity, but upgrading an old dependency belongs in a separate future review.
- Nothing in `main` or `projects/agentcheck-v2/` changed.

## Local visual check
1. Open experiment branch on GitHub and download a fresh ZIP.
2. Extract and open `portfolio-v2-preview`.
3. Run `python -m http.server 8000`.
4. Visit `http://localhost:8000/`, press Ctrl+Shift+R. (Serving from repository root instead? Use `http://localhost:8000/portfolio-v2-preview/`.)
5. Compare left/right composition at 1440 × 900 and mobile 390 × 844; capture screenshot and observe motion/FPS.
6. If not satisfied, state **“revert palette”** and restore original colors with the corrected grid.
