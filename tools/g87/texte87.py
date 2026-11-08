# -*- coding: utf-8 -*-
import json, csv, os
from datetime import datetime, timedelta
import g87_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/G87-{}.jpg"
t0=datetime(2026,11,9,6,0)
P=' Rezept im 1. Kommentar ⤵️'
HASH={'SpekOats':'#overnightoats #spekulatius #frühstück #lecker','Quarkbroetchen':'#brötchen #backen #ohnehefe #lecker',
 'ZimtschneckenPancakes':'#pancakes #zimtschnecken #frühstück #lecker','Pizzabroetchen':'#pizzabrötchen #backen #skyr #lecker',
 'ApfelQuarkbaellchen':'#quarkbällchen #weihnachtsmarkt #skyr #lecker','LasagneSuppe':'#lasagne #suppe #food #lecker',
 'NusseckenBowl':'#nussecken #bowl #backen #lecker','CordonBleuAuflauf':'#cordonbleu #auflauf #food #lecker',
 'BratapfelSkyrKuchen':'#kuchen #bratapfel #zuckerfrei #backen','GyrosBowl':'#gyros #bowl #food #lecker',
 'BienenstichBowl':'#bienenstich #bowl #backen #lecker','CheeseburgerAuflauf':'#cheeseburger #auflauf #food #lecker',
 'SchwarzwaelderSkyr':'#kuchen #schwarzwälderkirsch #zuckerfrei #backen','LaugenKnoten':'#laugengebäck #backen #ohnehefe #lecker',
 'BrownieKaesekuchen':'#kuchen #brownie #zuckerfrei #backen'}
NAME={'SpekOats':'Spekulatius-Overnight-Oats','Quarkbroetchen':'Quarkbrötchen wie vom Bäcker','ZimtschneckenPancakes':'Zimtschnecken-Pancakes',
 'Pizzabroetchen':'Pizzabrötchen aus Skyr-Teig','ApfelQuarkbaellchen':'Apfel-Quarkbällchen aus dem Ofen','LasagneSuppe':'Lasagne-Suppe aus einem Topf',
 'NusseckenBowl':'Nussecken-Bowl nur für dich','CordonBleuAuflauf':'Cordon-Bleu-Auflauf','BratapfelSkyrKuchen':'Bratapfel-Skyr-Kuchen',
 'GyrosBowl':'Gyros-Bowl nur für dich','BienenstichBowl':'Bienenstich-Bowl nur für dich','CheeseburgerAuflauf':'Cheeseburger-Auflauf',
 'SchwarzwaelderSkyr':'Schwarzwälder Skyr-Kuchen','LaugenKnoten':'Laugenknoten mit Käsefüllung','BrownieKaesekuchen':'Brownie-Käsekuchen'}
def portion_label(r):
    p=r['portion']
    if p.startswith('pro Stück'): return 'pro Stück'
    if p.startswith('pro Portion'): return 'pro Portion'
    if p.startswith('pro Glas'): return 'pro Glas'
    if p.startswith('pro Teller'): return 'pro Teller'
    return 'pro Bowl'
def anzahl_label(r):
    p=r['portion']; n=r['anzahl']
    if 'Bowl' in p: return '1 Portion, Glasform 15 × 10 cm'
    if p.startswith('pro Glas'): return f'{n} Gläser'
    if p.startswith('pro Teller'): return f'{n} Teller'
    if p.startswith('pro Portion'): return f'{n} Portionen'
    return f'{n} Stück' if n<12 else f'{n} Stücke'
posts=[]
for i,r in enumerate(G.R):
    k,p,c,f=G.macros4(r); key=r['key']
    EMO=['🤤','😍','🤗','😋','🥰']
    lab={'pro Stück':'pro Stück','pro Portion':'pro Portion','pro Glas':'pro Glas','pro Teller':'pro Teller','pro Bowl':'die ganze Bowl'}[portion_label(r)]
    if (i+1)%3==0: title=f"Höfliche Menschen bedanken sich 🤗 {k} kcal {lab}. Rezept im 1. Kommentar ⤵️"
    else: title=f"{k} kcal {lab} {EMO[i%5]} Rezept im 1. Kommentar ⤵️"
    text=title+"\n\n"+HASH[key]
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])
    if r['ex']: zut+="\n"+"\n".join(f"• {e}" for e in r['ex'])
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    fc=f"{NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({anzahl_label(r)}):\n{zut}\n\nSo geht's:\n{steps}\n\nNährwerte {portion_label(r)}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\n"
    if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
    fc+=f"Bleib satt! 💪\n\n{r['frage']}"
    dt=t0+timedelta(hours=i)
    posts.append(dict(n=i+1,key=key,date=dt.strftime('%Y-%m-%dT%H:%M:%S'),text=text,fc=fc,media=URL.format(key),alt=NAME[key],kcal=k,suess=r['suess']))
json.dump(posts,open(f"{D}/out/montag_posts.json","w"),ensure_ascii=False,indent=1)
# Plan
with open(f"{D}/out/posting-plan-montag.txt","w") as fh:
    fh.write("Posting-Plan Montag 09.11.2026 – 15 Beiträge stündlich, Reset-Tag (keine Werbung, keine Höflich-Titel, kein ESN)\n\n")
    for p_ in posts:
        fh.write(f"{p_['n']:02d} · {p_['date'][11:16]} · {'süß ' if p_['suess'] else 'herz'} · {NAME[p_['key']]} · {p_['kcal']} kcal\n")
# Texte
with open(f"{D}/out/texte-montag-15.txt","w") as fh, open(f"{D}/out/texte-montag-15-klick.md","w") as md:
    md.write("# Texte Montag 09.11.2026 (15 Beiträge)\n\n")
    for p_ in posts:
        fh.write(f"===== {p_['n']:02d} · {p_['date'][11:16]} · {NAME[p_['key']]}\n\nTITEL:\n{p_['text']}\n\n1. KOMMENTAR:\n{p_['fc']}\n\nBILD: {p_['media']}\n\n\n")
        md.write(f"## {p_['n']:02d} · {p_['date'][11:16]} · {NAME[p_['key']]}\n\n**Titel**\n\n```\n{p_['text']}\n```\n\n**1. Kommentar**\n\n```\n{p_['fc']}\n```\n\nBild: {p_['media']}\n\n")
# CSV im Metricool-Format (Kopfzeile wie bisher: Text, Date, Time, Draft, Facebook, ..., Picture Url 1, First Comment Text)
hdr=open(f"{D}/metricool_header.txt").read().strip().split(",") if os.path.exists(f"{D}/metricool_header.txt") else None
print(len(posts)); [print(p_["n"],p_["text"].replace(chr(10)," | ")) for p_ in posts]
