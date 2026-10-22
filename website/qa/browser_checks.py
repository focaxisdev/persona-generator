#!/usr/bin/env python3
"""Actual Chromium QA. Run with a localhost server at --url (default port 4173)."""
import argparse, json, hashlib, pathlib, datetime, re
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright
ROOT = pathlib.Path(__file__).resolve().parent
(ROOT / 'screenshots').mkdir(parents=True, exist_ok=True)
ap = argparse.ArgumentParser(); ap.add_argument('--url', default='http://127.0.0.1:4173'); args=ap.parse_args()
def source_hashes():
    return {f:hashlib.sha256((ROOT.parent/f).read_bytes()).hexdigest() for f in ['index.html','styles.css','demo.js','favicon.svg'] if (ROOT.parent/f).exists()}
start_hashes=source_hashes()
results={'source_sha256_at_start':start_hashes,'executed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':[], 'screenshots':[], 'limitations':['Automated targeted checks, not accessibility certification. External links checked structurally against repository files, not fetched. No screen-reader or real mobile device testing.']}
def check(name, condition, evidence=None):
    results['checks'].append({'name':name,'passed':bool(condition),'evidence':evidence})
def shot(page,name,full=True):
    page.screenshot(path=str(ROOT/'screenshots'/name),full_page=full); results['screenshots'].append(name)
def preview(page):
    page.get_by_role('button',name='顯示完整預覽',exact=False).click()
    return json.loads(page.locator('.demo-preview details').filter(has=page.locator('summary',has_text='完整資料與回答追溯')).locator('pre').text_content())
