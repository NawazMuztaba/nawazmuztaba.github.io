# Portfolio V2 — Original Resume Hosting & View/Download Integration
**Checkpoint:** 2026-11-07 | **Status:** REVIEW BRANCH ONLY; NOT DEPLOYED

## Owner's explicit correction and approval
- The owner explicitly rejected creating/regenerating a resume. The deliverable is hosting the **existing uploaded one-page PDF** and wiring reliable **View Resume** and **Download PDF** website controls.
- The owner explicitly approved keeping their personal phone number visible in the public resume. Do not remove it without a new instruction.
- The original uploaded PDF **was not rewritten or replaced**. An unnecessary generated-resume Python script was added during an early attempt and then deleted from M4 branch; there is **no net generator file** in the pull request.
- Separate editorial observations regarding a clipped skills line and a suboptimal AgentCheck hyperlink remain suggestions for a future owner-authorized resume update. **These issues were not silently edited in the current PDF.**

## Exact source artifact
| Property | Verified value |
|---|---|
| Original conversation upload | `Nawaz_Muztaba_Resume.pdf` |
| Original byte count | `329220` |
| Original SHA-256 | `94725e11537ad488169299a0cd5351c64134402dae06ee877e7897b80c8ae221` |
| Original Git blob SHA-1 | `1fd52b57cc228cddb2e85079c5bd9cc933b7753e` |
| Destination repository | `NawazMuztaba/nawazmuztaba.github.io` |
| M4 review branch | `feat/portfolio-v2-m4-identity-20261107` |
| Committed PDF path | `assets/Nawaz_Muztaba_Resume.pdf` |
| Production status | Not on `main`, not yet available as production-site PDF |

The exact original PDF bytes were transferred to the connected GitHub repository as a base64-encoded Git blob and checked against the independently computed Git blob SHA-1. The temporary transport text copy was moved to Trash from the personal Library; only the original Git PDF asset is committed to the PR branch.

## Website actions
**View:** `<a href="/assets/Nawaz_Muztaba_Resume.pdf" target="_blank" rel="noopener noreferrer" type="application/pdf">View resume</a>` in navigation and hero. This normally opens the PDF in a new browser tab with the browser's PDF reader.

**Download:** `<a href="/assets/Nawaz_Muztaba_Resume.pdf" download="Nawaz_Muztaba_Resume.pdf" type="application/pdf">Download PDF</a>` in the hero. The same-origin `download` attribute instructs modern browsers to save the file with a stable filename.

Both are root-relative URLs pointing to the same repository-root PDF asset, independent of preview versus future homepage location. Existing email-contact actions are not altered.

## Automated verification
- M4-specific Chromium suite: `qa/portfolio-v2/m4_identity_qa.py` checks responsive widths, navigation, preserved original globe source, and no unexpected changes to old content; its M3 baseline is adjusted by **only** the two explicitly approved resume-CTA changes.
- PDF-specific Chromium suite: `qa/portfolio-v2/resume_pdf_qa.py` verifies:
  - the binary local file's exact SHA-256 and length,
  - valid PDF header/trailer,
  - HTTP 200 and `application/pdf` MIME type,
  - both visible action URLs, new-tab target and download filename,
  - no horizontal overflow at 320, 390, 768, 901 and 1440px,
  - browser-generated file downloads matching the original PDF SHA-256.
  - the final revision additionally exercises an actual View Resume click and checks its opened URL.
- [Earlier green test run](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42326829430): M4 19 responsive widths and PDF 5 widths, 2 actual saved downloads, **zero reported failures**, original checksum matching.
- [Latest final browser run including View click](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42326967702): final run must be checked before treating the added click assertion as passed.

## Releasing correctly
- Merge **PR #10 into the prototype branch only** after QA, owner visual review, and agreement with content. Merging PR #10 does not itself publish the live homepage.
- PR #4 still targets `main`; do **not** merge it without a separate launch/release decision.
- **Stable URL solution:** the exact original PDF now resides in repository-root `assets/Nawaz_Muztaba_Resume.pdf` on the M4 review branch. The portfolio links are root-relative `/assets/Nawaz_Muztaba_Resume.pdf`, so they work both in `/portfolio-v2-preview/` and from the future root `/` homepage once the asset reaches `main`. No duplicate PDFs or special copy step are required.
- GitHub Pages deployment must include both the approved homepage and the root `assets/` PDF, and a deployed smoke test must confirm HTTP 200, `application/pdf`, and the download filename. Do not advertise a public-live resume URL until the release has occurred.

## Protected boundaries
- Original globe Git blob remains `1be0c45a592aa54aa78bf42682964a0d11303977`.
- `main` unchanged by this integration, PR #4 unmerged, AgentCheck case study and private project source untouched.

## Latest verified asset relocation
The PDF was moved, byte-for-byte, within the draft review branch from the preview assets folder to root `assets/`. The Git blob remains `1fd52b57cc228cddb2e85079c5bd9cc933b7753e` and the SHA-256 remains `94725e11537ad488169299a0cd5351c64134402dae06ee877e7897b80c8ae221`. Root-relative links now use `/assets/Nawaz_Muztaba_Resume.pdf`; the final browser suite is [run #42327524454](https://github.com/NawazMuztaba/nawazmuztaba.github.io/actions/runs/42327524454), whose conclusion must be checked before declaring complete verification.
