# -*- coding: utf-8 -*-
import json, os
D=os.path.dirname(os.path.abspath(__file__))
L="esn.com/instagram/FITMITKEV/aktion"; BIS="(bis Mi 2.12., 17:30 Uhr)"
URL="https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/main/esn/posts/{}.jpg"
P=[
("2026-11-23","12:00","ESN-P2-Morgen","Mein Frühstück unterwegs",
"Werbung\n\nMein Frühstück unterwegs: 2 Minuten statt Bäcker ☕\n\nCoffee to go mit Croissant: ca. 450 kcal und nur 10 g Eiweiß.\nMein Flexpresso mit Mandelmilch: ca. 145 kcal und 24 g Eiweiß.\n\nEin Drittel der Kalorien, mehr als doppelt so viel Eiweiß. Ich trinke jeden Morgen eine doppelte Portion.\n\nWas gibt's bei dir morgens? ☕🥐",
f"Werbung: Den Protein-Kaffee (Flexpresso) gibt es gerade in der ESN Black Week mit -25 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-24","12:00","ESN-P3-Riegel","Schokoriegel oder Proteinriegel",
"Werbung\n\nSchokoriegel oder Proteinriegel? 🍫\n\nSchokoriegel (50 g): ca. 240 kcal, 25 g Zucker, 3 g Eiweiß. Das sind 8 Stück Würfelzucker.\nDesigner Bar (45 g): unter 200 kcal, höchstens 2 g Zucker, 14 g Eiweiß. Weich, mit Füllung.\n\nSüß darf sein. Nur eben ohne Zuckerbombe.\n\nTeam Schokoriegel oder Team Proteinriegel? 😄",
f"Werbung: Die Designer Bar gibt es gerade in der ESN Black Week mit -30 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-25","12:00","ESN-P4-NeueSorten","3 neue Sorten, 3 Rezepte",
"Werbung\n\nNeu bei ESN: 3 neue Sorten vom Extra Creamy Protein, und ich habe direkt 3 Rezepte daraus gemacht 😍\n\n🍪 Vanilla Speculoos: Spekulatius-Mousse in 5 Minuten\n🥣 Cinnamon Cereal: Zimtschnecken-Overnight-Oats\n🍓 Strawberry Cream: Erdbeer-Quark-Bowl nur für dich\n\nAlle drei Rezepte findest du hier auf der Seite, jeweils mit über 30 g Eiweiß.\n\nWelche Sorte würdest du zuerst probieren?",
f"Werbung: Die neuen Sorten gibt es gerade in der ESN Black Week mit -30 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
# P5 (Do 26.11.) am 19.11. von Kev gestrichen – der Tag bleibt ohne Infobeitrag.
("2026-11-27","12:00","ESN-P6-Top3","Black Friday: meine Top 3",
"Werbung\n\nBlack Friday 🖤 Meine Top 3 für den Vorrat:\n\n1. Designer Protein Extra Creamy für meine Rezepte: -30 %\n2. Designer Bar als 12er Box für den Snack: -30 %\n3. Protein-Kaffee Flexpresso für morgens: -25 %\n\nTipp: Ab der 2. Bestellung in der Black Week ist der Versand ab 30 € kostenlos. Einfach die Codes FITMITKEV und SHIPAGAIN kombinieren.\n\nDie ESN Black Week gibt es nur 1x im Jahr. Was kommt bei dir in den Warenkorb?",
f"Werbung: Die beste Aktion des Jahres läuft. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-28","12:00","ESN-P7-Abendsnacks","4 Eiweiß-Snacks unter 200 kcal",
"Werbung\n\nAbends Hunger? Meine 4 Eiweiß-Snacks unter 200 kcal 🌙\n\n🥤 Shake: 30 g Proteinpulver + 300 ml Wasser, 115 kcal\n🍮 Schoko-Creme: 200 g Skyr + 15 g Proteinpulver Schoko, 185 kcal\n🍨 Schoko-Eis aus Hüttenkäse, 195 kcal\n🍫 Proteinriegel, 190 kcal\n\nAlle mit 14 bis 33 g Eiweiß. Kalorien im Blick, Genuss inklusive.\n\nSnacken ja. Aber mit Plan. Was ist dein Abendsnack?",
f"Werbung: Das Extra Creamy und die Riegel gibt es gerade in der ESN Black Week mit -30 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-29","12:00","ESN-P8-Klumpen","Proteinpulver ohne Klumpen",
"Werbung\n\nTipp aus meiner Küche: Proteinpulver ohne Klumpen 🥄\n\n1. Erst das Pulver, dann wenig Flüssigkeit. Zu einer glatten Paste rühren, dann den Rest dazu.\n2. In Skyr und Quark: Schneebesen, 30 Sekunden kräftig. Dann wird es cremig wie Mousse.\n3. Pudding und Grießbrei: erst 2 Minuten abkühlen lassen, dann einrühren.\n4. Shake: Flüssigkeit zuerst in den Shaker, dann Pulver drauf, 20 Sekunden schütteln.\n\nKochend heiß flockt Eiweiß aus. Deshalb kommt es bei mir immer zum Schluss rein.\n\nCremig statt klumpig: Die Reihenfolge macht's. Speichern nicht vergessen 😉",
f"Werbung: Mein Proteinpulver für alle Rezepte ist das Designer Protein von ESN. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-11-30","12:00","ESN-P9-Shakes","3 Shakes unter 250 kcal",
"Werbung\n\nShake, aber richtig: 3 Shakes unter 250 kcal 🥤\n\n🍪 Spekulatius-Shake: 30 g Vanilla Speculoos + 250 ml Milch (1,5 %) + Prise Zimt, 230 kcal\n🍓 Erdbeer-Shake: 30 g Strawberry Cream + 100 g Erdbeeren (TK) + 250 ml Wasser (Mixer), 145 kcal\n🍌 Schoko-Banane: 30 g Milk Chocolate + ½ Banane + 250 ml Wasser (Mixer), 170 kcal\n\nJeweils mit 24 bis 32 g Eiweiß. Eiskalt schmecken sie am besten.\n\nKein Shake muss nach Pappe schmecken. Welchen probierst du?",
f"Werbung: Die Sorten für die Shakes gibt es gerade in der ESN Black Week mit -30 %. Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-12-01","12:00","ESN-P10-Fragen","ESN Black Week kurz erklärt",
"Werbung\n\nEure Fragen zur ESN Black Week, kurz erklärt 👇\n\n❓ Wie lange läuft sie? Bis morgen, Mittwoch 2.12., 17:30 Uhr.\n❓ Wie viel Rabatt gibt es? Bis zu -70 %, Riegel und Extra Creamy -30 %, Whey und Isoclear -25 %.\n❓ Welche Sorte für die Rezepte? Vanilla Milk passt fast überall. Für Desserts die neuen Sorten.\n❓ Und der Versand? Ab der 2. Bestellung ab 30 € kostenlos mit dem Code SHIPAGAIN.\n\nDen Link mit meinem Code findest du im ersten Kommentar.\n\nNoch eine Frage? Schreib sie mir in die Kommentare 😊",
f"Werbung: Nur noch bis morgen: Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L} {BIS}"),
("2026-12-02","12:00","ESN-P11-Letzter-Tag","Letzte Chance: heute bis 17:30 Uhr",
"Werbung\n\nLetzte Chance: Heute um 17:30 Uhr endet die ESN Black Week ⏰\n\nDas hole ich mir noch (nur solange der Vorrat reicht):\n• Ultra Dark Chocolate (neu) für Schokopudding\n• Vanilla Speculoos (neu) für Spekulatius-Desserts\n• Designer Bar Mint (neu) als Snack\n\nDanach gibt es diese Preise erst wieder in einem Jahr.\n\nNur einmal im Jahr. Heute ist der letzte Tag.",
f"Werbung: Nur noch heute bis 17:30 Uhr: Black-Week-Rabatte mit Code FITMITKEV sichern 👉 {L}"),
]
out=[]
for d,z,f,alt,t,fc in P:
    assert t.startswith("Werbung") and fc.startswith("Werbung:") and L in fc and 'abnehm' not in (t+fc).lower() and 'Günstiger' not in t+fc and '-50' not in t+fc
    out.append(dict(datum=d,zeit=z,datei=f,date=f"{d}T{z}:00",text=t,fc=fc,media=URL.format(f),alt=alt))
json.dump(out,open(f"{D}/esn_produkt_posts.json","w"),ensure_ascii=False,indent=1)
with open(f"{D}/texte-esn-produkt-beitraege.txt","w") as h:
    h.write("ESN BLACK WEEK – PRODUKT-BEITRÄGE (je 12:00 Uhr)\nBeitrag 1 „Mein Einkaufszettel“ (So 22.11., 12:00): Text in tools/gesn/ESN-persoenliche-Beitraege-Entwurf.txt. Beitrag 5 (Do 26.11.) ist gestrichen.\n\n")
    for p in out:
        h.write(f"===== {p['datum'][8:10]}.{p['datum'][5:7]}. · {p['zeit']} · Bild {p['datei']}.jpg\n\nTEXT:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\n\n")
print(len(out))
