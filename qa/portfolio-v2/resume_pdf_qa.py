#!/usr/bin/env python3
"""Verify owner's unmodified PDF resume and the portfolio's view/download UX.

Runs only on a review branch; does not publish or modify the PDF.
"""
from __future__ import annotations
import functools
import hashlib
import http.server
import json
from pathlib import Path
import socketserver
import sys
import tempfile
import threading
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
REL = "portfolio-v2-preview/assets/Nawaz_Muztaba_Resume.pdf"
FILE = ROOT / REL
NAME = "Nawaz_Muztaba_Resume.pdf"
EXPECTED_SHA256 = "94725e11537ad488169299a0cd5351c64134402dae06ee877e7897b80c8ae221"
EXPECTED_BYTES = 329220
WIDTHS = [320, 390, 768, 901, 1440]
OUT = ROOT/"qa-artifacts"/"portfolio-v2-resume"
OUT.mkdir(parents=True, exist_ok=True)

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def run():
    report = {"file":REL,"views":{},"downloads":{},"errors":[]}
    if not FILE.is_file():
        report["errors"].append("PDF asset missing")
    else:
        content = FILE.read_bytes()
        report["local"] = {
          "size":len(content),"sha256":digest(content),
          "pdf_header":content.startswith(b"%PDF-"),
          "eof_marker":b"%%EOF" in content[-2048:]
        }
        if len(content) != EXPECTED_BYTES or digest(content) != EXPECTED_SHA256:
            report["errors"].append("PDF differs from original uploaded resume")
        if not content.startswith(b"%PDF-") or b"%%EOF" not in content[-2048:]:
            report["errors"].append("PDF header/trailer malformed")
    if report["errors"]:
        (OUT/"resume-report.json").write_text(json.dumps(report,indent=2))
        print(json.dumps(report,indent=2));return 1

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT))
    server = Server(("127.0.0.1", 0),handler)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    url=f"http://127.0.0.1:{server.server_address[1]}/portfolio-v2-preview/"
    asset=url+"assets/"+NAME

    try:
      with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=True,args=["--no-sandbox"])
        try:
          for width in WIDTHS:
            context=browser.new_context(viewport={"width":width,"height":900},
                                        accept_downloads=True)
            page=context.new_page()
            page.route("**/three.min.js",lambda route:route.fulfill(
                status=200,content_type="application/javascript",body=""))
            page.goto(url,wait_until="load",timeout=30000)
            view=page.locator(".hero-actions a",has_text="View resume")
            download=page.locator(".hero-actions a[download]")
            nav=page.locator(".nav-resume")
            ui={
              "view_count":view.count(),
              "download_count":download.count(),
              "view_href":view.get_attribute("href") if view.count() else None,
              "view_target":view.get_attribute("target") if view.count() else None,
              "download_href":download.get_attribute("href") if download.count() else None,
              "download_filename":download.get_attribute("download") if download.count() else None,
              "nav_href":nav.get_attribute("href") if nav.count() else None,
              "document_scrollWidth":page.evaluate("document.documentElement.scrollWidth")
            }
            if ui["document_scrollWidth"]>width+1:
                report["errors"].append(f"{width}px horizontal overflow")
            if ui["view_count"]!=1 or ui["download_count"]!=1:
                report["errors"].append(f"{width}px wrong resume CTA count")
            expected="./assets/"+NAME
            if (ui["view_href"]!=expected or ui["nav_href"]!=expected or
                ui["download_href"]!=expected or ui["download_filename"]!=NAME or
                ui["view_target"]!="_blank"):
                report["errors"].append(f"{width}px resume CTA link/attribute incorrect")
            response=context.request.get(asset,timeout=15000)
            response_body=response.body()
            ui["status"]=response.status
            ui["content_type"]=response.headers.get("content-type","")
            ui["http_sha256"]=digest(response_body)
            if response.status!=200 or "application/pdf" not in ui["content_type"].lower():
                report["errors"].append(f"{width}px PDF HTTP status/content type invalid")
            if digest(response_body)!=EXPECTED_SHA256:
                report["errors"].append(f"{width}px HTTP PDF differs from original")
            if width in (390,1440):
                # Exercise the actual View Resume click; Chromium should open a PDF tab.
                with page.expect_popup(timeout=15000) as popup_info:
                    view.click()
                popup=popup_info.value
                ui["view_popup_url"]=popup.url
                if not popup.url.split("?")[0].endswith("/"+NAME):
                    report["errors"].append(f"{width}px View Resume did not open the PDF")
                popup.close()
                page.locator(".hero-actions").screenshot(
                    path=str(OUT/f"resume-actions-{width}.png"),animations="disabled")
                with page.expect_download(timeout=12000) as info:
                    download.click()
                download_item=info.value
                ui["download_suggested_filename"]=download_item.suggested_filename
                if download_item.suggested_filename!=NAME:
                    report["errors"].append(f"{width}px wrong downloaded filename")
                with tempfile.TemporaryDirectory() as folder:
                    saved=Path(folder)/download_item.suggested_filename
                    download_item.save_as(str(saved))
                    ui["download_sha256"]=digest(saved.read_bytes())
                    if ui["download_sha256"]!=EXPECTED_SHA256:
                        report["errors"].append(f"{width}px downloaded bytes changed")
            report["views"][str(width)]=ui
            context.close()
        finally:browser.close()
    finally:
        server.shutdown()
        server.server_close()
    (OUT/"resume-report.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps({"viewports":len(report["views"]),
        "original_sha256":EXPECTED_SHA256,
        "actual_downloads_verified":sum("download_sha256" in v for v in report["views"].values()),
        "errors":report["errors"]},indent=2))
    return 1 if report["errors"] else 0

if __name__=="__main__":
    sys.exit(run())
