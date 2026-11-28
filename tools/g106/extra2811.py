# -*- coding: utf-8 -*-
# Zusatz Sa 28.11. / So 29.11.2026: vier zusätzliche süße Beiträge (alle mit neuem Bild).
#   Sa 28.11. 18:15  Philadelphia-Torte ohne Backen (neu)        Sa 28.11. 20:45  Schoko-Wölkchen (neu)
#   So 29.11. 06:10  Skyr-Kuchen mit Spekulatius (Rezept G93 vom 15.11., NEUES Foto, neue Schreibschrift-Zeile, neues Emoji – Rezept, Kalorien, 1. Kommentar unverändert)
#   So 29.11. 13:00  Zebrakuchen (neu)
#   Die festen Protein-Rezepte wandern dafür So–Mi von 6:10/13:00 auf 18:15/20:45.
#   Neue Kachel: goetterspeise (tools/tilex/kachel_glas.py).
# Aufruf im Arbeitsordner g106p:  python3 extra2811.py prompts   |   OHNE_BOX=1 python3 extra2811.py [--ohne-prep] [Key ...]   |   python3 extra2811.py texte <Commit>
import os, sys, json, copy, importlib.util
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import g106_data as G
from g106_data import Z
REPO = '/home/claude/fitmitkev-bilder'
spec = importlib.util.spec_from_file_location('g93_data', f'{REPO}/tools/g93/g93_data.py'); m93 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m93)
G.PIECE.setdefault('goetterspeise_beutel', (12, (40, 9, 0.5, 0)))   # 1 Beutel Götterspeise-Pulver zum Kochen (für 500 ml), ohne Zucker: fast nur Gelatine
SPEK = "thin flat rectangular Dutch speculaas spiced biscuits with an embossed windmill relief and slightly scalloped edges, light golden brown"

