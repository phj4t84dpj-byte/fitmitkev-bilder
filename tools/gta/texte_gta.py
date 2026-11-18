# -*- coding: utf-8 -*-
import json, os
import gta_data as G
D=os.path.dirname(os.path.abspath(__file__))
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/GTA-{}-ohneBox.jpg"
LAB={'KeyLimeBowl':('die ganze Bowl','pro Bowl'),'Cubano':('pro Sandwich','pro Sandwich'),'OfenNachos':('pro Portion','pro Portion')}
EMO={'KeyLimeBowl':'🤤','Cubano':'😋','OfenNachos':'😍'}
out=[]
for r in G.R:
    k,p,c,f=G.macros4(r); key=r['key']; t,nl=LAB[key]
    text=f"Heute erscheint GTA 6 🎮 {k} kcal {t} {EMO[key]} Rezept im 1. Kommentar ⤵️\n\n{r['tags']}"
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])+("\n"+"\n".join(f"• {e}" for e in r['ex']) if r['ex'] else '')
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    fc=f"{G.NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({G.FORM[key]}):\n{zut}\n\nSo geht's:\n{steps}\n\nNährwerte {nl}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\n"
    if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
    fc+=f"Bleib satt! 💪\n\n{r['frage']}"
    assert 'abnehm' not in (text+fc).lower() and 'esn' not in fc.lower()
    out.append(dict(key=key,text=text,fc=fc,media=URL.format(key),alt=G.NAME[key],kcal=k))
json.dump(out,open(f'{D}/out/gta_posts.json','w'),ensure_ascii=False,indent=1)
with open(f'{D}/out/texte-gta.txt','w') as fh:
    for o in out: fh.write(f"===== {o['alt']}\n\nTITEL:\n{o['text']}\n\n1. KOMMENTAR:\n{o['fc']}\n\nBILD: {o['media']}\n\n\n")
print(open(f'{D}/out/texte-gta.txt').read())
