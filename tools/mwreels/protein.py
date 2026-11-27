# Reel „Top 10 Proteinquellen“ als Ranking (1080x1920, 30 fps).
# Von Anfang an steht die Rangliste da, Namen und Bilder verdeckt (Weichzeichner + Fragezeichen). Platz 10 → 1:
# große Karte mit freigestelltem Bild, Name oben, Protein und kcal darunter; dann fliegt sie in ihre Zeile und deckt sie auf.
# Getaktet auf die Wort-Zeiten von Kevs Stimme. Aufruf: python3 protein.py <zeiten.json> <ordner mit cut_<key>.png> <aus.mp4>
import os, sys, json, random, subprocess
from playwright.sync_api import sync_playwright
from protein_daten import ITEMS, text

D = os.path.dirname(os.path.abspath(__file__)); S = os.path.dirname(D)
FO = f"{S}/fonts"; VN = f"{S}/render/vorher_nachher.jpg"
NAVY, BLUE, DARK, RED, GREEN, BADGE = "#12213f", "#163b7d", "#0d1d42", "#c1202b", "#2e7d32", "#c61f27"
MED = {1: "#d4a017", 2: "#9aa3ad", 3: "#b8733a"}
VOR, NACH, FPS = 0.5, 2.6, 30
TOP, RH, GAP = 1000, 54, 6


def T(txt, size, sw=13):
    return (f'<div class="tw" style="font-size:{size}px"><div class="t-sh" style="-webkit-text-stroke:{sw}px {DARK}">{txt}</div>'
            f'<div class="t-ol" style="-webkit-text-stroke:{sw}px {BLUE}">{txt}</div><div class="t-fi">{txt}</div></div>')


