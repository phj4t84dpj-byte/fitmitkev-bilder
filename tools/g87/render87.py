# -*- coding: utf-8 -*-
"""Facebook-Rezeptboard 1080x1350 (Ausgabe 2160x2700) im Original-Look (Quarkbällchen-Referenz):
   Original-Kacheln (aus den gesicherten Boards ausgeschnitten, tilex/tiles_orig), Anton/Kaushan/Poppins,
   weißer Titel mit blauer Kontur + dunklem Schlagschatten, warmer Hero mit Beige-Verlauf."""
import os, sys, html, json
from PIL import Image
from playwright.sync_api import sync_playwright
import g87_data as G
D=os.path.dirname(os.path.abspath(__file__))
S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"
TL=f"{S}/tilex/tiles_orig"
MAP=json.load(open(f"{TL}/_map_g87.json"))
os.makedirs(f"{D}/out",exist_ok=True)
NAVY="#12213f"; BLUE="#163b7d"; DARK="#0d1d42"; RED="#c1202b"; BADGE="#c61f27"
PLURAL={'Quarkbroetchen','ZimtschneckenPancakes','Pizzabroetchen','ApfelQuarkbaellchen','LaugenKnoten','SpekOats'}
XMP='''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?><x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/" xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/" xmlns:dc="http://purl.org/dc/elements/1.1/" photoshop:Credit="Fitmitkev"><Iptc4xmpExt:DigitalSourceType>http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia</Iptc4xmpExt:DigitalSourceType><dc:creator><rdf:Seq><rdf:li>Fitmitkev</rdf:li></rdf:Seq></dc:creator><dc:description><rdf:Alt><rdf:li xml:lang="x-default">Rezeptgrafik, Foto KI-generiert</rdf:li></rdf:Alt></dc:description></rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>'''

def tile_img(tile, scale):
    p=f"{TL}/{MAP.get(tile,tile)}.png"
    if not os.path.exists(p): raise SystemExit(f"Kachel fehlt: {tile}")
    w,h=Image.open(p).size
    return p, round(w/2*scale), round(h/2*scale)

def board_html(r,hero):
    k,p,c,f=G.macros4(r)
    n=len(r['zutaten']); scale=1.2 if n<=7 else 1.1
    rows=""
    for z in r['zutaten']:
        src,w,h=tile_img(z['tile'],scale)
        rows+=(f'<div class="row"><div class="tb"><img src="{src}" style="width:{w}px;height:{h}px"></div>'
               f'<div class="tx"><div class="amt">{html.escape(z["menge"])}</div><div class="nm">{html.escape(z["name"])}</div></div></div>')
    t1=html.escape(r['titel'][0]); t2=html.escape(r['titel'][1]) if len(r['titel'])>1 else ''
    L=max(len(x) for x in r['titel'])
    tsize=130 if L<=9 else (122 if L<=11 else (112 if L<=13 else (100 if L<=15 else 90)))
    lh=1.08 if any(ch in (r['titel'][1] if len(r['titel'])>1 else '') for ch in 'ÄÖÜ') else 1.0
    verb='haben' if r['key'] in PLURAL else 'hat'
    title_layers=''.join(f'<div class="{cls}">{t1}<br>{t2}</div>' for cls in ('t-sh','t-ol','t-fi'))
    hook=html.escape(r['hook'])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:A;src:url('{F}/anton/Anton-Regular.ttf')}}
