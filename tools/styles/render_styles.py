# -*- coding: utf-8 -*-
"""Stil-Varianten des G87-Boards: gleicher Aufbau (Kacheln links, Titelblock rechts, Badge, Foto, @fitmitkev),
nur Farbwelt, Schrift und Hintergrund-Textur wechseln. Aufruf: python3 render_styles.py <style> <key> ..."""
import os, sys, html, json, re
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
sys.path.insert(0,f"{S}/g87")
import g87_data as G
from foodcut import food_cut
import numpy as np
from textures import build_overlay, build_chalkwhite
F=f"{S}/fonts/gf/ofl"; TL=f"{S}/tilex/tiles_orig"; MAP=json.load(open(f"{TL}/_map_g87.json"))
HERO=f"{S}/g87/hero"; PHOTO=f"{S}/g87/assets/vorher_nachher.jpg"
OUT=f"{D}/out"; os.makedirs(OUT,exist_ok=True)
HERO_SHIFT={'SpekOats':(130,40),'BratapfelSkyrKuchen':(100,0)}
PLURAL={'Quarkbroetchen','ZimtschneckenPancakes','Pizzabroetchen','ApfelQuarkbaellchen','LaugenKnoten','SpekOats'}
XMP='''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?><x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description rdf:about="" xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/" xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/" xmlns:dc="http://purl.org/dc/elements/1.1/" photoshop:Credit="Fitmitkev"><Iptc4xmpExt:DigitalSourceType>http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia</Iptc4xmpExt:DigitalSourceType><dc:creator><rdf:Seq><rdf:li>Fitmitkev</rdf:li></rdf:Seq></dc:creator><dc:description><rdf:Alt><rdf:li xml:lang="x-default">Rezeptgrafik, Foto KI-generiert</rdf:li></rdf:Alt></dc:description></rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>'''

RAYS='''<svg style="position:absolute;left:0;top:30px" width="650" height="70" viewBox="0 0 650 70" fill="none" stroke="#b8935a" stroke-width="4" stroke-linecap="round">
<path d="M8 40 L48 32"/><path d="M14 56 L50 44"/><path d="M12 24 L48 20"/>
<path d="M642 40 L602 32"/><path d="M636 56 L600 44"/><path d="M638 24 L602 20"/></svg>'''

BASE=dict(title_font='A',t_fill='#fff',t_outline='#163b7d',t_sh='#0d1d42',t_stroke=11,t_off=(6,7),t_scale=1.0,t_ls=1,
    title_case=False,t_shadow_css='',t_fill_img='',
    hook_font='K',hook_fill='#fff',hook_stroke='#12213f',hook_size=60,hook_shadow='3px 4px 0 #12213f',
    txt='#12213f',txt2='#12213f',sub='#12213f',kc='#c1202b',kcs='#c1202b',amp='#12213f',
    glow='0 0 8px rgba(255,255,255,.95),0 0 18px rgba(255,255,255,.8),0 0 30px rgba(255,255,255,.5)',
    arrow='#12213f',badge_bg='#c61f27',badge_fg='#fff',badge_border='0',ig='#12213f',ig_font='K',ig_size=36,
    title_top=22,extra='',body_bg='#b69d82',frame=False)

