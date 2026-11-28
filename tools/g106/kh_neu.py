# -*- coding: utf-8 -*-
# Kalter Hund für So 29.11.2026 mit NEUEM Foto (kein Bild läuft mehr zweimal): gleiches Rezept wie G93 (125 kcal, 4 g Eiweiß pro Scheibe),
# neues Foto (Higgsfield gpt_image_2_6), neue Schreibschrift-Zeile. Zwei Varianten zur Auswahl:
#   A = ganzer Kuchen auf der Platte, zwei Scheiben davor · B = vier Scheiben auf dem Teller.
# Aufruf im Arbeitsordner g106p:  OHNE_BOX=1 python3 kh_neu.py
import os, sys, json, copy, importlib.util
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
import g106_data as G
REPO = '/home/claude/fitmitkev-bilder'
spec = importlib.util.spec_from_file_location('g93_data', f'{REPO}/tools/g93/g93_data.py'); m93 = importlib.util.module_from_spec(spec); spec.loader.exec_module(m93)
ALT = [r for r in m93.R if r['key'] == 'KalterHund'][0]
HOOK = 'Wie vom Kindergeburtstag:'
PROMPT = {
 'KalterHundA': 'A loaf-shaped German Kalter Hund no-bake chocolate biscuit cake with a smooth dark chocolate coating on a white rectangular serving platter seen from the front at a 30 degree angle, the whole platter fully visible with empty table space left and right of it, the front end cut off so the cut face shows many thin horizontal layers alternating pale golden rectangular butter biscuits and dark chocolate cream, two thick slices leaning against each other in front of the loaf on the platter, a few rectangular butter biscuits lying beside the platter.' + G.P_END,
 'KalterHundB': 'Four thick slices of a German Kalter Hund no-bake chocolate biscuit cake arranged overlapping like fallen dominoes on an oval white serving plate seen from the front at a 30 degree angle, the whole plate fully visible with empty table space left and right of it, the cut sides facing the camera clearly showing many thin horizontal layers alternating pale golden rectangular butter biscuits and dark chocolate cream, three rectangular butter biscuits lying beside the plate.' + G.P_END,
}
NEU = {}
for key in PROMPT:
    r = copy.deepcopy(ALT); r['key'] = key; r['hook_alt'] = ALT['hook']; r['prompt_alt'] = ALT['prompt']; r['hook'] = HOOK; r['prompt'] = PROMPT[key]
    assert G.macros4(r) == G.macros4(ALT) == (125, 4, 15, 5) and r['titel'] == ALT['titel'] and r['hook'] != ALT['hook']
    NEU[key] = r
PREP = {'KalterHundA': dict(s=0.74, glatt=True, mirror=True),   # gespiegelt: Kekse liegen rechts frei statt halb hinter dem Vorher-Nachher-Foto (gespiegelter Rand 'ref' erzeugt hier einen zweiten Kuchen am linken Rand → nicht nehmen)
        'KalterHundB': dict(s=0.70, glatt=True)}               # Teller am linken Bildrand angeschnitten → Randspalte wiederholen (gespiegelt entstünde ein zweiter Tellerrand)

if __name__ == '__main__':
    ap = f'{D}/hero/_auswahl.json'; A = json.load(open(ap))
    for k in NEU: A[k] = f'{k}_s1'
    json.dump(A, open(ap, 'w'), indent=1)
    import prep106
    for k, t in PREP.items(): prep106.T[k] = t; prep106.prep(k)
    import render106
    G.R = list(G.R) + list(NEU.values())
    render106.render(list(NEU))
