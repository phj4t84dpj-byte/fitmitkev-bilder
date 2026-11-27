# -*- coding: utf-8 -*-
"""Papier-Look für Kuchenherz und Omas Kochtopf (Kev 15.11.: „in diesem Stil“):
   oben ein linierter Block-Zettel mit Handschrift (Titel, rote Unterstreichung, Zutaten links, drei Herz-Sätze rechts),
   darunter das Foto; das freigestellte Gericht ragt über die Unterkante des Zettels. Seitenname unten links.
   Daten je Rezept: ptitel (Titel in Handschrift), zl (Zutatenzeilen, sonst aus 'zutaten'), herz (3 kurze Sätze)."""
import os, sys, html, json, importlib
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,D)
G=importlib.import_module(os.environ.get('DATA','n3_data'))
S=os.path.dirname(D) if os.path.isdir(os.path.dirname(D)+'/fonts') else '/tmp/claude-0/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/scratchpad'
F=f"{S}/fonts/gf/ofl"
PREFIX=os.environ.get('PREFIX','N3')
os.makedirs(f"{D}/out",exist_ok=True)
INK="#1b2a78"; RED="#c62828"; NAVY="#12213f"
XMP='''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?><x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/" xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/" xmlns:dc="http://purl.org/dc/elements/1.1/" photoshop:Credit="Fitmitkev"><Iptc4xmpExt:DigitalSourceType>http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia</Iptc4xmpExt:DigitalSourceType><dc:creator><rdf:Seq><rdf:li>Fitmitkev</rdf:li></rdf:Seq></dc:creator><dc:description><rdf:Alt><rdf:li xml:lang="x-default">Rezeptgrafik, Foto KI-generiert</rdf:li></rdf:Alt></dc:description></rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>'''
HEART='<svg viewBox="0 0 32 29" width="40" height="36"><path d="M16 28 C 6 20, 0 14, 0 8 C 0 3.5, 3.5 0, 8 0 C 11.5 0, 14.5 2, 16 5 C 17.5 2, 20.5 0, 24 0 C 28.5 0, 32 3.5, 32 8 C 32 14, 26 20, 16 28 Z" fill="#d32f2f"/></svg>'
LINE=42   # Linienabstand des Blocks (px)
# Foto: unten bündig, zentriert, verkleinert (s) und nach unten geschoben (dy, schneidet unten ab), damit das Gericht unter dem Zettel liegt
GEO={}
def geo(key):
    g=dict(s=0.92,dy=40,dx=0); g.update(GEO.get(key,{})); w=1080*g['s']; h=1350*g['s']
    return w,h,(1080-w)/2+g['dx'],1350-h+g['dy']

def zeilen(r):
    if r.get('zl'): return r['zl']
    return [f"{z['menge']} {z['name']}".replace('Stück ','') if z['menge'].endswith('Stück') else f"{z['menge']} {z['name']}" for z in r['zutaten']]

def board_html(r,hero,cut,paper_h):
    W,Hh,L,T=geo(r['key'])
    zl=''.join(f'<div class="z">- {html.escape(t)}</div>' for t in zeilen(r))
    hz=''.join(f'<div class="h">{HEART}<div class="ht">{html.escape(t)}</div></div>' for t in r['herz'])
    name=G.SEITEN[r['seite']]['name']
    clip=paper_h+20-45-T   # Freisteller erst ab ca. 45 px über der Zettel-Unterkante zeigen (Element-Koordinaten)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:C;src:url('{F}/caveat/Caveat[wght].ttf')}}