STYLES={
 'aktuell':dict(name='AKTUELL · warmer Weihnachtsmarkt-Look (Montag G87)',tex='beige',
    aT=[(0,.82),(.38,.62),(.70,.25),(1,0)],aL=[(0,.85),(.55,.7),(1,0)],aB=[(0,.55),(1,0)]),
 'anthrazit':dict(name='1 · ANTHRAZIT – dunkler Stein, wie deine Küchenplatte',tex='stone',
    aT=[(0,.96),(.38,.9),(.70,.5),(1,0)],aL=[(0,.96),(.55,.85),(1,0)],aB=[(0,.9),(1,0)],
    t_fill='#ffffff',t_outline='#131417',t_sh='#d4862a',t_stroke=10,t_off=(6,7),
    hook_fill='#f5b942',hook_stroke='#131417',hook_shadow='3px 4px 0 #131417',
    txt='#f4f0e8',txt2='#d9d3c8',sub='#f4f0e8',kc='#ff6d58',kcs='#cfc7bb',amp='#f4f0e8',
    glow='0 0 8px rgba(0,0,0,.75),0 0 18px rgba(0,0,0,.55)',arrow='#f4f0e8',ig='#f4f0e8',body_bg='#2e3034'),
 'festlich':dict(name='2 · FESTLICH – Rot & Gold (Weihnachtsedition)',tex='festive',
    aT=[(0,.94),(.38,.86),(.70,.45),(1,0)],aL=[(0,.94),(.55,.82),(1,0)],aB=[(0,.88),(1,0)],
    t_fill='#fff7e6',t_outline='#b9872c',t_sh='#3b0810',t_stroke=10,t_off=(6,7),
    hook_fill='#f7c95e',hook_stroke='#3b0810',hook_shadow='3px 4px 0 #3b0810',
    txt='#fff3dd',txt2='#efdcc0',sub='#fff3dd',kc='#ffd35c',kcs='#e3cfae',amp='#fff3dd',
    glow='0 0 8px rgba(60,8,16,.8),0 0 18px rgba(60,8,16,.6)',arrow='#f7c95e',badge_border='3px solid #f7c95e',ig='#f7c95e',body_bg='#6a1220'),
 'landhaus':dict(name='3 · LANDHAUS – helles Holz, frisch & clean',tex='whitewood',
    aT=[(0,.92),(.38,.8),(.70,.3),(1,0)],aL=[(0,.92),(.55,.76),(1,0)],aB=[(0,.65),(1,0)],
    t_fill='#1f3a5f',t_outline='#ffffff',t_sh='#b9c6d6',t_stroke=10,t_off=(5,6),
    hook_fill='#c1202b',hook_stroke='#ffffff',hook_shadow='2px 3px 0 #ffffff',body_bg='#eee9e1'),
 'editorial':dict(name='4 · EDITORIAL – Creme, Serifenschrift & Gold',tex='cream',
    aT=[(0,.93),(.38,.84),(.70,.38),(1,0)],aL=[(0,.93),(.55,.8),(1,0)],aB=[(0,.7),(1,0)],
    title_font='S',t_fill='#2b1a12',t_sh=None,t_stroke=0,t_scale=0.86,t_ls=0,
    t_shadow_css='0 0 10px rgba(255,250,240,.9),0 0 24px rgba(255,250,240,.7)',
    hook_fill='#b8935a',hook_stroke='',hook_shadow='',
    txt='#2b1a12',txt2='#4a3a30',sub='#2b1a12',kc='#a3261d',kcs='#8d7b6a',amp='#2b1a12',
    arrow='#b8935a',ig='#2b1a12',body_bg='#efe6d8',extra=RAYS),
 'kreide':dict(name='5 · KREIDETAFEL – Rezept wie auf der Tafel',tex='chalk',
    aT=[(0,.97),(.38,.92),(.70,.55),(1,0)],aL=[(0,.97),(.55,.88),(1,0)],aB=[(0,.92),(1,0)],
    t_fill='#f6f3ec',t_sh='rgba(0,0,0,.4)',t_stroke=0,t_off=(3,4),t_fill_img='chalkwhite.png',
    hook_font='C',hook_fill='#f6f3ec',hook_stroke='',hook_shadow='',hook_size=70,
    txt='#f3f0e9',txt2='#d8d4cb',sub='#f3f0e9',kc='#ffe27a',kcs='#c9c4b9',amp='#f3f0e9',
    glow='0 0 6px rgba(0,0,0,.5)',arrow='#f6f3ec',ig='#f6f3ec',ig_font='C',ig_size=46,body_bg='#243029'),
 'rezeptkarte':dict(name='6 · OMAS REZEPTKARTE – Karo, Papier & Schreibschrift',tex='paper',frame=True,
    aT=[(0,.94),(.38,.84),(.70,.36),(1,0)],aL=[(0,.94),(.55,.8),(1,0)],aB=[(0,.7),(1,0)],
    title_font='L',t_fill='#b3202c',t_outline='#fff8ea',t_sh='#cdbb9e',t_stroke=8,t_off=(4,5),t_scale=0.9,t_ls=0,title_case=True,
    hook_font='C',hook_fill='#5a4632',hook_stroke='',hook_shadow='',hook_size=70,
    txt='#4a3826',txt2='#5f4b38',sub='#4a3826',kc='#b3202c',kcs='#8c7a66',amp='#4a3826',
    arrow='#5a4632',ig='#5a4632',ig_font='C',ig_size=46,title_top=34,body_bg='#f4ecdc'),
}
for k,v in STYLES.items(): STYLES[k]={**BASE,**v}

