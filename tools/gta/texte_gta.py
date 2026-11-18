# -*- coding: utf-8 -*-
# GTA-6-Tag Do 19.11.2026: Titel, 1. Kommentar, Posting-Plan, fertige Metricool-Daten (out/_sched_gta.json)
import json, os
import gta_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f'{D}/out',exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/GTA-{}-Gamer.jpg"
EMO=['🤤','😍','😋','🥰','🤗']
out=[]; sched=[]
for i,r in enumerate(G.R):
    k,p,c,f=G.macros4(r); key=r['key']; t,nl=G.LAB[key]; zeit=G.ZEITEN[i]
    pre='Heute erscheint GTA 6 🎮' if zeit<'12:00' else 'GTA 6 ist da 🎮'
    text=f"{pre} {k} kcal {t} {EMO[i%5]} Rezept im 1. Kommentar ⤵️\n\n{r['tags']}"
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])+("\n"+"\n".join(f"• {e}" for e in r['ex']) if r['ex'] else '')
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    fc=f"{G.NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({G.FORM[key]}):\n{zut}\n\nSo geht's:\n{steps}\n\nNährwerte {nl}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\n"
    if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
    fc+=f"Bleib satt! 💪\n\n{r['frage']}"
    low=(text+fc).lower()
    assert 'abnehm' not in low and ' esn' not in low and 'höflich' not in low and '#' not in fc, key
    date=f"2026-11-19T{zeit}:00"
    out.append(dict(n=i+1,key=key,zeit=zeit,text=text,fc=fc,media=URL.format(key),alt=G.NAME[key],kcal=k,suess=r['suess'],hook=r['hook']))
    sched.append(dict(n=i+1,key=key,date=date,info={"autoPublish":True,"draft":False,"firstCommentText":fc,"hasNotReadNotes":False,"media":[URL.format(key)],
        "mediaAltText":[G.NAME[key]],"providers":[{"network":"facebook"}],"publicationDate":{"dateTime":date,"timezone":"Europe/Berlin"},"shortener":False,
        "smartLinkData":{"ids":[]},"text":text,"facebookData":{"type":"POST"}}))
json.dump(out,open(f'{D}/out/gta_posts.json','w'),ensure_ascii=False,indent=1)
json.dump(sched,open(f'{D}/out/_sched_gta.json','w'),ensure_ascii=False,indent=1)
with open(f'{D}/out/texte-gta.txt','w') as fh:
    for o in out: fh.write(f"===== {o['n']:02d} · {o['zeit']} · {o['alt']} · Hook „{o['hook']}“\n\nTITEL:\n{o['text']}\n\n1. KOMMENTAR:\n{o['fc']}\n\nBILD: {o['media']}\n\n\n")
with open(f'{D}/out/posting-plan-gta.txt','w') as fh:
    fh.write("Posting-Plan Donnerstag 19.11.2026 – GTA-6-Tag im Gamer-Look: 19 Rezepte + 6:10 und 13:00 ESN-Rezepte (bleiben, heller Look) + 17:30 Vergleichs-Beitrag = 22 Beiträge.\n\n")
    rows=[(o['zeit'],f"{o['n']:02d} · {'süß ' if o['suess'] else 'herz'} · {o['alt']} · {o['kcal']} kcal · Hook „{o['hook']}“") for o in out]+[(z,'FEST · '+t) for z,t in G.FEST.items()]
    for z,t in sorted(rows): fh.write(f"{z} · {t}\n")
print(len(out)); [print(o['n'],o['zeit'],o['text'].split(chr(10))[0]) for o in out]
