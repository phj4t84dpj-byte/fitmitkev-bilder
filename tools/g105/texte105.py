# -*- coding: utf-8 -*-
# G105 – Samstag 28.11.2026: Texte für die 14 neuen Rezepte -> out/samstag_neu_posts.json
import json, os
import g105_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/{}.jpg"
NAME={'FantaKuchen':'Fanta-Kuchen vom Blech in leicht','Donauwelle':'Donauwelle vom Blech in leicht','ApfelkuchenBlech':'Versunkener Apfelkuchen vom Blech','Amerikaner':'Amerikaner ohne Butter',
      'KinderBuenoBowl':'Kinder-Bueno-Bowl nur für dich','Shakshuka':'Shakshuka in leicht','Ofengemuese':'Ofengemüse mit Halloumi vom Blech','Carbonara':'Spaghetti Carbonara in leicht',
      'Huehnersuppe':'Hühnersuppe wie bei Oma','Bauerntopf':'Bauerntopf mit Hack','TortelliniAuflauf':'Tortellini-Auflauf','KlossGefuellt':'Gefüllte Klöße mit Hack und Rahm-Möhren',
      'KlossSoss':'Kloß mit Soß und Schweinebraten wie in Franken','Ofenkartoffel':'Ofenkartoffeln mit Kräuterquark'}
MENGE={'FantaKuchen':'20 Stücke, 1 Backblech 30 × 40 cm','Donauwelle':'20 Stücke, 1 Backblech 30 × 40 cm','ApfelkuchenBlech':'20 Stücke, 1 Backblech 30 × 40 cm','Amerikaner':'12 Stück',
       'KinderBuenoBowl':'1 Bowl, Glasform 15 × 10 cm','Shakshuka':'2 Portionen','Ofengemuese':'4 Portionen, 1 Backblech','Carbonara':'4 Portionen','Huehnersuppe':'4 Teller',
       'Bauerntopf':'4 Portionen','TortelliniAuflauf':'4 Portionen, Auflaufform ca. 30 × 20 cm','KlossGefuellt':'4 Portionen, 16 kleine Klöße','KlossSoss':'4 Portionen','Ofenkartoffel':'4 Portionen'}
EMO={'FantaKuchen':'😍','Donauwelle':'🤤','ApfelkuchenBlech':'😋','Amerikaner':'🥰','KinderBuenoBowl':'🤤','Shakshuka':'😋','Ofengemuese':'🥰','Carbonara':'🤤','Huehnersuppe':'🤗',
     'Bauerntopf':'😍','TortelliniAuflauf':'😋','KlossGefuellt':'🥰','KlossSoss':'😍','Ofenkartoffel':'🤗'}
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
    posts.append(dict(key=key,text=text,fc=fc,media=URL.format(f'G105-{key}-ohneBox'),alt=NAME[key],kcal=k,suess=r['suess'],hashtags=len(r['tags'].split())))
json.dump(posts,open(f"{D}/out/samstag_neu_posts.json","w"),ensure_ascii=False,indent=1)
print(len(posts),'ok')
