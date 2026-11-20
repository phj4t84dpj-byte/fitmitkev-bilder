# -*- coding: utf-8 -*-
# G99 – Sonntag 22.11.2026, Stand 20.11.: Texte für die 4 Rezepte nach Mitbewerber-Muster. Uhrzeiten folgen am 21.11. mit dem Rest des Tages.
# Test (Kev 20.11.): bei den zwei Gläsern steht das Rezept im Beitragstext, der 1. Kommentar ist nur ein Gruß. Vergleich: Spekulatius-Kirsch am 15.11. mit Rezept im Kommentar.
import json, os
import g99_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NAME={'NutellaBanane':'Nutella-Banane im Glas','DoenerKuchen':'Döner-Kuchen aus Skyr-Teig','PizzaKartoffeln':'Pizza-Kartoffeln aus dem Ofen','SpekKirschGlas':'Spekulatius-Kirsch im Glas'}
BILD={'NutellaBanane':'G99-NutellaBanane-ohneBox','DoenerKuchen':'G99-DoenerKuchen-ohneBox','PizzaKartoffeln':'G99-PizzaKartoffeln-ohneBox','SpekKirschGlas':'G93N-SpekKirschGlas-ohneBox'}
MENGE={'NutellaBanane':'1 Glas','DoenerKuchen':'4 Stücke, Springform 24 cm','PizzaKartoffeln':'4 Portionen, Auflaufform 20 × 30 cm','SpekKirschGlas':'2 Gläser'}
LAB={'NutellaBanane':'pro Glas','DoenerKuchen':'pro Stück','PizzaKartoffeln':'pro Portion','SpekKirschGlas':'pro Glas'}
KURZ={'NutellaBanane':'Nutella-Banane im Glas aus nur 3 Zutaten','SpekKirschGlas':'Spekulatius-Kirsch im Glas, ohne Backen'}
EMO={'NutellaBanane':'😍','DoenerKuchen':'😋','PizzaKartoffeln':'🤤','SpekKirschGlas':'🥰'}
posts=[]
for r in G.R:
    k,p,c,f=G.macros4(r); key=r['key']; lab=LAB[key]
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])
    if r['ex']: zut+="\n"+"\n".join(f"• {e}" for e in r['ex'])
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    naehr=f"Nährwerte {lab}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett"
    if key in G.REZEPT_IM_BEITRAG:
        text=(f"{k} kcal {lab} {EMO[key]} {KURZ[key]}\n\nZutaten ({MENGE[key]}):\n{zut}\n\nSo geht's:\n{steps}\n\n{naehr}\n\n{r['frage']}\n\n{r['tags']}")
        fc="Schmeckt nach Sünde, zählt wie Salat 😉\nBleib satt! 💪 Kev"
        assert 'Kommentar' not in text
    else:
        text=f"{k} kcal {lab} {EMO[key]} Rezept im 1. Kommentar ⤵️\n\n{r['tags']}"
        fc=f"{NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({MENGE[key]}):\n{zut}\n\nSo geht's:\n{steps}\n\n{naehr}\n\n"
        if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
        fc+=f"Bleib satt! 💪\n\n{r['frage']}"
        assert '#' not in fc
    low=(text+fc).lower()
    for w in ('esn','abnehm','höflich','melly','http'): assert w not in low,(key,w)
    assert r['tags'].split()[-1]=='#fitmitkev'
    posts.append(dict(key=key,text=text,fc=fc,media=URL.format(BILD[key]),alt=NAME[key],kcal=k,suess=r['suess'],rezept_im_beitrag=key in G.REZEPT_IM_BEITRAG,hashtags=len(r['tags'].split())))
json.dump(posts,open(f"{D}/out/sonntag_tests_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/out/texte-sonntag-tests.txt","w") as fh:
    fh.write("Sonntag 22.11.2026 – die 4 Rezepte nach Mellys Muster (Uhrzeiten folgen mit dem Rest des Tages)\nTest bei den zwei Gläsern: Rezept steht im Beitrag statt im 1. Kommentar.\n\n\n")
    for p_ in posts:
        fh.write(f"===== {NAME[p_['key']]}{'  ·  TEST: Rezept im Beitrag' if p_['rezept_im_beitrag'] else ''}\n\nBEITRAG:\n{p_['text']}\n\n1. KOMMENTAR:\n{p_['fc']}\n\nBILD: {p_['media']}\n\n\n")
for p_ in posts: print('=====',p_['key'],'\n'+p_['text'],'\n--- 1. Kommentar:\n'+p_['fc'][:260],'\n')
