# -*- coding: utf-8 -*-
"""Neue Zutaten-Kachel aus einem Produktfoto mit GLASSCHALE auf weißem Hintergrund freistellen.
Der übliche Weg (tools/g93/tiles_new.py, cut_white) entfernt helle farblose Flächen – bei Glas bliebe nur der Inhalt übrig.
Hier: Inhalt (kräftige Farbe) deckend, Glas halb durchsichtig (weißer Schleier + graue Kanten), Umriss = konvexe Hülle von Inhalt und Glaskanten.
Aufruf: python3 kachel_glas.py <bild.jpg> <ziel.png> [Zielgröße=150]"""
import sys, numpy as np, cv2
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
def cut(path, target=150):
    im = Image.open(path).convert('RGB'); a = np.asarray(im).astype(np.float32)
    mx = a.max(2); mn = a.min(2); sat = (mx - mn) / (mx + 1e-6)
    inhalt = sat > 0.22
    kante = mn < 236
    core = ndi.binary_closing(inhalt | kante, iterations=4)
    lab, n = ndi.label(core); sizes = ndi.sum(core, lab, range(1, n + 1)); core = lab == (1 + int(np.argmax(sizes)))
    pts = cv2.findNonZero(core.astype(np.uint8)); hull = cv2.convexHull(pts)
    m = np.zeros(core.shape, np.uint8); cv2.fillConvexPoly(m, hull, 1); m = m.astype(bool)
    inhalt = ndi.binary_fill_holes(ndi.binary_closing(inhalt, iterations=3)) & m
    glas = np.clip(0.30 + (255 - mn) / 70.0, 0, 0.95)                 # fast weißes Glas: leichter Schleier; graue Kanten: fast deckend
    alpha = np.where(inhalt, 1.0, glas) * m
    alpha = ndi.gaussian_filter(alpha, 1.2) * ndi.gaussian_filter(m.astype(np.float32), 1.0).clip(0, 1)
    rgba = np.dstack([a, alpha * 255]).astype(np.uint8)
    ys, xs = np.where(m); t = Image.fromarray(rgba, 'RGBA').crop((xs.min() - 4, ys.min() - 4, xs.max() + 5, ys.max() + 5))
    s = target / max(t.width, t.height); t = t.resize((round(t.width * s), round(t.height * s)), Image.LANCZOS)
    pad = 24; canvas = Image.new('RGBA', (t.width + 2 * pad, t.height + 2 * pad), (0, 0, 0, 0))
    hard = Image.fromarray((np.asarray(Image.fromarray((m * 255).astype(np.uint8)).crop((xs.min() - 4, ys.min() - 4, xs.max() + 5, ys.max() + 5)).resize(t.size, Image.LANCZOS))).astype(np.uint8))
    sh = Image.new('RGBA', canvas.size, (0, 0, 0, 0)); al = Image.new('L', canvas.size, 0); al.paste(hard, (pad + 3, pad + 10))
    al = al.filter(ImageFilter.GaussianBlur(7)).point(lambda v: int(v * 0.45)); sh.paste((45, 32, 20, 255), (0, 0), al)
    canvas = Image.alpha_composite(canvas, sh); canvas.alpha_composite(t, (pad, pad)); return canvas
if __name__ == '__main__':
    out = cut(sys.argv[1], int(sys.argv[3]) if len(sys.argv) > 3 else 150); out.save(sys.argv[2]); print(sys.argv[2], out.size)
