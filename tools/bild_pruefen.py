# -*- coding: utf-8 -*-
"""Prüft neue Boards gegen ALLE Boards im Repo: Lief dieses Bild (oder fast dasselbe) schon einmal?

Regel seit Sa 28.11.2026 (Kev): KEIN BILD LÄUFT ZWEIMAL. Jede Wiederholung eines Rezepts bekommt ein neues Foto.
Auch „fast gleich“ zählt als schon gezeigt (dasselbe Foto mit/ohne Box, andere Schreibschrift-Zeile).

Fingerabdruck: Bild auf 64x64 Graustufen, 2D-Kosinus-Transformation, die 255 gröbsten Anteile, jeweils über/unter Median.
Abstand = Zahl der abweichenden Stellen (0–255):
   0– 2   dasselbe Bild, nur neu gerendert
  22–38   dasselbe Foto mit/ohne Box bzw. mit anderer Schrift
  ab 44   neues Foto desselben Rezepts (gemessen 44–124)
Grenze: Abstand > 40. Achtung: Verschiedene Gerichte im gleichen Layout können auch unter 40 liegen –
„fast gleich“ gilt deshalb nur, wenn es dasselbe Gericht ist (Dateinamen ansehen).

Aufruf:  python3 tools/bild_pruefen.py <neues Board.jpg> [...]        (Vergleich mit boards/**/*.jpg, ohne die Datei selbst)
         python3 tools/bild_pruefen.py --alle-neu a.jpg b.jpg ...     zusätzlich die neuen untereinander vergleichen
"""
import os, sys, glob
import numpy as np
from PIL import Image
from scipy.fft import dctn

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRENZE = 40


def ph(path, n=16, s=64):
    im = Image.open(path)
    im.draft('L', (s * 4, s * 4))                      # JPEG gleich verkleinert dekodieren (schnell)
    im = im.convert('L').resize((s, s), Image.LANCZOS)
    d = dctn(np.asarray(im, dtype=float), norm='ortho')[:n, :n].flatten()[1:]
    return d > np.median(d)


def alle_boards():
    fs = sorted(set(glob.glob(f'{REPO}/boards/**/*.jpg', recursive=True)))
    return fs


def pruefe(neu, zeige=4, untereinander=False):
    alt = alle_boards()
    neu_abs = [os.path.abspath(p) for p in neu]
    A = [(p, ph(p)) for p in alt if os.path.abspath(p) not in neu_abs]
    N = [(p, ph(p)) for p in neu_abs]
    ok = True
    for p, h in N:
        d = sorted(((int((h != g).sum()), q) for q, g in A))
        if untereinander:
            d = sorted(d + [(int((h != g).sum()), q) for q, g in N if q != p])
        mind = d[0][0]
        urteil = 'NEU' if mind > GRENZE else ('GLEICH' if mind <= 2 else 'ZU NAH – ansehen (dasselbe Gericht?)')
        if mind <= GRENZE: ok = False
        print(f'{os.path.basename(p)}: kleinster Abstand {mind} → {urteil}')
        for dist, q in d[:zeige]:
            print(f'     {dist:3d}  {os.path.relpath(q, REPO) if q.startswith(REPO) else q}')
    print(f'{len(A)} Boards im Repo verglichen.')
    return ok


if __name__ == '__main__':
    args = sys.argv[1:]
    unter = '--alle-neu' in args
    args = [a for a in args if a != '--alle-neu']
    if not args: raise SystemExit(__doc__)
    sys.exit(0 if pruefe(args, untereinander=unter) else 1)
