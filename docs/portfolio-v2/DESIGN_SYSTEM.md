# Approved Design System — Direction A
**Status:** Approved art direction, not yet pixel-perfect production implementation.

## Brand and recruiter brief
Audience: SOC hiring managers, junior detection engineering teams, AI security teams, VAPT recruiters, and global technical contacts. The tone must say "security practitioner with auditable technical work", not "fictional hacker terminal". Prioritize credibility, ease of scanning, technical proof and two-click contact.

## Locked visual concept
- Style: premium dark cybersecurity / precise engineering / tasteful cinematic cyberpunk; deep navy rather than black-green.
- Signature: *large* luminous globe at right of hero on desktop; Earth landmasses recognizable (not only random wireframe polygon), soft cyan atmosphere, scattered emerald nodes, sparse curved orbital paths, subtle contour/grid lines. Slightly 3D and elegant. It should echo the generated 1672×941 concept image identified in VISUAL_REFERENCES.md.
- Desktop hero: logo NM upper left; nav Work, Experience, About, Contact; resume outline button upper right. Left hero ~55%: tiny eyebrow SOC OPERATIONS / AI SECURITY / SECURITY ENGINEERING, bold Nawaz Muztaba (white + cyan accent), tagline "I investigate threats. I build safer systems." with emerald accent on "safer systems"; one short evidence-grounded paragraph, prominent emerald "Explore Projects" button and outlined "View Resume" button. Under hero CTAs, tiny truthful skill chips. Right hero ~45%: large orbiting globe with **optional** subtle callouts, NOT fictitious live telemetry.
- Beneath fold: Featured / Selected Work as 3 separate premium cards with icon art, clear description and 2-4 technology chips; AgentCheck first. Balanced cyan/green lines, no excessive glow.
- High density but breathing room: subtle geometric background grids, extremely low-opacity dots, restrained separators and glass-like panels; avoid heavy noise or constant Matrix rain.

## Design tokens
| Token | Value | Use |
|---|---|---|
| background | #07111D | Main canvas |
| surface | #112536 | Cards/panels |
| text | #F0F6FA | Primary |
| cyan | #31E5E2 | Accent, outlines, 3D glow |
| emerald | #19D99A | Primary CTA, verified positive status |
| muted | #9CB8C8 | Supporting copy (confirm WCAG contrast) |
| border | #315269 | Subtle separators |
| caution | #FFC777 | Warnings, unverified/limitation labels |
| near-black | #040C14 | Deep globe backdrop |

Typography: accessible readable modern sans (e.g. Inter/system font) for headlines and body; technical monospace only for section labels and code snippets. Prefer ~16px body and line height 1.5+, large clear hero title. Avoid all-uppercase body copy and letter-spacing that harms reading.

## Visual hierarchy
1. Professional name/title; 2. concrete value statement; 3. accessible CTAs; 4. evidence-bearing work; 5. real experience and capabilities; 6. credentials/about; 7. contact.
Content more important than animation. No boot screen. Motion only for globe and sparing microinteractions. Ensure reduced-motion support, visible focus states, color contrast, touch targets, semantic headings, and static content without JS.

## Approved content
Hero: "I investigate threats. I build safer systems."
Role strip: "SOC Operations / AI Security / Security Engineering".
Short intro working draft: "SOC practitioner working across alert investigation, detection automation, and AI-agent security research." Tune after fact verification. This is a positioning statement, not a claim of production deployment for AI security.
Contact CTA use "Let's connect" or "Contact", not "Ready to breach the job market".
Project cards: AgentCheck / Intelligent SOC Automation / Sentinel-X. Don't use invented threat-severity badges or CVSS for unrelated projects.

## Interaction system
- Navbar fixed/sticky after scroll, no overlay of anchor targets.
- Links distinguishable without hovering; keyboard focus visible.
- Cards can have slight elevation and border glow on hover; never auto-expand core information only on hover.
- Desktop ~1440 artboard, content width ~1200, max 12-column grid.
- Tablet 6-column or 2-column; mobile single column.
- Spacing scale 8, 16, 24, 32, 40, 48, 64, 80.
- Never rely on a single hero image as alt-text substitute.
- Motion reduced when prefers-reduced-motion or user pause; pause on tab invisibility.
- Do NOT reuse AI-generated mockup text values/dates as factual site copy.
