# -*- coding: utf-8 -*-
# ESN-Rezepte 19.11.–2.12.: Titel + 1. Kommentar mit ESN-Zeile je Datum -> out/esn_rezepte_posts.json + out/texte-esn-rezepte.txt
import json, os
import gesn_data as G
D=os.path.dirname(os.path.abspath(__file__)); os.makedirs(f"{D}/out",exist_ok=True)
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/boards/ESN-{}-ohneBox.jpg"
LINK="esn.com/instagram/FITMITKEV/aktion"
NAME={'SchokoMousseESN':'Schoko-Mousse mit 5 Zutaten','TiramisuBowlESN':'Tiramisu-Bowl nur für dich','BratapfelQuarkESN':'Bratapfel-Dessert im Glas',
      'SchwarzwaelderGlasESN':'Schwarzwälder Kirsch im Glas','VanillepuddingPflaumenESN':'Vanillepudding mit Zimtpflaumen','SchokoKugelnESN':'Schoko-Kugeln ohne Backen',
      'SpekulatiusMousseESN':'Spekulatius-Mousse','ErdbeerBowlESN':'Erdbeer-Quark-Bowl nur für dich','ZimtschneckenOatsESN':'Zimtschnecken-Overnight-Oats',
      'DarkSchokoPuddingESN':'Dunkler Schokopudding','SpekulatiusTiramisuESN':'Spekulatius-Tiramisu im Glas','ErdbeerCheesecakeGlasESN':'Erdbeer-Cheesecake im Glas',
      'ZimtGriessbreiESN':'Zimt-Grießbrei wie bei Oma','SchokoEisESN':'Schoko-Eis aus Hüttenkäse'}
NEU={'Vanilla Speculoos','Cinnamon Cereal','Strawberry Cream','Ultra Dark Chocolate'}
def sorte(r):
    s=r['sorte']
    if s=='Ultra Dark Chocolate': return 'Ultra Dark Chocolate (neue Black Edition)'
    return s+(' (neu)' if s in NEU else '')
def zeile(datum, zeit, r, idx):
    s=sorte(r)
    if datum<'2026-11-22': return f"Werbung: Als Proteinpulver nehme ich hier das Designer Protein von ESN in {s}."
    if datum=='2026-11-22' and zeit<'12:00':
        return f"Werbung: Heute um 12 Uhr startet die ESN Black Week mit bis zu -70 %. Für dieses Rezept nehme ich das Designer Protein in {s}. Ab 12 Uhr Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {LINK} (bis Mi 2.12., 17:30 Uhr)"
    if datum=='2026-11-27':
        return f"Werbung: Black Friday bei ESN: In der Black Week gibt es bis zu -70 %. Für dieses Rezept nehme ich das Designer Protein in {s}. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {LINK} (bis Mi 2.12., 17:30 Uhr)"
    if datum=='2026-12-02':
        return f"Werbung: Letzter Tag! Die ESN Black Week mit bis zu -70 % endet heute um 17:30 Uhr. Für dieses Rezept nehme ich das Designer Protein in {s}. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {LINK}"
    V=[f"Werbung: Für dieses Rezept nehme ich das Designer Protein von ESN in {s}. Gerade ist Black Week mit bis zu -70 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {LINK} (bis Mi 2.12., 17:30 Uhr)",
       f"Werbung: Nur einmal im Jahr: ESN Black Week mit bis zu -70 %. Hier holen sich viele Stammkunden ihren Vorrat. Mein Proteinpulver für dieses Rezept: Designer Protein in {s}. Rabatte mit Code FITMITKEV sichern 👉 {LINK} (bis Mi 2.12., 17:30 Uhr)",
       f"Werbung: Die beste Aktion des Jahres läuft: ESN Black Week mit bis zu -70 %. In diesem Rezept steckt das Designer Protein in {s}. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {LINK} (bis Mi 2.12., 17:30 Uhr)"]
    return V[idx%3]
def anz(r):
    p=r['portion']; n=r['anzahl']
    if 'Bowl' in p: return '1 Portion, Glasform 15 × 10 cm'
    if p.startswith('pro Glas'): return f'{n} Gläser'
    if p.startswith('pro Kugel'): return f'{n} Kugeln'
    if p.startswith('pro Portion'): return f'{n} Portionen'
    return f'{n} Stück'
LAB={'pro Glas':'pro Glas','pro Kugel':'pro Kugel','pro Portion':'pro Portion','die ganze Bowl':'die ganze Bowl'}
NL={'pro Glas':'pro Glas','pro Kugel':'pro Kugel','pro Portion':'pro Portion','die ganze Bowl':'pro Bowl'}
EMO=['🤤','😍','😋','🥰','🤗']
BY={r['key']:r for r in G.R}
posts=[]; idx=0
for di,(datum,a,b) in enumerate(G.PLAN):
    for zeit,key in (('06:10',a),('13:00',b)):
        r=BY[key]; k,p,c,f=G.macros4(r)
        text=f"{k} kcal {LAB[r['portion']]} {EMO[idx%5]} Rezept im 1. Kommentar ⤵️\n\n{r['tags']}"
        zut="\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten'])
        steps="\n".join(f"{j+1}. {s}" for j,s in enumerate(r['schritte']))
        fc=(f"{NAME[key]}\n\n{r['intro'].format(k=k,p=p)}\n\nZutaten ({anz(r)}):\n{zut}\n\nSo geht's:\n{steps}\n\n"
            f"Nährwerte {NL[r['portion']]}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\n"
            f"Schmeckt nach Sünde, zählt wie Salat 😉\nBleib satt! 💪\n\n{r['frage']}\n\n{zeile(datum,zeit,r,idx)}")
        assert 'abnehm' not in (text+fc).lower() and 'Günstiger' not in fc and fc.count('Werbung:')==1
        if datum>='2026-11-22' and not (datum=='2026-11-22' and zeit<'12:00'): assert LINK in fc
        posts.append(dict(datum=datum,zeit=zeit,key=key,date=f"{datum}T{zeit}:00",text=text,fc=fc,media=URL.format(key),alt=NAME[key],kcal=k,sorte=r['sorte']))
        idx+=1
json.dump(posts,open(f"{D}/out/esn_rezepte_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/out/texte-esn-rezepte.txt","w") as fh:
    fh.write("ESN-Rezepte 19.11.–2.12.2026 – je 6:10 und 13:00 Uhr, alle ohne Box, Board ohne Marke, ESN-Zeile nur im 1. Kommentar\n\n")
    for p_ in posts:
        fh.write(f"===== {p_['datum']} · {p_['zeit']} · {NAME[p_['key']]} ({p_['sorte']})\n\nTITEL:\n{p_['text']}\n\n1. KOMMENTAR:\n{p_['fc']}\n\n\n")
print(len(posts))
for p_ in posts[:1]+posts[6:8]+posts[16:18]+posts[-2:]: print('---',p_['datum'],p_['zeit'],p_['key']); print(p_['fc'].split('\n\n')[-1])
