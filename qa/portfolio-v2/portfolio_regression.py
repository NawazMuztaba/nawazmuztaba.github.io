#!/usr/bin/env python3
"""APEX Portfolio V2: exact-baseline CSS visual comparison + functional smoke.
Uses the current branch, serving the actual preview files over localhost.
CSS comparison deliberately blocks Three.js, so moving globe rendering is tested separately.
"""
from __future__ import annotations
import functools
import hashlib
import http.server
import io
import json
import os
import pathlib
import socketserver
import subprocess
import sys
import threading
from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = "26bd33d879be44fd5cf52ff42b74748b5cd0b0d1"
CSS_PATH = "portfolio-v2-preview/styles.css"
WIDTHS = [320, 360, 390, 480, 740, 768, 900, 901, 960, 961, 1010, 1024, 1280, 1366, 1440, 1920]
OUT = ROOT / "qa-artifacts" / "portfolio-v2"
OUT.mkdir(parents=True, exist_ok=True)

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

def measure(page):
    return page.evaluate("""() => {
      const rect=s=>{const r=document.querySelector(s).getBoundingClientRect();
        return {x:r.x,y:r.y,right:r.right,bottom:r.bottom,width:r.width,height:r.height}};
      const title=document.querySelector('.hero h1');
      const rings=Array.from(document.querySelectorAll('.legacy-hero .cring'));
      return {
        scrollWidth:document.documentElement.scrollWidth,
        overflowElements:Array.from(document.querySelectorAll('body *')).map(el=>{
          const r=el.getBoundingClientRect();
          return {tag:el.tagName,cls:typeof el.className==='string'?el.className.slice(0,90):'',
                  id:el.id||'',left:Math.round(r.left),right:Math.round(r.right),width:Math.round(r.width)};
        }).filter(x=>x.right>innerWidth+1||x.left<-1).slice(0,12),
        viewportWidth:innerWidth,
        copy:rect('.hero-copy'),globe:rect('.legacy-hero'),globeContent:rect('.legacy-hero .original-globe'),
        titleScrollWidth:title.scrollWidth,titleClientWidth:title.clientWidth,
        ringAnimations:rings.map(x=>getComputedStyle(x).animationName),
        anchorTargets:Array.from(document.querySelectorAll('a[href^="#"]'))
          .filter(a=>a.getAttribute('href').length>1 && !document.getElementById(a.getAttribute('href').slice(1)))
          .map(a=>a.getAttribute('href')),
        projectCards:document.querySelectorAll('.project-card').length
      };
    }""")

def compare_images(a: bytes, b: bytes):
    ia,ib=Image.open(io.BytesIO(a)).convert('RGB'),Image.open(io.BytesIO(b)).convert('RGB')
    if ia.size!=ib.size: return {'match':False, 'reason':'dimensions_changed', 'before':ia.size, 'after':ib.size}
    difference=ImageChops.difference(ia,ib)
    box=difference.getbbox()
    # Separate minor headless anti-aliasing variance from meaningful rendered changes.
    mask=difference.convert('L').point(lambda value:255 if value>=12 else 0)
    changed=mask.histogram()[255]
    return {'match':box is None,'difference_bbox':box,'dimensions':ia.size,
            'changed_pixels_above_12':changed,'changed_pixel_fraction':changed/(ia.width*ia.height)}

