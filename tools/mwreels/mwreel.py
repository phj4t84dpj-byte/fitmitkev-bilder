# Mehrwert-Reels 1080x1920 im warmen Board-Look, animiert und auf die Wort-Zeiten von Kevs Stimme getaktet.
# Aufruf: python3 mwreel.py <Name> <zeiten.json> <bilder-ordner> <aus.mp4>   (Video ohne Ton, 30 fps)
# Die Stimme beginnt bei VOR Sekunden; das Mischen mit Stimme und Musik macht mischen.py (HF-Job).
import os, sys, json, re, random, subprocess
from playwright.sync_api import sync_playwright

D = os.path.dirname(os.path.abspath(__file__)); S = os.path.dirname(D)
FO = f"{S}/fonts"; VN = f"{S}/render/vorher_nachher.jpg"
NAVY, BLUE, DARK, RED, GREEN, GREY, BADGE = "#12213f", "#163b7d", "#0d1d42", "#c1202b", "#2e7d32", "#7a6f64", "#c61f27"
VOR, NACH, FPS = 0.5, 1.6, 30

# Inhalt je Reel. Ereignisse hängen an Wörtern des Sprechertexts: ("wort", n) = n-tes Vorkommen (ab 1).
SPEC = {
 "Unsichtbar": dict(
  text="Du isst kaum was – und trotzdem tut sich nichts? Dann schau mal auf die unsichtbaren Kalorien. Ein Esslöffel Öl in der Pfanne: 90. Ein Glas Orangensaft: 90. Drei Tassen Kaffee mit Zucker: 100. Eine Handvoll Nüsse: 200. Zusammen fast 500 Kalorien – und richtig satt macht davon nichts. Welche erwischt dich am häufigsten?",
  hook="Kaum gegessen?", titel=["DIE UNSICHTBAREN", "KALORIEN"], titel_bei=("Dann", 1),
  intro="Du isst kaum was –<br>und trotzdem<br><b>tut sich nichts?</b>",
  karten=[dict(bild="oel", name="1 EL Öl in der Pfanne", wert="90 kcal", bei=("Esslöffel", 1), wert_bei=("90", 1), farbe=RED),
          dict(bild="saft", name="1 Glas Orangensaft", wert="90 kcal", bei=("Glas", 1), wert_bei=("90", 2), farbe=RED),
          dict(bild="kaffee", name="3 Kaffee mit je 2 TL Zucker", wert="100 kcal", bei=("Drei", 1), wert_bei=("100", 1), farbe=RED),
          dict(bild="nuesse", name="1 Handvoll Nüsse", wert="200 kcal", bei=("Handvoll", 1), wert_bei=("200", 1), farbe=RED)],
  banner=("Zusammen fast <b>500 kcal</b> – und kaum satt", RED, ("Zusammen", 1)),
  frage=("Welche erwischt dich am häufigsten?", ("Welche", 1))),
 "Obst": dict(
  text="Obst hat zu viel Zucker? Ein Apfel hat rund 80 Kalorien und macht dich durch die Ballaststoffe satt. Ein Schokoriegel hat über 250 – und eine halbe Stunde später hast du wieder Hunger. Zwei Portionen Obst am Tag sind völlig in Ordnung. Nur Saft und Smoothies sind keine Sattmacher. Was ist dein Lieblingsobst?",
  hook="Stimmt das?", titel=["OBST HAT ZU", "VIEL ZUCKER?"], titel_bei=("Obst", 1),
  karten=[dict(bild="apfel", name="1 Apfel · macht satt", wert="80 kcal", bei=("Apfel", 1), wert_bei=("80", 1), farbe=GREEN),
          dict(bild="riegel", name="1 Schokoriegel · bald Hunger", wert="250 kcal", bei=("Schokoriegel", 1), wert_bei=("250", 1), farbe=RED),
          dict(bild="obstschale", name="2 Portionen Obst am Tag", wert="✓ völlig okay", bei=("Zwei", 1), wert_bei=("Ordnung", 1), farbe=GREEN),
          dict(bild="smoothie", name="Saft und Smoothies", wert="✗ kein Sattmacher", bei=("Saft", 1), wert_bei=("Sattmacher", 1), farbe=RED)],
  banner=("Obst ist <b>kein Problem</b> – Süßigkeiten schon", GREEN, ("Saft", 1)),
  frage=("Was ist dein Lieblingsobst?", ("Was", 1))),
 "Eiweiss50": dict(
  text="Ab 50 baut dein Körper jedes Jahr ein Stück Muskeln ab. Dagegen helfen Bewegung – und genug Eiweiß. Viele frühstücken ein Brötchen mit Marmelade: 5 Gramm Eiweiß. Eine Schale Skyr mit Beeren und Haferflocken: über 20 Gramm. Gleich viel Aufwand, 4× so viel Eiweiß – und du bist bis mittags satt. Was gibt es bei dir zum Frühstück?",
  hook="Ab 50 wichtig:", titel=["EIWEISS AM", "MORGEN"], titel_bei=("Ab", 1),
  intro="Ab 50 baut der Körper<br><b>jedes Jahr Muskeln ab.</b><br>Was hilft?",
  chips=[("💪 Bewegung", ("Bewegung", 1)), ("🥚 genug Eiweiß", ("genug", 1))],
  karten=[dict(bild="broetchen", name="Brötchen mit Marmelade", wert="5 g Eiweiß", bei=("Brötchen", 1), wert_bei=("5", 1), farbe=GREY),
          dict(bild="skyr", name="Skyr mit Beeren und Haferflocken", wert="20+ g Eiweiß", bei=("Skyr", 1), wert_bei=("20", 1), farbe=GREEN)],
  banner=("<b>4× so viel Eiweiß</b> – satt bis mittags", GREEN, ("Gleich", 1)),
  frage=("Was gibt es bei dir zum Frühstück?", ("Was", 1))),
}


