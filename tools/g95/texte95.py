# -*- coding: utf-8 -*-
# G95 – Dienstag 17.11.2026: Titel, 1. Kommentar, Posting-Plan, Texte (TXT + MD), dienstag_posts.json
import json, os
from datetime import datetime, timedelta
import g95_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/G95-{}.jpg"
NAME={'BratapfelPorridge':'Bratapfel-Porridge','Laugenbroetchen':'Laugenbrötchen aus Skyr-Teig','Elisenlebkuchen':'Elisenlebkuchen ohne Mehl','KaeseSchinkenWaffeln':'Käse-Schinken-Waffeln',
 'ApfelstrudelTiramisu':'Apfelstrudel-Tiramisu im Glas','Moussaka':'Moussaka in leicht','KirschStreuselBowl':'Kirsch-Streusel-Bowl nur für dich','HaehnchenNudelauflauf':'Cremiger Hähnchen-Nudelauflauf',
 'BrownieBowl':'Brownie-Bowl nur für dich','CordonBleuAuflauf':'Cordon-Bleu-Auflauf','HuettenEis':'Spekulatius-Eis aus Hüttenkäse','Schichtsalat':'Schichtsalat im Glas',
 'BenjaminBowl':'Benjamin-Blümchen-Bowl nur für dich','CurrywurstAuflauf':'Currywurst-Auflauf mit Kartoffeln','Haferplaetzchen':'Haferflocken-Plätzchen wie bei Oma','Nuggets':'Chicken Nuggets aus dem Ofen',
 'ApfelStreusel':'Apfel-Streusel-Skyr-Kuchen vom Blech','GefuelltePaprika':'Gefüllte Paprika wie bei Oma','RoteGruetze':'Rote Grütze mit Vanillesoße','SalamiPizza':'Salami-Pizza aus Skyr-Teig'}
FORM={'Laugenbroetchen':'Backblech','Elisenlebkuchen':'Backblech','Moussaka':'Auflaufform 20 × 30 cm','HaehnchenNudelauflauf':'Auflaufform 20 × 30 cm','CurrywurstAuflauf':'Auflaufform 20 × 30 cm',
 'Nuggets':'Backblech','GefuelltePaprika':'Auflaufform 25 × 35 cm','SalamiPizza':'je Ø 22 cm'}
EINZELN={'Laugenbroetchen','Elisenlebkuchen','KaeseSchinkenWaffeln'}
def portion_label(r):
    p=r['portion']
    for k in ('pro Stück','pro Portion','pro Glas','pro Teller','pro Pizza','pro Scheibe','pro Kugel','pro Waffel'):
        if p.startswith(k): return k
    return 'pro Bowl'
def _anzahl_base(r):
    p=r['portion']; n=r['anzahl']
    if 'Bowl' in p: return '1 Portion, Glasform 15 × 10 cm'
    if p.startswith('pro Glas'): return f'{n} Gläser'
    if p.startswith('pro Teller'): return f'{n} Teller'
    if p.startswith('pro Pizza'): return f'{n} Pizzen'
    if p.startswith('pro Scheibe'): return f'1 Zopf, {n} Scheiben' if r['key']=='Hefezopf' else f'{n} Scheiben'
    if p.startswith('pro Waffel'): return f'{n} Waffeln'
    if p.startswith('pro Kugel'): return f'{n} Kugeln'
    if p.startswith('pro Portion'): return '1 Portion' if n==1 else f'{n} Portionen'
    return f'{n} Stück' if (r['key'] in EINZELN or n<12) else f'{n} Stücke'
def anzahl_label(r):
    f=FORM.get(r['key']); base=_anzahl_base(r)
    return f'{base}, {f}' if f else base