NEU = dict(
 PhiladelphiaTorte=dict(key='PhiladelphiaTorte', suess=True, hook='Ohne Backen:', titel=['PHILADELPHIA-', 'TORTE'], portion='pro Stück', anzahl=12, vs=350,
  zutaten=[Z('150 g', 'Butterkekse', 'butterkekse', 'butterkeks', st=27), Z('50 g', 'Butter', 'butter', 'butter', 50), Z('400 g', 'Frischkäse light', 'frischkaese_light', 'frischkaese', 400),
           Z('500 g', 'Skyr', 'skyr', 'skyr', 500), Z('1 Beutel', 'Götterspeise Zitrone', 'goetterspeise', 'goetterspeise_beutel', st=1),
           Z('80 g', 'Erythrit', 'erythrit', 'erythrit', 80), Z('2 Stück', 'Zitronen', 'zitrone', 'zitrone', 100)],
  ex=['250 ml Wasser'], exnut=[],
  intro='Die Philadelphia-Torte, die früher auf keiner Feier gefehlt hat: knuspriger Keksboden, darauf eine zitronige Frischkäse-Creme, die im Kühlschrank von allein fest wird. Kein Ofen, 20 Minuten Arbeit, heute Abend gemacht und morgen zum Adventskaffee fertig. Bei mir mit Skyr statt Sahne und Erythrit statt Zucker: {k} kcal pro Stück statt 350 für das Original!',
  schritte=['Die Butterkekse fein zerbröseln, mit der geschmolzenen Butter mischen und als Boden in eine Springform (26 cm) mit Backpapier drücken. Kalt stellen.',
            'Das Götterspeise-Pulver (1 Beutel, reicht sonst für 500 ml) mit 250 ml Wasser und 40 g Erythrit verrühren, 5 Minuten quellen lassen und unter Rühren erhitzen (nicht kochen), bis sich alles gelöst hat. 15 Minuten abkühlen lassen.',
            'Frischkäse, Skyr, das restliche Erythrit und den Saft von 1½ Zitronen glatt rühren. Die lauwarme Götterspeise zügig unterrühren und die Creme auf den Keksboden gießen.',
            'Mindestens 4 Stunden, am besten über Nacht, kalt stellen. Die restliche halbe Zitrone in dünne Scheiben schneiden, die Torte damit garnieren und in 12 Stücke schneiden.'],
  frage='Philadelphia-Torte: mit Zitrone oder mit Mandarinen, wie kennst du sie?', tags='#philadelphiatorte #ohnebacken #kühlschranktorte #fitmitkev',
  name='Philadelphia-Torte ohne Backen', menge='12 Stücke, Springform 26 cm', emo='🤤',
  prompt="A round no-bake lemon cream cheese fridge cake on a white cake plate seen from the side at a 30 degree angle, the whole cake fully visible with empty table space left and right of it, a thin golden butter biscuit crumb base and a thick smooth pale lemon-yellow cream layer about 5 cm tall with a clean straight edge and a flat glossy top, decorated on top with a few thin lemon slices, one slice of the cake cut out and lying on a small white plate in front showing the crumb base and the creamy pale yellow filling, a small fork beside the plate."),
 SchokoWoelkchen=dict(key='SchokoWoelkchen', suess=True, hook='Jetzt auch in Schoko:', titel=['SCHOKO-', 'WÖLKCHEN'], portion='pro Stück', anzahl=30, vs=85,
  zutaten=[Z('200 g', 'Magerquark', 'magerquark', 'quark', 200), Z('100 g', 'Gemahlene Mandeln', 'gemahlene_mandeln', 'mandeln', 100), Z('70 g', 'Speisestärke', 'speisestaerke', 'speisestaerke', 70),
           Z('20 g', 'Backkakao', 'backkakao', 'kakao', 20), Z('70 g', 'Erythrit', 'erythrit', 'erythrit', 70), Z('1 Stück', 'Ei', 'ei', 'ei', st=1)],
  ex=['1 TL Backpulver, 1 Prise Salz', 'Puder-Erythrit zum Bestäuben'], exnut=[],
  intro='Die Wölkchen gibt es jetzt auch in Schoko: außen zart, innen weich wie ein kleiner Brownie und weiß bestäubt wie frisch verschneit. Wieder ganz ohne Butter und ohne Mehl, der Quark hält sie saftig. In 10 Minuten gerührt, 15 Minuten im Ofen: {k} kcal pro Wölkchen statt 85 für ein Schoko-Plätzchen!',
  schritte=['Quark, Ei, Erythrit und eine Prise Salz glatt rühren. Mandeln, Speisestärke, Kakao und Backpulver mischen und unterrühren. Den Teig 10 Minuten quellen lassen.',
            'Mit zwei Teelöffeln 30 kleine Häufchen auf ein Backblech mit Backpapier setzen und mit feuchten Fingern rund formen.',
            'Bei 170 °C Ober-/Unterhitze 15–18 Minuten backen. Abkühlen lassen und dick mit Puder-Erythrit bestäuben.'],
  frage='Wölkchen: Kokos, Zimt oder Schoko, welche Sorte ist deine?', tags='#wölkchen #schoko #plätzchen #fitmitkev',
  name='Schoko-Wölkchen ohne Butter und Mehl', menge='ca. 30 Stück', emo='🥰',
  prompt="A white plate piled high with many small round dark cocoa-brown soft chocolate cookies, each cookie a slightly domed mound with fine cracks, thickly dusted with white powdered sugar so that the dark brown cracks show through, three whole cookies lying on the table in front of the plate, all cookies whole and unbroken, nothing else beside the plate."),
 Zebrakuchen=dict(key='Zebrakuchen', suess=True, hook='Wie in der Kindheit:', titel=['ZEBRA-', 'KUCHEN'], portion='pro Stück', anzahl=16, vs=320,
  zutaten=[Z('4 Stück', 'Eier', 'eier', 'ei', st=4), Z('120 g', 'Erythrit', 'erythrit', 'erythrit', 120), Z('300 g', 'Dinkelmehl', 'dinkelmehl', 'dinkelmehl', 300),
           Z('250 g', 'Skyr', 'skyr', 'skyr', 250), Z('150 ml', 'Milch (1,5 %)', 'milch', 'milch', 150), Z('60 ml', 'Öl', 'oel', 'oel', 55), Z('25 g', 'Backkakao', 'backkakao', 'kakao', 25)],
  ex=['1 Päckchen Backpulver, 1 Prise Salz', 'Puder-Erythrit zum Bestäuben'], exnut=[],
  intro='Zebrakuchen wie früher auf dem Kindergeburtstag: heller und dunkler Rührteig, löffelweise in die Mitte der Form gegeben, die Streifen entstehen ganz von allein. Bei mir mit Skyr und nur wenig Öl statt einem Viertelliter, dazu Erythrit statt Zucker: {k} kcal pro Stück statt 320 für das Original!',
  schritte=['Den Ofen auf 175 °C Ober-/Unterhitze vorheizen und eine Springform (26 cm) mit Backpapier auslegen. Die Eier mit dem Erythrit 3 Minuten schaumig schlagen, Skyr, Öl und 120 ml Milch unterrühren, Mehl, Backpulver und Salz kurz unterheben.',
            'Den Teig halbieren. Unter eine Hälfte den Kakao und die restliche Milch rühren.',
            'Abwechselnd je 2 Esslöffel hellen und dunklen Teig immer genau in die Mitte der Form geben, bis beide Teige verbraucht sind. Nicht verstreichen, der Teig verläuft von allein (sonst die Form kurz rütteln).',
            '45–50 Minuten backen (Stäbchenprobe), auskühlen lassen, mit Puder-Erythrit bestäuben und in 16 Stücke schneiden.'],
  frage='Zebrakuchen: kennst du ihn noch von früher?', tags='#zebrakuchen #rührkuchen #omasrezepte #fitmitkev',
  name='Zebrakuchen in leicht', menge='16 Stücke, Springform 26 cm', emo='😋',
  prompt="A round German zebra marble cake on a white cake plate seen from the side at a 30 degree angle, the whole cake fully visible with empty table space left and right of it, golden brown top lightly dusted with powdered sugar, a large wedge cut out so the cut faces clearly show bold wavy vertical zebra stripes of pale yellow vanilla sponge alternating with dark brown cocoa sponge, two slices lying on a small white plate in front with the striped cut side facing the camera, a small fork beside the plate."),
)
# Bekanntes Rezept mit neuem Foto: Skyr-Kuchen mit Spekulatius (G93, lief zuletzt So 15.11. → ab So 29.11. wieder frei)
ALT = [r for r in m93.R if r['key'] == 'SpekSkyr'][0]
_r = copy.deepcopy(ALT); _r['key'] = 'SpekSkyrNeu'; _r['hook_alt'] = ALT['hook']; _r['hook'] = 'Zum 1. Advent:'
_r['prompt'] = ("A small round golden baked cheesecake about 5 cm tall with a smooth golden brown top lightly dusted with cinnamon and a thin brown spiced biscuit crumb base, standing on a round light wooden board "
                "seen from above at a 45 degree angle, the whole cake fully visible with empty table space left and right of it, two slices cut out of the cake, one slice lying on a small white plate in front "
                "showing the creamy pale filling and the thin brown base from the side, three " + SPEK + " lying flat on the table beside the board, one cinnamon stick, a small fork beside the plate.")
