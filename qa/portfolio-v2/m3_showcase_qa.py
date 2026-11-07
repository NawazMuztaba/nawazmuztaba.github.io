#!/usr/bin/env python3
"""M3 Portfolio V2 evidence-first cards: browser QA against merged PR #8 baseline.

This test is deliberately restricted to review-only content/layout. It never scans
targets, modifies production, or exercises private AgentCheck source.
"""
from __future__ import annotations

import functools
import http.server
import json
import os
from pathlib import Path
import socketserver
import subprocess
import sys
import threading

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
BASE = "dd7ea30285f7a651d967ddc5b9e938b306cc05ae"
HTML_PATH = "portfolio-v2-preview/index.html"
CSS_PATH = "portfolio-v2-preview/styles.css"
GLOBE_PATH = "portfolio-v2-preview/original-globe.js"
EXPECTED_GLOBE = "1be0c45a592aa54aa78bf42682964a0d11303977"
WIDTHS = [320, 360, 390, 480, 740, 760, 768, 900, 901, 960,
          961, 1000, 1001, 1010, 1180, 1181, 1280, 1366, 1440, 1920]
OUT = ROOT / "qa-artifacts" / "portfolio-v2-m3"
OUT.mkdir(parents=True, exist_ok=True)

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

def git_show(path):
    return subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT).decode("utf-8")

def observe(page):
    return page.evaluate("""() => {
      const rect = (el) => {
        const r = el.getBoundingClientRect();
        return {x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom};
      };
      const cards=[...document.querySelectorAll('#projects .project-card')];
      const grid=document.querySelector('.project-grid');
      const hero=document.querySelector('.hero');
      return {
        viewport:innerWidth,
        documentWidth:document.documentElement.scrollWidth,
        hero:rect(hero),
        heroCopy:rect(hero.querySelector('.hero-copy')),
        heroVisual:rect(hero.querySelector('.legacy-hero')),
        gridColumns:getComputedStyle(grid).gridTemplateColumns.split(/\\s+/).length,
        links:[...cards].map(c=>c.querySelector('a.project-link')?.href || ''),
        cardData:cards.map(c=>{
          const link=c.querySelector('a.project-link');
          const title=c.querySelector('h3');
          return {title:title?.textContent.trim(),headingId:title?.id,
            labelledBy:c.getAttribute('aria-labelledby'),
            details:c.querySelectorAll('dl.project-evidence dt').length,
            descriptions:[...c.querySelectorAll('dl.project-evidence dd')].map(e=>e.textContent.trim()),
            summaryFont:c.querySelector('.project-summary') ? parseFloat(getComputedStyle(c.querySelector('.project-summary')).fontSize) : 0,
            card:rect(c),link:link?rect(link):null};
        }),
        missingInternalAnchors:[...document.querySelectorAll('a[href^="#"]')]
          .filter(a=>a.hash.length>1&&!document.getElementById(a.hash.slice(1)))
          .map(a=>a.hash)
      };
    }""")

def check_hero_same(base, candidate, width):
    issues = []
    for item in ["heroCopy", "heroVisual"]:
        for prop in ["x", "y", "width", "height"]:
            diff = abs(base[item][prop] - candidate[item][prop])
            if diff > 1.01:
                issues.append(f"hero_changed:{item}.{prop}:{diff:.2f}px")
    return issues

