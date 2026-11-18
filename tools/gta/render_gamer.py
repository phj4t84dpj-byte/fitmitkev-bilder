# -*- coding: utf-8 -*-
"""Gamer-Look für den GTA-6-Tag (Do 19.11.2026, Kev 18.11. 22:14: „ich brauche dafür den Gamer Look“).
Gleiches Board-Gerüst wie render_gta.py (Kachelspalte, Titel, kcal-Zeile, -50 kg, Foto), aber dunkel mit Neon:
dunkler Hintergrund, Neon-Pink/Cyan am Titel, Neon-Schriftzug als Hook, grüne kcal-Zeile, Neon-Rahmen.
Keine Spiel-Logos, keine Figuren, keine Spiel-Schrift – „GTA“ steht nur als normaler Text im Hook."""
import os, sys, json
from PIL import Image
from playwright.sync_api import sync_playwright
import render_gta as RG
G=RG.G; D=RG.D
PINK="#ff2e9a"; CYAN="#19e3ff"; GREEN="#62ff7e"; BG="13,8,32"
CSS=f"""
body{{background:rgb({BG})}}
.fadeT{{background:linear-gradient(to bottom,rgba({BG},.90) 0%,rgba({BG},.72) 38%,rgba({BG},.30) 70%,rgba({BG},0) 100%)}}
.fadeL{{background:linear-gradient(to right,rgba({BG},.92) 0%,rgba({BG},.78) 55%,rgba({BG},0) 100%)}}
.fadeB{{background:linear-gradient(to right,rgba({BG},.62) 0%,rgba({BG},0) 100%)}}
.amt{{color:#fff}} .nm{{color:#d8d2ff}}
.hookb{{display:none}}
.hook{{color:#fff;text-shadow:0 0 6px #fff,0 0 14px {PINK},0 0 30px {PINK},0 0 54px {PINK}}}
.t-ol{{color:{PINK};-webkit-text-stroke:11px {PINK}}}
.t-sh{{color:{CYAN};-webkit-text-stroke:11px {CYAN};left:7px;top:8px}}
.tw{{filter:drop-shadow(0 0 18px rgba(255,46,154,.45))}}
.sub{{color:#fff;text-shadow:0 0 10px rgba(0,0,0,.95),0 0 22px rgba(0,0,0,.8)}}
.kc{{color:{GREEN};text-shadow:0 0 10px rgba(0,0,0,.95),0 0 22px rgba(0,0,0,.8)}}
.kc s{{color:#ff7fb0;opacity:.9}}
.kc .amp{{color:#fff}}
.badge{{box-shadow:0 0 18px rgba(198,31,39,.75)}}
.photo{{border-color:#fff;box-shadow:0 0 0 3px {CYAN},0 0 26px rgba(25,227,255,.75)}}
.ig{{color:#fff;text-shadow:0 0 12px rgba(0,0,0,.9)}}
.frame{{position:absolute;left:12px;top:12px;width:1056px;height:1326px;border-radius:30px;border:5px solid transparent;
  background:linear-gradient(135deg,{CYAN},{PINK} 50%,{CYAN}) border-box;-webkit-mask:linear-gradient(#000 0 0) padding-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;filter:drop-shadow(0 0 10px rgba(255,46,154,.8));pointer-events:none}}
.tag{{position:absolute;right:40px;bottom:36px;background:rgba({BG},.82);border:3px solid {CYAN};border-radius:16px;padding:6px 18px 7px;
  font-family:A;font-size:30px;letter-spacing:1.5px;color:#fff;box-shadow:0 0 16px rgba(25,227,255,.6)}}
.tag b{{color:{GREEN};font-weight:400}}
.tag i{{color:{PINK};font-style:normal;text-shadow:0 0 10px rgba(255,46,154,.8)}}
"""
def gamer_html(r,hero,herocut):
    h=RG.board_html(r,hero,herocut)
    h=h.replace('</style>',CSS+'</style>').replace(f'stroke="{RG.NAVY}"',f'stroke="{CYAN}"')
    h=h.replace('</body>','<div class="tag">🎮 <i>GTA VI</i> ZOCKER-FUTTER <b>IN LEICHT</b></div><div class="frame"></div></body>')
    return h
