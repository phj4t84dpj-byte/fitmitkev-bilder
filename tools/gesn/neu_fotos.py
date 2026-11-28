# -*- coding: utf-8 -*-
# Die festen Protein-Rezepte 6:10 / 13:00 (frühere ESN-Rezepte) für den zweiten Lauf Sa 28.11.–Mi 2.12. mit NEUEM Foto
# (Kev 28.11.: kein Bild läuft zweimal – „auch heute 13 Uhr umbauen, und alle anderen auch“).
# Gleiches Rezept, gleiche Kalorien, gleicher 1. Kommentar; neu: Foto (Higgsfield gpt_image_2_6, 4:5), Schreibschrift-Zeile, Emoji im Beitragstext.
# Aufruf im Arbeitsordner gesn:  OHNE_BOX=1 python3 neu_fotos.py [--ohne-prep] [Key ...]   → out/ESN-<Key>Neu-ohneBox.jpg
# Rohbilder (1024x1280) liegen im HF-Dataset kevrsztorm/fitmitkev-bilder: gesnneu/<Key>Neu_s1.jpg, gesnneu2/<Key>Neu_s2.jpg → nach raw/ kopieren.
# Alle neun Boards sind gegen sämtliche Boards im Repo geprüft (tools/bild_pruefen.py): kleinster Abstand 88–98, Grenze 40.
import os, sys, json, copy
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import gesn_data as G
P_END = (" Homemade, standing on a light wooden table, behind it a plain warm beige wall with soft golden bokeh fairy lights out of focus, cozy warm Christmas mood, "
         "natural soft warm light, shallow depth of field, professional food photography, realistic, appetizing, slightly imperfect like homemade, already served, no hands, "
         "no people, no text, no packaging, no logos, no fir branches, nothing else on the table, the upper third of the image is plain warm beige background with a few bokeh lights.")
LOEFFEL = " Exactly one small plain smooth stainless steel teaspoon with a straight simple handle lies on the table beside it; there is no other spoon, fork or cutlery anywhere in the picture."
SPEK = "thin flat rectangular Dutch speculaas spiced biscuits with an embossed windmill relief and slightly scalloped edges, light golden brown"
GLAS = ("A single portion in a small rectangular clear glass baking dish with handles and intact transparent glass walls, the front glass wall clearly visible and closed, "
        "both handles of the dish fully visible, the whole dish fully visible with empty table space left and right of it, ")
# Key: (neue Schreibschrift-Zeile, neuer Prompt)
NEU = {
 'SchokoKugelnESN': ('Snack für zwischendurch:',
   "A small rustic light grey ceramic bowl filled with a pile of round dark chocolate energy balls, about half of them coated in white desiccated coconut, seen from the front slightly from above, "
   "the whole bowl fully visible with empty table space left and right of it, three more balls lying on the table in front of the bowl, one of them cut in half showing the dense dark chocolate oat inside, a few rolled oats scattered on the table."),
 'SpekulatiusMousseESN': ('Advent im Glas:',
   "Two short wide clear glass dessert tumblers seen from above at a 45 degree angle, one in front and one slightly behind it, both fully visible with empty table space left and right, "
   "filled with fluffy light beige spiced mousse with a soft swirl on top, sprinkled with fine brown biscuit crumbs, one of the " + SPEK + " stuck into the mousse of each glass, two more of these biscuits lying flat on the table in front." + LOEFFEL),
 'ErdbeerBowlESN': ('Zum Löffeln:',
   GLAS + "seen from the front slightly from above, completely full and untouched, the layers clearly visible through the glass: a thin layer of golden butter biscuit crumbs at the bottom, "
   "a thick layer of smooth pale pink strawberry quark cream, the top covered with glossy red strawberry pieces in a little red strawberry sauce, one butter biscuit lying on the table beside the dish." + LOEFFEL),
 'ZimtschneckenOatsESN': ('Abends vorbereitet:',
   "Two small clear glass jars seen from above at a 45 degree angle, one in front and one slightly behind it, both fully visible with empty table space left and right, filled with creamy beige overnight oats "
   "with brown cinnamon swirls visible through the glass, each topped with a thick white cream cheese frosting spiral and a dusting of cinnamon like a cinnamon roll, one cinnamon stick lying on the table in front." + LOEFFEL),
 'DarkSchokoPuddingESN': ('Besser als aus dem Becher:',
   "Two small round clear glass dessert bowls seen from above at a 45 degree angle, one in front and one slightly behind it, both fully visible with empty table space left and right, "
   "filled with glossy smooth very dark chocolate pudding with a soft swirl on top, each topped with three red raspberries, a few more raspberries lying on the table in front." + LOEFFEL),
 'SpekulatiusTiramisuESN': ('Schicht für Schicht:',
   "One clear straight dessert glass in front seen slightly from above and a second one behind it slightly out of focus, both fully visible with empty table space left and right, clearly visible layers through the glass: "
   "espresso-soaked brown biscuit pieces alternating with thick white cream, the top generously dusted with dark cocoa powder, two " + SPEK + " lying flat on the table in front of the glasses." + LOEFFEL),
 'ErdbeerCheesecakeGlasESN': ('Käsekuchen zum Löffeln:',
   "Two short wide clear glass tumblers seen from above at a 45 degree angle, one in front and one slightly behind it, both fully visible with empty table space left and right, clearly visible layers through the glass: "
   "golden butter biscuit crumbs at the bottom and thick smooth white cheesecake cream, the top completely covered with glossy red strawberry sauce and sliced red strawberries, one rectangular petit beurre butter biscuit with scalloped edges and two strawberries lying on the table in front." + LOEFFEL),   # 1. Versuch zeigte einen runden Keks → rechteckiger Butterkeks wie auf der Kachel
 'ZimtGriessbreiESN': ('Warm und cremig:',
   "One deep white ceramic bowl in front seen from above at a 45 degree angle and a second bowl behind it slightly out of focus, both fully visible with empty table space left and right, "
   "filled with thick creamy pale semolina pudding, topped in the middle with a small heap of small diced red-skinned apple cubes and a generous dusting of cinnamon, one whole red apple and two cinnamon sticks lying on the table behind." + LOEFFEL),   # 1. Versuch zeigte Apfelscheiben – im Rezept stehen Apfelwürfel
 'SchokoEisESN': ('Nur 6 Zutaten:',
   "Two small clear glass dessert bowls seen from the front slightly from above, one in front and one slightly behind it, both fully visible with empty table space left and right, "
   "each with two round scoops of creamy dark chocolate ice cream with small dark chocolate chunks, a few chocolate shavings on top, a small piece of dark chocolate lying on the table in front." + LOEFFEL),
}
PREP = {k + 'Neu': dict(s=0.74, glatt=True) for k in NEU}
WAHL = {'ErdbeerCheesecakeGlasESNNeu': 's2', 'ZimtGriessbreiESNNeu': 's2'}   # gewähltes Rohbild, sonst s1 (bei diesen beiden wurde der Prompt nach dem 1. Versuch korrigiert)
ALT = {r['key']: r for r in G.R}
R = {}
for k, (hook, prompt) in NEU.items():
    r = copy.deepcopy(ALT[k]); r['key'] = k + 'Neu'; r['hook_alt'] = ALT[k]['hook']; r['hook'] = hook; r['prompt'] = prompt + P_END
    assert G.macros4(r) == G.macros4(ALT[k]) and r['titel'] == ALT[k]['titel'] and hook != ALT[k]['hook'], k
    R[r['key']] = r

