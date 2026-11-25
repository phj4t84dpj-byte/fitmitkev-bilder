# -*- coding: utf-8 -*-
# G103 – Donnerstag 26.11.2026: Texte für die 6 neuen Rezepte (3 aus der Kloßteig-Reihe) -> out/donnerstag_neu_posts.json
# Die Wiederholer (auch die mit neuem Foto aus dem Wiederholer-Test) behalten ihren 1. Kommentar vom letzten Lauf, siehe plan103.py.
import json, os
import g103_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NAME={'KlossHirsch':'Klöße mit Hirschgulasch und Preiselbeeren','KlossPilz':'Klöße mit Pilzrahmsoße','KlossFrikadellen':'Klöße mit Frikadellen in Zwiebelsoße',
      'Schneewittchen':'Schneewittchenkuchen vom Blech','JapanKaesekuchen':'Japanischer Käsekuchen mit Skyr','ToastHawaii':'Toast Hawaii in leicht'}
MENGE={'KlossHirsch':'4 Portionen','KlossPilz':'4 Portionen','KlossFrikadellen':'4 Portionen','Schneewittchen':'20 Stücke, 1 Backblech 30 × 40 cm','JapanKaesekuchen':'10 Stücke, Springform 20 cm','ToastHawaii':'4 Portionen, 8 Toasts'}
EMO={'KlossHirsch':'😍','KlossPilz':'🤤','KlossFrikadellen':'🥰','Schneewittchen':'😋','JapanKaesekuchen':'😍','ToastHawaii':'🤗'}
posts=[]
for r in [G.NEU[k] for k in NAME]:
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
    posts.append(dict(key=key,text=text,fc=fc,media=URL.format(f'G103-{key}-ohneBox'),alt=NAME[key],kcal=k,suess=r['suess'],hashtags=len(r['tags'].split())))
json.dump(posts,open(f"{D}/out/donnerstag_neu_posts.json","w"),ensure_ascii=False,indent=1)
for p_ in posts: print('=====',p_['key'],'\n'+p_['text'],'\n--- 1. Kommentar:\n'+p_['fc'],'\n')
