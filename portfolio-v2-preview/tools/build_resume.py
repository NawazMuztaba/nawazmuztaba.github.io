#!/usr/bin/env python3
"""Reproducible, one-page portfolio resume PDF.

Source: owner-supplied Nawaz_Muztaba_Resume.pdf, November 2026.
Only two editorial fixes: fully spell out AI-Agent Tool Authorization and use
the direct public AgentCheck case-study URL. Original self-reported numerical
achievements are retained, not independently certified by this generator.
Personal telephone is deliberately included with owner's explicit approval.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

INK=colors.HexColor("#192132")
NAVY=colors.HexColor("#243954")
ACCENT=colors.HexColor("#087C83")
MUTED=colors.HexColor("#506078")
W,H=A4
M=37.5
WIDTH=W-2*M
AGENTCHECK="https://nawazmuztaba.github.io/projects/agentcheck-v2/"
SOC_REPO="https://github.com/NawazMuztaba/intelligent-soc-automation"
SENT_REPO="https://github.com/NawazMuztaba/Sentinel-X"
LINKEDIN="https://www.linkedin.com/in/nawaz-muztaba/"
GITHUB="https://github.com/NawazMuztaba/"
EMAIL="nawazmuztaba000@gmail.com"
PHONE="+91 6200289203"

def build(path: Path):
    path.parent.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(path),pagesize=A4,pageCompression=1)
    c.setTitle("Nawaz Muztaba | SOC Analyst - Portfolio Resume")
    c.setAuthor("Nawaz Muztaba")
    c.setSubject("Owner-provided cybersecurity resume, corrected technical-skill line and project link")
    y=H-35.0

    def center(text,font,size,color=INK,after=0):
        nonlocal y
        c.setFillColor(color);c.setFont(font,size)
        c.drawCentredString(W/2,y,text)
        y-=size*1.25+after

    def para(text,sz=8.35,lead=10.8,after=3.8,indent=0,color=INK):
        nonlocal y
        style=ParagraphStyle("body",fontName="Helvetica",fontSize=sz,leading=lead,
                             textColor=color,alignment=TA_LEFT,spaceBefore=0,spaceAfter=0,
                             allowWidows=0,allowOrphans=0)
        p=Paragraph(text,style)
        _,h=p.wrap(WIDTH-indent,1000)
        p.drawOn(c,M+indent,y-h)
        y-=h+after

    def section(label):
        nonlocal y
        y-=7
        c.setFillColor(NAVY);c.setFont("Helvetica-Bold",9.25)
        c.drawString(M,y,label.upper())
        c.setStrokeColor(ACCENT);c.setLineWidth(0.65)
        c.line(M,y-3.9,W-M,y-3.9)
        y-=13.4

    def line(left,right="",url=None,after=4.1,sz=8.2):
        nonlocal y
        c.setFillColor(INK);c.setFont("Helvetica-Bold",sz)
        c.drawString(M,y,left)
        if url:
            x=M+c.stringWidth(left,"Helvetica-Bold",sz)+7
            c.setFillColor(ACCENT);c.setFont("Helvetica",8.1)
            c.drawString(x,y,"GitHub")
            c.linkURL(url,(x,y-2,x+34,y+9),relative=0)
        if right:
            c.setFillColor(MUTED);c.setFont("Helvetica",7.6)
            c.drawRightString(W-M,y,right)
        y-=10.3+after

    def bullet(text):
        nonlocal y
        c.setFillColor(ACCENT);c.setFont("Helvetica-Bold",8)
        c.drawString(M+4,y-7,"-")
        para(text,sz=8.05,lead=10.35,after=2.1,indent=14)

    center("NAWAZ MUZTABA","Helvetica-Bold",18.8,INK,after=0.6)
    center("SOC Analyst  |  Security Monitoring & Incident Investigation",
           "Helvetica",9.15,NAVY,after=2)
    # Contact line includes owner's explicitly approved public telephone.
    contact=(f"Mohali, Punjab, India  |  Open to Relocation  |  {PHONE}  |  "
             f'<link href="mailto:{EMAIL}" color="#087C83">{EMAIL}</link>  |  '
             f'<link href="{LINKEDIN}" color="#087C83">LinkedIn</link>  |  '
             f'<link href="{GITHUB}" color="#087C83">GitHub</link>')
    style=ParagraphStyle("contact",fontName="Helvetica",fontSize=7.8,leading=10.2,
                         alignment=1,textColor=MUTED)
    p=Paragraph(contact,style);_,ph=p.wrap(WIDTH,1000);p.drawOn(c,M,y-ph)
    y-=ph+1.0

    section("Professional Summary")
    para("SOC Analyst with hands-on experience in security alert triage, authentication and endpoint analysis, incident reporting, and severity-based escalation. Experienced with Rapid7 InsightIDR, SentinelOne, and Jira, with working knowledge of Microsoft Defender and KQL. Currently gaining hands-on experience with FortiSIEM for security monitoring and event correlation. Builds Python projects in detection automation, AI-agent authorization, and adversarial testing.",sz=8.0,lead=10.4,after=0)

    section("Professional Experience")
    line("SAFEAEON INC.  |  SOC Analyst  |  Mohali","Mar 2026 - Present",after=1.5)
    bullet("Investigated and triaged <b>1,000+ security alerts</b> across client environments using Rapid7, SentinelOne, and Jira; identified <b>250+ reportable alerts</b>, including <b>30+ client-verified true positives</b> covering authentication anomalies, account lockouts, privilege changes, mailbox activity, and malware-related events.")
    bullet("Performed incident investigation using up to <b>seven days of historical authentication, endpoint, process, and related security events</b> to validate alerts, determine reportability, and support escalation.")
    bullet("Prepared client-facing incident reports and followed SLA-driven workflows, escalating High/Critical alerts within <b>15 minutes</b> and delivering severity-based investigation reports.")
    y-=4
    line("VAISHNAV TECHNOLOGIES PVT LTD  |  Security Intern - VAPT","Jan - Mar 2025",after=1.5)
    bullet("Conducted web and network VAPT using <b>Burp Suite, Nmap, OpenVAS, and Nikto</b>, identifying SQL injection, XSS, exposed services, and security misconfigurations.")
    bullet("Performed post-exploitation and privilege-escalation exercises; documented findings using <b>CVSS</b> and supported red-team exercises through IOC analysis and MITRE ATT&amp;CK mapping.")

    section("Technical Skills")
    skills=[
      ("Security Operations","SOC monitoring, SIEM, alert triage, log analysis, incident investigation, reporting, escalation"),
      ("Platforms & Tools","Rapid7 InsightIDR, SentinelOne EDR, Microsoft Defender, Jira, Wireshark, Nmap, Burp Suite"),
      ("Querying & Scripting","Kusto Query Language (KQL), Python, SQLite"),
      ("Systems & Networking","Windows, Linux, TCP/IP, DNS, HTTP/HTTPS, DHCP, VPNs, firewalls, traffic analysis"),
      ("Frameworks","MITRE ATT&amp;CK, OWASP Top 10, vulnerability assessment"),
      ("Security Analysis","Authentication and endpoint logs, IOC analysis, prompt-injection testing, <b>AI-Agent Tool Authorization</b>"),
    ]
    for label,skills_text in skills:
        para(f"<b>{escape(label)}:</b> {skills_text}",sz=7.95,lead=10.0,after=1.4,indent=0)

    section("Projects")
    line("Intelligent SOC Automation System","Dec 2025 - Jan 2026",url=SOC_REPO,after=1.4)
    bullet("Built a SIEM-style detector processing <b>1,000+ simulated log events</b> and correlating <b>8+ attack patterns</b>, including brute force, port scans, and anomalous authentication, with MITRE ATT&amp;CK mapping.")
    bullet("Added severity-based prioritization and a Redis alert queue handling <b>200+ concurrent events</b>; reported a <b>~40% triage-time reduction</b> across five simulated scenarios.")
    y-=2
    line("AgentCheck V2 Alpha - AI-Agent Tool Authorization","Nov 2026",url=AGENTCHECK,after=1.4)
    bullet("Built a local Python/Qwen/Ollama testbench for indirect prompt-injection cases, strict tool-call validation, independent Guard authorization, and auditable SQLite side effects.")
    bullet("Verified one forced unauthorized tool request was denied before SQLite access; private PermitLab CI recorded <b>1,295 tests per Python version</b> (3.11-3.13) and <b>95.22% branch coverage</b>.")
    y-=2
    line("Sentinel-X - Automated VAPT & Attack Surface","Aug - Sep 2024",url=SENT_REPO,after=1.4)
    bullet("Automated assessment across <b>10+ target environments</b>, reporting <b>25+ misconfigurations</b> including exposed services, firewall gaps and weak TLS settings, with NIST CSF-aligned risk scoring.")
    bullet("Developed a Python workflow for recon, service enumeration, TLS analysis and reporting, reporting <b>~60% less manual recon time</b> and remediation-focused reports.")

    section("Certifications & Training")
    credentials=[
      "Microsoft Certified: Azure Data Fundamentals (DP-900) - Microsoft",
      "Certified Threat Intelligence & Governance Analyst (CTIGA) - Red Team Leaders",
      "Logging and Monitoring in Google Cloud - Google Cloud / Coursera",
      "Digital Forensics Essentials (DFE) - EC-Council / Coursera",
      "Cloud Computing - NPTEL, IIT Kharagpur",
    ]
    for name in credentials:
        para(escape(name),sz=7.8,lead=9.55,after=0.65)

    section("Education")
    line("B.Tech. in Computer Science & Engineering, Cybersecurity Specialization",
         "2022 - 2026",after=1,sz=7.9)
    para("Lovely Professional University, Phagwara, Punjab  |  CGPA: 7.5",sz=8,lead=10,after=3,color=MUTED)
    line("Senior Secondary (12th Grade) - PCM","2019 - 2021",after=1.2,sz=8)
    para("Trident Public School, Muzaffarpur, Bihar  |  84%",sz=8,lead=10,after=0,color=MUTED)

    if y<M-4:
        raise RuntimeError(f"Resume content exceeds one A4 page: bottom={y:.1f}pt (minimum {M-4:.1f}pt)")
    c.showPage()
    c.save()
    return y

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,
        default=Path(__file__).resolve().parents[1]/"assets"/"Nawaz_Muztaba_Resume.pdf")
    args=parser.parse_args()
    bottom=build(args.output)
    print(f"Created {args.output} (remaining bottom space: {bottom:.1f}pt)")