def run():
    report={'baseline_commit':BASE,'candidate_sha':os.environ.get('GITHUB_SHA', 'local'),
            'comparison_mode':'Three.js intentionally blocked for deterministic stylesheet-only visual comparison',
            'viewports':{},'interaction':{},'globe_runtime':{},'failures':[]}
    baseline_css=subprocess.check_output(['git','show',f'{BASE}:{CSS_PATH}'], cwd=ROOT).decode('utf-8')
    current_css=(ROOT/CSS_PATH).read_text(encoding='utf-8')
    handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(ROOT))
    server=Server(('127.0.0.1',0),handler)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    url=f'http://127.0.0.1:{server.server_address[1]}/portfolio-v2-preview/'
    try:
      with sync_playwright() as playwright:
        browser=playwright.chromium.launch(headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
        try:
          for width in WIDTHS:
            shots={}; data={}
            for version in ['baseline','candidate']:
              context=browser.new_context(viewport={'width':width,'height':900},device_scale_factor=1,reduced_motion='reduce')
              page=context.new_page()
              page.route('**/three.min.js',lambda route: route.fulfill(status=200,content_type='application/javascript',body=''))
              if version=='baseline':
                page.route('**/styles.css',lambda route: route.fulfill(status=200,content_type='text/css',body=baseline_css))
              page.goto(url,wait_until='load',timeout=30000)
              page.evaluate('document.fonts.ready')
              # Freeze any motion, without altering layout or the approved globe implementation.
              page.add_style_tag(content='*,*::before,*::after{animation:none!important;transition:none!important;caret-color:transparent!important}')
              data[version]=measure(page)
              shot=page.screenshot(full_page=True,animations='disabled',timeout=15000)
              shots[version]=shot
              if width in [390,900,901,960,961,1440]:
                (OUT/f'{width}-{version}.png').write_bytes(shot)
              context.close()
            diff=compare_images(shots['baseline'],shots['candidate'])
            m=data['candidate']
            issues=[]
            # Navigation fixes intentionally change 320–360px and 741–900px appearance.
            expected_approved_change=(width<=360 or 741<=width<=900 or 901<=width<=960)
            if diff.get('changed_pixel_fraction',1)>0.0003 and not expected_approved_change:
              issues.append('meaningful_pixel_difference_from_baseline')
            if m['scrollWidth']>width+1: issues.append('horizontal_document_overflow')
            if m['anchorTargets']: issues.append('unresolved_in_page_anchors')
            if m['projectCards']!=3: issues.append('featured_project_card_count')
            if width>=901 and m['globe']['x']<m['copy']['right']-2: issues.append('hero_columns_overlap')
            if width<=900 and m['globe']['y']<m['copy']['bottom']-2: issues.append('hero_stacked_sections_overlap')
            # Owner explicitly approved CSS-only scaling at 901–960px.
            if 901<=width<=960:
              if not (390<=m['globeContent']['width']<=405):
                issues.append('approved_narrow_desktop_globe_scale_not_applied')
              if m['globeContent']['right']>width+1:
                issues.append('approved_narrow_desktop_globe_still_clipped')
            if width==961 and not (459<=m['globeContent']['width']<=461):
              issues.append('full_size_globe_does_not_restore_above_960')
            if m['titleScrollWidth']>m['titleClientWidth']+3: issues.append('hero_heading_overflows_own_box')
            if issues: report['failures'].append({'viewport':width,'issues':issues,'baseline_scrollWidth':data['baseline']['scrollWidth'],'candidate_scrollWidth':m['scrollWidth'],'overflow_elements':m['overflowElements']})
            report['viewports'][str(width)]={'screenshot_comparison':diff,'candidate_layout':m,'issues':issues}

          context=browser.new_context(viewport={'width':390,'height':844},reduced_motion='reduce')
          page=context.new_page()
          page.route('**/three.min.js',lambda route: route.fulfill(status=200,content_type='application/javascript',body=''))
          page.goto(url,wait_until='load',timeout=30000)
          menu=page.locator('#menu-toggle'); nav=page.locator('#primary-navigation')
          menu.click()
          opened=menu.get_attribute('aria-expanded')=='true' and nav.is_visible()
          page.keyboard.press('Escape')
          closed=menu.get_attribute('aria-expanded')=='false' and not nav.is_visible()
          focus_returned=page.evaluate("document.activeElement?.id==='menu-toggle'")
          menu.click();nav.locator('a[href="#projects"]').click()
          link_closed=menu.get_attribute('aria-expanded')=='false' and not nav.is_visible()
          report['interaction']={'mobile_open':opened,'escape_closes':closed,'escape_returns_focus':focus_returned,'anchor_closes':link_closed}
          if not all(report['interaction'].values()):report['failures'].append({'interaction':report['interaction']})
          context.close()

          # Tablet breakpoint regression: the 768px header must use the mobile menu.
          context=browser.new_context(viewport={'width':768,'height':900},reduced_motion='reduce')
          page=context.new_page()
          page.route('**/three.min.js',lambda route: route.fulfill(status=200,content_type='application/javascript',body=''))
          page.goto(url,wait_until='load',timeout=30000)
          menu=page.locator('#menu-toggle'); nav=page.locator('#primary-navigation')
          tablet_visible=menu.is_visible()
          if tablet_visible: menu.click()
          tablet_open=tablet_visible and nav.is_visible() and menu.get_attribute('aria-expanded')=='true'
          page.keyboard.press('Escape')
          tablet_closed=not nav.is_visible() and menu.get_attribute('aria-expanded')=='false'
          report['interaction']['tablet_768_menu_visible']=tablet_visible
          report['interaction']['tablet_768_open']=tablet_open
          report['interaction']['tablet_768_escape_closes']=tablet_closed
          if not all([tablet_visible,tablet_open,tablet_closed]):
            report['failures'].append({'tablet_navigation':report['interaction']})
          context.close()

          # Actual runtime check (external CDN, WebGL enabled). A failure stays visible in the report.
          context=browser.new_context(viewport={'width':1440,'height':900},reduced_motion='no-preference')
          page=context.new_page();console_errors=[];page_errors=[]
          page.on('console',lambda m:console_errors.append(m.text) if m.type=='error' else None)
          page.on('pageerror',lambda e:page_errors.append(str(e)))
          try:
            page.goto(url,wait_until='load',timeout=45000)
            page.wait_for_timeout(900)
            three=page.evaluate("typeof window.THREE !== 'undefined'")
            canvas=page.locator('#tc')
            canvas_visible=canvas.is_visible()
            (OUT/'globe-runtime-1440.png').write_bytes(page.screenshot(full_page=True,timeout=15000))
            report['globe_runtime']={'three_loaded':three,'canvas_visible':canvas_visible,'console_errors':console_errors,'page_errors':page_errors,'screenshot':'globe-runtime-1440.png','browser_tested':True}
            if not three or not canvas_visible or page_errors or any('Original globe failed to initialize' in v or 'Original globe unavailable' in v for v in console_errors):
              report['failures'].append({'globe_runtime':report['globe_runtime']})
          except Exception as e:
            report['globe_runtime']={'browser_tested':False,'reason':str(e)[:350]}
            report['failures'].append({'globe_runtime':report['globe_runtime']})
          finally:context.close()
        finally:browser.close()
    finally:server.shutdown();server.server_close()
    (OUT/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({'viewports_tested':len(report['viewports']),'interaction':report['interaction'],
                      'globe_runtime':report['globe_runtime'],'failures':report['failures'],
                      'artifacts':str(OUT)},indent=2))
    return 1 if report['failures'] else 0

if __name__=='__main__':sys.exit(run())
