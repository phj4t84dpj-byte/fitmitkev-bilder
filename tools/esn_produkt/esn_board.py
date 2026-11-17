# -*- coding: utf-8 -*-
"""Produkt-Beiträge ESN Black Week (12:00, 22.11.–2.12.) im Mehrwert-Look, OHNE Vorher-Nachher-Foto/„-50 kg“ (Regel 12.11.).
Aufbau: Hook (Script) + Titel (Anton), 1–2 Abschnitte (Label + weiße Karte), Satz, Fuß = @fitmitkev + Aussage-Box.
Kartentypen: 'vs' (zwei Spalten: statt … / so …), 'rows' (Zeilen mit Bild/Emoji, Titel, Unterzeile, Wert), 'prod' (2–3 Produktbilder mit Text).
Aufruf: python3 esn_board.py <id> [...]   (ids siehe SPEC)"""
import os, sys, random, html as H
from PIL import Image
from playwright.sync_api import sync_playwright
D=os.path.dirname(os.path.abspath(__file__)); S=os.path.dirname(D)
F=f"{S}/fonts/gf/ofl"; B="/home/claude/fitmitkev-bilder/esn/bilder"
NAVY="#12213f"; BLUE="#163b7d"; DARK="#0d1d42"; RED="#c1202b"; GREEN="#2e7d32"; ORANGE="#c8641e"
def T(lines,size):
    L='<br>'.join(H.escape(l) for l in lines)
    return f'<div class="tw" style="font-size:{size}px"><div class="t-sh">{L}</div><div class="t-ol">{L}</div><div class="t-fi">{L}</div></div>'
def img(n): return f'{B}/{n}'
def card_vs(d):
    def col(c,cls):
        rows=''.join(f'<div class="vr2"><span class="e">{e}</span><span class="n">{H.escape(n)}</span><span class="w">{H.escape(w)}</span></div>' for e,n,w in c['rows'])
        pic=f'<img class="vimg" src="{img(c["img"])}">' if c.get('img') else ''
        return f'<div class="vc {cls}"><div class="vh">{H.escape(c["title"])}</div>{pic}{rows}<div class="vs">{c["sum"]}</div></div>'
    return f'<div class="vsw">{col(d["l"],"l")}<div class="vsmid">VS</div>{col(d["r"],"r")}</div>'
def card_rows(d):
    out=''
    for r in d:
        ic=f'<img src="{img(r[0])}">' if r[0].endswith(('.png','.jpg')) else f'<span>{r[0]}</span>'
        out+=f'<div class="rw"><div class="ri">{ic}</div><div class="rt"><div class="r1">{H.escape(r[1])}</div><div class="r2">{H.escape(r[2])}</div></div><div class="rv">{r[3]}</div></div>'
    return out
def card_prod(d):
    pic=lambda x: f'<img src="{img(x)}">' if x.endswith(('.png','.jpg')) else f'<div class="pe">{x}</div>'
    return '<div class="pw">'+''.join(f'<div class="pc">{pic(p[0])}<div class="p1">{H.escape(p[1])}</div><div class="p2">{p[2]}</div></div>' for p in d)+'</div>'