def btn(page,name): return page.get_by_role('button',name=name,exact=False)
def reset(page): btn(page,'重設：').click()
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    results['browser']=browser.version
    context=browser.new_context(viewport={'width':1440,'height':1000},permissions=['clipboard-read','clipboard-write'],accept_downloads=True,reduced_motion='reduce')
    context.add_init_script("""window.__writes=[]; const orig=Storage.prototype.setItem; Storage.prototype.setItem=function(k,v){window.__writes.push({kind:'storage',key:k});return orig.call(this,k,v)}; const d=Object.getOwnPropertyDescriptor(Document.prototype,'cookie'); if(d&&d.set)Object.defineProperty(document,'cookie',{get:()=>d.get.call(document),set:v=>{window.__writes.push({kind:'cookie'});d.set.call(document,v)}});""")
    page=context.new_page(); page.set_default_timeout(10000); requests=[]; console=[]; errors=[]; failed=[]
    page.on('request',lambda r:requests.append(r.url)); page.on('console',lambda m:console.append({'type':m.type,'text':m.text}) if m.type=='error' else None); page.on('pageerror',lambda e:errors.append(str(e))); page.on('response',lambda r:failed.append({'url':r.url,'status':r.status}) if r.status>=400 else None)
    try:
        page.goto(args.url,wait_until='networkidle')
        check('styles loaded',page.locator('link[rel=stylesheet]').evaluate('(e)=>!!e.sheet'))
        shot(page,'desktop-full.png'); shot(page,'desktop-hero-viewport.png',False); page.locator('.hero').screenshot(path=str(ROOT/'screenshots/desktop-hero.png')); results['screenshots'].append('desktop-hero.png')
        page.keyboard.press('Tab'); check('keyboard skip link is first tab stop',page.locator(':focus').inner_text()=='跳至主要內容')
        focus=page.locator(':focus').evaluate('(e)=>({outline:getComputedStyle(e).outline,rect:e.getBoundingClientRect().toJSON()})'); check('skip link focus visible',focus['rect']['y']>=0,focus)
        page.keyboard.press('Enter'); check('skip link targets main',page.evaluate('document.activeElement.id')=='main')
        links=page.locator('a').evaluate_all('(els)=>els.map(e=>({href:e.getAttribute("href"),text:e.textContent.trim()}))')
        bad=[]
        repo=ROOT.parent.parent
        for link in links:
            href=link['href'] or ''
            if href.startswith('#'):
                if not page.locator('[id="'+href[1:]+'"]').count(): bad.append(link)
            elif href.startswith('https://github.com/focaxisdev/persona-generator/blob/'):
                path='/'.join(urlparse(href).path.split('/')[5:])
                if not (repo/path).is_file(): bad.append(link)
            elif not href.startswith('https://'): bad.append(link)
        check('all rendered links have valid anchor or repository target',not bad,{'count':len(links),'invalid':bad})
        unlabeled=page.locator('input,textarea,select').evaluate_all('(els)=>els.filter(e=>!e.labels?.length&&!e.getAttribute("aria-label")).map(e=>e.outerHTML)')
        check('form controls have native label or accessible label',not unlabeled,unlabeled)
        p=preview(page); check('default ten unspecified and no rules',len(p['goals'])==10 and all(g['target']=='unspecified' and g['rule'] is None for g in p['goals']))
        check('export locked until confirmation',btn(page,'複製 Markdown').is_disabled() and btn(page,'下載 Markdown').is_disabled())
        btn(page,'確認此示範修訂').click(); check('unchecked review cannot confirm',btn(page,'複製 Markdown').is_disabled() and '勾選此修訂' in page.locator('.demo-status').inner_text())
        page.get_by_label('選擇目標（').select_option('high'); btn(page,'加入選擇').click(); p=preview(page)
        check('explicit anchor maps only chosen aspect',p['targets']['bfas.volatility']=='high' and sum(t!='unspecified' for t in p['targets'].values())==1)
        page.locator('.demo-preview').focus(); page.keyboard.press('Tab'); first=page.locator(':focus').evaluate('(e)=>e.tagName'); check('forward keyboard reaches preview details',first=='SUMMARY');
        for _ in range(11): page.keyboard.press('Tab')
        check('forward tab traverses closed preview details to review checkbox',page.locator(':focus').evaluate('(e)=>e.type')=='checkbox'); page.keyboard.press('Tab'); check('review checkbox forward tab reaches confirm',page.locator(':focus').inner_text()=='確認此示範修訂'); page.get_by_role('checkbox').check(); btn(page,'確認此示範修訂').click(); page.keyboard.press('Tab'); check('confirmed action forward tab reaches copy',page.locator(':focus').inner_text()=='複製 Markdown'); check('review confirmation enables export',btn(page,'複製 Markdown').is_enabled())
        page.get_by_role('checkbox').uncheck(); check('unchecking review revokes export',btn(page,'複製 Markdown').is_disabled()); page.get_by_role('checkbox').check(); btn(page,'確認此示範修訂').click(); btn(page,'複製 Markdown').click(); page.wait_for_timeout(150); copied=page.evaluate('navigator.clipboard.readText()'); check('copy matches exact displayed JSON',json.loads(copied.split('```json\n')[1].split('\n```')[0])==p)
        with page.expect_download() as event: btn(page,'下載 Markdown').click()
        dl=event.value; download=ROOT/'downloaded-demo.md'; dl.save_as(str(download)); text=download.read_text(); check('download exact preview and filename',dl.suggested_filename=='persona-design-demo.md' and json.loads(text.split('```json\n')[1].split('\n```')[0])==p)
        page.evaluate("Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw new Error('QA denial')}}})"); btn(page,'複製 Markdown').click(); page.wait_for_timeout(100); check('clipboard denial exposes exact readable fallback',page.locator('.demo-fallback').is_visible() and page.locator('.demo-fallback').input_value()==text); page.get_by_label('選填理由（').fill('changed input'); check('editing input invalidates previous preview and export',btn(page,'複製 Markdown').is_disabled() and btn(page,'確認此示範修訂').is_disabled() and '內容已改變' in page.locator('.demo-preview').inner_text())
        page.get_by_label('選擇目標（').select_option('low'); btn(page,'加入選擇').click(); p=preview(page)
        check('contradictory explicit answers retained and confirm blocked',len([a for a in p['answers'] if a['type']=='explicit_choice'])==2 and p['targets']['bfas.volatility']=='unspecified' and p['conflicts'][0]['status']=='unresolved' and page.get_by_role('checkbox').is_disabled())
        page.locator('.demo-conflicts').evaluate('(e)=>e.scrollIntoView({block:"start",behavior:"instant"})'); shot(page,'conflict-review.png',False)
        page.get_by_label('解決衝突 C1：').select_option('middle'); btn(page,'明確解決 C1').click(); p=preview(page); check('explicit conflict resolution retained',p['targets']['bfas.volatility']=='middle' and p['conflicts'][0]['status']=='resolved' and len(p['conflict_resolution_history'])==1)
        reset(page); page.get_by_label('輸入模式').select_option('free'); payload='<img src=x onerror="window.__xss=1"> I want a warm and organized fictional agent.'
        page.get_by_label('描述虛構代理應有的行為').fill(payload); btn(page,'保留簡答為未知').click(); p=preview(page)
        check('free text remains verbatim unknown with no inferred targets',p['unknown_answers'][0]['text']==payload and p['unknown_answers'][0]['interpretation']=='unknown' and all(v=='unspecified' for v in p['targets'].values()) and page.get_by_role('checkbox').is_disabled())
        check('HTML payload rendered literally without execution',page.evaluate('window.__xss===undefined') and page.locator('.demo-history img').count()==0 and payload in page.locator('.demo-history').inner_text())
        btn(page,'明確保留 A001 為未知').click(); p=preview(page); check('keep unknown explicitly permits review without mapping',p['unknown_answers'][0]['review']=='explicitly_keep_unknown' and page.get_by_role('checkbox').is_enabled() and all(v=='unspecified' for v in p['targets'].values()))
        page.get_by_label('手動描述矛盾').fill('Fictional requirements conflict'); btn(page,'標記衝突').click(); p=preview(page); check('manual flag blocks review',p['conflicts'][0]['type']=='manual' and page.get_by_role('checkbox').is_disabled()); btn(page,'我已檢視此手動標記').click(); p=preview(page); check('manual resolution retains history',p['conflicts'][0]['status']=='resolved' and p['conflict_resolution_history'][0]['resolution'].startswith('User explicitly'))
        reset(page); p=preview(page); check('reset clears page memory',p['answers']==[] and p['conflicts']==[] and all(v=='unspecified' for v in p['targets'].values()))
        page.get_by_label('輸入模式').select_option('free'); page.get_by_label('描述虛構代理應有的行為').fill('Keep the opening friendly'); btn(page,'保留簡答為未知').click(); page.get_by_label('輸入模式').select_option('choice'); page.get_by_label('選填：明確連結').select_option('A001'); page.get_by_label('選擇目標（').select_option('high'); btn(page,'加入選擇').click(); p=preview(page); check('linked explicit choice preserves raw unknown and permits review',p['unknown_answers'][0]['interpretation']=='unknown' and p['unknown_answers'][0]['review']=='explicit_choice_added_raw_remains_unknown' and p['answers'][1]['raw_answer_id']=='A001' and page.get_by_role('checkbox').is_enabled()); page.reload(wait_until='networkidle'); p=preview(page); check('reload clears page memory',p['answers']==[] and all(v=='unspecified' for v in p['targets'].values()))
        reset(page)
        for width,height in [(1440,1000),(768,844),(760,844),(390,844),(375,844),(320,844)]:
            page.set_viewport_size({'width':width,'height':height}); page.evaluate('window.scrollTo({top:0,behavior:"instant"})')
            dims=page.evaluate('({viewport:innerWidth,scroll:document.documentElement.scrollWidth})'); check(f'page has no horizontal overflow at {width}px',dims['scroll']<=dims['viewport'],dims)
            clipped=page.locator('button,select,textarea').evaluate_all('(es)=>es.filter(e=>e.getBoundingClientRect().width&&((e.getBoundingClientRect().right>innerWidth+1)||(e.getBoundingClientRect().left<0))).map(e=>({text:e.textContent.slice(0,80),rect:e.getBoundingClientRect().toJSON()}))')
            check(f'visible controls within viewport at {width}px',not clipped,clipped)
            if width==390:
                sizes=page.locator('.pilot-details p,.pilot-limit,.pilot-status>span,.source-line,.local-disclosure,.faq-list details p,.aspect dd,#persona-demo select,#persona-demo textarea').evaluate_all('(es)=>es.map(e=>({selector:e.tagName+"."+e.className,size:parseFloat(getComputedStyle(e).fontSize),control:["SELECT","TEXTAREA"].includes(e.tagName)}))'); check('mobile body readability14px and inputs16px',all(v['size']>=(16 if v['control'] else 14) for v in sizes),sizes)
                shot(page,'mobile-hero.png',False); shot(page,'mobile-full.png'); page.locator('#persona-demo').scroll_into_view_if_needed(); shot(page,'mobile-workbench.png',False)
            p=preview(page);
            if width==390:
                page.locator('.demo-preview').evaluate('(e)=>e.scrollIntoView({block:"start",behavior:"instant"})'); shot(page,'mobile-preview.png',False)
            page.locator('.demo-preview summary').filter(has_text='完整資料與回答追溯').click(); dims=page.evaluate('({viewport:innerWidth,scroll:document.documentElement.scrollWidth})'); check(f'full JSON preview no page overflow at {width}px',dims['scroll']<=dims['viewport'],dims); reset(page)
        results['computed_color_samples']=page.locator('body,.hero-description,.eyebrow,.button,.demo-notice,.demo-status').evaluate_all('(es)=>es.slice(0,30).map(e=>{let b=e;while(b&&getComputedStyle(b).backgroundColor==="rgba(0, 0, 0, 0)")b=b.parentElement;let s=getComputedStyle(e);return {selector:e.className||e.tagName,color:s.color,background:b?getComputedStyle(b).backgroundColor:null,fontSize:s.fontSize,fontWeight:s.fontWeight}})')
        def luminance(color):
            rgb=[int(v)/255 for v in re.findall(r'\d+',color)[:3]]
            return sum(c*k for c,k in zip([v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb],[.2126,.7152,.0722]))
        for sample in results['computed_color_samples']:
            if sample['background'] and sample['background']!='rgba(0, 0, 0, 0)':
                a,b=luminance(sample['color']),luminance(sample['background']); sample['contrast_ratio']=round((max(a,b)+.05)/(min(a,b)+.05),2)
        writes=page.evaluate('window.__writes'); check('no storage or cookie writes after interactions',not writes and page.evaluate('localStorage.length')==0 and not context.cookies(),{'writes':writes,'localStorageLength':page.evaluate('localStorage.length'),'cookies':context.cookies()})
        external=[u for u in requests if urlparse(u).netloc!=urlparse(args.url).netloc and not u.startswith('blob:')]; check('no external requests on load or demo interactions',not external,external)
        check('no browser console errors',not console,console); check('no uncaught page errors',not errors,errors); check('no failed asset responses',not failed,failed)
        results['requests']=requests
    except Exception as e:
        check('test execution completed',False,str(e)); shot(page,'failure.png')
    finally:
        results['source_sha256']=source_hashes(); check('application files unchanged during QA run',start_hashes==results['source_sha256'],{'start':start_hashes,'end':results['source_sha256']})
        results['summary']={'passed':sum(c['passed'] for c in results['checks']),'failed':sum(not c['passed'] for c in results['checks'])}
        (ROOT/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n'); browser.close()
print(json.dumps(results['summary']))

raise SystemExit(1 if results['summary']['failed'] else 0)