def render(keys):
    by={r['key']:r for r in G.R}
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        for key in keys:
            r=by[key]; hero=f"{D}/hero/{key}.jpg"
            if not os.path.exists(hero): print("kein Hero:",key); continue
            from foodcut import food_cut
            open(f"{D}/out/{key}.html","w").write(gamer_html(r,hero,food_cut(key)))
            pg.goto('file://'+f"{D}/out/{key}.html"); pg.wait_for_timeout(350)
            pg.evaluate('''()=>{const ds=[...document.querySelectorAll('.tw div')];let fs=parseFloat(getComputedStyle(ds[0]).fontSize);
              const w=()=>{const r=document.createRange();r.selectNodeContents(ds[2]);return r.getBoundingClientRect().width;};
              while(w()>640&&fs>60){fs-=2;ds.forEach(d=>d.style.fontSize=fs+'px');}
              const hk=[document.querySelector('.hook'),document.querySelector('.hookb')];let hs=parseFloat(getComputedStyle(hk[0]).fontSize);
              while(hk[0].offsetWidth>600&&hs>34){hs-=2;hk.forEach(d=>d.style.fontSize=hs+'px');}
              const kc=document.querySelector('.kc');let ks=parseFloat(getComputedStyle(kc).fontSize);
              while(kc.scrollWidth>650&&ks>26){ks-=1;kc.style.fontSize=ks+'px';}
              document.querySelector('.rib').style.display='none';}''')
            pg.wait_for_timeout(200)
            assert 'GTA VI' in r['hook'] or 'GTA-VI' in r['hook'], key
            hits=pg.evaluate('''()=>{const A=document.querySelector('.arrow').getBoundingClientRect();const P=[[6,14],[50,2],[100,20],[118,78]];const pts=[];
              for(let i=0;i<=40;i++){const t=i/40,u=1-t;pts.push([A.left+u*u*u*P[0][0]+3*u*u*t*P[1][0]+3*u*t*t*P[2][0]+t*t*t*P[3][0],A.top+u*u*u*P[0][1]+3*u*u*t*P[1][1]+3*u*t*t*P[2][1]+t*t*t*P[3][1]]);}
              [[96,70],[120,84],[124,56]].forEach(p=>pts.push([A.left+p[0],A.top+p[1]]));const hits=[];
              document.querySelectorAll('.amt,.nm').forEach(e=>{const r=document.createRange();r.selectNodeContents(e);
                for(const b of r.getClientRects()){if(pts.some(p=>p[0]>b.left-10&&p[0]<b.right+10&&p[1]>b.top-3&&p[1]<b.bottom+3)){hits.push(e.textContent);break;}}});
              const col=document.querySelector('.col').getBoundingClientRect();let ov=0;document.querySelectorAll('.row').forEach(e=>{const b=e.getBoundingClientRect();if(b.bottom>col.bottom+2||b.top<col.top-2)ov++;});
              if(ov)hits.push('SPALTE LÄUFT ÜBER');return hits;}''')
            if hits: print('  !! Pfeil/Spalte kollidiert mit:',hits)
            nm=f"GTAVI-{key}"
            pg.screenshot(path=f"{D}/out/{nm}.png")
            Image.open(f"{D}/out/{nm}.png").convert("RGB").save(f"{D}/out/{nm}.jpg",quality=92,xmp=RG.XMP.encode())
            os.remove(f"{D}/out/{nm}.png"); print("ok",nm)
        b.close()
if __name__=='__main__':
    render(sys.argv[1:] or [r['key'] for r in G.R])
