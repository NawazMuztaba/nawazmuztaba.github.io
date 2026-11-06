# Phase 2 Content and Evidence Audit
**Source hierarchy:** 2026-11-07 owner-provided revised one-page resume (working reference); live GitHub main HTML reviewed read-only; public AgentCheck study and its README; previously observed private-repo CI facts are prior chat context, requiring re-check before republishing. Owner claims are not independently verified merely because they are in a resume.

## Current GitHub evidence inspected
- Repository: NawazMuztaba/nawazmuztaba.github.io; main index.html was 1,165 lines with title "Nawaz Muztaba | Penetration Tester" and Three.js r128.
- Main index includes old role as Penetration Tester / Red Team Enthusiast, old about, old certification list, an animated fake security boot, percent skills and radar, VAPT internship only, three prior project cards, bogus-looking ATS percentages, a Formspree placeholder ("YOUR_FORM_ID"), and links to soc01.pdf + red01.pdf.
- GitHub fetch_file returned NOT_FOUND for both soc01.pdf and red01.pdf on current default branch when reviewed; do not reuse those download links. Deleted files may remain in history.
- Existing case study page: https://nawazmuztaba.github.io/projects/agentcheck-v2/ and public README. That published README carries an older CI snapshot (1,274 passing each Python 3.11–3.13; 95.22% coverage); later private work was reported to reach 1,295 per version with same coverage. Do NOT combine numbers or change published study without separate review.
- PR #2 (older "feature AgentCheck homepage" proposal): OPEN and deferred; don't merge or alter.
- Main GitHub Pages still uses the existing index (no redesign authorized).

## Proposed public content with verification state
| Area | Working copy / situation | Release gate |
|---|---|---|
| Owner name | Nawaz Muztaba | Owner supplied |
| Positioning | SOC operations / detection automation / bounded AI security research | Accurate framing, no implied production AI gateway |
| SafeAeon | March 2026–Present, SOC monitoring/investigation | Verify company name and **official role** ("SOC Analyst" vs "SOC Analyst Intern"), ensure no sensitive client data |
| Work metrics | Owner resume revised from 650/125/17 to 1000+/250+/30+ alerts/true positives | Do not publish without traceable, privacy-safe evidence; omit if not available |
| Vaishnav | VAPT & penetration testing internship, Jan–Mar 2025 | Verify exact location and description; avoid exposing private customers |
| FortiSIEM | Currently learning/training | Must label as learning unless verified hands-on professional use |
| Microsoft Defender / KQL | In current resume as working knowledge | Avoid overstating scope |
| Education | B.Tech CSE Cybersecurity, LPU, 2022–2026, CGPA 7.5 | Verify completion status; remove "final-year" and "graduating May 2026" if dated |
| Intelligent SOC Automation | Python / Redis / log detection / SIEM-style simulated events | Verify repo URL, timing and metrics (1,000+, 8+, 200+, ~40%) before publishing |
| Sentinel-X | Python VAPT / scanning and assessment | Date conflict: original resume Aug–Nov 2025; latest pasted resume Aug–Sep 2024; verify |
| MobSF | Older project, omitted from main resume | Optional archive, not top-three featured work |
| AgentCheck V2 Alpha | Local Qwen/Ollama with independent Guard, synthetic SQLite evidence; public bounded technical case study | Safe to feature with exact caveats |
| DP-900 | Microsoft Azure Data Fundamentals certification in resume | Verify credential link if possible; use accurate official title |
| CTIGA, DFE, Google Cloud/Coursera, NPTEL | Listed in owner's latest resume | Verify issuer, certificate type and links |
| CEH / eJPT / CompTIA Linux+ | Claims in old homepage, NOT supported as earned by latest resume | Remove as earned until actual evidence; do not imply CEH-certified professional |
| Resume PDFs | Previous soc01.pdf/red01.pdf deleted on current main; updated one-page SOC resume produced in chat | Recheck actual approved file and consent before publishing it, don't reintroduce old PDFs |

## Project-specific claims (careful)
AgentCheck observed Qwen indirect prompt injection: lower-trust document reached Qwen, but the model did NOT make an unauthorized payroll tool request. Separate deterministic forbidden-call test was denied before a protected SQLite read; this establishes the Guard decision boundary in the bounded synthetic setup, not an observed successful model-hijack prevention. No production agent integration, public disclosure of private source or general immunity claim. Private CI total is project/repository-wide, not "AgentCheck only". If displaying any CI metric cite date+scope and verify recent run.

## Operational quality and policy
- Broken resume links critical.
- Formspree fallback mailto shows success despite no confirmed send; change to actual mailto link, or configure provider + await acknowledged success. Avoid public form unless spam/protection is handled.
- Boot screen claims 847 firewall rules, blocked attacks, CEH verified, Burp Suite Pro ready; these are theatrical, NOT operational facts. Replace with honest styling only.
- Percent skill bars and CVSS scores are unsupported measurements and give false precision; use skill categories and demos.
- Use semantic titles, meta description, Open Graph image, favicon, keyboard navigation and reduced-motion support.
- Don't expose email addresses beyond owner-approved public contact; never expose personal phone number by default just because it was in a resume.
- No API keys, customer data, logs or other private case details in repository.
