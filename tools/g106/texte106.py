# -*- coding: utf-8 -*-
# G106 – Sonntag 29.11.2026: Texte für die 15 neuen Rezepte -> out/sonntag_neu_posts.json
import json, os
import g106_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NAME={'Quarkstollen':'Quarkstollen ohne Hefe','FrankfurterKranz':'Frankfurter Kranz in leicht','Tassenkuchen':'Schoko-Tassenkuchen in 3 Minuten','Spitzbuben':'Spitzbuben mit Marmelade',
      'PrinzenrolleBowl':'Prinzenrolle-Bowl nur für dich','Zwetschgenkuchen':'Zwetschgenkuchen vom Blech','Eiweissbrot':'Eiweißbrot aus Frischkäse','Kartoffelsuppe':'Kartoffelsuppe mit Würstchen',
      'Enchiladas':'Enchiladas mit Hähnchen aus dem Ofen','Fischstaebchen':'Fischstäbchen mit Püree aus dem Ofen','CroqueMonsieur':'Croque Monsieur in leicht',
      'KlossKohlrouladen':'Klöße mit Kohlrouladen-Pfanne','KlossGans':'Klöße mit Hähnchenkeule wie Gans','SpinatQuiche':'Spinat-Quiche mit Skyr-Teig','GefuellteZucchini':'Gefüllte Zucchini mit Hack und Käse'}
MENGE={'Quarkstollen':'1 Stollen, 16 Scheiben','FrankfurterKranz':'16 Stücke, Kranzform 24 cm','Tassenkuchen':'1 große Tasse','Spitzbuben':'ca. 30 Stück',
       'PrinzenrolleBowl':'1 Bowl, Glasform 15 × 10 cm','Zwetschgenkuchen':'20 Stücke, 1 Backblech 30 × 40 cm','Eiweissbrot':'1 Kastenform, 12 Scheiben','Kartoffelsuppe':'4 Teller',
       'Enchiladas':'4 Portionen à 2 Stück, Auflaufform','Fischstaebchen':'4 Portionen','CroqueMonsieur':'4 Stück','KlossKohlrouladen':'4 Portionen, 16 kleine Klöße',
       'KlossGans':'4 Portionen, 16 kleine Klöße','SpinatQuiche':'8 Stücke, Quicheform 26 cm','GefuellteZucchini':'4 Portionen'}
EMO={'Quarkstollen':'😍','FrankfurterKranz':'🤤','Tassenkuchen':'😋','Spitzbuben':'🥰','PrinzenrolleBowl':'🤤','Zwetschgenkuchen':'😍','Eiweissbrot':'😋','Kartoffelsuppe':'🤗',
     'Enchiladas':'🤤','Fischstaebchen':'😋','CroqueMonsieur':'😍','KlossKohlrouladen':'🥰','KlossGans':'😍','SpinatQuiche':'😋','GefuellteZucchini':'🤤'}
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
    posts.append(dict(key=key,text=text,fc=fc,media=URL.format(f'G106-{key}-ohneBox'),alt=NAME[key],kcal=k,suess=r['suess'],hashtags=len(r['tags'].split())))
json.dump(posts,open(f"{D}/out/sonntag_neu_posts.json","w"),ensure_ascii=False,indent=1)
print(len(posts),'ok')