assert G.macros4(_r) == (130, 13, 11, 3) and _r['hook'] != ALT['hook'], G.macros4(_r)
NEU['SpekSkyrNeu'] = _r
for _k, _v in NEU.items():
    if not _v['prompt'].rstrip().endswith('bokeh lights.'): _v['prompt'] = _v['prompt'] + G.P_END
    _v.setdefault('kurz', ['–', '–', '–'])     # Kurzschritte nur für die Box-Variante; Boards laufen ohne Box
PREP = {k: dict(s=0.74, glatt=True) for k in NEU}
PREP['Zebrakuchen'] = dict(s=0.74, glatt=True, cl=(32, 355, 425))     # Licht am linken Bildrand (sonst waagerechter heller Streifen neben der Kachelspalte)
PREP['SpekSkyrNeu'] = dict(s=0.74, glatt=True, cl=(32, 300, 370))
WAHL = {}          # gewähltes Rohbild je Key, sonst s1
PLAN = [('PhiladelphiaTorte', '2026-11-28T18:15:00'), ('SchokoWoelkchen', '2026-11-28T20:45:00'), ('SpekSkyrNeu', '2026-11-29T06:10:00'), ('Zebrakuchen', '2026-11-29T13:00:00')]

def texte(commit):
    alt93 = [p for p in json.load(open(f'{REPO}/tools/g93/sonntag_posts.json', encoding='utf-8')) if p['key'] == 'SpekSkyr'][0]
    posts = []
    for key, date in PLAN:
        r = NEU[key]; k, p, c, f = G.macros4(r)
        if key == 'SpekSkyrNeu':
            text = alt93['text'].replace('🤗', '😍'); fc = alt93['fc']; name = alt93['alt']
            assert '😍' in text and text != alt93['text'] and str(k) + ' kcal' in text
        else:
            zut = "\n".join(f"• {z['menge']} {z['name']}" for z in r['zutaten']) + "\n" + "\n".join(f"• {e}" for e in r['ex'])
            steps = "\n".join(f"{j + 1}. {s}" for j, s in enumerate(r['schritte']))
            text = f"{k} kcal {r['portion']} {r['emo']} Rezept im 1. Kommentar ⤵️\n\n{r['tags']}"
            fc = (f"{r['name']}\n\n{r['intro'].format(k=k, p=p)}\n\nZutaten ({r['menge']}):\n{zut}\n\nSo geht's:\n{steps}\n\n"
                  f"Nährwerte {r['portion']}: ca. {k} kcal | {p} g Eiweiß | {c} g Kohlenhydrate | {f} g Fett\n\nSchmeckt nach Sünde, zählt wie Salat 😉\nBleib satt! 💪\n\n{r['frage']}")
            name = r['name']
        low = (text + fc).lower()
        for w in ('esn', 'abnehm', 'höflich', 'http'): assert w not in low, (key, w)
        assert '#' not in fc and k < r['vs']
        posts.append(dict(key=key, date=date, text=text, fc=fc, alt=name, kcal=k, suess=True, neu=(key != 'SpekSkyrNeu'), bild='neu', board=f'G106-{key}-ohneBox.jpg',
                          media=f'https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/{commit}/boards/G106-{key}-ohneBox.jpg'))
    return posts

