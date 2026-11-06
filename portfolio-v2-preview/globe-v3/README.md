# APEX Globe V3 — Fidelity-first motion proof

**State: REVIEW ONLY.** Parent portfolio prototype PR #4 remains unmerged. This branch creates a separate V3 proof, based on the exact owner-selected artwork (1448×1086). **Neither main, root index.html, nor projects/agentcheck-v2/** are changed.

## What changed
The V2.1/V2.2 WebGL reinterpretations did not visually match the owner-approved image and the owner reported frame drops. V3 keeps that image visually intact as a single optimized high-quality WebP while moving red/green signal dots and minimal scan rings using SVG/CSS. There is no Three.js, per-frame JS loop, bloom postprocessing or fictional real-time events.

**Critical:** A single 2D picture cannot be a physically accurate, pixel-identical 360° 3D model. This demo **does not rotate Earth**. It is an animated, reference-faithful design prototype for art-direction signoff. A separate 3D reconstruction would be a further optional trade-off.

## Required image asset (not in GitHub yet)
The verified original image is supplied by owner in ChatGPT, 1448×1086 RGBA, SHA-256:
`d07e72b4a32774f4fbf926c990209d5d91b6dca7021a945ecc1e422050ec8569`.

A compressed high-quality **globe-reference.webp** is included in the complete local downloadable ZIP, along with original PNG, full CSS/JS, spec and a runnable preview. This GitHub connector cannot attach binary bytes directly from this session. To make the GitHub branch copy work, upload the included `globe-reference.webp` into `portfolio-v2-preview/globe-v3/assets/` **on this feature branch only**. Do not upload to main.

## Preview
From the full extracted local folder run `python -m http.server 8000` and open http://localhost:8000/. For this GitHub path, after image upload, serve the repository locally and visit `http://localhost:8000/portfolio-v2-preview/globe-v3/`.

## Evidence
- Headless Chromium exercised desktop 1440×900, mobile 390×844 and reduced motion; asset loaded, no JavaScript page errors or horizontal overflow.
- A red orbit signal changed coordinates over 950ms; after clicking Pause, its coordinates remained unchanged for 850ms.
- Headless browser is **not** the owner's hardware; benchmark FPS there separately.
- Need owner visual approval before integrating into the portfolio hero. Neither PR #3 nor #4 should be merged for V3.
