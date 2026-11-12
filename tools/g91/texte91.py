# -*- coding: utf-8 -*-
# G91 – Freitag 13.11.2026: Titel, 1. Kommentar, Posting-Plan, Texte (TXT + MD), freitag_posts.json
import json, os
from datetime import datetime, timedelta
import g91_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/G91-{}.jpg"
t0=datetime(2026,11,13,6,10); T_END=datetime(2026,11,13,20,45)
# Zeitfenster wie Mittwoch (Kev 10.11.: „lieber ab 6:10 bis 20:45“), 20 Beiträge (Kev 12.11.: „20 pro Tag“) gleichmäßig verteilt,
# auf volle 5 Minuten gerundet (Abstände 55–60 Minuten)
N_POSTS=len(G.R); SPAN=(T_END-t0).total_seconds()/60
OFFS=[int(round(i*SPAN/(N_POSTS-1)/5.0))*5 for i in range(N_POSTS)]
assert N_POSTS==20 and OFFS[0]==0 and OFFS[-1]==SPAN and all(45<=b-a<=50 for a,b in zip(OFFS,OFFS[1:])),OFFS
NAME={'MarmorBowl':'Marmorkuchen-Bowl nur für dich','Pide':'Pide mit Hack und Ei','Poffertjes':'Poffertjes mit Skyr','OfenOmelett':'Ofen-Omelett mit Schinken',
 'Milchreis':'Milchreis mit Zimt wie bei Oma','SmashWrap':'Smash-Burger-Wrap','HimbeerSkyr':'Vanille-Skyr-Kuchen mit Himbeerspiegel','Champignons':'Champignons mit Knoblauchsoße',
 'ApfelkuchenBowl':'Apfelkuchen-Bowl nur für dich','Rouladen':'Rinderrouladen wie bei Oma','FrankfurterKranz':'Frankfurter Kranz in leicht','Souvlaki':'Hähnchen-Souvlaki mit Tzatziki',
 'LebkuchenBlech':'Lebkuchen vom Blech','Reibekuchen':'Reibekuchen aus dem Ofen','Crepes':'Zimt-Crêpes','Schupfnudeln':'Schupfnudeln mit Sauerkraut',
 'Plaetzchen':'Ausstech-Plätzchen','Langos':'Langos ohne Fritteuse','Eierschecke':'Eierschecke in leicht','Gulasch':'Rindergulasch mit Kartoffeln'}
FORM={'Pide':'Backblech','OfenOmelett':'Auflaufform 20 × 30 cm','HimbeerSkyr':'Springform 20 cm','FrankfurterKranz':'Kranzform','LebkuchenBlech':'Backblech',
 'Reibekuchen':'Backblech','Plaetzchen':'Backblech','Eierschecke':'Springform 26 cm'}
EINZELN={'Pide','SmashWrap','Crepes','Plaetzchen','Langos','LebkuchenBlech'}   # einzelne Teile -> „Stück“, Kuchenstücke -> „Stücke“
assert set(NAME)=={r['key'] for r in G.R}
def portion_label(r):
    p=r['portion']
    for k in ('pro Stück','pro Portion','pro Glas','pro Teller'):
        if p.startswith(k): return k
    return 'pro Bowl'
def _anzahl_base(r):
    p=r['portion']; n=r['anzahl']
    if 'Bowl' in p: return '1 Portion, Glasform 15 × 10 cm'
    if p.startswith('pro Glas'): return f'{n} Gläser'
    if p.startswith('pro Teller'): return f'{n} Teller'
    if p.startswith('pro Portion'): return '1 Portion' if n==1 else f'{n} Portionen'
    return f'{n} Stück' if (r['key'] in EINZELN or n<12) else f'{n} Stücke'
def anzahl_label(r):
    f=FORM.get(r['key']); base=_anzahl_base(r)
    return f'{base}, {f}' if f else base
