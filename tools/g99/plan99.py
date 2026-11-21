# -*- coding: utf-8 -*-
# G99 – Sonntag 22.11.2026: Tagesplan aus den 8 festen Rezepten (out/sonntag_tests_posts.json, von texte99.py) und 8 bewährten Treffern vom So 15.11.
# Schreibt out/sonntag_posts.json, out/posting-plan-sonntag.txt, out/texte-sonntag.txt.
import json, os
D=os.path.dirname(os.path.abspath(__file__)); REPO=os.environ.get('REPO','/home/claude/fitmitkev-bilder')
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NEU8={p['key']:p for p in json.load(open(f"{D}/out/sonntag_tests_posts.json"))}
ALT={p['key']:p for f in ('tools/g93/sonntag_posts.json','tools/g93n/sonntag_neu_posts.json') for p in json.load(open(f"{REPO}/{f}"))}
# (Uhrzeit, Schlüssel, Hashtags für Wiederholer – None = wie am 15.11.)
PLAN=[('07:30','Eiersalat',None),('08:15','KalterHund',None),('09:00','DoenerKuchen',None),('09:45','Hefezopf',None),
      ('10:25','ZwiebelSahne','#zwiebelsahneschnitzel #schnitzel #fitmitkev'),('11:30','HanutaBowl',None),('12:30','Sonntagsbraten',None),('13:40','PizzaKartoffeln',None),
      ('14:20','SpekKirschGlas',None),('15:00','BamiGoreng',None),('15:40','EinTeig',None),('16:25','Lahmacun',None),
      ('17:10','QuarkWoelkchen',None),('18:00','Blumenkohlsuppe',None),('19:00','Tortellini',None),('20:45','NutellaBanane',None)]
FEST={'06:10':'ESN-Rezept Spekulatius-Mousse','06:50':'ESN K2','11:00':'ESN P1','12:00':'ESN P0','13:00':'ESN-Rezept Erdbeer-Bowl','20:15':'Buch-Beitrag'}
GRUPPE_A={1,4,5,6,10,13,15,16}          # 2–3 Hashtags; übrige 4–5
BILD_ALT={'HanutaBowl':'G93N-HanutaBowl-ohneBox'}
NEU7={'NutellaBanane','DoenerKuchen','PizzaKartoffeln','EinTeig','QuarkWoelkchen','Sonntagsbraten','Blumenkohlsuppe'}
SW=[False,True,False,True,False,True,False,False,True,False,True,False,True,False,False,True]
posts=[]
for n,(zeit,key,tags) in enumerate(PLAN,1):
    if key in NEU8:
        q=NEU8[key]; text,fc,media,alt,kcal,suess,rib=q['text'],q['fc'],q['media'],q['alt'],q['kcal'],q['suess'],q['rezept_im_beitrag']
    else:
        q=ALT[key]; titel,_,alt_tags=q['text'].partition('\n\n'); text=titel+'\n\n'+(tags or alt_tags); fc=q['fc']
        bild=BILD_ALT.get(key,f'G93-{key}-ohneBox'); assert os.path.exists(f"{REPO}/boards/{bild}.jpg"), bild
        media,alt,kcal,suess,rib=URL.format(bild),q['alt'],q['kcal'],q['suess'],False
        assert '#' not in fc
    tg=[w for w in text.split() if w.startswith('#')]; nt=len(tg)
    assert tg[-1]=='#fitmitkev' and 2<=nt<=5 and (nt<=3)==(n in GRUPPE_A), (n,key,nt)
    assert suess==SW[n-1], ('süß/herzhaft',n,key)
    low=(text+fc).lower()
    for w in ('esn','abnehm','höflich','rezeptbuch','http','melly','gta','15.11','box „'): assert w not in low,(key,w)
    assert zeit not in FEST
    posts.append(dict(n=n,key=key,date=f'2026-11-22T{zeit}:00',text=text,fc=fc,media=media,alt=alt,box=False,kcal=kcal,suess=suess,hashtags=nt,gruppe='A (2–3)' if nt<=3 else 'B (4–5)',
                      neu=key in NEU7,rezept_im_beitrag=rib,buch=False))
assert len(posts)==16 and len({p['date'] for p in posts})==16 and len({p['key'] for p in posts})==16
assert sum(p['gruppe'][0]=='A' for p in posts)==8 and sum(p['suess'] for p in posts)==7
json.dump(posts,open(f"{D}/out/sonntag_posts.json","w"),ensure_ascii=False,indent=1)
alle=[(p['date'][11:16],f"{p['n']:02d} · {'süß ' if p['suess'] else 'herz'} · {p['alt']} · {p['kcal']} kcal · {p['hashtags']} Hashtags{' · NEU' if p['neu'] else ''}{' · TEST: Rezept im Beitrag' if p['rezept_im_beitrag'] else ''}") for p in posts]
alle+=[(t,f"–– · schon eingeplant · {x}") for t,x in FEST.items()]
with open(f"{D}/out/posting-plan-sonntag.txt","w") as fh:
    fh.write("Posting-Plan Sonntag 22.11.2026 – 22 Beiträge: 16 Rezepte (neu anzulegen) + 6 feste Beiträge (schon eingeplant).\n")
    fh.write("7 neue Rezepte, 9 bewährte. Alle Boards ohne Box. Keine Buch-Zeile, keine ESN-Zeile in den 16 Rezepten.\nTest: bei den zwei Gläsern (14:20 und 20:45) steht das Rezept im Beitrag statt im 1. Kommentar.\n\n")
    for t,x in sorted(alle): fh.write(f"{t} · {x}\n")
with open(f"{D}/out/texte-sonntag.txt","w") as fh:
    for p in posts:
        fh.write(f"===== {p['n']:02d} · {p['date'][11:16]} · {p['alt']}{'  ·  TEST: Rezept im Beitrag' if p['rezept_im_beitrag'] else ''}\n\nBEITRAG:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\nBILD: {p['media']}\n\n\n")
print(open(f"{D}/out/posting-plan-sonntag.txt").read())
