# Nawaz Muztaba — Cybersecurity Portfolio

A public portfolio of security engineering, AI-agent authorization research, detection engineering and application security work.

**Website:** [nawazmuztaba.github.io](https://nawazmuztaba.github.io/)  
**Projects section:** [View portfolio projects](https://nawazmuztaba.github.io/#projects)

## Featured case study — AgentCheck V2 Alpha

**[Read the visual technical case study](https://nawazmuztaba.github.io/projects/agentcheck-v2/)** · **[Browse the public project documentation and demonstration](projects/agentcheck-v2/)**

AgentCheck is a local research experiment within APEX PermitLab. It asks whether an application-owned authorization Guard can prevent a forbidden AI-agent tool request from reaching a disposable SQLite resource, even when the agent encounters malicious instructions in a synthetic retrieved document.

The observed local Qwen test **did not generate the forbidden payroll request**. A separate deterministic forbidden-request control was **denied before the protected handler ran**, with zero recorded service reads. The results are deliberately kept distinct.

The private V2 implementation's final PR-head CI passed **1,274 tests on each of Python 3.11/3.12/3.13** with **95.22% branch-aware coverage**. The public repository includes a smaller independent educational Python/SQLite demonstration with **8 tests per Python version**, not the full private framework.

### Start here

- [AgentCheck case study](projects/agentcheck-v2/CASE_STUDY.md) — problem, architecture, engineering decisions and findings
- [Evidence and test methodology](projects/agentcheck-v2/EVIDENCE.md) — what CI proved versus what was owner-reported
- [Synthetic Guard demo](projects/agentcheck-v2/demo/README.md) — self-contained Python standard-library example, no Ollama or external APIs
- [Security and rights boundaries](projects/agentcheck-v2/SECURITY.md) — explicit non-production scope and usage limitations

## Other public projects

- [Sentinel-X — VAPT and Attack Surface Research](https://github.com/NawazMuztaba/Sentinel-X)
- [Intelligent SOC Automation](https://github.com/NawazMuztaba/intelligent-soc-automation)

## Scope and attribution

The public AgentCheck demo is a **fictional, independently written educational reconstruction** and must not be confused with the private V2 research code. This portfolio does not claim a production security gateway, universal prompt-injection protection, authenticated external SIEM telemetry, or a successful Qwen hijack in the observed experiment.

The complete APEX PermitLab development repository remains private. No general open-source reuse license has been selected for the published case-study/demo files.

**Research and portfolio owner:** [Nawaz Muztaba](https://github.com/NawazMuztaba).
