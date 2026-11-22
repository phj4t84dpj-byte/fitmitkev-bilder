# -*- coding: utf-8 -*-
# G100 – Montag 23.11.2026: Texte für die 4 neuen Rezepte -> out/montag_neu_posts.json
import json, os
import g100_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NAME={'KokosWoelkchen':'Kokos-Wölkchen aus 5 Zutaten','Schichtsalat':'Schichtsalat über Nacht','HackNudeln':'Gebratene Nudeln mit Hack','PizzaWrap':'Pizza-Wrap aus körnigem Frischkäse','Frikassee':'Hühnerfrikassee mit Knödeln'}
MENGE={'KokosWoelkchen':'30 Stück, Backblech','Schichtsalat':'6 Portionen, große Glasschüssel','HackNudeln':'4 Portionen','PizzaWrap':'2 Wraps, Backblech','Frikassee':'4 Portionen'}
EMO={'KokosWoelkchen':'🥰','Schichtsalat':'🤗','HackNudeln':'🤤','PizzaWrap':'😋','Frikassee':'🤗'}
posts=[]
for r in G.R:
    k,p,c,f=G.macros4(r); key=r['key']; lab=r['portion']
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])
    if r['ex']: zut+="\n"+"\n".join(f"• {e}" for e in r['ex'])
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    naehr=f"Nährwerte {lab}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett"
    text=f"{k} kcal {lab} {EMO[key]} Rezept im 1. Kommentar ⤵️\n\n{r['tags']}"
    fc=f"{NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({MENGE[key]}):\n{zut}\n\nSo geht's:\n{steps}\n\n{naehr}\n\n"
    if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
    fc+=f"Bleib satt! 💪\n\n{r['frage']}"
    assert '#' not in fc
    low=(text+fc).lower()
    for w in ('esn','abnehm','höflich','melly','http','miracel'): assert w not in low,(key,w)
    assert r['tags'].split()[-1]=='#fitmitkev'
    posts.append(dict(key=key,text=text,fc=fc,media=URL.format(f'G100-{key}-ohneBox'),alt=NAME[key],kcal=k,suess=r['suess'],hashtags=len(r['tags'].split())))
json.dump(posts,open(f"{D}/out/montag_neu_posts.json","w"),ensure_ascii=False,indent=1)
for p_ in posts: print('=====',p_['key'],'\n'+p_['text'],'\n--- 1. Kommentar:\n'+p_['fc'],'\n')
