# Reel „10 Proteinquellen“ (1080x1920, 30 fps): je Quelle oben der Name, in der Mitte das Foto, darunter Protein und kcal je 100 g.
# Getaktet auf die Wort-Zeiten von Kevs Stimme (ausrichten.py). Aufruf: python3 protein.py <zeiten.json> <bilder-ordner> <aus.mp4>
import os, sys, json, random, subprocess
from playwright.sync_api import sync_playwright
from protein_daten import ITEMS, text

D = os.path.dirname(os.path.abspath(__file__)); S = os.path.dirname(D)
FO = f"{S}/fonts"; VN = f"{S}/render/vorher_nachher.jpg"
NAVY, BLUE, DARK, RED, GREEN, BADGE = "#12213f", "#163b7d", "#0d1d42", "#c1202b", "#2e7d32", "#c61f27"
VOR, NACH, FPS = 0.5, 2.8, 30


def T(txt, size, sw=13):
    return (f'<div class="tw" style="font-size:{size}px"><div class="t-sh" style="-webkit-text-stroke:{sw}px {DARK}">{txt}</div>'
            f'<div class="t-ol" style="-webkit-text-stroke:{sw}px {BLUE}">{txt}</div><div class="t-fi">{txt}</div></div>')


def html(bd):
    random.seed(9)
    bok = ''.join(f'<div class="b" style="left:{random.randint(-60,1080)}px;top:{random.randint(-60,1900)}px;width:{(s:=random.randint(40,150))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,10)}px)"></div>' for _ in range(60))
    items = ""
    for i, (k, name, _, p, _, kc, _, zus) in enumerate(ITEMS):
        items += (f'<div class="it" id="i{i}"><div class="nm">{T(name.upper(), 116 if len(name) < 12 else 96)}</div>'
                  f'<img class="ph2" src="{bd}/{k}.jpg">'
                  f'<div class="pills"><div class="pl pr" id="p{i}">{p} g Protein</div><div class="pl kc" id="c{i}">{kc} kcal</div></div>'
                  f'<div class="zu">{zus}</div></div>')
    thumbs = ''.join(f'<img src="{bd}/{k}.jpg">' for k, *_ in ITEMS)
    rows = ''.join(f'<div class="rr"><img src="{bd}/{k}.jpg"><span class="rn">{name}</span><span class="rp">{p} g</span><span class="rk">{kc} kcal</span></div>'
                   for k, name, _, p, _, kc, _, _ in ITEMS)
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:A;src:url('{FO}/Anton-Regular.ttf')}}
@font-face{{font-family:K;src:url('{FO}/KaushanScript-Regular.ttf')}}
@font-face{{font-family:P;src:url('{FO}/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{FO}/Poppins-SemiBold.ttf');font-weight:600}}
body{{margin:0;width:1080px;height:1920px;overflow:hidden;position:relative;font-family:P;background:radial-gradient(ellipse at 70% 30%,#d9c3a5 0%,#c7ab89 45%,#b0926f 100%)}}
#bk{{position:absolute;left:0;top:0;width:1080px;height:1920px;transform-origin:50% 40%}}
.b{{position:absolute;border-radius:50%;background:radial-gradient(circle,#fff3c9 0%,#ffd98a 55%,rgba(255,210,120,0) 72%)}}
.brand{{position:absolute;left:60px;top:70px;display:flex;align-items:center;gap:16px}}
.ph{{width:96px;height:100px;border-radius:12px;border:4px solid #fff;object-fit:cover}}
.badge{{background:{BADGE};color:#fff;font-family:A;font-size:40px;padding:0 18px 2px;border-radius:12px;line-height:1.15}}
.ig{{font-family:K;font-size:38px;color:{NAVY}}}
.cnt{{position:absolute;right:60px;top:88px;background:{NAVY};color:#fff;font-family:A;font-size:44px;border-radius:14px;padding:2px 22px 4px;opacity:0}}
.head{{position:absolute;left:0;top:200px;width:1080px;text-align:center}}
.hookw{{display:inline-block;position:relative;transform:rotate(-4deg)}}
.hook,.hookb{{font-family:K;font-size:64px;line-height:1.15;white-space:nowrap}}
.hook{{color:#fff;position:relative;z-index:2}}
.hookb{{position:absolute;left:0;top:0;color:{NAVY};-webkit-text-stroke:10px {NAVY};text-shadow:3px 5px 0 {NAVY};z-index:1}}
.tw{{position:relative;font-family:A;line-height:1.04;letter-spacing:1px}}
.t-fi{{position:relative;color:#fff;z-index:3}}
.t-ol{{position:absolute;left:0;top:0;width:100%;color:{BLUE};z-index:2}}
.t-sh{{position:absolute;left:7px;top:8px;width:100%;color:{DARK};z-index:1}}
.it{{position:absolute;left:0;top:420px;width:1080px;text-align:center;opacity:0}}
.nm{{height:140px;display:flex;align-items:flex-end;justify-content:center}}
.ph2{{width:820px;height:820px;object-fit:cover;border-radius:36px;border:8px solid #fff;box-shadow:0 14px 34px rgba(60,40,20,.3);margin-top:26px}}
.pills{{display:flex;justify-content:center;gap:28px;margin-top:30px}}
.pl{{font-family:A;font-size:76px;color:#fff;border-radius:24px;padding:4px 34px 8px;box-shadow:0 8px 20px rgba(60,40,20,.25);opacity:0}}
.pr{{background:{GREEN}}} .kc{{background:{NAVY}}}
.zu{{font-size:36px;font-weight:600;color:{NAVY};margin-top:14px}}
#intro{{position:absolute;left:0;top:430px;width:1080px;text-align:center;opacity:0}}
#intro .g{{display:grid;grid-template-columns:repeat(4,220px);gap:22px;justify-content:center;margin-top:28px}}
#intro .g img{{width:220px;height:220px;object-fit:cover;border-radius:24px;border:6px solid #fff;box-shadow:0 8px 20px rgba(60,40,20,.25)}}
#intro .g img:nth-child(9){{grid-column:2}}
#intro .sub{{font-size:46px;font-weight:700;color:{NAVY}}}
#out{{position:absolute;left:60px;top:420px;width:960px;opacity:0}}
.rr{{display:flex;align-items:center;background:rgba(255,255,255,.95);border-radius:18px;margin-bottom:10px;padding:6px 18px 6px 6px;box-shadow:0 6px 14px rgba(60,40,20,.18);font-size:36px;font-weight:700;color:{NAVY}}}
.rr img{{width:76px;height:76px;object-fit:cover;border-radius:12px;margin-right:20px}}
.rn{{flex:1}} .rp{{width:150px;text-align:right;color:{GREEN};font-family:A;font-size:46px;font-weight:400}} .rk{{width:200px;text-align:right;font-family:A;font-size:46px;font-weight:400}}
#fr{{position:absolute;left:60px;top:1540px;width:960px;height:110px;border-radius:24px;background:#fff6e0;border:4px solid #e9a23b;color:{NAVY};font-size:46px;font-weight:700;display:flex;align-items:center;justify-content:center;opacity:0}}
</style></head><body><div id="bk">{bok}</div>
<div class="brand"><img class="ph" src="{VN}"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="cnt" id="cnt">1/10</div>
<div class="head"><div class="hookw"><div class="hookb">pro 100 g</div><div class="hook">pro 100 g</div></div>{T('10 PROTEINQUELLEN', 92, 11)}</div>
<div id="intro"><div class="sub">Protein und Kalorien im Vergleich</div><div class="g">{thumbs}</div></div>
{items}<div id="out">{rows}</div><div id="fr"><span>💬 Welche ist dein Favorit?</span></div>
<script>
function e(x){{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}}
window.render=function(t,S){{
 document.getElementById('bk').style.transform='scale('+(1+t*0.003)+')';
 const I=S.items, n=I.length;
 const it=document.getElementById('intro'); let a=e(t/.4), z=Math.max(0,1-(t-(I[0][0]-.3))/.3); it.style.opacity=Math.min(a,z);
 let cur=-1;
 for(let i=0;i<n;i++){{
  const el=document.getElementById('i'+i), s=I[i][0], en=(i+1<n?I[i+1][0]:S.outro);
  if(t<s-.05||t>en+.3){{el.style.opacity=0;continue;}}
  if(t>=s) cur=i;
  const pin=e((t-s)/.3), pout=t>en?e((t-en)/.3):0;
  el.style.opacity=Math.min(pin,1-pout); el.style.transform='translateX('+(140*(1-pin)-160*pout)+'px)';
  [['p',1],['c',2]].forEach(([id,k])=>{{const q=e((t-I[i][k])/.3); const x=document.getElementById(id+i); x.style.opacity=q; x.style.transform='scale('+(1.35-0.35*q)+')';}});
 }}
 const c=document.getElementById('cnt'); if(cur>=0&&t<S.outro){{c.style.opacity=1;c.textContent=(cur+1)+'/10';}} else c.style.opacity=0;
 const o=document.getElementById('out'), po=e((t-S.outro)/.4); o.style.opacity=po; o.style.transform='translateY('+(40*(1-po))+'px)';
 const fr=document.getElementById('fr'), pf=e((t-S.outro-.2)/.35); fr.style.opacity=pf; fr.style.transform='scale('+(0.85+0.15*pf)+')';
}};
</script></body></html>"""


def main(zpath, bd, aus):
    z = json.load(open(zpath)); W = z["woerter"]
    sprech, idx, io = text()
    toks = [x for x in sprech.split() if x != "–"]
    assert len(toks) == len(W), (len(toks), len(W))
    st = [VOR + w["s"] for w in W]
    S = {"items": [[st[a] - 0.1, st[pz] - 0.05, st[kz] - 0.05] for a, pz, kz in idx], "outro": st[io] - 0.1}
    dauer = VOR + z["dauer"] + NACH
    print("Dauer", round(dauer, 2), S, flush=True)
    hp = "/tmp/claude-0/protein_reel.html"; open(hp, "w").write(html(bd))
    n = int(dauer * FPS)
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", aus], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto("file://" + hp); pg.wait_for_timeout(800)
        for f in range(n):
            pg.evaluate("([t,S])=>render(t,S)", [f / FPS, S])
            ff.stdin.write(pg.screenshot(type="jpeg", quality=90))
        b.close()
    ff.stdin.close(); ff.wait(); print("fertig", aus, n)


if __name__ == "__main__":
    main(*sys.argv[1:4])
