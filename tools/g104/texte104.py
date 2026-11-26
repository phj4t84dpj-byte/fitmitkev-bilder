# -*- coding: utf-8 -*-
# G104 – Freitag 27.11.2026: Texte für die 14 neuen Rezepte -> out/freitag_neu_posts.json
import json, os
import g104_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NAME={'OmelettRoellchen':'Omelett-Röllchen mit Spinat und Feta','ChiliKartoffeln':'Chili-Cheese-Kartoffeln vom Blech','HaehnchenBrokkoliAuflauf':'Hähnchen-Brokkoli-Auflauf',
      'Gruenkohl':'Grünkohl mit Mettwürstchen und Kartoffeln','KlossStroganoff':'Klöße mit Boeuf Stroganoff','Backfisch':'Backfisch-Brötchen aus dem Ofen',
      'Hackbaellchen':'Hackbällchen in Tomatensoße mit Reis','KlossSchweinefilet':'Klöße mit Schweinefilet in Pfefferrahm','KlossMeerrettich':'Klöße mit Tafelspitz und Meerrettichsoße',
      'Butterkuchen':'Butterkuchen vom Blech in leicht','QuarkGugelhupf':'Quark-Gugelhupf','ToffifeeBowl':'Toffifee-Bowl nur für dich','Germknoedel':'Germknödel mit Vanillesoße',
      'SchokokussTorte':'Schokokuss-Torte ohne Backen'}
MENGE={'OmelettRoellchen':'2 Portionen','ChiliKartoffeln':'4 Portionen, 8 Kartoffelhälften','HaehnchenBrokkoliAuflauf':'4 Portionen, Auflaufform ca. 30 × 20 cm','Gruenkohl':'4 Portionen',
       'KlossStroganoff':'4 Portionen','Backfisch':'4 Brötchen','Hackbaellchen':'4 Portionen, 24 Bällchen','KlossSchweinefilet':'4 Portionen','KlossMeerrettich':'4 Portionen',
       'Butterkuchen':'20 Stücke, 1 Backblech 30 × 40 cm','QuarkGugelhupf':'16 Stücke, Gugelhupfform 22 cm','ToffifeeBowl':'1 Bowl, Glasform 15 × 10 cm','Germknoedel':'4 Knödel',
       'SchokokussTorte':'12 Stücke, Springform 24 cm'}
EMO={'OmelettRoellchen':'😋','ChiliKartoffeln':'🤤','HaehnchenBrokkoliAuflauf':'🥰','Gruenkohl':'😍','KlossStroganoff':'🤤','Backfisch':'😋','Hackbaellchen':'🥰',
     'KlossSchweinefilet':'😍','KlossMeerrettich':'🤗','Butterkuchen':'😍','QuarkGugelhupf':'🤗','ToffifeeBowl':'🤤','Germknoedel':'🥰','SchokokussTorte':'😋'}
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
    posts.append(dict(key=key,text=text,fc=fc,media=URL.format(f'G104-{key}-ohneBox'),alt=NAME[key],kcal=k,suess=r['suess'],hashtags=len(r['tags'].split())))
json.dump(posts,open(f"{D}/out/freitag_neu_posts.json","w"),ensure_ascii=False,indent=1)
print(len(posts),'ok')