def run():
    report = {"milestone":"M3 evidence-first project cards",
              "base_sha":BASE,"candidate_sha":os.environ.get("GITHUB_SHA","local"),
              "widths":{},"navigation":{},"globe":{},"failures":[]}
    base_html=git_show(HTML_PATH)
    base_css=git_show(CSS_PATH)
    original_globe_hash=subprocess.check_output(
        ["git","hash-object",str(ROOT/GLOBE_PATH)],cwd=ROOT).decode().strip()
    report["original_globe_blob_sha"]=original_globe_hash
    if original_globe_hash!=EXPECTED_GLOBE:
        report["failures"].append("original_globe_source_changed")
    current_html=(ROOT/HTML_PATH).read_text(encoding="utf-8")
    if not all(x in current_html for x in [
        "Evidence to inspect","Implementation","AgentCheck V2 Alpha",
        "Intelligent SOC Automation","Sentinel-X"]):
        report["failures"].append("missing_expected_evidence_content")
    if any(x in current_html for x in ["23 successful exploits","1000+ assets","production-grade"]):
        report["failures"].append("unsupported_project_metric_or_claim")

    handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT))
    server=Server(("127.0.0.1",0),handler)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    url=f"http://127.0.0.1:{server.server_address[1]}/portfolio-v2-preview/"
    try:
      with sync_playwright() as p:
        browser=p.chromium.launch(headless=True,args=[
          "--no-sandbox","--enable-unsafe-swiftshader","--use-gl=angle","--use-angle=swiftshader"])
        try:
          for width in WIDTHS:
            measurements={}
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
              measurements[version]=observe(page)
              if width in (390,768,1180,1440):
                page.locator("#projects").screenshot(
                    path=str(OUT/f"work-{width}-{version}.png"),animations="disabled")
              if width in (390,901,1440) and version=="candidate":
                page.locator(".hero").screenshot(
                    path=str(OUT/f"hero-{width}-candidate.png"),animations="disabled")
              context.close()

            baseline=measurements["baseline"];candidate=measurements["candidate"]
            expected_columns=1 if width<=760 else 2 if width<=1180 else 3
            issues=check_hero_same(baseline,candidate,width)
            if candidate["documentWidth"]>width+1:issues.append("horizontal_document_overflow")
            if candidate["gridColumns"]!=expected_columns:issues.append("wrong_project_grid_columns")
            if len(candidate["cardData"])!=3:issues.append("wrong_project_card_count")
            if candidate["missingInternalAnchors"]:issues.append("broken_internal_anchors")
            names=["AgentCheck V2 Alpha","Intelligent SOC Automation","Sentinel-X"]
            links=[
              "https://nawazmuztaba.github.io/projects/agentcheck-v2/",
              "https://github.com/NawazMuztaba/intelligent-soc-automation",
              "https://github.com/NawazMuztaba/Sentinel-X"
            ]
            if candidate["links"]!=links:issues.append("unexpected_public_project_link")
            for index,card in enumerate(candidate["cardData"]):
              if card["title"]!=names[index] or not card["headingId"] or card["labelledBy"]!=card["headingId"]:
                issues.append(f"card_{index+1}_heading_or_aria_label")
              if card["details"]!=2 or any(not v for v in card["descriptions"]):
                issues.append(f"card_{index+1}_evidence_missing")
              if card["summaryFont"]<14:issues.append(f"card_{index+1}_summary_text_small")
              if card["link"] is None:
                issues.append(f"card_{index+1}_link_missing")
              else:
                if card["link"]["x"]<card["card"]["x"]-1 or card["link"]["right"]>card["card"]["right"]+1:
                  issues.append(f"card_{index+1}_link_clipped_horizontally")
                if card["link"]["bottom"]>card["card"]["bottom"]+1:
                  issues.append(f"card_{index+1}_link_clipped_vertically")
            report["widths"][str(width)]={"issues":issues,"columns":candidate["gridColumns"],
                "documentWidth":candidate["documentWidth"],"cardCount":len(candidate["cardData"])}
            if issues:report["failures"].append({"width":width,"issues":issues})

          for width in (390,768):
            context=browser.new_context(viewport={"width":width,"height":844},reduced_motion="reduce")
            page=context.new_page()
            page.route("**/three.min.js",lambda route:route.fulfill(
                status=200,content_type="application/javascript",body=""))
            page.goto(url,wait_until="load",timeout=30000)
            menu=page.locator("#menu-toggle");nav=page.locator("#primary-navigation")
            menu.click()
            opened=menu.get_attribute("aria-expanded")=="true" and nav.is_visible()
            page.keyboard.press("Escape")
            closed=menu.get_attribute("aria-expanded")=="false" and not nav.is_visible()
            focus=page.evaluate("document.activeElement?.id==='menu-toggle'")
            report["navigation"][str(width)]={"opens":opened,"escape_closes":closed,"focus_restored":focus}
            if not all([opened,closed,focus]):report["failures"].append({"menu_width":width})
            context.close()

          context=browser.new_context(viewport={"width":1440,"height":900})
          page=context.new_page();errors=[];page_errors=[]
          page.on("console",lambda m:errors.append(m.text) if m.type=="error" else None)
          page.on("pageerror",lambda err:page_errors.append(str(err)))
          try:
            page.goto(url,wait_until="load",timeout=45000)
            page.wait_for_timeout(800)
            three=page.evaluate("typeof window.THREE !== 'undefined'")
            canvas=page.locator("#tc").is_visible()
            page.locator(".hero").screenshot(path=str(OUT/"hero-1440-globe-runtime.png"))
            report["globe"]={"three_loaded":three,"canvas_visible":canvas,
                              "console_errors":errors,"page_errors":page_errors}
            if not three or not canvas or errors or page_errors:
              report["failures"].append("globe_runtime_smoke_failed")
          except Exception as err:
            report["globe"]={"error":str(err)[:400]}
            report["failures"].append("globe_runtime_smoke_exception")
          finally:context.close()
        finally:browser.close()
    finally:
      server.shutdown();server.server_close()
    (OUT/"report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps({"viewports":len(report["widths"]),
                      "navigation":report["navigation"],"globe":report["globe"],
                      "original_globe_blob_sha":report["original_globe_blob_sha"],
                      "failures":report["failures"]},indent=2))
    return 1 if report["failures"] else 0

if __name__=="__main__":
    sys.exit(run())
