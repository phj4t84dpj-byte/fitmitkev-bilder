# -*- coding: utf-8 -*-
# G93N – Sonntag 15.11.2026: 6 neue Beiträge auf den Plätzen 9, 10, 11, 15, 17, 19 des Sonntags (gleiche Uhrzeiten wie G93)
import json, os
import g93n_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/G93N-{}.jpg"
SO={p['n']:p for p in json.load(open('/home/claude/fitmitkev-bilder/tools/g93/sonntag_posts.json'))}
NAME={'HanutaBowl':'Hanuta-Bowl nur für dich','BigMacSalat':'Big-Mac-Salat im Glas','SpekKirschGlas':'Spekulatius-Kirsch im Glas',
      'BiscoffBowl':'Lotus-Biscoff-Bowl nur für dich','BratapfelSpekGlas':'Bratapfel-Spekulatius im Glas','MilchschnitteBowl':'Milchschnitte-Bowl nur für dich'}
EMO={9:'🥰',10:'🤗',11:'🤤',15:'😍',17:'😋',19:'🤤'}
posts=[]
for r in G.R:
    n=r['n']; k,p,c,f=G.macros4(r); key=r['key']
    bowl='Bowl' in r['portion']
    title=f"{k} kcal {'die ganze Bowl' if bowl else 'pro Glas'} {EMO[n]} Rezept im 1. Kommentar ⤵️"
    text=title+"\n\n"+r['tags']
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])
    if r['ex']: zut+="\n"+"\n".join(f"• {e}" for e in r['ex'])
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    anz='1 Portion, Glasform 15 × 10 cm' if bowl else f"{r['anzahl']} Gläser"
    fc=f"{NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({anz}):\n{zut}\n\nSo geht's:\n{steps}\n\n"
    fc+=f"Nährwerte {'pro Bowl' if bowl else 'pro Glas'}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\n"
    if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
    fc+=f"Bleib satt! 💪\n\n{r['frage']}"
    if r.get('buch'): fc+="\n\n"+r['buch']
    assert '#' not in fc and 'abnehm' not in (text+fc).lower()
    box=n not in G.OHNE_BOX; nt=len(r['tags'].split()); assert nt==G.HASHTAG_SOLL[n]
    assert SO[n]['box']==box and SO[n]['suess']==r['suess']
    posts.append(dict(n=n,key=key,date=SO[n]['date'],text=text,fc=fc,media=URL.format(key if box else key+'-ohneBox'),alt=NAME[key],box=box,kcal=k,suess=r['suess'],
                      hashtags=nt,gruppe='A (2–3)' if nt<=3 else 'B (4–5)',ersetzt=SO[n]['key']))
json.dump(posts,open(f"{D}/out/sonntag_neu_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/out/texte-sonntag-neu.txt","w") as fh:
    for p_ in posts: fh.write(f"===== {p_['n']:02d} · {p_['date'][11:16]} · {p_['alt']}\n\nTITEL:\n{p_['text']}\n\n1. KOMMENTAR:\n{p_['fc']}\n\nBILD: {p_['media']}\n\n\n")
for p_ in posts: print(p_['n'],p_['date'][11:16],p_['alt'],'| ersetzt',p_['ersetzt'],'|',p_['text'].split(chr(10))[0])
