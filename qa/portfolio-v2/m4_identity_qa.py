#!/usr/bin/env python3
"""M4 identity QA: real Chromium comparison against verified M3 merge.
Review-only. No outbound assessment scans, deployment, or private sources.
"""
from __future__ import annotations
import functools
import hashlib
import http.server
import json
import os
from pathlib import Path
import socketserver
import subprocess
import sys
import threading
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[2]
BASE="ef27f795a63cc3e86e2fe8ce7d7d0f64c89adbff"
HTML="portfolio-v2-preview/index.html"
CSS="portfolio-v2-preview/styles.css"
GLOBE="portfolio-v2-preview/original-globe.js"
GLOBE_BLOB="1be0c45a592aa54aa78bf42682964a0d11303977"
WIDTHS=[320,360,390,480,740,768,900,901,960,961,1000,1001,1010,1180,1181,1280,1366,1440,1920]
OUT=ROOT/"qa-artifacts"/"portfolio-v2-m4"
OUT.mkdir(parents=True,exist_ok=True)

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address=True
    daemon_threads=True

def git_show(file):
    return subprocess.check_output(["git","show",f"{BASE}:{file}"],cwd=ROOT).decode()

def measure(page):
    return page.evaluate("""() => {
       const rect=s=>{let r=document.querySelector(s).getBoundingClientRect();
         return {x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom}};
       const details=document.querySelector(".details-grid");
       const about=document.querySelector(".about-grid");
       const experience=document.querySelector("#experience");
       const cards=[...document.querySelectorAll(".capability-list>div")];
       const roles=[...document.querySelectorAll(".timeline-entry")];
       return {
         viewport:innerWidth,scrollWidth:document.documentElement.scrollWidth,
         hero:rect(".hero"),heroCopy:rect(".hero-copy"),heroVisual:rect(".legacy-hero"),
         work:rect(".work-section"),projectGrid:rect(".project-grid"),
         detailColumns:getComputedStyle(details).gridTemplateColumns.split(/\\s+/).length,
         aboutColumns:getComputedStyle(about).gridTemplateColumns.split(/\\s+/).length,
         experience:rect("#experience"),about:rect("#about"),
         timelineRoles:roles.map(n=>n.querySelector("h3")?.textContent.trim()),
         timelineEntries:roles.map(n=>{let r=n.getBoundingClientRect();return {top:r.top,bottom:r.bottom}}),
         timelineBullets:document.querySelectorAll(".timeline-highlights li").length,
         skillCardCount:cards.length,
         skillContexts:document.querySelectorAll(".capability-context").length,
         cardFonts:cards.map(x=>x.querySelector(".capability-context") ? parseFloat(getComputedStyle(x.querySelector(".capability-context")).fontSize) : 0),
         experienceBulletsFont:document.querySelector(".timeline-highlights") ? parseFloat(getComputedStyle(document.querySelector(".timeline-highlights")).fontSize) : 0,
         projectCardCount:document.querySelectorAll(".project-card").length,
         internalMissing:[...document.querySelectorAll('a[href^="#"]')].filter(a=>a.hash.length>1&&!document.getElementById(a.hash.slice(1))).map(a=>a.hash),
         capabilityAnchor:!!document.getElementById("capabilities"),
         educationText:document.querySelector(".about-card")?.textContent||"",
         sectionHeadingIds:[...experience.querySelectorAll("h2")].map(x=>x.id)
       };
    }""")

def invariant_rects(base,candidate):
    problems=[]
    for key in ("hero","heroCopy","heroVisual","work","projectGrid"):
        for field in ("x","y","width","height"):
            delta=abs(base[key][field]-candidate[key][field])
            if delta>1.1:
                problems.append(f"existing_layout_changed:{key}.{field}:{delta:.2f}px")
    return problems

