# Responsive Wireframes / Content Architecture
**Status:** Phase 2 approved direction; textual wireframes are canonical layout intent, not pixel-perfect implementation.

## Navigation and information architecture
Home consists of:
1. Hero: professional identity, short SOC/AI security intro, two CTAs, signature globe
2. Featured Work: AgentCheck V2 Alpha / Intelligent SOC Automation / Sentinel-X
3. Professional Experience: SafeAeon / Vaishnav, factual timeline
4. Technical Capabilities: SOC/Detection / Security Engineering / AI Security Research / VAPT
5. About & Education: B.Tech CSE with Cybersecurity specialization, no outdated "final-year" claim after graduation without verifying degree status
6. Credentials: earned and verified only, verification links when available
7. Contact: email / LinkedIn / GitHub / resume link, avoid false success messages

### Desktop 1440px (max content ~1200px, 12-column)
~~~
+------------------------------------------------------------------+
| NM                       Work Experience About Contact  [Resume] |
+------------------------------------------------------------------+
| EYEBROW: SOC OPERATIONS / AI SECURITY / SECURITY ENGINEERING       |
|                                                                  |
| Nawaz Muztaba                 +--------------------------------+  |
| I investigate threats.        |  BIG INTERACTIVE 3D GLOBE     |  |
| I build safer systems.        |  recognizable cyan Earth      |  |
| Real, concise intro           |  emerald orbits + nodes       |  |
| [Explore Projects] [Resume]   |  restrained labels            |  |
|                                 +-------------------------------+ |
+------------------------------------------------------------------+
| FEATURED SECURITY PROJECTS                                       |
| [AgentCheck V2 Alpha] [Intelligent SOC Automation] [Sentinel-X]  |
| concise evidence    concise evidence        concise evidence     |
+------------------------------------------------------------------+
| PROFESSIONAL EXPERIENCE           | TECHNICAL CAPABILITIES       |
| SafeAeon + Vaishnav               | SOC/AI security/Python/VAPT  |
+------------------------------------------------------------------+
| ABOUT / EDUCATION                 | VERIFIED CREDENTIALS          |
+------------------------------------------------------------------+
| CONTACT / EMAIL / LINKEDIN / GITHUB / RESUME                      |
+------------------------------------------------------------------+
~~~
Hero 2 columns around 55/45. At 1440 top nav visible, project cards begin near fold. Desktop globe should look as close as feasible to the original approved ChatGPT concept, not be reduced to a simple outline icon.

### Tablet ~768–1024
Nav collapses thoughtfully; hero may become stacked around 960px depending on content. Project cards use 2 columns or 1 as required by actual readable width. Keep labels and CTA access. Globe may simplify in geometry/texture and controls.

### Mobile ~390x844
~~~
+-------------------------+
| NM                  [☰] |
+-------------------------+
| SOC / AI SECURITY       |
| Nawaz Muztaba           |
| I investigate threats.  |
| I build safer systems.  |
| Concise intro           |
| [Explore Projects]      |
| [View Resume]           |
| [Static globe image]    |
+-------------------------+
| FEATURED PROJECTS       |
| [AgentCheck V2 Alpha]   |
| [SOC Automation]        |
| [Sentinel-X]            |
+-------------------------+
| EXPERIENCE               |
| SKILLS                   |
| ABOUT / EDUCATION        |
| CREDENTIALS              |
| [CONTACT]                |
+-------------------------+
~~~
Mobile: 16–20px padding, target about 44x44px or larger, all links keyboard/touch reachable, static fallback preferred by default, never force a high-GPU animation. No horizontal scrolling; no important data behind hover.

## Project card system
Each card contains: truthful problem statement, what owner built, one evidence/capability line, restrained tech tags, explicit clickable "View case study" or "View GitHub" linking to a publicly accessible page. Distinguish private source project from public demo.
For AgentCheck: link https://nawazmuztaba.github.io/projects/agentcheck-v2/; description must say independent application Guard controls locally simulated tool actions, NOT that model was successfully hijacked and blocked.
For SOC Automation and Sentinel-X: confirm public GitHub repo paths and metrics before showing them.

## Accessibility states
Keyboard menu open/close, active nav, visible focus; links and buttons have text labels. Globe pause button accessible; globe is decorative unless meaningful data has an equivalent text description. Body content visible without JavaScript. Respect user prefers-reduced-motion.

## Do not propagate mockup hallucinations
The generated wireframe contains example work dates and decorative text; its exact *visual arrangement* is approved, not its factual text. Consult CONTENT_AUDIT.md before publishing.
