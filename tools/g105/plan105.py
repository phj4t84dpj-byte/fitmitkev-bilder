# -*- coding: utf-8 -*-
# G105 – Samstag 28.11.2026: 14 neue Rezepte + 2 Wiederholer (Rotweinkuchen 21.11., Mutzen 18.11.) + Mehrwert MW3 Brot (14.11.: 49.805, 4,5-fach) um 17:45.
# Fest: 6:10 ESN Vanillepudding (434673825), 13:00 ESN Schoko-Kugeln (434673941), 15:00 F2 Launch Festtagsküche (443732145). 20:15 kein Buch-Beitrag (Kev 26.11.).
import json, os
D=os.path.dirname(os.path.abspath(__file__)); REPO='/home/claude/fitmitkev-bilder'
NEU={p['key']:p for p in json.load(open(f"{D}/out/samstag_neu_posts.json"))}
W={p['key']:p for p in json.load(open(f"{REPO}/tools/g98/samstag_posts.json"))+json.load(open(f"{REPO}/tools/g96/mittwoch_posts.json"))}
PLAN=[('06:50','Shakshuka'),('07:35','FantaKuchen'),('08:20','Ofengemuese'),('09:00','Rotweinkuchen'),('09:40','KlossGefuellt'),('10:20','Donauwelle'),
      ('11:00','Carbonara'),('11:40','Mutzen'),('12:20','Huehnersuppe'),('13:40','Bauerntopf'),('14:20','KinderBuenoBowl'),('15:40','ApfelkuchenBlech'),
      ('16:20','KlossSoss'),('17:00','Amerikaner'),('19:15','TortelliniAuflauf'),('20:15','Ofenkartoffel')]
ZUL={'Rotweinkuchen':'21.11. · 71.526 (14.11.: 292.436)','Mutzen':'18.11. · 147.466'}
MWT=open(f"{REPO}/mehrwert/MW3-Brot-Text.txt").read()
mw_text=MWT.split('==================== BEITRAGSTEXT ====================')[1].split('==================== 1. KOMMENTAR ====================')[0].strip()
mw_fc=MWT.split('==================== 1. KOMMENTAR ====================')[1].strip()
MW=dict(n=0,key='MW3',date='2026-11-28T17:45:00',text=mw_text,fc=mw_fc,media='https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/mehrwert/MW3-Brot.jpg',
        alt='Brot macht dick? Vollkornbrot mit zwei Belägen im Kalorienvergleich',board='MW3-Brot',kcal=None,suess=None,neu=False,zuletzt='14.11. · 49.805 · 4,5-fach',hashtags=2)
FEST={'06:10':('ESN-Rezept Vanillepudding mit Zimtpflaumen, süß (schon eingeplant, Id 434673825)',True),'13:00':('ESN-Rezept Schoko-Kugeln, süß (schon eingeplant, Id 434673941)',True),
      '15:00':('F2 Launch „Festtagsküche in leicht“ (schon eingeplant, Id 443732145)',None)}
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
    posts.append(dict(n=n,key=key,date=f'2026-11-28T{zeit}:00',text=text,fc=fc,media=media,alt=q['alt'],board=bild,kcal=q['kcal'],suess=bool(q['suess']),neu=key in NEU,zuletzt=ZUL.get(key),hashtags=len(tg)))
low=(MW['text']+MW['fc']).lower()
for w in ('esn','abnehm','http','📖'): assert w not in low,('MW',w)
seq=sorted([(p['date'][11:16],p['suess']) for p in posts]+[(t,s) for t,(x,s) in FEST.items()]+[('17:45',None)])
for a,b in zip(seq,seq[1:]): assert not (a[1] and b[1]), ('zwei süße hintereinander',a,b)
assert len(posts)==16 and len(posts)+len(FEST)+1==20 and sum(not p['neu'] for p in posts)==2
assert all(not p['suess'] for p in posts if p['date'][11:16]>='17:30')
json.dump(posts+[MW],open(f"{D}/out/samstag_posts.json","w"),ensure_ascii=False,indent=1)
alle=[(p['date'][11:16],f"{p['n']:02d} · {'süß ' if p['suess'] else 'herz'} · {p['alt']} · {p['kcal']} kcal · "+('NEU' if p['neu'] else 'Wiederholer, zuletzt '+p['zuletzt'])) for p in posts]+[(t,'–– · fest · '+x) for t,(x,s) in FEST.items()]+[('17:45','MW · Mehrwert „Brot macht dick?“ (Wiederholer, 14.11.: 49.805 Reichweite, bester Mehrwert-Beitrag)')]
with open(f"{D}/out/posting-plan-samstag.txt","w") as fh:
    fh.write("Posting-Plan Samstag 28.11.2026 – 20 Beiträge: 14 neue Rezepte, 2 Wiederholer, 2 ESN-Rezepte, Launch Festtagsküche, 1 Mehrwert-Beitrag.\n")
    fh.write("Alle neuen Fotos aus Higgsfield (GPT Image 2.6), alle Boards ohne Box. Rezepte nach dem SEO-Wochenplan (Google-Suchen).\n")
    fh.write("Kloß-Reihe: 09:40 Gefüllte Klöße mit Hack, 16:20 Kloß mit Soß wie in Franken. 20:15 kein Buch-Beitrag, dort ein Rezept.\n\n")
    for t,x in sorted(alle): fh.write(f"{t} · {x}\n")
with open(f"{D}/out/texte-samstag.txt","w") as fh:
    for p in posts: fh.write(f"===== {p['n']:02d} · {p['date'][11:16]} · {p['alt']}{'  ·  NEU' if p['neu'] else '  ·  Wiederholer'}\n\nBEITRAG:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\nBILD: {p['media']}\n\n\n")
    fh.write(f"===== 17:45 · Mehrwert · {MW['alt']}  ·  Wiederholer\n\nBEITRAG:\n{MW['text']}\n\n1. KOMMENTAR:\n{MW['fc']}\n\nBILD: {MW['media']}\n")
print(open(f"{D}/out/posting-plan-samstag.txt").read())