def norm(w):
    return re.sub(r"[^0-9a-zäöüß×]", "", w.lower())


def stuecke(toks, strich=()):
    out, cur = [], []
    for i, t in enumerate(toks):
        cur.append(i)
        n = len(" ".join(toks[j] for j in cur))
        nxt = len(toks[i + 1]) if i + 1 < len(toks) else 0
        if re.search(r"[.,!?:]$", t) or i in strich or len(cur) >= 3 or n + 1 + nxt > 18:
            out.append(cur); cur = []
    if cur: out.append(cur)
    return out


def html(sp, toks, bild_dir):
    random.seed(7)
    bok = ''.join(f'<div class="b" style="left:{random.randint(-60,1080)}px;top:{random.randint(-60,1900)}px;width:{(s:=random.randint(40,150))}px;height:{s}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,10)}px)"></div>' for _ in range(60))
    L = '<br>'.join(sp["titel"])
    n = len(sp["karten"]); chips = sp.get("chips", [])
    karten = ""
    # Raster: 4 Karten = 2x2; 2 Karten (+Chips) = Chips oben, Karten groß nebeneinander
    for k, c in enumerate(sp["karten"]):
        if n == 4: x, y, w, h, im = 60 + (k % 2) * 490, 560 + (k // 2) * 450, 470, 430, 290
        else: x, y, w, h, im = 60 + k * 490, 710, 470, 600, 450
        karten += (f'<div class="c" id="k{k}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
                   f'<img src="{bild_dir}/{c["bild"]}.jpg" style="height:{im}px"><div class="nm">{c["name"]}</div>'
                   f'<div class="wt" id="w{k}" style="color:{c["farbe"]}">{c["wert"]}</div></div>')
    for k, (t, _) in enumerate(chips):
        karten += f'<div class="chip" id="c{k}" style="left:{60 + k * 490}px;top:560px">{t}</div>'
    if sp.get("intro"):
        y0 = 710 if chips else 560
        karten += f'<div id="intro" style="top:{y0}px;height:{1310 - y0 if chips else 880}px"><div>{sp["intro"]}</div></div>'
    bt, bc, _ = sp["banner"]
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
.top{{position:absolute;left:0;top:200px;width:1080px;text-align:center}}
.hookw{{display:inline-block;position:relative;transform:rotate(-4deg)}}
.hook,.hookb{{font-family:K;font-size:74px;line-height:1.15;white-space:nowrap}}
.hook{{color:#fff;position:relative;z-index:2}}
.hookb{{position:absolute;left:0;top:0;color:{NAVY};-webkit-text-stroke:11px {NAVY};text-shadow:3px 5px 0 {NAVY};z-index:1}}
.tw{{position:relative;font-family:A;font-size:112px;line-height:1.04;letter-spacing:1px;margin-top:6px}}
.t-fi{{position:relative;color:#fff;z-index:3}}
.t-ol{{position:absolute;left:0;top:0;width:100%;color:{BLUE};-webkit-text-stroke:13px {BLUE};z-index:2}}
.t-sh{{position:absolute;left:7px;top:8px;width:100%;color:{DARK};-webkit-text-stroke:13px {DARK};z-index:1}}
.c{{position:absolute;background:rgba(255,255,255,.95);border-radius:26px;padding:12px;box-sizing:border-box;text-align:center;box-shadow:0 10px 26px rgba(60,40,20,.25);opacity:0}}
.c img{{width:100%;object-fit:cover;border-radius:18px;display:block}}
.nm{{font-size:30px;font-weight:600;color:{NAVY};line-height:1.15;margin-top:10px;height:62px;display:flex;align-items:center;justify-content:center}}
.wt{{font-family:A;font-size:50px;line-height:1.1;opacity:0}}
.chip{{position:absolute;width:470px;height:120px;border-radius:24px;background:{NAVY};color:#fff;font-size:42px;font-weight:700;display:flex;align-items:center;justify-content:center;opacity:0}}
#intro{{position:absolute;left:60px;width:960px;border-radius:30px;background:rgba(255,255,255,.93);box-shadow:0 10px 26px rgba(60,40,20,.25);display:flex;align-items:center;justify-content:center;text-align:center;font-size:70px;font-weight:700;line-height:1.25;color:{NAVY};opacity:0}}
#intro b{{color:{RED}}}
#ban{{position:absolute;left:60px;top:1465px;width:960px;min-height:110px;border-radius:24px;background:{bc};color:#fff;font-size:42px;font-weight:600;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px 24px;box-sizing:border-box;opacity:0}}
#ban b{{color:#ffe27a;font-weight:700}}
#fr{{position:absolute;left:60px;top:1465px;width:960px;min-height:110px;border-radius:24px;background:#fff6e0;border:4px solid #e9a23b;color:{NAVY};font-size:42px;font-weight:700;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px 24px;box-sizing:border-box;opacity:0}}
#cap{{position:absolute;left:0;top:1600px;width:1080px;text-align:center;font-family:P;font-weight:700;font-size:60px;color:#fff;-webkit-text-stroke:0;text-shadow:0 0 1px #000,3px 3px 0 #000,-3px 3px 0 #000,3px -3px 0 #000,-3px -3px 0 #000,0 4px 0 #000,0 -4px 0 #000,4px 0 0 #000,-4px 0 0 #000}}
#cap i{{font-style:normal;color:#ffd400}}
</style></head><body><div id="bk">{bok}</div>
<div class="brand"><img class="ph" src="{VN}"><div class="badge">-50 kg</div><div class="ig">@fitmitkev</div></div>
<div class="top" id="top"><div class="hookw"><div class="hookb">{sp['hook']}</div><div class="hook">{sp['hook']}</div></div>
<div class="tw"><div class="t-sh">{L}</div><div class="t-ol">{L}</div><div class="t-fi">{L}</div></div></div>
{karten}<div id="ban"><span>{bt}</span></div><div id="fr"><span>💬 {sp['frage'][0]}</span></div><div id="cap"></div>
<script>
function e(x){{x=Math.max(0,Math.min(1,x));return 1-Math.pow(1-x,3)}}
function pop(el,t,t0,d){{const p=e((t-t0)/(d||.35));el.style.opacity=p;el.style.transform='scale('+(0.82+0.18*p)+')';}}
window.render=function(t,S){{
 document.getElementById('bk').style.transform='scale('+(1+t*0.004)+')';
 const top=document.getElementById('top'); const p=e((t-S.titel)/.4); top.style.opacity=Math.max(.0,p); top.style.transform='translateY('+(30*(1-p))+'px)';
 S.karten.forEach((k,i)=>{{const el=document.getElementById('k'+i); pop(el,t,k[0]);
   const w=document.getElementById('w'+i); const q=e((t-k[1])/.3); w.style.opacity=q; w.style.transform='scale('+(1.4-0.4*q)+')';}});
 S.chips.forEach((c,i)=>pop(document.getElementById('c'+i),t,c));
 const it=document.getElementById('intro'); if(it){{ if(t<S.intro_ende) pop(it,t,0.1); else it.style.opacity=Math.max(0,1-(t-S.intro_ende)/.3); }}
 const fr=S.frage, ban=document.getElementById('ban');
 if(t<fr){{pop(ban,t,S.banner);}} else {{ban.style.opacity=Math.max(0,1-(t-fr)/.25);}}
 pop(document.getElementById('fr'),t,fr);
 let cap=''; for(const c of S.cap){{ if(t>=c[0]&&t<c[1]) cap=c[2]; }} document.getElementById('cap').innerHTML=cap;
}};
</script></body></html>"""


def main(name, zpath, bild_dir, aus):
    sp = SPEC[name]
    z = json.load(open(zpath)); W = z["woerter"]
    toks = [t for t in sp["text"].split() if norm(t)]
    assert len(toks) == len(W), (len(toks), len(W))
    st = [VOR + w["s"] for w in W]
    def zeit(key):
        wort, n = key; k = 0
        for i, t in enumerate(toks):
            if norm(t) == norm(wort):
                k += 1
                if k == n: return st[i] - 0.05
        raise KeyError(key)
    dauer = VOR + z["dauer"] + NACH
    S = {"titel": 0.0,
         "karten": [[zeit(c["bei"]), zeit(c["wert_bei"])] for c in sp["karten"]],
         "chips": [zeit(b) for _, b in sp.get("chips", [])],
         "intro_ende": zeit(sp["karten"][0]["bei"]) - 0.35,
         "banner": zeit(sp["banner"][2]), "frage": zeit(sp["frage"][1]), "cap": []}
    strich, k = set(), -1
    for t in sp["text"].split():
        if norm(t): k += 1
        else: strich.add(k)
    teile = stuecke(toks, strich)
    for k, idx in enumerate(teile):
        a = st[idx[0]] - 0.05
        b = st[teile[k + 1][0]] - 0.05 if k + 1 < len(teile) else VOR + W[-1]["e"] + 0.5
        txt = " ".join(f"<i>{toks[i]}</i>" if re.search(r"\d", toks[i]) else toks[i] for i in idx)
        S["cap"].append([a, b, txt])
    print(name, "Dauer", round(dauer, 2), "Karten", S["karten"], flush=True)
    hp = f"/tmp/claude-0/mwreel_{name}.html"; open(hp, "w").write(html(sp, toks, bild_dir))
    n = int(dauer * FPS)
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", aus],
                          stdin=subprocess.PIPE)
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        pg.goto("file://" + hp); pg.wait_for_timeout(600)
        for f in range(n):
            pg.evaluate("([t,S])=>render(t,S)", [f / FPS, S])
            ff.stdin.write(pg.screenshot(type="jpeg", quality=90))
        b.close()
    ff.stdin.close(); ff.wait()
    print("fertig", aus, n, "Bilder")


if __name__ == "__main__":
    main(*sys.argv[1:5])