if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['prompts']:
        n = int(a[1]) if len(a) > 1 else 1; reqs = []
        for k in NEU:
            for j in range(n): reqs.append({"index": len(reqs), "params": {"model": "gpt_image_2_6", "aspect_ratio": "4:5", "prompt": NEU[k]['prompt']}})
        print(json.dumps(reqs, ensure_ascii=False)); sys.exit()
    if a[:1] == ['werte']:
        for k, r in NEU.items(): print(k, G.macros4(r), 'statt', r['vs'], '| Kacheln', len(r['zutaten']))
        sys.exit()
    if a[:1] == ['texte']:
        P = texte(a[1]); json.dump(P, open(f'{D}/out/extra2811_posts.json', 'w'), ensure_ascii=False, indent=1)
        for p in P: print('=' * 70, '\n', p['date'], p['key'], '\n', p['text'], '\n---\n', p['fc'])
        sys.exit()
    ohne_prep = '--ohne-prep' in a; keys = [x for x in a if not x.startswith('--')] or list(NEU)
    ap = f'{D}/hero/_auswahl.json'; A = json.load(open(ap))
    for k in keys: A[k] = f"{k}_{WAHL.get(k, 's1')}"
    json.dump(A, open(ap, 'w'), indent=1)
    import prep106
    for k in keys:
        prep106.T[k] = PREP[k]
        if not (ohne_prep and os.path.exists(f'{D}/hero/{k}.jpg')): prep106.prep(k)
    import render106
    G.R = list(G.R) + [NEU[k] for k in keys]
    render106.render(keys)