@font-face{{font-family:K;src:url('{F}/kaushanscript/KaushanScript-Regular.ttf')}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-SemiBold.ttf');font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:P;background:#b69d82}}
.hero{{position:absolute;left:0;top:0;width:1080px;height:1350px;object-fit:cover}}
.fadeT{{position:absolute;left:0;top:0;width:1080px;height:820px;background:linear-gradient(to bottom,rgba(181,157,132,.82) 0%,rgba(181,157,132,.62) 38%,rgba(181,157,132,.25) 70%,rgba(181,157,132,0) 100%)}}
.fadeL{{position:absolute;left:0;top:0;width:520px;height:1100px;background:linear-gradient(to right,rgba(181,157,132,.85) 0%,rgba(181,157,132,.7) 55%,rgba(181,157,132,0) 100%)}}
.fadeB{{position:absolute;left:0;top:850px;width:420px;height:500px;background:linear-gradient(to right,rgba(181,157,132,.55) 0%,rgba(181,157,132,0) 100%)}}
.col{{position:absolute;left:40px;top:38px;width:380px;height:{704 if n>=8 else 690}px;display:flex;flex-direction:column;justify-content:space-evenly}}
.row{{display:flex;align-items:center;gap:14px}}
.tb{{width:100px;flex:none;display:flex;justify-content:center;align-items:center}}
.tx{{flex:1;min-width:0}}
.amt{{font-size:29px;font-weight:700;color:{NAVY};line-height:1.0}}
.nm{{font-size:21px;font-weight:600;color:{NAVY};line-height:1.12;margin-top:3px}}
.title{{position:absolute;left:400px;top:22px;width:650px;text-align:center}}
.hookw{{display:inline-block;position:relative;transform:rotate(-4deg);margin-bottom:8px}}
.hook{{font-family:K;font-size:60px;color:#fff;line-height:1.15;position:relative;z-index:2;white-space:nowrap}}
.hookb{{position:absolute;left:0;top:0;font-family:K;font-size:60px;line-height:1.15;color:{NAVY};-webkit-text-stroke:9px {NAVY};text-shadow:3px 4px 0 {NAVY};z-index:1;white-space:nowrap}}
.tw{{position:relative;display:block;margin-top:6px}}
.tw div{{font-family:A;font-size:{tsize}px;line-height:{lh};letter-spacing:1px;white-space:nowrap;width:100%}}
.t-fi{{position:relative;color:#fff;z-index:3}}
.t-ol{{position:absolute;left:0;top:0;color:{BLUE};-webkit-text-stroke:11px {BLUE};z-index:2}}
.t-sh{{position:absolute;left:6px;top:7px;color:{DARK};-webkit-text-stroke:11px {DARK};z-index:1}}
.sub{{font-size:34px;font-weight:700;color:{NAVY};margin-top:14px;line-height:1.1;text-shadow:0 0 8px rgba(255,255,255,.95),0 0 18px rgba(255,255,255,.8),0 0 30px rgba(255,255,255,.5)}}
.kc{{font-size:37px;font-weight:700;color:{RED};margin-top:2px;line-height:1.15;text-shadow:0 0 8px rgba(255,255,255,.95),0 0 18px rgba(255,255,255,.8),0 0 30px rgba(255,255,255,.5)}}
.kc s{{color:{RED};opacity:.72;margin-right:8px;font-size:31px}}
.kc .amp{{color:{NAVY}}}
.arrow{{position:absolute;left:296px;top:588px}}
.badge{{position:absolute;left:100px;top:890px;background:{BADGE};color:#fff;font-family:A;font-size:50px;padding:2px 28px 4px;border-radius:14px;letter-spacing:1px;line-height:1.1}}
.photo{{position:absolute;left:43px;top:968px;width:280px;height:288px;border-radius:20px;border:6px solid #fff;object-fit:cover;box-shadow:0 6px 16px rgba(0,0,0,.18)}}
.ig{{position:absolute;left:118px;top:1258px;font-family:K;font-size:36px;color:{NAVY}}}
</style></head><body>
<img class="hero" src="{hero}"><div class="fadeT"></div><div class="fadeL"></div><div class="fadeB"></div>
<div class="col">{rows}</div>
<div class="title"><div class="hookw"><div class="hookb">{hook}</div><div class="hook">{hook}</div></div>
<div class="tw">{title_layers}</div>
<div class="sub">{verb} {html.escape(r['portion'])} nur</div>
<div class="kc"><s>{r['vs']} kcal</s> {k} kcal <span class="amp">&amp;</span> {p} g Protein</div></div>
<svg class="arrow" width="140" height="100" viewBox="0 0 140 100"><path d="M6 14 C 50 2, 100 20, 118 78" stroke="{NAVY}" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M96 70 L120 84 L124 56" stroke="{NAVY}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="badge">-50 kg</div>
<img class="photo" src="{D}/assets/vorher_nachher.jpg">
<div class="ig">@fitmitkev</div>
</body></html>"""

def render(keys):
    by={r['key']:r for r in G.R}
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        for key in keys:
            r=by[key]; hero=f"{D}/hero/{key}.jpg"
            if not os.path.exists(hero): print("kein Hero:",key); continue
            h=board_html(r,hero); open(f"{D}/out/{key}.html","w").write(h)
            pg.goto('file://'+f"{D}/out/{key}.html"); pg.wait_for_timeout(350)
            pg.evaluate('''()=>{const ds=[...document.querySelectorAll('.tw div')];let fs=parseFloat(getComputedStyle(ds[0]).fontSize);
              const w=()=>{const r=document.createRange();r.selectNodeContents(ds[2]);return r.getBoundingClientRect().width;};
              while(w()>640&&fs>60){fs-=2;ds.forEach(d=>d.style.fontSize=fs+'px');}
              const hk=[document.querySelector('.hook'),document.querySelector('.hookb')];let hs=parseFloat(getComputedStyle(hk[0]).fontSize);
              while(hk[0].offsetWidth>600&&hs>34){hs-=2;hk.forEach(d=>d.style.fontSize=hs+'px');}
              const kc=document.querySelector('.kc');let ks=parseFloat(getComputedStyle(kc).fontSize);
              while(kc.scrollWidth>650&&ks>26){ks-=1;kc.style.fontSize=ks+'px';}}''')
            pg.wait_for_timeout(200)
            pg.screenshot(path=f"{D}/out/G87-{key}.png")
            Image.open(f"{D}/out/G87-{key}.png").convert("RGB").save(f"{D}/out/G87-{key}.jpg",quality=92,xmp=XMP.encode())
            os.remove(f"{D}/out/G87-{key}.png"); print("ok",key)
        b.close()
if __name__=='__main__':
    render(sys.argv[1:] or [r['key'] for r in G.R])