EMO=['🤤','😍','😋','🥰','🤗']
posts=[]
for i,r in enumerate(G.R):
    k,p,c,f=G.macros4(r); key=r['key']; n=i+1
    lab={'pro Stück':'pro Stück','pro Portion':'pro Portion','pro Glas':'pro Glas','pro Teller':'pro Teller','pro Pizza':'pro Pizza','pro Scheibe':'pro Scheibe','pro Kugel':'pro Kugel','pro Waffel':'pro Waffel','pro Bowl':'die ganze Bowl'}[portion_label(r)]
    title=f"{k} kcal {lab} {EMO[i%5]} Rezept im 1. Kommentar ⤵️"
    text=title+"\n\n"+r['tags']
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])
    if r['ex']: zut+="\n"+"\n".join(f"• {e}" for e in r['ex'])
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    fc=f"{NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({anzahl_label(r)}):\n{zut}\n\nSo geht's:\n{steps}\n\n"
    fc+=f"Nährwerte {portion_label(r)}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\n"
    if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
    fc+=f"Bleib satt! 💪\n\n{r['frage']}"
    if r.get('hinweis'): fc+="\n\n"+r['hinweis']
    assert 'esn' not in fc.lower()
    assert '#' not in fc.replace('📖','') and 'abnehm' not in (text+fc).lower() and 'höflich' not in text.lower()
    dt=datetime.strptime('2026-11-17 '+G.ZEITEN[i],'%Y-%m-%d %H:%M'); nt=len(r['tags'].split())
    assert nt==G.HASHTAG_SOLL[n] and r['tags'].split()[-1]=='#fitmitkev'
    box=n not in G.OHNE_BOX
    posts.append(dict(n=n,key=key,date=dt.strftime('%Y-%m-%dT%H:%M:%S'),text=text,fc=fc,media=URL.format(key if box else key+'-ohneBox'),alt=NAME[key],box=box,kcal=k,suess=r['suess'],hoeflich=False,
                      hashtags=nt,gruppe='A (2–3)' if nt<=3 else 'B (4–5)',vorhanden=r.get('vorhanden'),buch=bool(r.get('hinweis'))))
ga=[p_ for p_ in posts if p_['gruppe'][0]=='A']; gb=[p_ for p_ in posts if p_['gruppe'][0]=='B']
assert len(ga)==len(gb)==10 and sum(p_['suess'] for p_ in ga)==sum(p_['suess'] for p_ in gb)==5
ob=[p_ for p_ in posts if not p_['box']]; assert len(ob)==10 and sum(p_['suess'] for p_ in ob)==5 and sum(p_['hashtags']<=3 for p_ in ob)==5
json.dump(posts,open(f"{D}/out/dienstag_posts.json","w"),ensure_ascii=False,indent=1)
neu=[p_ for p_ in posts if not p_['vorhanden']]
json.dump(neu,open(f"{D}/out/dienstag_neu_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/out/posting-plan-dienstag.txt","w") as fh:
    fh.write("Posting-Plan Dienstag 17.11.2026 – 20 Rezept-Plätze 6:10–20:45 (Platz 18 um 21:30), dazu 17:30 Mehrwert-Post „So viel Eiweiß steckt in deinem Frühstück“ und 19:15 Buch-Beitrag „Eure Fragen zu den Büchern“.\n")
    fh.write("6 Plätze schon angelegt (am 14.11. von Montag verschoben). Box halb/halb: 10 mit, 10 ohne (je 5 süß + 5 herzhaft). Keine ESN-Zeile, kein Höflich-Titel. Buch-Zeile unter 3 (Elisenlebkuchen) und 8 (Hähnchen-Nudelauflauf).\n\n")
    for p_ in sorted(posts,key=lambda x:x['date']):
        fh.write(f"{p_['n']:02d} · {p_['date'][11:16]} · {'süß ' if p_['suess'] else 'herz'} · {NAME[p_['key']]} · {p_['kcal']} kcal · {p_['hashtags']} Hashtags (Gruppe {p_['gruppe'][0]}) · {'mit Box' if p_['box'] else 'ohne Box'}{' · BUCH' if p_['buch'] else ''}{' · schon angelegt' if p_['vorhanden'] else ''}\n")
with open(f"{D}/out/texte-dienstag.txt","w") as fh:
    for p_ in neu:
        fh.write(f"===== {p_['n']:02d} · {p_['date'][11:16]} · {NAME[p_['key']]}\n\nTITEL:\n{p_['text']}\n\n1. KOMMENTAR:\n{p_['fc']}\n\nBILD: {p_['media']}\n\n\n")
print(len(neu)); [print(p_["n"],p_["date"][11:16],p_["text"].replace(chr(10)+chr(10),'  |  ')) for p_ in neu]
