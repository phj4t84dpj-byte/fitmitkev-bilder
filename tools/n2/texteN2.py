# -*- coding: utf-8 -*-
# N2 – Texte und Plan für die drei Nischenseiten, Mo 16.–Mi 18.11.2026
import json, os
import n2_data as N
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/N2-{}.jpg"
EMO=['😍','🤤','😋','🥰','🤗']
WT=['Montag','Dienstag','Mittwoch']
posts=[]
for r in sorted(N.R,key=lambda r:(r['tag'],r['seite'],r['slot'])):
    s=N.SEITEN[r['seite']]
    text=f"{r['name']} {EMO[(r['slot']+r['tag'])%5]} Rezept im 1. Kommentar ⤵️\n\n{r['tags']} {s['tag']}"
    zl=r['zl'] if r['stil']=='zettel' else [f"{z['menge']} {z['name']}" for z in r['zutaten']]
    zut="\n".join(f"• {z}" for z in zl+r['ex'])
    steps="\n".join(f"{i}. {t}" for i,t in enumerate(r['schritte'],1))
    fc=f"{r['name']}\n\n{r['intro']}\n\nZutaten ({r['aus']}):\n{zut}\n\nSo geht's:\n{steps}\n\nZeit: {r['zeit']}\n\nGuten Appetit! 😋\n\n{r['frage']}"
    assert all(w not in (text+fc).lower() for w in ('kcal','abnehm','fitmitkev')),r['key']
    posts.append(dict(seite=r['seite'],blog=s['blog'],key=r['key'],date=f"{N.TAGE[r['tag']]}T{N.ZEITEN[r['slot']]}:00",text=text,fc=fc,media=URL.format(r['key']),alt=r['name']))
json.dump(posts,open(f"{D}/out/n2_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/out/Texte-Nischenseiten-Mo-Mi.txt","w") as fh:
    for p in posts:
        t=N.TAGE.index(p['date'][:10])
        fh.write(f"===== {WT[t]} · {N.SEITEN[p['seite']]['name']} · {p['date'][11:16]} · {p['alt']}\n\nTITEL:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\n\n")
for p in posts: print(p['date'][5:16],p['seite'],p['text'].split(chr(10))[0])
