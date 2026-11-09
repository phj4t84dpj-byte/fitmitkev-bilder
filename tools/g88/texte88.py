# -*- coding: utf-8 -*-
import json, os
from datetime import datetime, timedelta
import g88_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/G88-{}.jpg"
t0=datetime(2026,11,10,6,0); STEP=45
HOEFLICH={11,16}   # 1-basierte Beitragsnummern mit „Höfliche Menschen“-Titel (Test)
NAME={'BratapfelPorridge':'Bratapfel-Porridge','KoernerBroetchen':'Körnerbrötchen aus Skyr-Teig','Kaiserschmarrn':'Kaiserschmarrn aus dem Ofen',
 'LaugenBrezeln':'Laugenbrezeln aus Skyr-Teig','Apfeltaschen':'Apfeltaschen aus Skyr-Teig','KaeseSchinkenWaffeln':'Käse-Schinken-Waffeln',
 'KirschStreuselBowl':'Kirsch-Streusel-Bowl nur für dich','KaeseLauchSuppe':'Käse-Lauch-Suppe mit Hack','KokosMandelBowl':'Kokos-Mandel-Kuchen-Bowl nur für dich',
 'Hackbraten':'Hackbraten mit Kartoffelpüree','MandarinenSchmand':'Mandarinen-Schmand-Kuchen vom Blech','GefuelltePaprika':'Gefüllte Paprika mit Hack und Reis',
 'EierlikoerSkyrKuchen':'Eierlikör-Skyr-Kuchen','HaehnchenJaegersosse':'Hähnchen in Jägersoße mit Nudeln','Zupfkuchen':'Russischer Zupfkuchen',
 'CurrywurstAuflauf':'Currywurst-Auflauf mit Kartoffeln','MohnStreuselkuchen':'Mohn-Streuselkuchen vom Blech','ZuercherGeschnetzeltes':'Züricher Geschnetzeltes mit Reis',
 'ZimtschneckenSkyrKuchen':'Zimtschnecken-Skyr-Kuchen','Senfeier':'Senfeier mit Kartoffelpüree'}
def portion_label(r):
    p=r['portion']
    for k in ('pro Stück','pro Portion','pro Glas','pro Teller'):
        if p.startswith(k): return k
    return 'pro Bowl'
FORM={'KoernerBroetchen':'Backblech','Kaiserschmarrn':'Auflaufform 20 × 30 cm','LaugenBrezeln':'Backblech','Apfeltaschen':'Backblech','KaeseSchinkenWaffeln':'Waffeleisen',
 'Hackbraten':'Auflaufform 20 × 30 cm','MandarinenSchmand':'Blech 25 × 35 cm','GefuelltePaprika':'Auflaufform 25 × 35 cm','EierlikoerSkyrKuchen':'Springform 26 cm',
 'Zupfkuchen':'Springform 26 cm','CurrywurstAuflauf':'Auflaufform 20 × 30 cm','MohnStreuselkuchen':'Blech 25 × 35 cm','ZimtschneckenSkyrKuchen':'Springform 26 cm'}
def anzahl_label(r):
    p=r['portion']; n=r['anzahl']; f=FORM.get(r['key'])
    base=_anzahl_base(r)
    return f'{base}, {f}' if f else base
def _anzahl_base(r):
    p=r['portion']; n=r['anzahl']
    if 'Bowl' in p: return '1 Portion, Glasform 15 × 10 cm'
    if p.startswith('pro Glas'): return f'{n} Gläser'
    if p.startswith('pro Teller'): return f'{n} Teller'
    if p.startswith('pro Portion'): return f'{n} Portionen'
    return f'{n} Stück' if n<12 else f'{n} Stücke'
EMO=['🤤','😍','😋','🥰','🤗']
posts=[]
for i,r in enumerate(G.R):
    k,p,c,f=G.macros4(r); key=r['key']; n=i+1
    lab={'pro Stück':'pro Stück','pro Portion':'pro Portion','pro Glas':'pro Glas','pro Teller':'pro Teller','pro Bowl':'die ganze Bowl'}[portion_label(r)]
    if n in HOEFLICH: title=f"Höfliche Menschen bedanken sich 🤗 {k} kcal {lab}. Rezept im 1. Kommentar ⤵️"
    else: title=f"{k} kcal {lab} {EMO[i%5]} Rezept im 1. Kommentar ⤵️"
    text=title+"\n\n"+r['tags']
    zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])
    if r['ex']: zut+="\n"+"\n".join(f"• {e}" for e in r['ex'])
    steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
    fc=f"{NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({anzahl_label(r)}):\n{zut}\n\nSo geht's:\n{steps}\n\nNährwerte {portion_label(r)}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\n"
    if r['suess']: fc+="Schmeckt nach Sünde, zählt wie Salat 😉\n"
    fc+=f"Bleib satt! 💪\n\n{r['frage']}"
    dt=t0+timedelta(minutes=STEP*i)
    posts.append(dict(n=n,key=key,date=dt.strftime('%Y-%m-%dT%H:%M:%S'),text=text,fc=fc,media=URL.format(key),alt=NAME[key],kcal=k,suess=r['suess'],hoeflich=n in HOEFLICH))
json.dump(posts,open(f"{D}/out/dienstag_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/out/posting-plan-dienstag.txt","w") as fh:
    fh.write("Posting-Plan Dienstag 10.11.2026 – 20 Beiträge 6:00–20:15 alle 45 Minuten (Reset Tag 2: keine Werbung, Höflich-Titel nur bei 11 und 16)\n\n")
    for p_ in posts:
        fh.write(f"{p_['n']:02d} · {p_['date'][11:16]} · {'süß ' if p_['suess'] else 'herz'} · {NAME[p_['key']]} · {p_['kcal']} kcal{'  · HÖFLICH' if p_['hoeflich'] else ''}\n")
with open(f"{D}/out/texte-dienstag-20.txt","w") as fh, open(f"{D}/out/texte-dienstag-20-klick.md","w") as md:
    md.write("# Texte Dienstag 10.11.2026 (20 Beiträge)\n\n")
    for p_ in posts:
        fh.write(f"===== {p_['n']:02d} · {p_['date'][11:16]} · {NAME[p_['key']]}\n\nTITEL:\n{p_['text']}\n\n1. KOMMENTAR:\n{p_['fc']}\n\nBILD: {p_['media']}\n\n\n")
        md.write(f"## {p_['n']:02d} · {p_['date'][11:16]} · {NAME[p_['key']]}\n\n**Titel**\n\n```\n{p_['text']}\n```\n\n**1. Kommentar**\n\n```\n{p_['fc']}\n```\n\nBild: {p_['media']}\n\n")
print(len(posts)); [print(p_["n"],p_["date"][11:16],p_["text"].split(chr(10))[0]) for p_ in posts]