CARD={'vs':card_vs,'rows':card_rows,'prod':card_prod}
SPEC={
 'P1':dict(out='ESN-P1-Einkaufszettel', hook="Jetzt geht's los:", title=['MEIN EINKAUFSZETTEL','FÜR DIE BLACK WEEK'], size=76,
   secs=[dict(lab='DAS KOMMT BEI MIR IN DEN WARENKORB', col=RED, type='rows', d=[
      ('kev/sq-Kev-Flexpresso-3-Sorten.jpg','Flexpresso für morgens','White & Dark Chocolate Mocha, Chocolate','-25 %'),
      ('kev/sq-Kev-ExtraCreamy-3-Dosen.jpg','Extra Creamy für meine Rezepte','Vanilla Milk, Cinnamon Cereal, neue Black Edition','-30 %'),
      ('kev/sq-Kev-Riegel-angeschnitten.jpg','Designer Bar als 12er Box','quer durch die Sorten, neu: Dark Chocolate Mint','-30 %'),
      ('kev/sq-Kev-Isoclear-3-Glaeser-vorn.jpg','Isoclear nach dem Training','Peach Iced Tea, Green Apple, Fresh Cherry','-25 %'),
      ('kev/sq-Kev-FlavorPowder-oben.jpg','Designer Flavor Powder','zum Süßen von Skyr und Quark','-40 %')])],
   mid='Dazu täglich neue Daily Deals mit bis zu -70 %.<br><span>Läuft bis Mittwoch, 2.12., 17:30 Uhr.</span>',
   msg='Zum Speichern:<br><span>mein Vorrat für den Winter.</span>',
   css='.ri{width:104px;height:104px;overflow:hidden}.ri img{max-width:104px;max-height:104px;border-radius:14px}.rw{padding:9px 0}'),
 'P2':dict(out='ESN-P2-Morgen', hook='Mein Morgen:', title=['ZWEI MINUTEN','STATT BÄCKER'], size=84,
   secs=[dict(lab='DAS FRÜHSTÜCK UNTERWEGS GEGEN MEINS', col=BLUE, type='vs', d=dict(
      l=dict(title='Coffee to go + Croissant', rows=[('☕','Latte Macchiato groß','ca. 220 kcal'),('🥐','Butter-Croissant','ca. 230 kcal')], sum='ca. 450 kcal · 10 g Eiweiß'),
      r=dict(title='Mein Protein-Kaffee', rows=[('☕','30 g Protein-Kaffeepulver','ca. 110 kcal'),('🥛','250 ml Milch (1,5 %)','ca. 120 kcal')], sum='ca. 230 kcal · 30 g Eiweiß'))),
   ],
   mid='Kaffee ist schon drin: Pulver in den Shaker, Milch drauf, schütteln.<br><span>Ich trinke ihn jeden Morgen direkt nach dem Aufstehen.</span>',
   msg='Halb so viele Kalorien,<br><span>dreimal so viel Eiweiß.</span>'),
 'P3':dict(out='ESN-P3-Riegel', hook='Süßes ohne Zuckerfalle:', title=['SCHOKORIEGEL','ODER PROTEINRIEGEL?'], size=78,
   secs=[dict(lab='SO SIEHT DER VERGLEICH AUS', col=RED, type='vs', d=dict(
      l=dict(title='Schokoriegel (50 g)', rows=[('🔥','Kalorien','ca. 240 kcal'),('🍬','Zucker','ca. 25 g'),('💪','Eiweiß','ca. 3 g')], sum='8 Stück Würfelzucker'),
      r=dict(title='Designer Bar (45 g)', img='designer-bar-mint.png', rows=[('🔥','Kalorien','ca. 200 kcal'),('🍬','Zucker','ca. 2 g'),('💪','Eiweiß','ca. 14 g')], sum='weich, mit Füllung'))),
   ],
   mid='Werte je nach Sorte leicht unterschiedlich.<br><span>Mein Snack, wenn nachmittags die Lust auf Süßes kommt.</span>',
   msg='Süß darf sein.<br><span>Ohne die Zuckerbombe.</span>'),
 'P4':dict(out='ESN-P4-NeueSorten', hook='Neu bei ESN:', title=['3 NEUE SORTEN,','3 REZEPTE'], size=86,
   secs=[dict(lab='DAS MACHE ICH DARAUS', col=GREEN, type='rows', d=[
      ('extra-creamy-480g-vanilla-speculoos.png','Vanilla Speculoos','Spekulatius-Mousse in 5 Minuten','295<br><small>kcal</small>'),
      ('extra-creamy-480g-cinnamon-cereal.png','Cinnamon Cereal','Zimtschnecken-Overnight-Oats','430<br><small>kcal</small>'),
      ('extra-creamy-480g-strawberry-cream.png','Strawberry Cream','Erdbeer-Quark-Bowl nur für dich','335<br><small>kcal</small>')])],
   mid='Alle drei Rezepte findest du hier auf der Seite.<br><span>Ohne Backen, jeweils mit über 30 g Eiweiß.</span>',
   msg='Neue Sorten heißt bei mir:<br><span>neue Rezepte.</span>'),
 'P5':dict(out='ESN-P5-Dose', hook='Gerechnet:', title=['SO WEIT REICHT','EINE DOSE'], size=86,
   secs=[dict(lab='480 G DOSE = 16 PORTIONEN À 30 G', col=BLUE, type='rows', d=[
      ('🥣','Morgens','Overnight Oats, Porridge, Skyr-Bowl','×5'),('🍮','Dessert','Mousse, Pudding, Tiramisu im Glas','×6'),('🥤','Unterwegs','Shake mit Milch oder Wasser','×5'),('🛒','ca. 1,22 € pro Portion','ca. 23 g Eiweiß · 480 g für 19,53 € statt 27,90 € (neue Sorten)','-30 %')])],
   mid='Preise laut ESN für die Black Week, bis Mi 2.12., 17:30 Uhr.',
   msg='16 Rezepte<br><span>aus einer Dose.</span>'),
 'P6':dict(out='ESN-P6-Top3', hook='Black Friday:', title=['MEINE TOP 3','FÜR DEN VORRAT'], size=86,
   secs=[dict(lab='DAS KOMMT BEI MIR IN DEN WARENKORB', col=RED, type='prod', d=[
      ('extra-creamy-480g-cinnamon-cereal.png','Designer Protein Extra Creamy','für Rezepte<br><b>-30 %</b>'),
      ('designer-bar-mint-box.png','Designer Bar 12er Box','als Snack<br><b>-30 %</b>'),
      ('☕','Protein-Kaffee Flexpresso','für morgens<br><b>-25 %</b>')])],
   mid='Tipp: Ab der 2. Bestellung in der Black Week ist der Versand ab 30 € kostenlos<br><span>mit dem Code SHIPAGAIN.</span>',
   msg='Einmal im Jahr<br><span>fülle ich den Vorrat auf.</span>'),
 'P7':dict(out='ESN-P7-Abendsnacks', hook='Abends Hunger?', title=['4 EIWEISS-SNACKS','UNTER 200 KCAL'], size=80,
   secs=[dict(lab='MEINE SNACKS FÜR DEN ABEND', col=BLUE, type='rows', d=[
      ('🥤','Shake','30 g Proteinpulver + 300 ml Wasser','115<br><small>kcal</small>'),
      ('🍮','Schoko-Creme','200 g Skyr + 15 g Proteinpulver Schoko','185<br><small>kcal</small>'),
      ('🍨','Schoko-Eis','1 Portion Eis aus Hüttenkäse','195<br><small>kcal</small>'),
      ('🍫','Proteinriegel','1 Riegel (45 g)','200<br><small>kcal</small>')])],
   mid='Alle mit 14 bis 33 g Eiweiß.<br><span>Kalorien im Blick, Genuss inklusive.</span>',
   msg='Snacken ja.<br><span>Aber mit Plan.</span>'),
 'P8':dict(out='ESN-P8-Klumpen', hook='Tipp aus meiner Küche:', title=['PROTEINPULVER','OHNE KLUMPEN'], size=86,
   secs=[dict(lab='SO RÜHRE ICH ES EIN', col=GREEN, type='rows', d=[
      ('1️⃣','Erst das Pulver, dann wenig Flüssigkeit','zu einer glatten Paste rühren, dann den Rest dazu','✓'),
      ('2️⃣','In Skyr und Quark: Schneebesen','30 Sekunden kräftig, dann wird es cremig wie Mousse','✓'),
      ('3️⃣','Pudding und Grießbrei: erst abkühlen lassen','2 Minuten vom Herd, dann einrühren','✓'),
      ('4️⃣','Shake: Flüssigkeit zuerst in den Shaker','dann Pulver drauf, 20 Sekunden schütteln','✓')])],
   mid='Kochend heiß flockt Eiweiß aus. Deshalb kommt es bei mir immer zum Schluss rein.',
   msg='Cremig statt klumpig:<br><span>Reihenfolge macht\'s.</span>'),
 'P9':dict(out='ESN-P9-Shakes', hook='Shake, aber richtig:', title=['3 SHAKES UNTER','250 KCAL'], size=86,
   secs=[dict(lab='EINFACH IN DEN SHAKER', col=BLUE, type='rows', d=[
      ('extra-creamy-30g-vanilla-speculoos.png','Spekulatius-Shake','30 g Vanilla Speculoos + 250 ml Milch (1,5 %) + Prise Zimt','230<br><small>kcal</small>'),
      ('extra-creamy-30g-strawberry-cream.png','Erdbeer-Shake','30 g Strawberry Cream + 100 g TK-Erdbeeren + 250 ml Wasser (Mixer)','145<br><small>kcal</small>'),
      ('extra-creamy-30g-milk-chocolate.png','Schoko-Banane','30 g Milk Chocolate + ½ Banane + 250 ml Wasser (Mixer)','170<br><small>kcal</small>')])],
   mid='Jeweils mit 24 bis 32 g Eiweiß.<br><span>Eiskalt schmecken sie am besten.</span>',
   msg='Kein Shake muss<br><span>nach Pappe schmecken.</span>'),
 'P10':dict(out='ESN-P10-Fragen', hook='Eure Fragen:', title=['BLACK WEEK','KURZ ERKLÄRT'], size=90,
   secs=[dict(lab='DAS WERDE ICH AM HÄUFIGSTEN GEFRAGT', col=BLUE, type='rows', d=[
      ('❓','Wie lange läuft die Black Week?','bis Mittwoch, 2.12., um 17:30 Uhr','2.12.'),
      ('❓','Wie viel Rabatt gibt es?','bis zu -70 %, Riegel und Extra Creamy -30 %, Whey und Isoclear -25 %','-70 %'),
      ('❓','Welche Sorte für deine Rezepte?','Vanilla Milk passt fast überall, für Desserts die neuen Sorten','🥄'),
      ('❓','Und der Versand?','ab der 2. Bestellung ab 30 € kostenlos mit SHIPAGAIN','📦')])],
   mid='Den Link mit meinem Code findest du im ersten Kommentar.',
   msg='Noch eine Frage?<br><span>Schreib sie mir in die Kommentare.</span>'),
 'P11':dict(out='ESN-P11-Letzter-Tag', hook='Letzte Chance:', title=['HEUTE BIS','17:30 UHR'], size=96,
   secs=[dict(lab='DAS HOLE ICH MIR NOCH', col=RED, type='prod', d=[
      ('extra-creamy-black-edition-ultra-dark.png','Ultra Dark Chocolate','neu, für Schokopudding<br><b>19,53 €</b>'),
      ('extra-creamy-480g-vanilla-speculoos.png','Vanilla Speculoos','neu, für Spekulatius-Desserts<br><b>-30 %</b>'),
      ('designer-bar-mint.png','Designer Bar Mint','neu, als Snack<br><b>-30 %</b>')])],
   mid='Danach gibt es diese Preise erst wieder in einem Jahr.',
   msg='Nur einmal im Jahr.<br><span>Heute ist der letzte Tag.</span>'),
}
CSS=f"""@font-face{{font-family:A;src:url('{F}/anton/Anton-Regular.ttf')}}
@font-face{{font-family:K;src:url('{F}/kaushanscript/KaushanScript-Regular.ttf')}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-SemiBold.ttf');font-weight:600}}
body{{margin:0;width:1080px;height:1350px;overflow:hidden;position:relative;font-family:P;background:radial-gradient(ellipse at 70% 30%,#d9c3a5 0%,#c7ab89 45%,#b0926f 100%)}}
.b{{position:absolute;border-radius:50%;background:radial-gradient(circle,#fff3c9 0%,#ffd98a 55%,rgba(255,210,120,0) 72%)}}
.top{{position:absolute;left:0;top:22px;width:1080px;text-align:center}}
.hookw{{display:inline-block;position:relative;transform:rotate(-4deg)}}
.hook,.hookb{{font-family:K;font-size:56px;line-height:1.15;white-space:nowrap}}
.hook{{color:#fff;position:relative;z-index:2}}
.hookb{{position:absolute;left:0;top:0;color:{NAVY};-webkit-text-stroke:9px {NAVY};text-shadow:3px 4px 0 {NAVY};z-index:1}}
.tw{{position:relative;font-family:A;line-height:1.04;letter-spacing:1px;margin-top:12px}}
.t-fi{{position:relative;color:#fff;z-index:3}}
.t-ol{{position:absolute;left:0;top:0;width:100%;color:{BLUE};-webkit-text-stroke:11px {BLUE};z-index:2}}
.t-sh{{position:absolute;left:6px;top:7px;width:100%;color:{DARK};-webkit-text-stroke:11px {DARK};z-index:1}}
.body{{position:absolute;left:40px;width:1000px;display:flex;flex-direction:column;gap:14px}}
.lab{{height:64px;border-radius:16px;color:#fff;font-family:A;font-size:38px;letter-spacing:1px;display:flex;align-items:center;justify-content:center}}
.card{{background:rgba(255,255,255,.95);border-radius:22px;box-shadow:0 8px 22px rgba(60,40,20,.22);box-sizing:border-box;padding:18px 22px}}
.vsw{{display:flex;align-items:stretch;gap:12px}}
.vc{{flex:1;border-radius:16px;padding:14px 16px;display:flex;flex-direction:column}}
.vc.l{{background:#f6e7e4}} .vc.r{{background:#e6f1e6}}
.vh{{font-family:A;font-size:38px;color:{NAVY};text-align:center;margin-bottom:6px;line-height:1.1}}
.vimg{{height:200px;object-fit:contain;margin:0 auto 4px}}
.vr2{{display:flex;align-items:center;gap:10px;font-size:27px;font-weight:600;color:#3d3128;padding:10px 0;border-bottom:1.5px solid rgba(0,0,0,.08)}}
.vr2 .e{{font-size:34px}} .vr2 .n{{flex:1}} .vr2 .w{{font-weight:700;color:{NAVY};white-space:nowrap}}
.vs{{margin-top:auto;padding-top:14px;font-family:A;font-size:36px;text-align:center}}
.vc.l .vs{{color:{RED}}} .vc.r .vs{{color:{GREEN}}}
.vsmid{{align-self:center;font-family:A;font-size:38px;color:#fff;background:{NAVY};border-radius:50%;width:74px;height:74px;display:flex;align-items:center;justify-content:center;flex:none}}
.rw{{display:flex;align-items:center;gap:20px;padding:14px 0;border-bottom:2px solid #eee4d6}} .rw:last-child{{border-bottom:none}}
.ri{{width:124px;height:124px;border-radius:18px;background:#f3ebdf;display:flex;align-items:center;justify-content:center;flex:none;font-size:56px}}
.ri img{{max-width:116px;max-height:116px}}
.rt{{flex:1}} .r1{{font-size:34px;font-weight:700;color:{NAVY};line-height:1.15}} .r2{{font-size:25px;font-weight:600;color:#5a4a3a;line-height:1.25;margin-top:2px}}
.rv{{font-family:A;font-size:46px;color:{GREEN};text-align:center;min-width:110px;line-height:1}} .rv small{{font-size:22px;color:#5a4a3a;font-family:P}}
.pw{{display:flex;gap:14px}}
.pc{{flex:1;background:#f6f0e6;border-radius:16px;padding:12px;text-align:center}}
.pe{{height:300px;display:flex;align-items:center;justify-content:center;font-size:170px}}
.pc img{{height:300px;max-width:100%;object-fit:contain}}
.p1{{font-family:A;font-size:33px;color:{NAVY};line-height:1.1;margin-top:6px}} .p2{{font-size:24px;font-weight:600;color:#5a4a3a;line-height:1.3;margin-top:4px}} .p2 b{{color:{RED};font-family:A;font-size:34px;font-weight:400}}
.mid{{font-size:29px;font-weight:700;color:{NAVY};line-height:1.3;text-align:center;padding:0 10px}} .mid span{{color:{RED}}}
.foot{{position:absolute;left:40px;top:1196px;width:1000px;height:128px;display:flex;align-items:center;gap:22px}}
.ig{{font-family:K;font-size:40px;color:{NAVY};flex:none;padding-left:8px}}
.msg{{flex:1;background:{NAVY};color:#fff;border-radius:22px;height:118px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:31px;font-weight:700;line-height:1.2;padding:0 20px}}
.msg span{{color:#ffd98a}}"""
def build(k):
    s=SPEC[k]; random.seed(hash(k)%1000)
    bok=''.join(f'<div class="b" style="left:{random.randint(-40,1060)}px;top:{random.randint(-40,1300)}px;width:{(z:=random.randint(30,110))}px;height:{z}px;opacity:{random.uniform(.15,.45):.2f};filter:blur({random.randint(2,9)}px)"></div>' for _ in range(40))
    secs=''.join(f'<div class="lab" style="background:{x["col"]}">{H.escape(x["lab"])}</div><div class="card">{CARD[x["type"]](x["d"])}</div>' for x in s['secs'])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{s.get('css','')}</style></head><body>{bok}
