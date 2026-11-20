# -*- coding: utf-8 -*-
# G98 – Samstag 21.11.2026: Titel, 1. Kommentar, Posting-Plan, Texte (TXT), samstag_posts.json
import json, os
from datetime import datetime
import g98_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/G98-{}.jpg"
NAME={'Reibekuchen':'Reibekuchen aus dem Ofen','Milchreis':'Milchreis mit Zimt wie bei Oma','Reispfanne':'Paprika-Hack-Reis-Pfanne','Vanillekipferl':'Vanillekipferl in leicht',
      'MarmorBowl':'Marmorkuchen-Bowl nur für dich','PizzaHawaii':'Pizza Hawaii aus Skyr-Teig','Curry':'Hähnchen-Curry mit Reis','Rotweinkuchen':'Rotweinkuchen in leicht',
      'KaeseNudeln':'Schinken-Käse-Nudeln aus einem Topf','SuessSauer':'Hähnchen süß-sauer aus dem Ofen','Cevapcici':'Cevapcici mit Ofen-Pommes','Rumkugeln':'Rumkugeln ohne Zucker',
      'CrispyBurger':'Crispy-Chicken-Burger aus dem Ofen','OfenTacos':'Ofen-Tacos mit Hack','SchokoShake':'Schoko-Milchshake wie im Diner','Churros':'Churros aus dem Ofen'}
FORM={'Reibekuchen':'Backblech','Vanillekipferl':'Backblech','Rotweinkuchen':'Kastenform 25 cm','CrispyBurger':'Backblech','OfenTacos':'Auflaufform 20 × 30 cm','Churros':'20 Churros, Backblech'}
EINZELN={'Vanillekipferl'}
LABELS=('pro Stück','pro Portion','pro Glas','pro Teller','pro Pizza','pro Scheibe','pro Kugel','pro Burger')
def portion_label(r):
    p=r['portion']
    for k in LABELS:
        if p.startswith(k): return k
    return 'pro Bowl'
def _anzahl_base(r):
    p=r['portion']; n=r['anzahl']
    if 'Bowl' in p: return '1 Portion, Glasform 15 × 10 cm'
    if p.startswith('pro Glas'): return f'{n} Gläser'
    if p.startswith('pro Pizza'): return f'{n} Pizzen'
    if p.startswith('pro Kugel'): return f'{n} Kugeln'
    if p.startswith('pro Burger'): return f'{n} Burger'
    if p.startswith('pro Portion'): return '1 Portion' if n==1 else f'{n} Portionen'
    return f'{n} Stück' if (r['key'] in EINZELN or n<12) else f'{n} Stücke'
def anzahl_label(r):
    f=FORM.get(r['key']); base=_anzahl_base(r)
    return f'{base}, {f}' if f else base
EMO=['🤤','😍','😋','🥰','🤗']
posts=[]
for i,r in enumerate(G.R):
    k,p,c,f=G.macros4(r); key=r['key']; n=i+1
    pl=portion_label(r); lab='die ganze Bowl' if pl=='pro Bowl' else pl
    title=f"{k} kcal {lab} {EMO[i%5]} Rezept im 1. Kommentar ⤵️"
    text=title+"\n\n"+r['tags']
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])
    if r['ex']: zut+="\n"+"\n".join(f"• {e}" for e in r['ex'])
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    fc=f"{NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({anzahl_label(r)}):\n{zut}\n\nSo geht's:\n{steps}\n\n"
    fc+=f"Nährwerte {pl}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\n"
    if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
    fc+=f"Bleib satt! 💪\n\n{r['frage']}"
    assert not r.get('hinweis')
    low=(text+fc).lower()
    for w in ('esn','abnehm','höflich','rezeptbuch','gta','http'): assert w not in low, (key,w)
    assert '#' not in fc
    dt=datetime.strptime('2026-11-21 '+G.ZEITEN[i],'%Y-%m-%d %H:%M'); nt=len(r['tags'].split())
    assert nt==G.HASHTAG_SOLL[n] and r['tags'].split()[-1]=='#fitmitkev'
    posts.append(dict(n=n,key=key,date=dt.strftime('%Y-%m-%dT%H:%M:%S'),text=text,fc=fc,media=URL.format(key+'-ohneBox'),alt=NAME[key],box=False,kcal=k,suess=r['suess'],hoeflich=False,
                      hashtags=nt,gruppe='A (2–3)' if nt<=3 else 'B (4–5)',fastfood=key in G.FASTFOOD,buch=False))
ga=[p_ for p_ in posts if p_['gruppe'][0]=='A']; gb=[p_ for p_ in posts if p_['gruppe'][0]=='B']
assert len(ga)==8 and len(gb)==8 and len({p_['date'] for p_ in posts})==16
json.dump(posts,open(f"{D}/out/samstag_posts.json","w"),ensure_ascii=False,indent=1)
alle=[(p_['date'][11:16],f"{p_['n']:02d} · {'süß ' if p_['suess'] else 'herz'} · {NAME[p_['key']]} · {p_['kcal']} kcal · {p_['hashtags']} Hashtags (Gruppe {p_['gruppe'][0]}){' · FAST FOOD (neu)' if p_['fastfood'] else ''}") for p_ in posts]
alle+=[(t,f"–– · schon eingeplant · {x}") for t,x in G.FEST.items()]
with open(f"{D}/out/posting-plan-samstag.txt","w") as fh:
    fh.write("Posting-Plan Samstag 21.11.2026 – 22 Beiträge: 16 Rezepte (neu anzulegen) + 6 feste Beiträge (schon eingeplant).\n")
    fh.write("Alle Boards ohne Box. Keine Buch-Zeile, keine ESN-Zeile in den 16 Rezepten, kein Höflich-Titel.\n\n")
    for t,x in sorted(alle): fh.write(f"{t} · {x}\n")
with open(f"{D}/out/texte-samstag.txt","w") as fh:
    for p_ in posts:
        fh.write(f"===== {p_['n']:02d} · {p_['date'][11:16]} · {NAME[p_['key']]}\n\nTITEL:\n{p_['text']}\n\n1. KOMMENTAR:\n{p_['fc']}\n\nBILD: {p_['media']}\n\n\n")
print(len(posts)); [print(p_["n"],p_["date"][11:16],p_["text"].replace(chr(10)+chr(10),'  |  ')) for p_ in posts]