def tcase(s): return re.sub(r"[A-ZÄÖÜ][A-ZÄÖÜ]+",lambda m:m.group(0)[0]+m.group(0)[1:].lower(),s)

def food_cut_light(key):
    """Freisteller nur hinter der Kachelspalte maskieren – im Titelblock bleibt das Essen oberste Ebene
    (Titel hat Kontur, kcal-Zeile hat Glow)."""
    dst=f"{OUT}/cut_{key}.png"
    if os.path.exists(dst): return dst
    food_cut(key)
    rgba=np.asarray(Image.open(f"{S}/g87/hero_cut/{key}.png").convert('RGBA')).copy(); h,w=rgba.shape[:2]
    sx,sy=w/1080,h/1350; yy,xx=np.mgrid[0:h,0:w]; X=xx/sx; Y=yy/sy
    dx=np.maximum(np.maximum(0-X,X-430),0); dy=np.maximum(np.maximum(0-Y,Y-765),0)
    m=np.clip(np.hypot(dx,dy)/40,0,1)
    rgba[:,:,3]=(rgba[:,:,3]*m).astype(np.uint8)
    Image.fromarray(rgba).save(dst); return dst

def tile_img(tile,scale):
    p=f"{TL}/{MAP.get(tile,tile)}.png"
    if not os.path.exists(p): raise SystemExit(f"Kachel fehlt: {tile}")
    w,h=Image.open(p).size
    return p,round(w/2*scale),round(h/2*scale)

