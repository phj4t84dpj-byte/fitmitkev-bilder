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
    return f'<div class="vsw">{col(d["l"],"l")}<div class="vsmid">{d.get("mid","VS")}</div>{col(d["r"],"r")}</div>'
def card_rows(d):
    out=''
    for r in d:
        ic=f'<img src="{img(r[0])}">' if r[0].endswith(('.png','.jpg')) else f'<span>{r[0]}</span>'
        out+=f'<div class="rw"><div class="ri">{ic}</div><div class="rt"><div class="r1">{H.escape(r[1])}</div><div class="r2">{H.escape(r[2])}</div></div><div class="rv">{r[3]}</div></div>'
    return out
def card_prod(d):
    pic=lambda x: f'<img src="{img(x)}">' if x.endswith(('.png','.jpg')) else f'<div class="pe">{x}</div>'
    return '<div class="pw">'+''.join(f'<div class="pc">{pic(p[0])}<div class="p1">{H.escape(p[1])}</div><div class="p2">{p[2]}</div></div>' for p in d)+'</div>'
def card_foto(d):
    return f'<img class="fo" src="{img(d["img"])}"><div class="foc">{H.escape(d["cap"])}</div>'+card_rows(d['rows'])
def card_sorten(d):
    return ''.join(f'<div class="sr"><img class="sp" src="{img("bars/"+k+"-pack.jpg")}"><img class="sf" src="{img("bars/"+k+"-food.jpg")}"><div class="st"><div class="sn">{H.escape(n)}</div><div class="sd">{H.escape(t)}</div></div></div>' for k,n,t in d)