EMO=['🤤','😍','😋','🥰','🤗']
posts=[]
for i,r in enumerate(G.R):
    k,p,c,f=G.macros4(r); key=r['key']; n=i+1
    lab={'pro Stück':'pro Stück','pro Portion':'pro Portion','pro Glas':'pro Glas','pro Teller':'pro Teller','pro Bowl':'die ganze Bowl'}[portion_label(r)]
    title=f"{k} kcal {lab} {EMO[i%5]} Rezept im 1. Kommentar ⤵️"
    text=title+"\n\n"+r['tags']
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])
    if r['ex']: zut+="\n"+"\n".join(f"• {e}" for e in r['ex'])
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    fc=f"{NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({anzahl_label(r)}):\n{zut}\n\nSo geht's:\n{steps}\n\nNährwerte {portion_label(r)}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\n"
    if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
    fc+=f"Bleib satt! 💪\n\n{r['frage']}"
    assert '#' not in fc and 'abnehm' not in (text+fc).lower() and 'höflich' not in text.lower()
    dt=t0+timedelta(minutes=OFFS[i]); nt=len(r['tags'].split())
    assert nt==G.HASHTAG_SOLL[n] and r['tags'].split()[-1]=='#fitmitkev'
    posts.append(dict(n=n,key=key,date=dt.strftime('%Y-%m-%dT%H:%M:%S'),text=text,fc=fc,media=URL.format(key),alt=NAME[key],kcal=k,suess=r['suess'],hoeflich=False,
                      hashtags=nt,gruppe='A (2–3)' if nt<=3 else 'B (4–5)'))
ga=[p_ for p_ in posts if p_['gruppe'][0]=='A']; gb=[p_ for p_ in posts if p_['gruppe'][0]=='B']
assert len(ga)==len(gb)==10 and sum(p_['suess'] for p_ in ga)==sum(p_['suess'] for p_ in gb)==5
json.dump(posts,open(f"{D}/out/freitag_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/out/posting-plan-freitag.txt","w") as fh:
    fh.write("Posting-Plan Freitag 13.11.2026 – 20 Beiträge 6:10–20:45, alle 45–50 Minuten. NEU: alle Boards mit Box „So geht's“ (Rezept im Bild), ausführlich weiter im 1. Kommentar. Dazu 17:30 Mehrwert-Post „Was ein Wochenende kostet“.\n")
    fh.write("Keine Werbung, kein Höflich-Titel. Hashtag-Test, Gruppen wie am Mittwoch: Gruppe A = 2–3 Hashtags, Gruppe B = 4–5 (je 10 Beiträge, 5 süß + 5 herzhaft).\n\n")
    for p_ in posts:
        fh.write(f"{p_['n']:02d} · {p_['date'][11:16]} · {'süß ' if p_['suess'] else 'herz'} · {NAME[p_['key']]} · {p_['kcal']} kcal · {p_['hashtags']} Hashtags (Gruppe {p_['gruppe'][0]})\n")
with open(f"{D}/out/texte-freitag-20.txt","w") as fh, open(f"{D}/out/texte-freitag-20-klick.md","w") as md:
    md.write("# Texte Freitag 13.11.2026 (20 Beiträge)\n\n")
    for p_ in posts:
        fh.write(f"===== {p_['n']:02d} · {p_['date'][11:16]} · {NAME[p_['key']]}\n\nTITEL:\n{p_['text']}\n\n1. KOMMENTAR:\n{p_['fc']}\n\nBILD: {p_['media']}\n\n\n")
        md.write(f"## {p_['n']:02d} · {p_['date'][11:16]} · {NAME[p_['key']]}\n\n**Titel**\n\n```\n{p_['text']}\n```\n\n**1. Kommentar**\n\n```\n{p_['fc']}\n```\n\nBild: {p_['media']}\n\n")
print(len(posts)); [print(p_["n"],p_["date"][11:16],p_["text"].replace(chr(10)+chr(10),'  |  ')) for p_ in posts]
