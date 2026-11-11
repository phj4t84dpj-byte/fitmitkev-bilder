#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arbeitsbereich für die Board-Werkzeuge aus dem Repo aufbauen (nach einem Reset oder in einem neuen Chat).

Die Skripte in tools/g87 … g90 erwarten die Ordner so, wie sie im Arbeitsbereich der Session lagen:
  <ziel>/fonts/gf/ofl/anton/Anton-Regular.ttf · …/kaushanscript/KaushanScript-Regular.ttf · …/poppins/Poppins-{Bold,SemiBold}.ttf
  <ziel>/tilex/tiles_orig/*.png + _map_g87.json     Kachel-Bibliothek (neue Kacheln landen hier)
  <ziel>/g87, g88, g89, g90, …                      Skripte je Serie (g90 holt Tabellen aus g89 ← g88 ← g87)
  <ziel>/<serie>/assets/vorher_nachher.jpg, raw/, hero/, out/

Aufruf:  python3 tools/einrichten.py <ziel>
<ziel> ist ein Ordner AUSSERHALB des Repos (z. B. der Scratchpad der Session). Vorhandene Dateien bleiben unangetastet.

Danach:
  cd <ziel>/g90 && python3 prep.py <Key> && python3 render90.py <Key>
    braucht raw/<Name>.jpg – die Rohbilder liegen nicht auf GitHub, sondern auf Hugging Face
    (Dataset kevrsztorm/fitmitkev-bilder, Ordner g90/): hf_fs attach, dann grab.py Name=Kennung.
  Neue Serie: <ziel>/g90 nach <ziel>/g91 kopieren, Dateien und Bezeichner 90 → 91 umbenennen,
    Rezepte (g91_data.py), Prompts (jobs_g91.py) und Texte (texte91.py) neu schreiben.
  Neue Kacheln aus <ziel>/tilex/tiles_orig am Ende nach tools/tiles_orig zurückkopieren und committen.

Braucht Python mit Pillow, numpy, OpenCV (cv2), scipy und Playwright mit Chromium.
"""
import os, sys, shutil, glob

R = os.path.dirname(os.path.abspath(__file__))  # …/tools
FONTS = {'Anton-Regular.ttf': 'anton', 'KaushanScript-Regular.ttf': 'kaushanscript',
         'Poppins-Bold.ttf': 'poppins', 'Poppins-SemiBold.ttf': 'poppins'}


def cp(src, dst):
    """Kopiert, ohne Vorhandenes zu überschreiben. Gibt 1 zurück, wenn kopiert wurde."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst):
        return 0
    shutil.copy2(src, dst)
    return 1


def main(ziel):
    ziel = os.path.abspath(ziel)
    repo = os.path.dirname(R)
    if (ziel + os.sep).startswith(repo + os.sep):
        raise SystemExit('Ziel muss außerhalb des Repos liegen (das Repo soll ohne unversionierte Dateien bleiben).')
    n = 0
    for f, d in FONTS.items():
        n += cp(f'{R}/fonts/{f}', f'{ziel}/fonts/gf/ofl/{d}/{f}')
    for f in glob.glob(f'{R}/tiles_orig/*'):
        n += cp(f, f'{ziel}/tilex/tiles_orig/{os.path.basename(f)}')
    serien = sorted((d for d in os.listdir(R) if d[:1] == 'g' and d[1:].isdigit() and int(d[1:]) >= 87),
                    key=lambda d: int(d[1:]))
    for s in serien:
        for f in glob.glob(f'{R}/{s}/*'):
            if os.path.isfile(f):
                n += cp(f, f'{ziel}/{s}/{os.path.basename(f)}')
        n += cp(f'{R}/render/vorher_nachher.jpg', f'{ziel}/{s}/assets/vorher_nachher.jpg')
        for sub in ('raw', 'hero', 'out'):
            os.makedirs(f'{ziel}/{s}/{sub}', exist_ok=True)
        # Dateien, die die Skripte in Unterordnern erwarten (im Repo liegen sie flach im Serienordner)
        if os.path.exists(f'{R}/{s}/auswahl.json'):
            n += cp(f'{R}/{s}/auswahl.json', f'{ziel}/{s}/hero/_auswahl.json')
        for j in glob.glob(f'{R}/{s}/*_posts.json') + glob.glob(f'{R}/{s}/*_metricool_ids.json'):
            n += cp(j, f'{ziel}/{s}/out/{os.path.basename(j)}')
    print(f'{n} Dateien nach {ziel} kopiert · Serien: {", ".join(serien)} · neueste: {serien[-1]}')
    print(f'Weiter: cd {ziel}/{serien[-1]}  (Rohbilder nach raw/ holen, dann prep.py und render{serien[-1][1:]}.py)')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