<div class="top"><div class="hookw"><div class="hookb">{H.escape(s['hook'])}</div><div class="hook">{H.escape(s['hook'])}</div></div>{T(s['title'],s['size'])}</div>
<div class="body" id="bd">{secs}<div class="mid">{s['mid']}</div></div>
<div class="foot"><div class="ig">@fitmitkev</div><div class="msg"><div>{s['msg']}</div></div></div></body></html>"""
if __name__=='__main__':
    os.makedirs(f'{D}/esn',exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350},device_scale_factor=2)
        for k in (sys.argv[1:] or list(SPEC)):
            h=build(k); open(f'{D}/esn/_b.html','w').write(h); pg.goto(f'file://{D}/esn/_b.html'); pg.wait_for_timeout(500)
            top=pg.evaluate("()=>Math.round(document.querySelector('.top').getBoundingClientRect().bottom)")
            pg.evaluate(f"()=>{{const b=document.getElementById('bd');b.style.top='{top+18}px';}}")
            bot=pg.evaluate("()=>Math.round(document.getElementById('bd').getBoundingClientRect().bottom)")
            free=1180-bot
            if free>0: pg.evaluate(f"()=>{{const b=document.getElementById('bd');b.style.top='{top+18+free//2}px';}}")
            print(k,'Titel unten',top,'Inhalt unten',bot,'(max 1180)', 'OK' if bot<=1180 else 'ZU LANG')
            pg.screenshot(path=f'{D}/esn/_b.png'); Image.open(f'{D}/esn/_b.png').convert('RGB').save(f"{D}/esn/{SPEC[k]['out']}.jpg",quality=92)
        b.close()
