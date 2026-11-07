# Portfolio V2 M4 — Latest Resume Reconciliation and Publication Gate
**Source:** User-uploaded `Nawaz_Muztaba_Resume.pdf` in the ChatGPT conversation on 2026-11-07. **Do not commit this document's private source PDF to public GitHub automatically.** This page contains only editorial findings; **no phone number or other private contact identifier** is copied from the PDF.
**State:** Draft content alignment, not employment/credential verification or resume publication approval.

## 1. Incoming resume review
- PDF: one A4 page, 329,220 bytes (322 KiB); rendered and visually inspected on 2026-11-07.
- The top-level header describes owner as `SOC Analyst | Security Monitoring & Incident Investigation` and lists SafeAeon as `SOC Analyst`, March 2026–present. Previous 2026 offer documents and earlier chats listed `SOC Analyst (Intern)`; no later HR conversion/regular-employee record has yet been independently reviewed. **Latest owner-authored resume supersedes the earlier portfolio draft for displayed title, but official employment type remains an unresolved publication gate.**
- SOC work in resume: alert investigation/triage, retrospective authentication and endpoint analysis, reportability, incident reports and severity-based escalation; Rapid7 InsightIDR, SentinelOne, Jira, Microsoft Defender/KQL as working knowledge and FortiSIEM as learning/in progress.
- Vaishnav: security internship (VAPT/pentesting), Jan–Mar 2025, with Burp Suite, Nmap, OpenVAS, Nikto, OWASP/CVSS and documented remediation.
- Education: LPU B.Tech CSE (Cybersecurity) 2022–2026; resume states CGPA `7.5`, reflecting owner's previously approved rounded `7.48`. Degree award/graduation completion **not yet independently verified**.
- Credential names as self-reported in resume (not independently issuer-validated here):
  1. Microsoft Certified: Azure Data Fundamentals (DP-900)
  2. Certified Threat Intelligence & Governance Analyst (CTIGA) — Red Team Leaders
  3. Logging and Monitoring in Google Cloud — Google Cloud / Coursera
  4. Digital Forensics Essentials (DFE) — EC-Council / Coursera
  5. Cloud Computing — NPTEL / IIT Kharagpur
  Owner previously reported passing DP-900 in April 2026; do not infer that all entries are proctored certification exams. Verify issuer-specific credential URL and correct credential type (certification/course/certificate) before creating public badges.

## 2. Resume numerical claims — retain in owner's resume, evidence gate for public marketing
**Do not automatically remove metrics that owner may have independently observed, but do not transplant them into public showcase as verified outcomes until methodology/permission is documented.**
- SafeAeon: `1000+` security alerts, `250+` reportable cases, `30+` client-verified true positives; historical analysis up to seven days; High/Critical `15 minutes` escalation and SLA-based reporting. Evidence requested: time window, distinct alert/case counting method, permission to publish aggregates, and clarification of `client-verified` label without disclosing any client identifiers.
- SOC automation project: `1,000+` simulated log events, `8+` patterns, `200+` concurrent events, `~40%` claimed triage-time improvement in five scenarios. Evidence requested: synthetic dataset, test harness, baseline/treatment timing, alert queue concurrency definition and logs. Source-code presence alone does not verify outcomes.
- AgentCheck/PermitLab: 1,295 CI tests per Python version and 95.22% branch coverage reported in resume. Existing public case study and private CI evidence must be linked without revealing private repo; model-security success must remain distinct from independent guard enforcement.
- Sentinel-X: `10+` target environments, `25+` misconfigurations, `~60%` recon time reduction, NIST CSF alignment. Require authorization/provenance for every target and repeatable timing methodology; refrain from promoting third-party artifacts publicly until privacy/authorization review.
- Do not include actual customer alerts, hostnames, IPs, confidential investigations or raw third-party scan results in public portfolio.

## 3. PDF technical review and publication blockers
- The PDF is compact and its email, LinkedIn, main GitHub and three project hyperlinks are embedded; it is technically suitable in size for website hosting.
- **Visible PDF clipping:** the last Technical Skills bullet ends with `AI-Agent Tool Authorizatio`; edit the source Word document and re-export before publishing.
- **AgentCheck link:** currently goes to a GitHub tree path with `utm_source=chatgpt.com`, not the canonical public case-study route. Prefer `https://nawazmuztaba.github.io/projects/agentcheck-v2/` once approved.
- Verify other live links and spelling; don't claim the PDF is polished/final until rendered and inspected again.
- **Public privacy:** current PDF contains a personal phone number and email. Uploading to a **public GitHub branch, commit history, GitHub Pages or CDN** makes those details publicly accessible, even if the PR remains a draft. Owner must decide whether the public PDF should retain the number or use a contact-only version. Avoid committing exact uploaded PDF without this decision and without review of its project metrics and exposed third-party claims.
- **Serving policy:** Keep the working `mailto:` `Request resume` CTA until there is an approved and accessible PDF asset. Never point `Download resume` at a missing file or embed an unreadable base64 PDF into HTML. Upon approved asset creation, switch CTAs atomically, verify HTTP 200 and PDF content type, keyboard accessibility, and cache behavior. Keep a rollback.

## 4. M4 draft updates already staged in review PR #10
- New PR branch: `feat/portfolio-v2-m4-identity-20261107` -> prototype branch (NOT `main`).
- The latest resume's owner-selected `SOC Analyst` title is used in the **review draft** instead of stale `Intern`. Its contractual employment type **is still not officially confirmed by this audit**.
- Clarified investigation/reporting activity, accurate `Microsoft Defender (working knowledge)` and `KQL (working knowledge)`, FortiSIEM as learning, and LPU CGPA `7.5/10 (resume-listed)`. No unverified project numerical metrics added to the website.
- Existing project cards, navigation, hero, original globe source/color/geometry, and all protected code remain unchanged.
- Review QA run: https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42325218872; confirm final pass/fail before merging.
- First M4 QA run had a test-harness null-selector error on old baseline; fixed in newer run. Do not confuse test exceptions with validated visual regressions.

## 5. Next steps
1. Complete PR #10 Chromium QA, inspect desktop/mobile screenshots, confirm source-only changes, and request owner review. **Do not merge into `main`.**
2. Re-export resume after correcting the clipped skill line and AgentCheck link. Preserve relevant defensible metrics in owner copy, but document counting method and release permission.
3. Ask for an explicit public-download privacy choice (retain personal mobile number vs omit it from public version) before uploading any PDF to the public repo.
4. Collect verified issuer links/credential evidence and confirm employment-type conversion/degree award before final credential/experience badges.
5. Implement verified credential display and approved download asset in a separate M4.2 review PR with full QA; final publication stays behind PR #4 and release gate.

## Guardrails
- Original globe blob baseline `1be0c45a592aa54aa78bf42682964a0d11303977`.
- PR #9 merged into prototype at `ef27f795a63cc3e86e2fe8ce7d7d0f64c89adbff`.
- No edits to production `main`, public AgentCheck case-study code, Sentinel-X/SOC repos or private PermitLab repo.