CARD={'vs':card_vs,'rows':card_rows,'prod':card_prod,'foto':card_foto,'sorten':card_sorten}
SORTEN_CSS='.card{padding:8px 20px}.sr{display:flex;align-items:center;gap:14px;height:71px;border-bottom:1.5px solid #eee4d6}.sr:last-child{border-bottom:none}.sp{height:62px;border-radius:8px;flex:none}.sf{height:62px;width:76px;object-fit:cover;border-radius:10px;flex:none}.sn{font-size:19px;font-weight:700;letter-spacing:1.5px;color:#c1202b;text-transform:uppercase;line-height:1.2}.sd{font-size:30px;font-weight:700;color:#12213f;line-height:1.15;white-space:nowrap}.lab{font-size:34px}.msg{font-size:27px;line-height:1.3}'
SORTEN_MSG='Code FITMITKEV: <span>Black-Week-Rabatte sichern.</span><br>Link im 1. Kommentar 👇'
SPEC={
 # K1/K2 (Kev 19.11., 17:45): Ankündigung Sa 21.11. und Start So 22.11. auch im Info-Design, nur ein Bild je Beitrag.
 'K1':dict(out='ESN-K1-Ankuendigung', hook='Oft gefragt:', title=['DAS NEHME','ICH SELBST'], size=92,
   secs=[dict(lab='MEINE TOP 5', col=BLUE, type='rows', d=[
      ('kev/sq-Kev-Flexpresso-3-Sorten.jpg','Flexpresso','mein Protein-Kaffee am Morgen','-25 %'),
      ('kev/sq-Kev-Riegel-angeschnitten.jpg','Designer Bar','wenn die Lust auf Süßes kommt, ohne Zuckerzusatz','-30 %'),
      ('kev/sq-Kev-ExtraCreamy-VanillaMilk.jpg','Extra Creamy Protein','für Mousse, Pudding und Oats','-30 %'),
      ('kev/sq-Kev-Isoclear-3-Glaeser-vorn.jpg','Isoclear','Protein-Eistee mit Geschmack','-25 %'),
      ('kev/sq-Kev-FlavorPowder-oben.jpg','Designer Flavor Powder','zum Süßen von Skyr und Quark','-40 %')])],
   mid='Morgen um 12 Uhr startet die ESN Black Week<br><span>mit bis zu -70 %. Nur 1x im Jahr.</span>',
   msg='Code FITMITKEV: <span>Black-Week-Rabatte sichern.</span><br>Link im 1. Kommentar 👇',
   css='.ri{width:104px;height:104px;overflow:hidden}.ri img{max-width:104px;max-height:104px;border-radius:14px}.rw{padding:9px 0}.msg{font-size:27px;line-height:1.3}'),
 # K3 (Kev auf der Prüfseite, 19.11., 20:04): Black-Friday-Abend „lieber ein Top-5-Bild als Infografik mit meinen Top 5 Produkten“ statt des Riegel-Fotos.
 'K3':dict(out='ESN-K3-Black-Friday-Top5', hook='Black Friday:', title=['MEINE TOP 5','PRODUKTE'], size=98,
   secs=[dict(lab='DAS NEHME ICH SELBST', col=RED, type='rows', d=[
      ('kev/sq-Kev-Flexpresso-3-Sorten.jpg','1. Flexpresso','mein Protein-Kaffee am Morgen','-25 %'),
      ('kev/sq-Kev-Riegel-angeschnitten.jpg','2. Designer Bar','wenn die Lust auf Süßes kommt','-30 %'),
      ('kev/sq-Kev-ExtraCreamy-VanillaMilk.jpg','3. Extra Creamy Protein','für Mousse, Pudding und Oats','-30 %'),
      ('kev/sq-Kev-Isoclear-3-Glaeser-vorn.jpg','4. Isoclear','mein Protein-Eistee','-25 %'),
      ('kev/sq-Kev-FlavorPowder-oben.jpg','5. Designer Flavor Powder','zum Süßen von Skyr und Quark','-40 %')])],
   mid='Die ESN Black Week läuft noch bis Mittwoch, 17:30 Uhr.<br><span>Mit bis zu -70 %. Nur 1x im Jahr.</span>',
   msg='Code FITMITKEV: <span>Black-Week-Rabatte sichern.</span><br>Link im 1. Kommentar 👇',
   css='.ri{width:104px;height:104px;overflow:hidden}.ri img{max-width:104px;max-height:104px;border-radius:14px}.rw{padding:9px 0}.msg{font-size:27px;line-height:1.3}'),
 'K2':dict(out='ESN-K2-Start', hook='Es ist so weit:', title=['HEUTE UM 12 UHR:','ESN BLACK WEEK'], size=84,
   secs=[dict(lab='DAS ERWARTET DICH', col=RED, type='rows', d=[
      ('🔥','Bis zu -70 %','mit den Daily Deals, jeden Tag neu ab 8 Uhr','-70 %'),
      ('extra-creamy-480g-vanilla-speculoos.png','3 neue Sorten Extra Creamy Protein','Vanilla Speculoos, Cinnamon Cereal, Strawberry Cream','neu'),
      ('kev/sq-Kev-ExtraCreamy-3-Dosen.jpg','Black Edition','Extra Creamy Protein Ultra Dark Chocolate','neu'),
      ('designer-bar-mint.png','Designer Bar Dark Chocolate Mint','die neue Riegel-Sorte','neu'),
      ('⏰','Läuft bis Mittwoch, 2.12.','Ende um 17:30 Uhr','2.12.')])],
   mid='Um 11 Uhr zeige ich dir hier meinen Einkaufszettel.<br><span>Die ESN Black Week gibt es nur 1x im Jahr.</span>',
   msg='Code FITMITKEV: <span>Black-Week-Rabatte sichern.</span><br>Link im 1. Kommentar 👇',
   css='.ri{width:104px;height:104px;overflow:hidden;font-size:50px}.ri img{max-width:104px;max-height:104px;border-radius:14px}.rw{padding:9px 0}.msg{font-size:27px;line-height:1.3}'),
 'P0':dict(out='ESN-P0-Jetzt-gehts-los', hook='ESN Black Week:', title=["JETZT GEHT'S LOS"], size=106,
   secs=[dict(lab='DIE RABATTE IM ÜBERBLICK', col=RED, type='rows', d=[
      ('%','Daily Deals','bis zu -70 %, jeden Tag neu ab 8 Uhr','-70 %'),
      ('extra-creamy-30g-vanilla-milk.png','Proben und Collagen','30-g-Proben, Collagen Peptides','-50 %'),
      ('kev/sq-Kev-FlavorPowder-oben.jpg','Flavor Powder und Porridge','Designer Flavor Powder, Protein Porridge, Kreatin','-40 %'),
      ('designer-bar-mint-box.png','Riegel und Extra Creamy Protein','Designer Bar, Oatbar, GOAT Bar, Pancake-Mix, Rice Pudding','-30 %'),
      ('kev/sq-Kev-Flexpresso-3-Sorten.jpg','Flexpresso, Isoclear, Whey','Designer Whey, Iso Whey, Cold Brew, Matcha','-25 %'),
      ('shaker-black.png','Shaker und Zubehör','alles, was kein Lebensmittel ist','-20 %')])],
   mid='Läuft bis Mittwoch, 2.12., 17:30 Uhr.<br><span>Die ESN Black Week gibt es nur 1x im Jahr.</span>',
   msg='Code FITMITKEV: <span>Black-Week-Rabatte sichern.</span><br>Link im 1. Kommentar 👇',
   css='.ri{width:84px;height:84px;font-size:44px;overflow:hidden}.ri img{max-width:84px;max-height:84px;border-radius:12px}.ri img[src$=".png"]{max-width:74px;max-height:74px;border-radius:0}.rw:first-child .ri{background:#c1202b;color:#fff;font-family:A;font-size:54px}.rw{padding:8px 0;gap:18px}.r1{font-size:32px}.r2{font-size:23px}.msg{font-size:27px;line-height:1.3}'),
 'P1':dict(out='ESN-P1-Einkaufszettel', hook="Gleich geht's los:", title=['MEIN EINKAUFSZETTEL','FÜR DIE BLACK WEEK'], size=76,
   secs=[dict(lab='DAS KOMMT BEI MIR IN DEN WARENKORB', col=RED, type='rows', d=[
      ('kev/sq-Kev-Flexpresso-3-Sorten.jpg','Flexpresso für morgens','White & Dark Chocolate Mocha, Chocolate','-25 %'),
      ('kev/sq-Kev-ExtraCreamy-3-Dosen.jpg','Extra Creamy Protein für meine Rezepte','Vanilla Milk, Cinnamon Cereal, neue Black Edition','-30 %'),
      ('kev/sq-Kev-Riegel-angeschnitten.jpg','Designer Bar als 12er Box','quer durch die Sorten, neu: Dark Chocolate Mint','-30 %'),
      ('kev/sq-Kev-Isoclear-3-Glaeser-vorn.jpg','Isoclear = Protein-Eistee mit Geschmack','Peach Iced Tea, Green Apple, Fresh Cherry','-25 %'),
      ('kev/sq-Kev-FlavorPowder-oben.jpg','Designer Flavor Powder','zum Süßen von Skyr und Quark','-40 %')])],
   mid='Start heute um 12 Uhr, dazu Daily Deals mit bis zu -70 %.<br><span>Läuft bis Mittwoch, 2.12., 17:30 Uhr.</span>',
   msg='Code FITMITKEV: <span>Black-Week-Rabatte sichern.</span><br>Link im 1. Kommentar 👇',
   css='.ri{width:104px;height:104px;overflow:hidden}.ri img{max-width:104px;max-height:104px;border-radius:14px}.rw{padding:9px 0}.msg{font-size:27px;line-height:1.3}'),
 'P2':dict(out='ESN-P2-Morgen', hook='Mein Morgen:', title=['ZWEI MINUTEN','STATT BÄCKER'], size=84,
   secs=[dict(lab='DAS FRÜHSTÜCK UNTERWEGS GEGEN MEINS', col=BLUE, type='vs', d=dict(
      l=dict(title='Coffee to go + Croissant', rows=[('','Latte Macchiato groß','ca. 220 kcal'),('','Butter-Croissant','ca. 230 kcal')], sum='ca. 450 kcal · 10 g Eiweiß'),
      r=dict(title='Mein Protein-Kaffee', img='shop/flexpresso.png', rows=[('','30 g Flexpresso','ca. 110 kcal'),('','250 ml Mandelmilch (ungesüßt)','ca. 35 kcal')], sum='ca. 145 kcal · 24 g Eiweiß'))),
   ],
   mid='Ein Drittel der Kalorien, mehr als doppelt so viel Eiweiß.<br><span>Ich trinke jeden Morgen eine doppelte Portion.</span>',
   msg='Code FITMITKEV: <span>Black-Week-Rabatte sichern.</span><br>Link im 1. Kommentar 👇',
   css='.msg{font-size:27px;line-height:1.3}.vimg{height:170px}'),
 'P3':dict(out='ESN-P3-Riegel', hook='Süßes ohne Zuckerfalle:', title=['SCHOKORIEGEL','ODER PROTEINRIEGEL?'], size=78,
   secs=[dict(lab='SO SIEHT DER VERGLEICH AUS', col=RED, type='vs', d=dict(
      l=dict(title='Schokoriegel (50 g)', rows=[('','Kalorien','ca. 240 kcal'),('','Zucker','ca. 25 g'),('','Eiweiß','ca. 3 g')], sum='8 Stück Würfelzucker'),
      r=dict(title='Designer Bar (45 g)', img='designer-bar-mint.png', rows=[('','Kalorien','unter 200 kcal'),('','Zucker','max. 2 g'),('','Eiweiß','ca. 14 g')], sum='weich, mit Füllung'))),
   ],
   mid='Werte je nach Sorte leicht unterschiedlich.<br><span>Mein Snack, wenn nachmittags die Lust auf Süßes kommt.</span>',
   msg='Süß darf sein.<br><span>Ohne die Zuckerbombe.</span>'),
 'P4':dict(out='ESN-P4-NeueSorten', hook='Neu bei ESN:', title=['3 NEUE SORTEN,','3 REZEPTE'], size=86,
   secs=[dict(lab='EXTRA CREAMY PROTEIN: DAS MACHE ICH DARAUS', col=GREEN, type='rows', d=[
      ('extra-creamy-480g-vanilla-speculoos.png','Vanilla Speculoos','Spekulatius-Mousse in 5 Minuten','295<br><small>kcal</small>'),
      ('extra-creamy-480g-cinnamon-cereal.png','Cinnamon Cereal','Zimtschnecken-Overnight-Oats','430<br><small>kcal</small>'),
      ('extra-creamy-480g-strawberry-cream.png','Strawberry Cream','Erdbeer-Quark-Bowl nur für dich','335<br><small>kcal</small>')])],
   mid='Alle drei Rezepte findest du hier auf der Seite.<br><span>Ohne Backen, jeweils mit über 30 g Eiweiß.</span>',
   msg='Neue Sorten heißt bei mir:<br><span>neue Rezepte.</span>'),
 # P5 „So weit reicht eine Dose“: am 19.11. von Kev gestrichen.
 'P6':dict(out='ESN-P6-Top3', hook='Black Friday:', title=['MEINE TOP 3','FÜR DEN VORRAT'], size=86,
   secs=[dict(lab='DAS KOMMT BEI MIR IN DEN WARENKORB', col=RED, type='prod', d=[
      ('extra-creamy-480g-cinnamon-cereal.png','Designer Protein Extra Creamy','für Rezepte<br><b>-30 %</b>'),
      ('designer-bar-mint-box.png','Designer Bar 12er Box','als Snack<br><b>-30 %</b>'),
      ('kev/sq-Kev-Flexpresso-3-Sorten.jpg','Protein-Kaffee Flexpresso','für morgens<br><b>-25 %</b>')])],
   mid='Tipp: Ab der 2. Bestellung ist der Versand ab 30 € kostenlos.<br><span>Einfach die Codes FITMITKEV und SHIPAGAIN kombinieren.</span>',
   msg='ESN Black Week:<br><span>nur 1x im Jahr.</span>',
   css='.pc img[src*="kev/"]{border-radius:18px;height:270px;margin:15px 0}'),
 'P7':dict(out='ESN-P7-Abendsnacks', hook='Abends Hunger?', title=['4 EIWEISS-SNACKS','UNTER 200 KCAL'], size=80,
   secs=[dict(lab='MEINE SNACKS FÜR DEN ABEND', col=BLUE, type='rows', d=[
      ('shaker-black.png','Shake','30 g Proteinpulver + 300 ml Wasser','115<br><small>kcal</small>'),
      ('extra-creamy-30g-milk-chocolate.png','Schoko-Creme','200 g Skyr + 15 g Proteinpulver Schoko','185<br><small>kcal</small>'),
      ('extra-creamy-black-edition-ultra-dark.png','Schoko-Eis','1 Portion Eis aus Hüttenkäse','195<br><small>kcal</small>'),
      ('shop/designerbar.png','Proteinriegel','1 Riegel (45 g)','190<br><small>kcal</small>')])],
   mid='Alle mit 14 bis 33 g Eiweiß.<br><span>Kalorien im Blick, Genuss inklusive.</span>',
   msg='Snacken ja.<br><span>Aber mit Plan.</span>'),
 'P8':dict(out='ESN-P8-Klumpen', hook='Tipp aus meiner Küche:', title=['PROTEINPULVER','OHNE KLUMPEN'], size=86,
   secs=[dict(lab='SO RÜHRE ICH ES EIN', col=GREEN, type='rows', d=[
      ('1','Erst das Pulver, dann wenig Flüssigkeit','zu einer glatten Paste rühren, dann den Rest dazu','✓'),
      ('2','In Skyr und Quark: Schneebesen','30 Sekunden kräftig, dann wird es cremig wie Mousse','✓'),
      ('3','Pudding und Grießbrei: erst abkühlen lassen','2 Minuten vom Herd, dann einrühren','✓'),
      ('4','Shake: Flüssigkeit zuerst in den Shaker','dann Pulver drauf, 20 Sekunden schütteln','✓')])],
   mid='Kochend heiß flockt Eiweiß aus. Deshalb kommt es bei mir immer zum Schluss rein.',
   msg='Cremig statt klumpig:<br><span>Reihenfolge macht\'s.</span>',
   css='.ri{background:#12213f;color:#fff;font-family:A;font-size:66px}'),
 'P9':dict(out='ESN-P9-Shakes', hook='Shake, aber richtig:', title=['3 SHAKES UNTER','250 KCAL'], size=86,
   secs=[dict(lab='EINFACH IN DEN SHAKER', col=BLUE, type='rows', d=[
      ('extra-creamy-30g-vanilla-speculoos.png','Spekulatius-Shake','30 g Vanilla Speculoos + 250 ml Milch (1,5 %) + Prise Zimt','230<br><small>kcal</small>'),
      ('extra-creamy-30g-strawberry-cream.png','Erdbeer-Shake','30 g Strawberry Cream + 100 g TK-Erdbeeren + 250 ml Wasser (Mixer)','145<br><small>kcal</small>'),
      ('extra-creamy-30g-milk-chocolate.png','Schoko-Banane','30 g Milk Chocolate + ½ Banane + 250 ml Wasser (Mixer)','170<br><small>kcal</small>')])],
   mid='Jeweils mit 24 bis 32 g Eiweiß.<br><span>Eiskalt schmecken sie am besten.</span>',
   msg='Kein Shake muss<br><span>nach Pappe schmecken.</span>'),
 'P10':dict(out='ESN-P10-Fragen', hook='Eure Fragen:', title=['ESN BLACK WEEK','KURZ ERKLÄRT'], size=88,
   secs=[dict(lab='DAS WERDE ICH AM HÄUFIGSTEN GEFRAGT', col=BLUE, type='rows', d=[
      ('?','Wie lange läuft die Black Week?','bis Mittwoch, 2.12., um 17:30 Uhr','2.12.'),
      ('?','Wie viel Rabatt gibt es?','bis zu -70 %, Riegel und Extra Creamy -30 %, Whey und Isoclear -25 %','-70 %'),
      ('?','Welche Sorte für deine Rezepte?','Vanilla Milk passt fast überall, für Desserts die neuen Sorten',f'<img src="{B}/shop/extracreamy-vanilla.png" style="height:104px">'),
      ('?','Und der Versand?','ab der 2. Bestellung ab 30 € kostenlos mit SHIPAGAIN','30 €')])],
   mid='Den Link mit meinem Code findest du im ersten Kommentar.',
   msg='Noch eine Frage?<br><span>Schreib sie mir in die Kommentare.</span>',
   css='.ri{background:#12213f;color:#fff;font-family:A;font-size:70px}'),
 # B1–B3 (Kev 19.11., 20:22): Buch-Beiträge Fr 20.–So 22.11., je 20:15 Uhr, im Info-Design, ein Bild. Ausgabe nach verkaufsseite/.
 # Kalorien: Wohlfühlküche laut Buch (Lasagne 340 von der Buchseite, übrige aus claude/rezept-archiv-und-ebooks.md), Plätzchen aus archiv/rezepte.json (Schlüssel der Buchrezepte).
 'B1':dict(out='Buch-Fr-Welches-Buch', hook='Süß oder herzhaft?', title=['WELCHES BUCH','PASST ZU DIR?'], size=90,
   secs=[dict(lab='MEINE ZWEI REZEPTBÜCHER', col=BLUE, type='vs', d=dict(mid='ODER',
      l=dict(title='Weihnachtsbäckerei', img='../../verkaufsseite/cover-weihnachten.jpg', rows=[('','36 süße Rezepte',''),('','Plätzchen, Stollen, Kuchen',''),('','Quarkbällchen ohne Fritteuse','')], sum='9,99 €'),
      r=dict(title='Wohlfühlküche', img='../../verkaufsseite/cover-wohlfuehlkueche.jpg', rows=[('','36 herzhafte Gerichte',''),('','Lasagne, Gulasch, Aufläufe',''),('','alle unter 500 kcal','')], sum='9,99 €')))],
   mid='Du kannst dich nicht entscheiden?<br><span>Beide zusammen für 14,99 € statt 19,98 €.</span>',
   msg='Sofort als PDF aufs Handy.<br><span>Link im 1. Kommentar 👇</span>',
   css='.vimg{height:318px;border-radius:8px;box-shadow:0 6px 16px rgba(0,0,0,.28)}.vc.l{background:#f7e9ea}.vc.r{background:#f8ecdf}.vc.l .vs{color:#8C1C24}.vc.r .vs{color:#A2462B}.vsmid{font-size:24px;width:86px;height:86px}.vr2{justify-content:center;text-align:center}.vr2 .n{flex:none}.vh{margin-bottom:12px}'),
 'B2':dict(out='Buch-Sa-Plaetzchen', hook='Bald ist 1. Advent:', title=['5 PLÄTZCHEN','UNTER 75 KCAL'], size=96,
   secs=[dict(lab='AUS MEINER WEIHNACHTSBÄCKEREI', col='#8C1C24', type='rows', d=[
      ('../../archiv/fotos/g78_G78Vanillekipferl.jpg','Vanillekipferl','Rezept für 30 Stück','70<br><small>kcal</small>'),
      ('../../archiv/fotos/g27_G27Zimtsterne.jpg','Zimtsterne','Rezept für 30 Stück','50<br><small>kcal</small>'),
      ('../../archiv/fotos/g78_G78SpekPlaetzchen.jpg','Spekulatius','Rezept für 30 Stück','65<br><small>kcal</small>'),
      ('../../archiv/fotos/g79_G79Butterplaetzchen.jpg','Butterplätzchen','zum Ausstechen, Rezept für 40 Stück','50<br><small>kcal</small>'),
      ('../../archiv/fotos/g78_G78Kokosmakronen.jpg','Kokosmakronen','Rezept für 20 Stück','65<br><small>kcal</small>')])],
   mid='Kalorien pro Stück. Alle 5 Rezepte stehen in meinem Buch<br><span>„Weihnachtsbäckerei in leicht“, mit 31 weiteren.</span>',
   msg='Sofort als PDF: 9,99 €.<br><span>Link im 1. Kommentar 👇</span>',
   css='.ri{width:108px;height:108px;overflow:hidden}.ri img{max-width:none;max-height:none;width:108px;height:108px;object-fit:cover}.rw{padding:9px 0}.msg{font-size:27px;line-height:1.3}.mid{font-size:27px}'),
 'B3':dict(out='Buch-So-Wochenplan', hook='Plan für deine Woche:', title=['5 ABENDESSEN','UNTER 500 KCAL'], size=96,
   secs=[dict(lab='AUS MEINER WOHLFÜHLKÜCHE', col='#A2462B', type='rows', d=[
      ('../../verkaufsseite/lasagne.jpg','Montag: Lasagne','mit Skyr-Creme statt Béchamel','340<br><small>kcal</small>'),
      ('../../verkaufsseite/butter-chicken.jpg','Dienstag: Butter Chicken','mit Reis','445<br><small>kcal</small>'),
      ('../../archiv/fotos/g40_G40Koenigsberger.jpg','Mittwoch: Königsberger Klopse','mit Kartoffeln und Roter Bete','420<br><small>kcal</small>'),
      ('../../archiv/fotos/g80_G80CheeseburgerPfanne.jpg','Donnerstag: Cheeseburger-Pfanne','alles aus einer Pfanne','405<br><small>kcal</small>'),
      ('../../verkaufsseite/doener.jpg','Freitag: Döner','im Skyr-Fladenbrot','445<br><small>kcal</small>')])],
   mid='Kalorien pro Portion. Alle 5 Rezepte stehen in meinem Buch<br><span>„Wohlfühlküche in leicht“, mit 31 weiteren.</span>',
   msg='Sofort als PDF: 9,99 €.<br><span>Link im 1. Kommentar 👇</span>',
   css='.ri{width:108px;height:108px;overflow:hidden}.ri img{max-width:none;max-height:none;width:108px;height:108px;object-fit:cover}.rw{padding:9px 0}.msg{font-size:27px;line-height:1.3}.mid{font-size:27px}.r1{font-size:32px}'),
 # B4 (Kev 22.11., 10:20 per Dialog: „Buch-Beitrag täglich weiter“): Mo 23.11., 20:15. Kalorien aus archiv/rezepte.json (Buch-Schlüssel G80SpekKuchenNah, G80Nussecken,
 # G49SpekBiskuitrolle, G78RiesenZimtschnecke, G67EierGugelhupf) – Kev prüft die fünf Werte gegen sein PDF.
 'B4':dict(out='Buch-Mo-Adventskuchen', hook='Für den Adventskaffee:', title=['5 KUCHEN','UNTER 140 KCAL'], size=96,
   secs=[dict(lab='AUS MEINER WEIHNACHTSBÄCKEREI', col='#8C1C24', type='rows', d=[
      ('../../archiv/fotos/g80_G80SpekKuchenNah.jpg','Skyr-Kuchen mit Spekulatius','Rezept für 8 Stücke','125<br><small>kcal</small>'),
      ('../../archiv/fotos/g80_G80Nussecken.jpg','Nussecken','Rezept für 16 Stück','125<br><small>kcal</small>'),
      ('../../archiv/fotos/g49_G49SpekBiskuitrolle.jpg','Spekulatius-Biskuitrolle','Rezept für 12 Stücke','130<br><small>kcal</small>'),
      ('../../archiv/fotos/g78_G78RiesenZimtschnecke.jpg','Zimtschnecken-Kuchen','Rezept für 12 Stücke','135<br><small>kcal</small>'),
      ('../../archiv/fotos/g67_G67EierGugelhupf.jpg','Eierlikör-Gugelhupf','Rezept für 16 Stücke','135<br><small>kcal</small>')])],
   mid='Kalorien pro Stück. Alle 5 Rezepte stehen in meinem Buch<br><span>„Weihnachtsbäckerei in leicht“, mit 31 weiteren.</span>',
   msg='Sofort als PDF: 9,99 €.<br><span>Link im 1. Kommentar 👇</span>',
   css='.ri{width:108px;height:108px;overflow:hidden}.ri img{max-width:none;max-height:none;width:108px;height:108px;object-fit:cover}.rw{padding:9px 0}.msg{font-size:27px;line-height:1.3}.mid{font-size:27px}.r1{font-size:32px}'),
 # B5 (Morgen-Check 23.11.): Di 24.11., 20:15. Kapitel „Lasagne & Aufläufe“ der Wohlfühlküche. Kalorien aus archiv/rezepte.json (G80KartoffelGratin, G54BlumenkohlAuflauf,
 # G77KartoffelHack, G80GnocchiAuflauf, G80HaehnchenNudelauflauf) – Kev prüft die fünf Werte gegen sein PDF. Cordon-Bleu-Auflauf bewusst nicht dabei (läuft am selben Tag um 13:40 als Rezept mit 435 kcal).
 'B5':dict(out='Buch-Di-Auflaeufe', hook='Ofen an, Füße hoch:', title=['5 AUFLÄUFE','UNTER 500 KCAL'], size=96,
   secs=[dict(lab='AUS MEINER WOHLFÜHLKÜCHE', col='#A2462B', type='rows', d=[
      ('../../archiv/fotos/g80_G80KartoffelGratin.jpg','Kartoffelgratin','cremig, mit Käse überbacken','355<br><small>kcal</small>'),
      ('../../archiv/fotos/g54_G54BlumenkohlAuflauf.jpg','Blumenkohl-Auflauf','mit Kartoffeln und Schinken','370<br><small>kcal</small>'),
      ('../../archiv/fotos/g77_G77KartoffelHack.jpg','Kartoffel-Hack-Auflauf','mit Püree-Haube','390<br><small>kcal</small>'),
      ('../../archiv/fotos/g80_G80GnocchiAuflauf.jpg','Gnocchi-Auflauf','mit Hack und Mozzarella','445<br><small>kcal</small>'),
      ('../../archiv/fotos/g80_G80HaehnchenNudelauflauf.jpg','Hähnchen-Nudelauflauf','mit Brokkoli in cremiger Soße','470<br><small>kcal</small>')])],
   mid='Kalorien pro Portion. Alle 5 Rezepte stehen in meinem Buch<br><span>„Wohlfühlküche in leicht“, mit 31 weiteren.</span>',
   msg='Sofort als PDF: 9,99 €.<br><span>Link im 1. Kommentar 👇</span>',
   css='.ri{width:108px;height:108px;overflow:hidden}.ri img{max-width:none;max-height:none;width:108px;height:108px;object-fit:cover}.rw{padding:9px 0}.msg{font-size:27px;line-height:1.3}.mid{font-size:27px}.r1{font-size:32px}'),
 # P12/P13 (Kev 19.11., 18:50): „Wie kann man sich die Designer Bars vorstellen?“ – Sorten und Vergleiche 1:1 aus Kevs zwei Story-Grafiken
 # (Packungs- und Geschmacksbilder daraus ausgeschnitten: esn/bilder/bars/). 22 Sorten in 2 Teilen, je ein Bild.
 # Kev 19.11., 19:00: „lieber schon vor der Black Week, am Samstag“ → Sa 21.11., 9:00 und 18:30, Balken deshalb „Ab morgen 12 Uhr“.
 'P12':dict(out='ESN-P12-Designer-Bar-Sorten-1', hook='Teil 1 von 2:', title=['SO SCHMECKEN DIE','DESIGNER BARS'], size=84,
   secs=[dict(lab='AB MORGEN 12 UHR IN DER BLACK WEEK: 12ER BOX -30 %', col=RED, type='sorten', d=[
      ('maple-walnut','Maple Walnut','Pancakes mit Ahornsirup & Walnuss'),
      ('caramel-latte','Caramel Latte','Karamell-Latte-Macchiato'),
      ('dark-chocolate-mocha','Dark Chocolate Mocha','Mokka mit Zartbitter'),
      ('spekulatius','Spekulatius','Klassischer Spekulatius'),
      ('cookie-dough','Cookie Dough','Roher Keksteig'),
      ('peanut-caramel','Peanut Caramel','Erdnuss-Karamell-Schokoriegel'),
      ('cinnamon-cereal','Cinnamon Cereal','Zimt-Cerealien'),
      ('peanut-butter-pretzel','Peanut Butter Pretzel','Schoko-Brezeln mit Erdnussbutter'),
      ('tropical-vanilla','Tropical Vanilla','Vanilleeis mit Mango & Kokos'),
      ('hazelnut-nougat','Hazelnut Nougat','Haselnuss-Nougat-Praline'),
      ('fudge-brownie','Fudge Brownie','Fudge-Brownie')])],
   mid='', msg=SORTEN_MSG, css=SORTEN_CSS),
 'P13':dict(out='ESN-P13-Designer-Bar-Sorten-2', hook='Teil 2 von 2:', title=['SO SCHMECKEN DIE','DESIGNER BARS'], size=84,
   secs=[dict(lab='AB MORGEN 12 UHR IN DER BLACK WEEK: 12ER BOX -30 %', col=RED, type='sorten', d=[
      ('speculoos','Speculoos','Karamell-Kekse mit Kekscreme'),
      ('strawberry-white-chocolate','Strawberry White Chocolate','Erdbeeren in weißer Schokolade'),
      ('dark-chocolate-raspberry','Dark Chocolate Raspberry','Schoko-Himbeer-Torte'),
      ('white-chocolate-raspberry','White Chocolate Raspberry','Weiße Schoki mit Himbeeren'),
      ('dark-chocolate-salted-almond','Dark Chocolate Salted Almond','Zartbitter mit Mandeln & Meersalz'),
      ('strawberry-yogurt','Strawberry Yogurt','Erdbeer-Joghurt-Schokoriegel'),
      ('dark-cookie-white-choc','Dark Cookie White Choc','Schoko-Doppelkeks in weißer Schokolade'),
      ('almond-coconut','Almond Coconut','Kokos-Mandel-Praline'),
      ('white-chocolate-pistachio','White Chocolate Pistachio','Dubai-Schokolade'),
      ('lebkuchen','Lebkuchen','Schoko-Lebkuchen'),
      ('lemon-cheesecake','Lemon Cheesecake','Zitronen-Käsekuchen')])],
   mid='', msg=SORTEN_MSG, css=SORTEN_CSS),
 # P14: erster Entwurf „Designer Bar von innen“ (19.11.), Kev nicht gezeigt, nicht eingeplant – nur als Reserve.
 'P14':dict(out='ESN-P14-Designer-Bar-innen', hook='So kannst du sie dir vorstellen:', title=['DIE DESIGNER BAR','VON INNEN'], size=88,
   secs=[dict(lab='WIE EIN SCHOKORIEGEL, NUR MIT ANDEREN WERTEN', col=BLUE, type='foto', d=dict(
      img='kev/wide-Kev-Riegel-angeschnitten.jpg', cap='6 von 24 Sorten, frisch angeschnitten in meiner Küche',
      rows=[('kev/sq-Kev-Riegel-Kern.jpg','Außen Schokolade mit Crunch','innen ein weicher Kern mit Füllung','✓'),
            ('2 g','Ohne Zuckerzusatz','höchstens 2 g Zucker je Riegel','✓'),
            ('15 g','Bis zu 15 g Eiweiß','je Riegel (45 g), unter 200 kcal','✓'),
            ('24','24 Sorten','z. B. Spekulatius, Lebkuchen, Dark Chocolate Mint','✓')]))],
   mid='In der Black Week: <span>12er Box mit -30 %.</span>',
   msg='Code FITMITKEV: <span>Black-Week-Rabatte sichern.</span><br>Link im 1. Kommentar 👇',
   css='.fo{width:100%;border-radius:16px;display:block}.foc{font-size:23px;font-weight:600;color:#5a4a3a;text-align:center;margin:8px 0 2px}.ri{width:94px;height:94px;background:#12213f;color:#fff;font-family:A;font-size:44px;overflow:hidden}.ri img{max-width:none;max-height:none;width:94px;height:94px;object-fit:cover}.rw{padding:6px 0}.lab{font-size:33px}.msg{font-size:27px;line-height:1.3}'),
 'P11':dict(out='ESN-P11-Letzter-Tag', hook='Letzte Chance:', title=['HEUTE BIS','17:30 UHR'], size=96,
   secs=[dict(lab='DAS HOLE ICH MIR NOCH · NUR SOLANGE DER VORRAT REICHT', col=RED, type='prod', d=[
      ('extra-creamy-black-edition-ultra-dark.png','Ultra Dark Chocolate','neu, für Schokopudding<br><b>19,53 €</b>'),
      ('extra-creamy-480g-vanilla-speculoos.png','Vanilla Speculoos','neu, für Spekulatius-Desserts<br><b>-30 %</b>'),
      ('designer-bar-mint.png','Designer Bar Mint','neu, als Snack<br><b>-30 %</b>')])],
   mid='Danach gibt es diese Preise erst wieder in einem Jahr.',
   msg='Nur einmal im Jahr.<br><span>Heute ist der letzte Tag.</span>',
   css='.lab{font-size:31px}'),
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
.vr2 .e{{font-size:34px}} .vr2 .e:empty{{display:none}} .vr2 .n{{flex:1}} .vr2 .w{{font-weight:700;color:{NAVY};white-space:nowrap}}
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
.mid{{font-size:29px;font-weight:700;color:{NAVY};line-height:1.3;text-align:center;padding:0 10px}} .mid span{{color:{RED}}} .mid:empty{{display:none}}
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
