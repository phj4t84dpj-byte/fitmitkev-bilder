# -*- coding: utf-8 -*-
import json, os
D=os.path.dirname(os.path.abspath(__file__))
L="esn.com/instagram/FITMITKEV/aktion"; BIS="(bis Mi 2.12., 17:30 Uhr)"
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/esn/posts/{}.jpg"
P=[
("2026-11-23","12:00","ESN-P2-Morgen","Mein Frühstück unterwegs",
"Werbung\n\nMein Frühstück unterwegs: 2 Minuten statt Bäcker ☕\n\nCoffee to go mit Croissant: ca. 450 kcal und nur 10 g Eiweiß.\nMein Protein-Kaffee mit Milch: ca. 230 kcal und 30 g Eiweiß.\n\nHalb so viele Kalorien, dreimal so viel Eiweiß.\n\nWas gibt's bei dir morgens? ☕🥐",
f"Werbung: Den Protein-Kaffee (Flexpresso) gibt es gerade in der ESN Black Week mit -25 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-24","12:00","ESN-P3-Riegel","Schokoriegel oder Proteinriegel",
"Werbung\n\nSchokoriegel oder Proteinriegel? 🍫\n\nSchokoriegel (50 g): ca. 240 kcal, 25 g Zucker, 3 g Eiweiß. Das sind 8 Stück Würfelzucker.\nDesigner Bar (45 g): ca. 200 kcal, 2 g Zucker, 14 g Eiweiß. Weich, mit Füllung.\n\nSüß darf sein. Nur eben ohne Zuckerbombe.\n\nTeam Schokoriegel oder Team Proteinriegel? 😄",
f"Werbung: Die Designer Bar gibt es gerade in der ESN Black Week mit -30 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-25","12:00","ESN-P4-NeueSorten","3 neue Sorten, 3 Rezepte",
"Werbung\n\nNeu bei ESN: 3 neue Sorten, und ich habe direkt 3 Rezepte daraus gemacht 😍\n\n🍪 Vanilla Speculoos: Spekulatius-Mousse in 5 Minuten\n🥣 Cinnamon Cereal: Zimtschnecken-Overnight-Oats\n🍓 Strawberry Cream: Erdbeer-Quark-Bowl nur für dich\n\nAlle drei Rezepte findest du hier auf der Seite, jeweils mit über 30 g Eiweiß.\n\nWelche Sorte würdest du zuerst probieren?",
f"Werbung: Die neuen Sorten gibt es gerade in der ESN Black Week mit -30 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-26","12:00","ESN-P5-Dose","So weit reicht eine Dose",
"Werbung\n\nIch habe mal nachgerechnet: So weit reicht eine Dose 🧮\n\n480 g sind 16 Portionen à 30 g.\n• Morgens: 5 × Overnight Oats, Porridge oder Skyr-Bowl\n• Dessert: 6 × Mousse, Pudding oder Tiramisu im Glas\n• Unterwegs: 5 × Shake\n\nIn der Black Week kostet die Portion ca. 1,22 €, mit ca. 23 g Eiweiß.\n\n16 Rezepte aus einer Dose. Wofür würdest du sie nehmen?",
f"Werbung: Die 480-g-Dose gibt es gerade für 19,53 € statt 27,90 €. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-27","12:00","ESN-P6-Top3","Black Friday: meine Top 3",
"Werbung\n\nBlack Friday 🖤 Meine Top 3 für den Vorrat:\n\n1. Designer Protein Extra Creamy für meine Rezepte: -30 %\n2. Designer Bar als 12er Box für den Snack: -30 %\n3. Protein-Kaffee Flexpresso für morgens: -25 %\n\nTipp: Ab der 2. Bestellung in der Black Week ist der Versand ab 30 € kostenlos mit dem Code SHIPAGAIN.\n\nEinmal im Jahr fülle ich den Vorrat auf. Was kommt bei dir in den Warenkorb?",
f"Werbung: Die beste Aktion des Jahres läuft. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-28","12:00","ESN-P7-Abendsnacks","4 Eiweiß-Snacks unter 200 kcal",
"Werbung\n\nAbends Hunger? Meine 4 Eiweiß-Snacks unter 200 kcal 🌙\n\n🥤 Shake: 30 g Proteinpulver + 300 ml Wasser, 115 kcal\n🍮 Schoko-Creme: 200 g Skyr + 15 g Proteinpulver Schoko, 185 kcal\n🍨 Schoko-Eis aus Hüttenkäse, 195 kcal\n🍫 Proteinriegel, 200 kcal\n\nAlle mit 14 bis 33 g Eiweiß. Kalorien im Blick, Genuss inklusive.\n\nSnacken ja. Aber mit Plan. Was ist dein Abendsnack?",
f"Werbung: Das Extra Creamy und die Riegel gibt es gerade in der ESN Black Week mit -30 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-29","12:00","ESN-P8-Klumpen","Proteinpulver ohne Klumpen",
"Werbung\n\nTipp aus meiner Küche: Proteinpulver ohne Klumpen 🥄\n\n1. Erst das Pulver, dann wenig Flüssigkeit. Zu einer glatten Paste rühren, dann den Rest dazu.\n2. In Skyr und Quark: Schneebesen, 30 Sekunden kräftig. Dann wird es cremig wie Mousse.\n3. Pudding und Grießbrei: erst 2 Minuten abkühlen lassen, dann einrühren.\n4. Shake: Flüssigkeit zuerst in den Shaker, dann Pulver drauf, 20 Sekunden schütteln.\n\nKochend heiß flockt Eiweiß aus. Deshalb kommt es bei mir immer zum Schluss rein.\n\nCremig statt klumpig: Die Reihenfolge macht's. Speichern nicht vergessen 😉",
f"Werbung: Mein Proteinpulver für alle Rezepte ist das Designer Protein von ESN. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-30","12:00","ESN-P9-Shakes","3 Shakes unter 250 kcal",
"Werbung\n\nShake, aber richtig: 3 Shakes unter 250 kcal 🥤\n\n🍪 Spekulatius-Shake: 30 g Vanilla Speculoos + 250 ml Milch (1,5 %) + Prise Zimt, 230 kcal\n🍓 Erdbeer-Shake: 30 g Strawberry Cream + 100 g Erdbeeren (TK) + 250 ml Wasser (Mixer), 145 kcal\n🍌 Schoko-Banane: 30 g Milk Chocolate + ½ Banane + 250 ml Wasser (Mixer), 170 kcal\n\nJeweils mit 24 bis 32 g Eiweiß. Eiskalt schmecken sie am besten.\n\nKein Shake muss nach Pappe schmecken. Welchen probierst du?",
f"Werbung: Die Sorten für die Shakes gibt es gerade in der ESN Black Week mit -30 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-12-01","12:00","ESN-P10-Fragen","Black Week kurz erklärt",
"Werbung\n\nEure Fragen zur Black Week, kurz erklärt 👇\n\n❓ Wie lange läuft sie? Bis morgen, Mittwoch 2.12., 17:30 Uhr.\n❓ Wie viel Rabatt gibt es? Bis zu -70 %, Riegel und Extra Creamy -30 %, Whey und Isoclear -25 %.\n❓ Welche Sorte für die Rezepte? Vanilla Milk passt fast überall. Für Desserts die neuen Sorten.\n❓ Und der Versand? Ab der 2. Bestellung ab 30 € kostenlos mit dem Code SHIPAGAIN.\n\nDen Link mit meinem Code findest du im ersten Kommentar.\n\nNoch eine Frage? Schreib sie mir in die Kommentare 😊",
f"Werbung: Nur noch bis morgen: Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-12-02","12:00","ESN-P11-Letzter-Tag","Letzte Chance: heute bis 17:30 Uhr",
"Werbung\n\nLetzte Chance: Heute um 17:30 Uhr endet die ESN Black Week ⏰\n\nDas hole ich mir noch:\n• Ultra Dark Chocolate (neu) für Schokopudding\n• Vanilla Speculoos (neu) für Spekulatius-Desserts\n• Designer Bar Mint (neu) als Snack\n\nDanach gibt es diese Preise erst wieder in einem Jahr.\n\nNur einmal im Jahr. Heute ist der letzte Tag.",
f"Werbung: Nur noch heute bis 17:30 Uhr: Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L}"),
]
out=[]
for d,z,f,alt,t,fc in P:
    assert t.startswith("Werbung") and fc.startswith("Werbung:") and L in fc and 'abnehm' not in (t+fc).lower() and 'Günstiger' not in t+fc and '-50' not in t+fc
    out.append(dict(datum=d,zeit=z,datei=f,date=f"{d}T{z}:00",text=t,fc=fc,media=URL.format(f),alt=alt))
json.dump(out,open(f"{D}/esn_produkt_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/texte-esn-produkt-beitraege.txt","w") as h:
    h.write("ESN BLACK WEEK – PRODUKT-BEITRÄGE (je 12:00 Uhr)\nBeitrag 1 „Mein Einkaufszettel“ (So 22.11., 12:00) folgt, sobald du mir deine Sorten sagst.\n\n")
    for p in out:
        h.write(f"===== {p['datum'][8:10]}.{p['datum'][5:7]}. · {p['zeit']} · Bild {p['datei']}.jpg\n\nTEXT:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\n\n")
print(len(out))
