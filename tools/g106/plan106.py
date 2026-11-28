# -*- coding: utf-8 -*-
# G106 – Sonntag 29.11.2026 (1. Advent): 15 neue Rezepte + 1 Wiederholer (Kalter Hund 22.11.) + Mehrwert MW9 Plätzchen-Check um 17:45.
# Fest: 6:10 ESN Spekulatius-Mousse (434674276), 13:00 ESN Erdbeer-Quark-Bowl (434674408), 15:00 F3 Festmenü (443732213); 16:45 Reel Mini-Marmorkuchen zusätzlich. 20:15 kein Buch-Beitrag.
import json, os
D=os.path.dirname(os.path.abspath(__file__)); REPO='/home/claude/fitmitkev-bilder'
NEU={p['key']:p for p in json.load(open(f"{D}/out/sonntag_neu_posts.json"))}
W={p['key']:p for p in json.load(open(f"{REPO}/tools/g99/sonntag_posts.json"))}
PLAN=[('06:50','Eiweissbrot'),('07:35','KalterHund'),('08:20','Kartoffelsuppe'),('09:00','FrankfurterKranz'),('09:40','Enchiladas'),('10:20','Quarkstollen'),
      ('11:00','KlossKohlrouladen'),('11:40','Tassenkuchen'),('12:20','SpinatQuiche'),('13:40','Fischstaebchen'),('14:20','Spitzbuben'),('15:40','PrinzenrolleBowl'),
      ('16:20','KlossGans'),('17:00','Zwetschgenkuchen'),('19:15','CroqueMonsieur'),('20:15','GefuellteZucchini')]
ZUL={'KalterHund':'22.11.'}
MWT=open(f"{REPO}/mehrwert/MW9-Plaetzchen-Text.txt").read()
mw_text=MWT.split('==================== BEITRAGSTEXT ====================')[1].split('==================== 1. KOMMENTAR ====================')[0].strip()
mw_fc=MWT.split('==================== 1. KOMMENTAR ====================')[1].strip()
MW=dict(n=0,key='MW9',date='2026-11-29T17:45:00',text=mw_text,fc=mw_fc,media='https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/mehrwert/MW9-Plaetzchen.jpg',
        alt='Plätzchen-Check: so viel kcal hat 1 Plätzchen',board='MW9-Plaetzchen',kcal=None,suess=None,neu=True,zuletzt=None,hashtags=2)
FEST={'06:10':('ESN-Rezept Spekulatius-Mousse, süß (schon eingeplant, Id 434674276)',True),'13:00':('ESN-Rezept Erdbeer-Quark-Bowl, süß (schon eingeplant, Id 434674408)',True),
      '15:00':('F3 Festmenü zum 1. Advent, Buch „Festtagsküche in leicht“ (schon eingeplant, Id 443732213)',None)}
posts=[]
for n,(zeit,key) in enumerate(PLAN,1):
    if key in NEU: q=NEU[key]
    else: q=W[key]
    text,fc,media=q['text'],q['fc'],q['media']
    if '\n\n📖' in fc: fc=fc.split('\n\n📖')[0]
    bild=media.split('/')[-1][:-4]; assert os.path.exists(f"{REPO}/boards/{bild}.jpg") or key in NEU, bild
    tg=[w for w in text.split() if w.startswith('#')]; assert tg[-1]=='#fitmitkev' and 2<=len(tg)<=5, key
    low=(text+fc).lower()
    for w in ('esn','abnehm','höflich','rezeptbuch','http','melly','gta','food','#lecker','#zuckerfrei','📖'): assert w not in low,(key,w)
    assert 'Rezept im 1. Kommentar' in text and q['kcal']<=500
    posts.append(dict(n=n,key=key,date=f'2026-11-29T{zeit}:00',text=text,fc=fc,media=media,alt=q['alt'],board=bild,kcal=q['kcal'],suess=bool(q['suess']),neu=key in NEU,zuletzt=ZUL.get(key),hashtags=len(tg)))
low=(MW['text']+MW['fc']).lower()
for w in ('esn','abnehm','http','📖'): assert w not in low,('MW',w)
seq=sorted([(p['date'][11:16],p['suess']) for p in posts]+[(t,s) for t,(x,s) in FEST.items()]+[('17:45',None)])
for a,b in zip(seq,seq[1:]): assert not (a[1] and b[1]), ('zwei süße hintereinander',a,b)
assert len(posts)==16 and len(posts)+len(FEST)+1==20 and sum(not p['neu'] for p in posts)==1
assert all(not p['suess'] for p in posts if p['date'][11:16]>='17:30')
json.dump(posts+[MW],open(f"{D}/out/sonntag_posts.json","w"),ensure_ascii=False,indent=1)
alle=[(p['date'][11:16],f"{p['n']:02d} · {'süß ' if p['suess'] else 'herz'} · {p['alt']} · {p['kcal']} kcal · "+('NEU' if p['neu'] else 'Wiederholer, zuletzt '+p['zuletzt'])) for p in posts]+[(t,'–– · fest · '+x) for t,(x,s) in FEST.items()]+[('17:45','MW · Mehrwert „Plätzchen-Check: so viel hat 1 Plätzchen“ (NEU)')]
with open(f"{D}/out/posting-plan-sonntag.txt","w") as fh:
    fh.write("Posting-Plan Sonntag 29.11.2026 (1. Advent) – 20 Beiträge: 15 neue Rezepte, 1 Wiederholer, 2 ESN-Rezepte, Festmenü-Beitrag zum Buch, 1 Mehrwert-Beitrag. Dazu 16:45 das Marmorkuchen-Reel.\n")
    fh.write("Alle neuen Fotos aus Higgsfield (GPT Image 2.6), alle Boards ohne Box. Rezepte nach dem SEO-Wochenplan (Google-Suchen).\n")
    fh.write("Kloß-Reihe endet heute: 11:00 Nr. 12 Kohlrouladen-Pfanne, 16:20 Nr. 3 Hähnchenkeule wie Gans. 20:15 kein Buch-Beitrag, dort ein Rezept.\n\n")
    for t,x in sorted(alle): fh.write(f"{t} · {x}\n")
with open(f"{D}/out/texte-sonntag.txt","w") as fh:
    for p in posts: fh.write(f"===== {p['n']:02d} · {p['date'][11:16]} · {p['alt']}{'  ·  NEU' if p['neu'] else '  ·  Wiederholer'}\n\nBEITRAG:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\nBILD: {p['media']}\n\n\n")
    fh.write(f"===== 17:45 · Mehrwert · {MW['alt']}  ·  Wiederholer\n\nBEITRAG:\n{MW['text']}\n\n1. KOMMENTAR:\n{MW['fc']}\n\nBILD: {MW['media']}\n")
print(open(f"{D}/out/posting-plan-sonntag.txt").read())