@font-face{{font-family:K;src:url('{F}/kaushanscript/KaushanScript-Regular.ttf')}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;background:#8a6a4a}}
.bg{{position:absolute;left:-60px;top:-60px;width:1200px;height:1470px;object-fit:cover;filter:blur(22px) brightness(.85)}}
.hero{{position:absolute;left:{L:.1f}px;top:{T:.1f}px;width:{W:.1f}px;height:{Hh:.1f}px;-webkit-mask-image:linear-gradient(to right,transparent 0,#000 46px,#000 calc(100% - 46px),transparent 100%)}}
.cut{{clip-path:inset({clip:.1f}px 0 0 0)}}
.paper{{position:absolute;left:22px;top:20px;width:1036px;height:{paper_h}px;background-color:#fdfdfb;
  background-image:repeating-linear-gradient(to bottom,transparent 0,transparent {LINE-2}px,#c9d9ec {LINE-2}px,#c9d9ec {LINE}px);
  background-position:0 6px;box-shadow:0 12px 30px rgba(30,15,0,.35),0 2px 6px rgba(30,15,0,.25);border-radius:3px}}
.margin{{position:absolute;left:84px;top:0;width:3px;height:100%;background:#e7a4a4}}
.hole{{position:absolute;left:30px;width:22px;height:22px;border-radius:50%;background:radial-gradient(circle at 45% 40%,#5b4a3a 0,#3b2e22 60%,#2a2018 100%)}}
.ti{{position:absolute;left:100px;right:20px;top:14px;text-align:center;font-family:C;font-weight:700;font-size:96px;line-height:1.05;color:{INK};white-space:nowrap}}
.ul{{position:absolute;left:120px;right:40px;height:7px;border-radius:4px;background:{RED};transform:rotate(-.4deg)}}
.zh{{position:absolute;left:112px;font-family:C;font-weight:700;font-size:68px;line-height:1;color:{INK}}}
.zs{{position:absolute;left:118px;width:470px}}
.z{{font-family:C;font-weight:600;font-size:48px;line-height:{LINE}px;height:{LINE}px;color:{INK};white-space:nowrap}}
.hs{{position:absolute;left:600px;right:30px}}
.h{{display:flex;gap:16px;align-items:flex-start;margin-bottom:{LINE//2}px}}
.h svg{{flex:none;margin-top:8px}}
.ht{{font-family:C;font-weight:600;font-size:48px;line-height:{LINE}px;color:{INK}}}
.logo{{position:absolute;left:30px;top:1196px;width:128px;height:128px;border-radius:50%;border:5px solid #fff;box-shadow:0 4px 14px rgba(0,0,0,.35)}}
.pg{{position:absolute;left:172px;top:1222px;transform:rotate(-3deg)}}
.pg div{{font-family:K;font-size:64px;line-height:1.1;white-space:nowrap}}
.pgf{{position:relative;color:#fff;z-index:2}}
.pgb{{position:absolute;left:0;top:0;color:{NAVY};-webkit-text-stroke:10px {NAVY};text-shadow:3px 5px 0 {NAVY};z-index:1}}
</style></head><body>
<img class="bg" src="{hero}"><img class="hero" src="{hero}">
<div class="paper"><div class="margin"></div><div class="hole" style="top:96px"></div>
<div class="ti">{html.escape(r['ptitel'])}</div><div class="ul" style="top:122px"></div>
<div class="zh" style="top:148px">Zutaten:</div><div class="zs" style="top:{6+LINE*5-2}px">{zl}</div>
<div class="hs" style="top:{6+LINE*4+8}px">{hz}</div></div>
<img class="logo" src="/tmp/claude-0/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/scratchpad/logos/{r['seite']}.png"><div class="pg"><div class="pgb">{html.escape(name)}</div><div class="pgf">{html.escape(name)}</div></div>
</body></html>"""

def render(keys):
    by={r['key']:r for r in G.R}
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        for key in keys:
            r=by[key]; hero=f"{D}/hero/{key}.jpg"; cut=None
            n=len(zeilen(r))
            paper_h=max(6+LINE*(5+n)+24, 520)
            open(f"{D}/out/{key}_p.html","w").write(board_html(r,hero,cut,paper_h))
            pg.goto('file://'+f"{D}/out/{key}_p.html"); pg.wait_for_timeout(400)
            info=pg.evaluate('''()=>{const t=document.querySelector('.ti');let fs=parseFloat(getComputedStyle(t).fontSize);
              while(t.scrollWidth>t.clientWidth&&fs>60){fs-=2;t.style.fontSize=fs+'px';}
              const out=[];document.querySelectorAll('.z').forEach(e=>{if(e.scrollWidth>470)out.push('Zeile zu lang: '+e.textContent)});
              const hs=document.querySelector('.hs').getBoundingClientRect(),p=document.querySelector('.paper').getBoundingClientRect();
              if(hs.bottom>p.bottom-10)out.push('Herzen laufen über');
              document.querySelectorAll('.ht').forEach(e=>{if(e.getBoundingClientRect().height>2*42+4)out.push('Herz-Satz zu lang: '+e.textContent)});
              return out;}''')
            if info: print('  !!',key,info)
            nm=f"{PREFIX}-{key}"
            pg.screenshot(path=f"{D}/out/{nm}.png")
            Image.open(f"{D}/out/{nm}.png").convert("RGB").save(f"{D}/out/{nm}.jpg",quality=92,xmp=XMP.encode())
            os.remove(f"{D}/out/{nm}.png"); print("ok",nm,paper_h)
        b.close()
if __name__=='__main__':
    render(sys.argv[1:])