def board_html(r,st,hero,herocut,overlay):
    k,p,c,f=G.macros4(r)
    n=len(r['zutaten']); scale=1.2 if n<=7 else 1.1
    colh=704 if n>=8 else 690
    hs=[Image.open(f"{TL}/{MAP.get(z['tile'],z['tile'])}.png").size[1]/2 for z in r['zutaten']]
    def total(sc): return sum(max(h*sc,58)+4 for h in hs)
    while total(scale)>colh-6 and scale>0.7: scale-=0.02
    rows=""
    for z in r['zutaten']:
        src,w,h=tile_img(z['tile'],scale)
        rows+=(f'<div class="row"><div class="tb"><img src="{src}" style="width:{w}px;height:{h}px"></div>'
               f'<div class="tx"><div class="amt">{html.escape(z["menge"])}</div><div class="nm">{html.escape(z["name"])}</div></div></div>')
    tit=[tcase(t) if st['title_case'] else t for t in r['titel']]
    t1=html.escape(tit[0]); t2=html.escape(tit[1]) if len(tit)>1 else ''
    L=max(len(x) for x in r['titel'])
    tsize=(130 if L<=9 else (122 if L<=11 else (112 if L<=13 else (100 if L<=15 else 90))))*st['t_scale']
    lh=1.08 if any(ch in (r['titel'][1] if len(r['titel'])>1 else '') for ch in 'ÄÖÜ') else 1.0
    if st['title_font'] in 'LS': lh=max(lh,1.05)
    verb='haben' if r['key'] in PLURAL else 'hat'
    layers=''
    if st['t_sh']: layers+=f'<div class="t-sh">{t1}<br>{t2}</div>'
    if st['t_stroke']>0: layers+=f'<div class="t-ol">{t1}<br>{t2}</div>'
    layers+=f'<div class="t-fi">{t1}<br>{t2}</div>'
    hook=html.escape(r['hook'])
    hookb=f'<div class="hookb">{hook}</div>' if st['hook_stroke'] else ''
    dx,dy=HERO_SHIFT.get(r['key'],(0,0)); shift=f'left:{dx}px;top:{dy}px' if (dx or dy) else ''
    fill_css=(f"background:url('{OUT}/{st['t_fill_img']}') 0 0/540px 675px;-webkit-background-clip:text;color:transparent;"
              if st['t_fill_img'] else f"color:{st['t_fill']};")
    shadow_css=f"text-shadow:{st['t_shadow_css']};" if st['t_shadow_css'] else ''
    sh_stroke=f"-webkit-text-stroke:{st['t_stroke']}px {st['t_sh']};" if (st['t_sh'] and st['t_stroke']>0) else ''
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:A;src:url('{F}/anton/Anton-Regular.ttf')}}
@font-face{{font-family:K;src:url('{F}/kaushanscript/KaushanScript-Regular.ttf')}}
@font-face{{font-family:L;src:url('{F}/lobster/Lobster-Regular.ttf')}}
@font-face{{font-family:S;src:url('{F}/dmserifdisplay/DMSerifDisplay-Regular.ttf')}}
@font-face{{font-family:C;src:url('{F}/caveat/Caveat[wght].ttf');font-weight:400 700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-SemiBold.ttf');font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:P;background:{st['body_bg']}}}
.hero,.ov{{position:absolute;left:0;top:0;width:1080px;height:1350px;object-fit:cover}}
.col{{position:absolute;left:40px;top:38px;width:380px;height:{colh}px;display:flex;flex-direction:column;justify-content:space-evenly}}
.row{{display:flex;align-items:center;gap:14px}}
.tb{{width:100px;flex:none;display:flex;justify-content:center;align-items:center}}
.tx{{flex:1;min-width:0}}
.amt{{font-size:29px;font-weight:700;color:{st['txt']};line-height:1.0}}
.nm{{font-size:21px;font-weight:600;color:{st['txt2']};line-height:1.12;margin-top:3px}}
.title{{position:absolute;left:400px;top:{st['title_top']}px;width:650px;text-align:center}}
.hookw{{display:inline-block;position:relative;transform:rotate(-4deg);margin-bottom:8px}}
.hook{{font-family:{st['hook_font']};font-weight:700;font-size:{st['hook_size']}px;color:{st['hook_fill']};line-height:1.15;position:relative;z-index:2;white-space:nowrap}}
.hookb{{position:absolute;left:0;top:0;font-family:{st['hook_font']};font-weight:700;font-size:{st['hook_size']}px;line-height:1.15;color:{st['hook_stroke'] or 'transparent'};-webkit-text-stroke:9px {st['hook_stroke'] or 'transparent'};text-shadow:{st['hook_shadow'] or 'none'};z-index:1;white-space:nowrap}}
.tw{{position:relative;display:block;margin-top:6px}}
.tw div{{font-family:{st['title_font']};font-size:{tsize:.0f}px;line-height:{lh};letter-spacing:{st['t_ls']}px;white-space:nowrap;width:100%}}
.t-fi{{position:relative;z-index:3;{fill_css}{shadow_css}}}
.t-ol{{position:absolute;left:0;top:0;color:{st['t_outline']};-webkit-text-stroke:{st['t_stroke']}px {st['t_outline']};z-index:2}}
.t-sh{{position:absolute;left:{st['t_off'][0]}px;top:{st['t_off'][1]}px;color:{st['t_sh']};{sh_stroke}z-index:1}}
.sub{{font-size:34px;font-weight:700;color:{st['sub']};margin-top:14px;line-height:1.1;text-shadow:{st['glow']}}}
.kc{{font-size:37px;font-weight:700;color:{st['kc']};margin-top:2px;line-height:1.15;text-shadow:{st['glow']}}}
.kc s{{color:{st['kcs']};opacity:.78;margin-right:8px;font-size:31px}}
.kc .amp{{color:{st['amp']}}}
.arrow{{position:absolute;left:296px;top:588px}}
.badge{{position:absolute;left:100px;top:890px;background:{st['badge_bg']};color:{st['badge_fg']};font-family:A;font-size:50px;padding:2px 28px 4px;border-radius:14px;letter-spacing:1px;line-height:1.1;border:{st['badge_border']}}}
.photo{{position:absolute;left:43px;top:968px;width:280px;height:288px;border-radius:20px;border:6px solid #fff;object-fit:cover;box-shadow:0 6px 16px rgba(0,0,0,.18)}}
.ig{{position:absolute;left:118px;top:1258px;font-family:{st['ig_font']};font-weight:700;font-size:{st['ig_size']}px;color:{st['ig']}}}
</style></head><body>
<img class="hero" src="{hero}" style="{shift}"><img class="ov" src="{overlay}"><img class="hero" src="{herocut}" style="{shift}">
<div class="col">{rows}</div>
<div class="title">{st['extra']}<div class="hookw">{hookb}<div class="hook">{hook}</div></div>
<div class="tw">{layers}</div>
<div class="sub">{verb} {html.escape(r['portion'])} nur</div>
<div class="kc"><s>{r['vs']} kcal</s> {k} kcal <span class="amp">&amp;</span> {p} g Protein</div></div>
<svg class="arrow" width="140" height="100" viewBox="0 0 140 100"><path d="M6 14 C 50 2, 100 20, 118 78" stroke="{st['arrow']}" stroke-width="8" fill="none" stroke-linecap="round"/><path d="M96 70 L120 84 L124 56" stroke="{st['arrow']}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="badge">-50 kg</div>
<img class="photo" src="{PHOTO}">
<div class="ig">@fitmitkev</div>
</body></html>"""

JS='''()=>{const ds=[...document.querySelectorAll('.tw div')];const fi=document.querySelector('.t-fi');let fs=parseFloat(getComputedStyle(fi).fontSize);
  const w=()=>{const r=document.createRange();r.selectNodeContents(fi);return r.getBoundingClientRect().width;};
  while(w()>640&&fs>50){fs-=2;ds.forEach(d=>d.style.fontSize=fs+'px');}
  const hk=[...document.querySelectorAll('.hook,.hookb')];let hs=parseFloat(getComputedStyle(hk[0]).fontSize);
  while(hk[0].offsetWidth>600&&hs>34){hs-=2;hk.forEach(d=>d.style.fontSize=hs+'px');}
  const kc=document.querySelector('.kc');let ks=parseFloat(getComputedStyle(kc).fontSize);
  while(kc.scrollWidth>650&&ks>26){ks-=1;kc.style.fontSize=ks+'px';}}'''

def render(styles,keys):
    by={r['key']:r for r in G.R}
    build_chalkwhite(OUT)
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        for sk in styles:
            st=STYLES[sk]; ov=build_overlay(sk,st,OUT)
            for key in keys:
                r=by[key]; hero=f"{HERO}/{key}.jpg"
                h=board_html(r,st,hero,food_cut(key) if sk=='aktuell' else food_cut_light(key),ov); hp=f"{OUT}/{sk}-{key}.html"; open(hp,"w").write(h)
                pg.goto('file://'+hp); pg.wait_for_timeout(400); pg.evaluate(JS); pg.wait_for_timeout(250)
                png=f"{OUT}/{sk}-{key}.png"; pg.screenshot(path=png)
                Image.open(png).convert("RGB").save(f"{OUT}/STIL-{sk}-{key}.jpg",quality=92,xmp=XMP.encode())
                os.remove(png); os.remove(hp); print("ok",sk,key)
        b.close()

if __name__=='__main__':
    a=sys.argv[1:]
    styles=[x for x in a if x in STYLES] or list(STYLES)
    keys=[x for x in a if x not in STYLES] or ['BratapfelSkyrKuchen','LasagneSuppe']
    render(styles,keys)
