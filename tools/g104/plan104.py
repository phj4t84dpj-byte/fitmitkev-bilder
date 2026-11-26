# -*- coding: utf-8 -*-
# G104 – Freitag 27.11.2026: Tagesplan 14 neue Rezepte + 2 Wiederholer (Zimtsterne, Gewürzkuchen vom 18.11., Board/Text/Kommentar unverändert).
# Fest: 6:10 ESN Bratapfel-Dessert (434673568), 13:00 ESN Schwarzwälder Kirsch (434673693), 15:00 F1 Festtagsküche-Teaser (441366336), 20:15 Buch B8 (tools/promo/buch_posts_ab_2311.json).
import json, os
D=os.path.dirname(os.path.abspath(__file__)); REPO='/home/claude/fitmitkev-bilder'
NEU={p['key']:p for p in json.load(open(f"{D}/out/freitag_neu_posts.json"))}
W={p['key']:p for p in json.load(open(f"{REPO}/tools/g96/mittwoch_posts.json"))}
PLAN=[('06:50','OmelettRoellchen'),('07:35','ToffifeeBowl'),('08:20','ChiliKartoffeln'),('09:00','Zimtsterne'),('09:40','HaehnchenBrokkoliAuflauf'),
      ('10:20','Gewuerzkuchen'),('11:00','Gruenkohl'),('11:40','Butterkuchen'),('12:20','KlossStroganoff'),('13:40','Backfisch'),('14:20','QuarkGugelhupf'),
      ('15:40','SchokokussTorte'),('16:20','Hackbaellchen'),('17:00','Germknoedel'),('17:45','KlossSchweinefilet'),('19:15','KlossMeerrettich')]
FEST={'06:10':('ESN-Rezept Bratapfel-Dessert im Glas, süß (schon eingeplant, Id 434673568)',True),'13:00':('ESN-Rezept Schwarzwälder Kirsch im Glas, süß (schon eingeplant, Id 434673693)',True),
      '15:00':('F1 Teaser „Festtagsküche in leicht“ (schon eingeplant, Id 441366336)',None),'20:15':('Buch-Beitrag B8 „5 Desserts unter 450 kcal“ aus der Weihnachtsbäckerei, mit Hinweis auf Buch Nr. 3',None)}
posts=[]
for n,(zeit,key) in enumerate(PLAN,1):
    if key in NEU: q=NEU[key]; wdh=None
    else: q=W[key]; wdh='18.11. · '+{'Zimtsterne':'160.097 · 16-fach','Gewuerzkuchen':'102.870 · 10-fach'}[key]
    text,fc,media=q['text'],q['fc'],q['media']
    if '\n\n📖' in fc: fc=fc.split('\n\n📖')[0]   # Buch-Zeile vom 18.11. fällt weg (seit 23.11. keine Buch-Zeile unter Rezepten, Werbung nur 20:15)
    bild=media.split('/')[-1][:-4]; assert os.path.exists(f"{REPO}/boards/{bild}.jpg") or key in NEU, bild
    tg=[w for w in text.split() if w.startswith('#')]; assert tg[-1]=='#fitmitkev' and 2<=len(tg)<=5, key
    low=(text+fc).lower()
    for w in ('esn','abnehm','höflich','rezeptbuch','http','melly','gta','food','#lecker','#zuckerfrei','📖'): assert w not in low,(key,w)
    assert 'Rezept im 1. Kommentar' in text and q['kcal']<=500
    posts.append(dict(n=n,key=key,date=f'2026-11-27T{zeit}:00',text=text,fc=fc,media=media,alt=q['alt'],board=bild,kcal=q['kcal'],suess=bool(q['suess']),neu=key in NEU,zuletzt=wdh,hashtags=len(tg)))
# süß/herzhaft im Wechsel über alle Beiträge (feste mitgezählt, Buch-Beiträge neutral)
seq=sorted([(p['date'][11:16],p['suess']) for p in posts]+[(t,s) for t,(x,s) in FEST.items()])   # Buch-/Teaser-Beiträge (None) trennen im Feed zwei Rezepte
for a,b in zip(seq,seq[1:]): assert not (a[1] and b[1]), ('zwei süße hintereinander',a,b)
assert len(posts)==16 and len(posts)+len(FEST)==20 and sum(not p['neu'] for p in posts)==2
assert all(not p['suess'] for p in posts if p['date'][11:16]>='17:30')
json.dump(posts,open(f"{D}/out/freitag_posts.json","w"),ensure_ascii=False,indent=1)
alle=[(p['date'][11:16],f"{p['n']:02d} · {'süß ' if p['suess'] else 'herz'} · {p['alt']} · {p['kcal']} kcal · "+('NEU' if p['neu'] else 'Wiederholer, zuletzt '+p['zuletzt'])) for p in posts]+[(t,'–– · fest · '+x) for t,(x,s) in FEST.items()]
with open(f"{D}/out/posting-plan-freitag.txt","w") as fh:
    fh.write("Posting-Plan Freitag 27.11.2026 – 20 Beiträge: 14 neue Rezepte, 2 Wiederholer, 2 ESN-Rezepte, Teaser Festtagsküche, Buch-Beitrag.\n")
    fh.write("Alle neuen Fotos aus Higgsfield (GPT Image 2.6). Toffifee-Bowl, Germknödel und Schokokuss-Torte mit Kevs Bildern.\n")
    fh.write("Kloßteig-Reihe: 12:20 Boeuf Stroganoff, 17:45 Schweinefilet in Pfefferrahm, 19:15 Tafelspitz mit Meerrettich.\nAlle Boards ohne Box.\n\n")
    for t,x in sorted(alle): fh.write(f"{t} · {x}\n")
with open(f"{D}/out/texte-freitag.txt","w") as fh:
    for p in posts: fh.write(f"===== {p['n']:02d} · {p['date'][11:16]} · {p['alt']}{'  ·  NEU' if p['neu'] else '  ·  Wiederholer'}\n\nBEITRAG:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\nBILD: {p['media']}\n\n\n")
    b8=[b for b in json.load(open(f"{REPO}/tools/promo/buch_posts_ab_2311.json"))['posts'] if b['key']=='B8'][0]
    fh.write(f"===== 20:15 · Buch-Beitrag B8 · {b8['alt']}\n\nBEITRAG:\n{b8['text']}\n\n1. KOMMENTAR:\n{b8['fc']}\n\nBILD: {b8['media']}\n")
print(open(f"{D}/out/posting-plan-freitag.txt").read())
