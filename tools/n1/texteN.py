# -*- coding: utf-8 -*-
# N1 – Texte und Plan für die drei Nischenseiten, Sonntag 15.11.2026
import json, os
import n1_data as N
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/N1-{}.jpg"
TAG='2026-11-15'
NAME={'KHZimtschnecken':'Zimtschnecken mit Frischkäse-Guss','KHBienenstich':'Bienenstich vom Blech wie früher','KHKirschStreusel':'Kirsch-Streuselkuchen vom Blech','KHVanillekipferl':'Vanillekipferl wie bei Oma','KHStollen':'Christstollen mit Marzipan',
 'HHEierMuffins':'Rührei-Muffins aus dem Airfryer','HHGebrannteMandeln':'Gebrannte Mandeln aus dem Airfryer','HHHaehnchenschenkel':'Knusprige Hähnchenkeulen aus dem Airfryer','HHBratapfel':'Bratäpfel aus dem Airfryer','HHCurrywurst':'Currywurst mit Pommes aus dem Airfryer',
 'OKArmeRitter':'Arme Ritter mit Zimt und Zucker','OKRouladen':'Rinderrouladen wie bei Oma','OKErbseneintopf':'Erbseneintopf mit Würstchen','OKApfelstrudel':'Apfelstrudel mit Vanillesoße','OKKohlrouladen':'Kohlrouladen in Rahmsoße'}
EMO=['😍','🤤','😋','🥰','🤗']
posts=[]
for r in N.R:
    s=N.SEITEN[r['seite']]
    text=f"{NAME[r['key']]} {EMO[r['slot']]} Rezept im 1. Kommentar ⤵️\n\n{r['tags']} {s['tag']}"
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])+("\n"+"\n".join(f"• {e}" for e in r['ex']) if r['ex'] else '')
    steps="\n".join(f"{i}. {t}" for i,t in enumerate(r['schritte'],1))
    fc=f"{NAME[r['key']]}\n\n{r['intro']}\n\nZutaten ({r['aus']}):\n{zut}\n\nSo geht's:\n{steps}\n\nZeit: {r['zeit']}\n\nGuten Appetit! 😋\n\n{r['frage']}"
    assert all(w not in (text+fc).lower() for w in ('kcal','abnehm','fitmitkev'))
    posts.append(dict(seite=r['seite'],blog=s['blog'],key=r['key'],date=f"{TAG}T{N.ZEITEN[r['slot']]}:00",text=text,fc=fc,media=URL.format(r['key']),alt=NAME[r['key']]))
json.dump(posts,open(f"{D}/out/n1_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/out/Texte-Nischenseiten-Sonntag.txt","w") as fh:
    for p in posts: fh.write(f"===== {N.SEITEN[p['seite']]['name']} · {p['date'][11:16]} · {p['alt']}\n\nTITEL:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\n\n")
for p in posts: print(p['seite'],p['date'][11:16],p['text'].split(chr(10))[0])