if __name__ == '__main__':
    if sys.argv[1:] == ['prompts']:
        print(json.dumps([{"index": i, "params": {"model": "gpt_image_2_6", "aspect_ratio": "4:5", "prompt": r['prompt']}} for i, r in enumerate(R.values())], ensure_ascii=False)); sys.exit()
    args = [a for a in sys.argv[1:] if not a.startswith('--')]; OHNE_PREP = '--ohne-prep' in sys.argv   # --ohne-prep: nur neu rendern (Hero und Freisteller bleiben)
    keys = [k if k.endswith('Neu') else k + 'Neu' for k in args] or list(R)
    ap = f'{D}/hero/_auswahl.json'; A = json.load(open(ap))
    for k in keys: A[k] = f"{k}_{WAHL.get(k, 's1')}"
    json.dump(A, open(ap, 'w'), indent=1)
    # prep aus dem G106-Arbeitsordner nehmen (kennt `glatt` = oben angesetzter Rand ohne Lichter-Streifen), aber auf diesen Ordner zeigen lassen
    import importlib.util
    P106 = next(d for d in (os.path.join(os.path.dirname(D), n) for n in ('g106p', 'g106')) if os.path.exists(os.path.join(d, 'prep106.py')))   # Arbeitsordner g106p bzw. im Repo tools/g106
    sys.path.append(P106)
    sp = importlib.util.spec_from_file_location('prep106', os.path.join(P106, 'prep106.py')); prep = importlib.util.module_from_spec(sp); sp.loader.exec_module(prep)
    prep.D = D
    for k in keys:
        prep.T[k] = PREP[k]
        if not (OHNE_PREP and os.path.exists(f'{D}/hero/{k}.jpg')): prep.prep(k)
    import renderesn
    for k in keys:                        # Kachel-Reihenfolge des alten Boards übernehmen (sonst liegt der Pfeil über einer langen Beschriftung)
        if k[:-3] in renderesn.ORDER: renderesn.ORDER[k] = renderesn.ORDER[k[:-3]]
    # Diese Boards haben kein Vorher-Nachher-Foto links unten. Auf dem dunkleren Holztisch der neuen Fotos stand dort sonst ein heller Kasten
    # (Beige-Verlauf der Kachelspalte bis y=1100, daneben der unverblasste Freisteller). Deshalb läuft der linke Verlauf hier unter den Kacheln
    # weich aus (y 700→805, darunter ist der Freisteller voll da) und der untere Verlauf entfällt: der Tisch läuft bis zum linken Rand durch.
    CSS_NEU = ('<style>.fadeL{height:805px;-webkit-mask-image:linear-gradient(to bottom,#000 0,#000 87%,transparent 100%);'
               'mask-image:linear-gradient(to bottom,#000 0,#000 87%,transparent 100%)}.fadeB{display:none}</style></head>')
    _bh = renderesn.board_html
    def board_html(r, hero, herocut):
        h = _bh(r, hero, herocut); assert h.count('</head>') == 1
        return h.replace('</head>', CSS_NEU)
    renderesn.board_html = board_html
    G.R = list(G.R) + [R[k] for k in keys]
    renderesn.render(keys)
