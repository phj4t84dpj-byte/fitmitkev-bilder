# -*- coding: utf-8 -*-
# N4 – Texte und Plan für die drei Nischenseiten So 29.11.2026. Aufruf: python3 texteN4.py <commit>
import json, os, sys
import n4_data as N
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
C=sys.argv[1] if len(sys.argv)>1 else 'main'
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/"+C+"/boards/N4-{}.jpg"
EMO=['😍','🤤','😋','🥰','🤗']
WT=['Sonntag']
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
json.dump(posts,open(f"{D}/out/n4_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/out/Texte-Nischenseiten-Sonntag.txt","w") as fh:
    for p in posts:
        fh.write(f"===== {WT[0]} 29.11. · {N.SEITEN[p['seite']]['name']} · {p['date'][11:16]} · {p['alt']}\n\nTITEL:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\n\n")
for p in posts: print(p['date'][5:16],p['seite'],p['text'].split(chr(10))[0])