def run():
    results={"base":BASE,"candidate":os.environ.get("GITHUB_SHA","local"),
             "source":{},"viewports":{},"navigation":{},"globe":{},"failures":[]}
    base_html=git_show(HTML)
    base_css=git_show(CSS)
    html=(ROOT/HTML).read_text(encoding="utf-8")
    css=(ROOT/CSS).read_text(encoding="utf-8")
    cut='<section class="details-section shell"'
    back='<section class="contact-section shell"'
    s0,s1=base_html.index(cut),html.index(cut)
    e0,e1=base_html.index(back,s0),html.index(back,s1)
    source_checks={
       "all_earlier_html_unchanged":html[:s1]==base_html[:s0],
       "contact_footer_html_unchanged":html[e1:]==base_html[e0:],
       "existing_css_preserved":css.startswith(base_css.strip()),
       "original_globe_blob":subprocess.check_output(
           ["git","hash-object",str(ROOT/GLOBE)],cwd=ROOT).decode().strip()==GLOBE_BLOB,
       "no_certifications_published":all(x not in html for x in
           ["CEH Certified","eJPT Certified","Linux+ Certified","AZ-900 Certified"]),
       "no_claimed_graduation":'degree-award status is not asserted' in html,
       "m3_three_project_cards":html.count('<article class="project-card')==3
    }
    results["source"]=source_checks
    for key,ok in source_checks.items():
        if not ok:results["failures"].append(f"source:{key}")
    handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT))
    server=Server(("127.0.0.1",0),handler)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    url=f"http://127.0.0.1:{server.server_address[1]}/portfolio-v2-preview/"
    try:
      with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,args=["--no-sandbox",
             "--enable-unsafe-swiftshader","--use-gl=angle","--use-angle=swiftshader"])
        try:
          for width in WIDTHS:
            state={}
            for version in ("baseline","candidate"):
              context=browser.new_context(viewport={"width":width,"height":900},
                   device_scale_factor=1,reduced_motion="reduce")
              page=context.new_page()
              page.route("**/three.min.js",lambda route:route.fulfill(
                 status=200,content_type="application/javascript",body=""))
              if version=="baseline":
                page.route("**/portfolio-v2-preview/",lambda route:route.fulfill(
                    status=200,content_type="text/html; charset=utf-8",body=base_html))
                page.route("**/styles.css",lambda route:route.fulfill(
                    status=200,content_type="text/css",body=base_css))
              page.goto(url,wait_until="load",timeout=30000)
              page.add_style_tag(content="*,*::before,*::after{animation:none!important;transition:none!important}")
              state[version]=measure(page)
              if width in (320,390,768,1440):
                page.locator(".details-section").screenshot(
                  path=str(OUT/f"experience-{width}-{version}.png"),
                  animations="disabled",timeout=15000)
                if version=="candidate":
                  page.locator(".about-section").screenshot(
                    path=str(OUT/f"about-{width}.png"),animations="disabled")
              context.close()
            baseline,candidate=state["baseline"],state["candidate"]
            issues=invariant_rects(baseline,candidate)
            expected_cols=1 if width<=740 else 2
            if candidate["scrollWidth"]>width+1:issues.append("horizontal_overflow")
            if candidate["detailColumns"]!=expected_cols:issues.append("details_grid_columns")
            if candidate["aboutColumns"]!=expected_cols:issues.append("about_grid_columns")
            if candidate["timelineRoles"]!=["SOC Analyst","Security Intern (VAPT)"]:
                issues.append("role_titles_or_order")
            if candidate["timelineBullets"]!=5:issues.append("incorrect_bullet_count")
            if candidate["skillCardCount"]!=4 or candidate["skillContexts"]!=4:
                issues.append("incorrect_capability_card_count")
            if any(font<12.5 for font in candidate["cardFonts"]):
                issues.append("capability_text_too_small")
            if candidate["experienceBulletsFont"]<12.5:
                issues.append("experience_text_too_small")
            if len(candidate["timelineEntries"])==2 and candidate["timelineEntries"][0]["bottom"]>candidate["timelineEntries"][1]["top"]+2:
                issues.append("timeline_entry_overlap")
            if candidate["projectCardCount"]!=3:issues.append("project_card_regression")
            if candidate["internalMissing"]:issues.append("broken_anchor")
            if not candidate["capabilityAnchor"]:issues.append("capabilities_anchor_missing")
            if "Lovely Professional University" not in candidate["educationText"] or "7.5/10" not in candidate["educationText"]:
                issues.append("education_content_missing")
            results["viewports"][str(width)]={"issues":issues,
                  "scrollWidth":candidate["scrollWidth"],
                  "detailColumns":candidate["detailColumns"],
                  "skillCards":candidate["skillCardCount"]}
            if issues:results["failures"].append({"width":width,"issues":issues})
          for width in (390,768):
            context=browser.new_context(viewport={"width":width,"height":844},reduced_motion="reduce")
            page=context.new_page()
            page.route("**/three.min.js",lambda route:route.fulfill(
                status=200,content_type="application/javascript",body=""))
            page.goto(url,wait_until="load",timeout=30000)
            b=page.locator("#menu-toggle"); nav=page.locator("#primary-navigation")
            b.click()
            opened=b.get_attribute("aria-expanded")=="true" and nav.is_visible()
            page.keyboard.press("Escape")
            closed=b.get_attribute("aria-expanded")=="false" and not nav.is_visible()
            focus=page.evaluate("document.activeElement?.id==='menu-toggle'")
            results["navigation"][str(width)]={"opens":opened,
                 "escape_closes":closed,"focus_restored":focus}
            if not all([opened,closed,focus]):
                results["failures"].append({"navigation_width":width})
            context.close()
          context=browser.new_context(viewport={"width":1440,"height":900})
          page=context.new_page();console_errors=[];page_errors=[]
          page.on("console",lambda m:console_errors.append(m.text) if m.type=="error" else None)
          page.on("pageerror",lambda e:page_errors.append(str(e)))
          try:
            page.goto(url,wait_until="load",timeout=45000)
            page.wait_for_timeout(700)
            three=page.evaluate("typeof window.THREE !== 'undefined'")
            visible=page.locator("#tc").is_visible()
            results["globe"]={"three_loaded":three,"canvas_visible":visible,
                  "console_errors":console_errors,"page_errors":page_errors}
            if not three or not visible or console_errors or page_errors:
                results["failures"].append("globe_smoke_failed")
          except Exception as e:
            results["globe"]={"error":str(e)[:300]}
            results["failures"].append("globe_smoke_exception")
          finally:context.close()
        finally:browser.close()
    finally:
      server.shutdown();server.server_close()
    (OUT/"report.json").write_text(json.dumps(results,indent=2),encoding="utf-8")
    print(json.dumps({"viewports":len(results["viewports"]),
      "source":results["source"],"navigation":results["navigation"],
      "globe":results["globe"],"failures":results["failures"]},indent=2))
    return 1 if results["failures"] else 0

if __name__=="__main__":
    sys.exit(run())