def html(bd):
    random.seed(9)
    bok = ''.join(f'<div class="b" style="left:{random.randint(-60,1080)}px;top:{random.randint(-60,1900)}px;width:{(s:=random.randint(40,150))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,10)}px)"></div>' for _ in range(60))
    rows, cards = "", ""
    for i, (k, name, _, p, _, kc, _, zus, pl, _) in enumerate(ITEMS):
        y = TOP + (pl - 1) * (RH + GAP); col = MED.get(pl, NAVY)
        rows += (f'<div class="rw" id="r{i}" style="top:{y}px"><div class="rk" style="background:{col}">{pl}</div>'
                 f'<div class="th"><img class="bl" src="{bd}/cut_{k}.png"><img class="sh" src="{bd}/cut_{k}.png"><span class="q">?</span></div>'
                 f'<div class="rn"><span class="hid">? ? ? ? ?</span><span class="shw">{name}</span></div>'
                 f'<div class="rv"><span class="hid">?? g</span><span class="shw"><b>{p} g</b> · {kc} kcal</span></div></div>')
        cards += (f'<div class="cd" id="k{i}"><div class="pl" style="background:{col if pl <= 3 else RED}">PLATZ {pl}</div>'
                  f'<div class="nm">{T(name.upper(), 92 if len(name) < 12 else 78)}</div>'
                  f'<img class="ct" src="{bd}/cut_{k}.png">'
                  f'<div class="pills"><div class="pi pr" id="p{i}">{p} g Protein</div><div class="pi kc" id="c{i}">{kc} kcal</div></div>'
                  f'<div class="zu">{zus}</div></div>')
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
.head{{position:absolute;left:0;top:180px;width:1080px;text-align:center}}
.hookw{{display:inline-block;position:relative;transform:rotate(-4deg)}}
.hook,.hookb{{font-family:K;font-size:52px;line-height:1.15;white-space:nowrap}}
.hookw{{margin-bottom:8px}}
.hook{{color:#fff;position:relative;z-index:2}}
.hookb{{position:absolute;left:0;top:0;color:{NAVY};-webkit-text-stroke:10px {NAVY};text-shadow:3px 5px 0 {NAVY};z-index:1}}
.tw{{position:relative;font-family:A;line-height:1.04;letter-spacing:1px}}
.t-fi{{position:relative;color:#fff;z-index:3}}
.t-ol{{position:absolute;left:0;top:0;width:100%;color:{BLUE};z-index:2}}
.t-sh{{position:absolute;left:7px;top:8px;width:100%;color:{DARK};z-index:1}}
.rw{{position:absolute;left:60px;width:960px;height:{RH}px;background:rgba(255,255,255,.93);border-radius:14px;display:flex;align-items:center;box-shadow:0 6px 14px rgba(60,40,20,.18);box-sizing:border-box;padding-right:24px}}
.rk{{width:64px;height:{RH}px;border-radius:14px 0 0 14px;color:#fff;font-family:A;font-size:36px;display:flex;align-items:center;justify-content:center;flex:none}}
.th{{position:relative;width:60px;height:50px;margin:0 14px 0 10px;flex:none}}
.th img{{position:absolute;left:0;top:0;width:60px;height:50px;object-fit:contain}}
.th .bl{{filter:blur(9px) brightness(.9)}} .th .sh{{opacity:0;filter:drop-shadow(0 4px 6px rgba(0,0,0,.25))}}
.q{{position:absolute;left:0;top:0;width:60px;height:50px;display:flex;align-items:center;justify-content:center;font-family:A;font-size:40px;color:#fff;-webkit-text-stroke:3px {NAVY}}}
.rn{{flex:1;font-size:32px;font-weight:700;color:{NAVY};position:relative;height:{RH}px}}
.rv{{width:300px;text-align:right;font-family:A;font-size:36px;color:{NAVY};position:relative;height:{RH}px}}
.rv b{{font-weight:400;color:{GREEN}}}
.rn span,.rv span{{position:absolute;left:0;right:0;top:0;line-height:{RH}px}} .rv span{{text-align:right}}
.hid{{color:#9b8f82;letter-spacing:4px}} .shw{{opacity:0}}
#dim{{position:absolute;left:0;top:0;width:1080px;height:1920px;background:rgba(13,29,66,.55);opacity:0}}
.cd{{position:absolute;left:0;top:385px;width:1080px;height:600px;text-align:center;opacity:0}}
.cd .pl{{display:inline-block;font-family:A;font-size:50px;letter-spacing:2px;color:#fff;border-radius:14px;padding:0 22px 2px;margin-top:6px;box-shadow:0 6px 14px rgba(60,40,20,.2)}}
.cd .nm{{height:110px;display:flex;align-items:center;justify-content:center}}
.ct{{width:380px;height:276px;object-fit:contain;filter:drop-shadow(0 18px 20px rgba(60,40,20,.35));margin-top:0}}
.pills{{display:flex;justify-content:center;gap:24px;margin-top:8px}}
.pi{{font-family:A;font-size:58px;color:#fff;border-radius:22px;padding:2px 30px 6px;opacity:0}}
.pr{{background:{GREEN}}} .kc{{background:{NAVY}}}
.zu{{font-size:28px;margin-top:4px;font-weight:600;color:{NAVY}}}
#intro{{position:absolute;left:90px;top:470px;width:900px;height:420px;border-radius:36px;background:rgba(255,255,255,.93);box-shadow:0 10px 26px rgba(60,40,20,.25);display:flex;align-items:center;justify-content:center;text-align:center;font-size:76px;font-weight:700;line-height:1.25;color:{NAVY};opacity:0}}
#intro b{{color:{RED}}}
#fr{{position:absolute;left:60px;top:440px;width:960px;height:120px;border-radius:24px;background:#fff6e0;border:4px solid #e9a23b;color:{NAVY};font-size:46px;font-weight:700;display:flex;align-items:center;justify-content:center;opacity:0}}
</style></head><body><div id="bk">{bok}</div>
<div class="brand"><img class="ph" src="{VN}"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="head"><div class="hookw"><div class="hookb">pro 100 g · bis Platz 1!</div><div class="hook">pro 100 g · bis Platz 1!</div></div><div style="margin-top:16px">{T('TOP 10 PROTEINQUELLEN', 84, 10)}</div></div>
{rows}{cards}<div id="intro"><div>Wer schafft es<br>auf <b>Platz 1?</b> 🤔</div></div><div id="fr"><span>💬 Welche isst du am liebsten?</span></div>
<script>
function e(x){{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}}
function io(x){{x=Math.max(0,Math.min(1,x));return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2}}
window.render=function(t,S){{
 document.getElementById('bk').style.transform='scale('+(1+t*0.003)+')';
 const I=S.items, n=I.length;
 for(let i=0;i<n;i++){{
  const [s,pz,kz,fly,rank]=I[i]; const cd=document.getElementById('k'+i), r=document.getElementById('r'+i);
  const en=(i+1<n?I[i+1][0]:S.outro);
  if(t<s-.05||t>en+.3) cd.style.opacity=0;
  else {{ const pin=e((t-s)/.3), pout=t>en?e((t-en)/.3):0;
   cd.style.opacity=Math.min(pin,1-pout); cd.style.transform='translateX('+(160*(1-pin)-180*pout)+'px) scale('+(0.9+0.1*pin)+')'; }}
  [['p',pz],['c',kz]].forEach(([id,tt])=>{{const q=e((t-tt)/.3); const x=document.getElementById(id+i); x.style.opacity=q; x.style.transform='scale('+(1.35-0.35*q)+')';}});
  const u=e((t-(kz+.35))/.35);
  r.querySelectorAll('.hid').forEach(x=>x.style.opacity=1-u); r.querySelectorAll('.shw').forEach(x=>x.style.opacity=u);
  r.querySelector('.bl').style.opacity=1-u; r.querySelector('.q').style.opacity=1-u; r.querySelector('.sh').style.opacity=u;
  const g=u*(1-e((t-kz-1.0)/.9)); r.style.boxShadow='0 6px 14px rgba(60,40,20,.18), 0 0 0 '+(6*g)+'px #ffd400'; r.style.transform='scale('+(1+0.03*g)+')';
 }}
 const it=document.getElementById('intro'), i0=S.items[0][0]; it.style.opacity=t<i0?e((t-.1)/.35):Math.max(0,1-(t-i0)/.25); it.style.transform='scale('+(0.9+0.1*e((t-.1)/.35))+')';
 const pf=e((t-S.outro)/.35), fr=document.getElementById('fr'); fr.style.opacity=pf; fr.style.transform='scale('+(0.85+0.15*pf)+')';
}};
</script></body></html>"""


def main(zpath, bd, aus):
    z = json.load(open(zpath)); W = z["woerter"]
    sprech, idx, io_ = text()
    toks = [x for x in sprech.split() if x != "–"]
    assert len(toks) == len(W), (len(toks), len(W))
    st = [VOR + w["s"] for w in W]
    items = []
    for j, (a, pz, kz) in enumerate(idx):
        nxt = st[idx[j + 1][0]] if j + 1 < len(idx) else st[io_]
        items.append([st[a] - 0.1, st[pz] - 0.05, st[kz] - 0.05, nxt - 0.65, ITEMS[j][8]])
    S = {"items": items, "outro": st[io_] - 0.1}
    dauer = VOR + z["dauer"] + NACH
    print("Dauer", round(dauer, 2), flush=True)
    hp = "/tmp/claude-0/protein_ranking.html"; open(hp, "w").write(html(bd))
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
