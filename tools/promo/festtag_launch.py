# -*- coding: utf-8 -*-
"""Launch-Beiträge „Festtagsküche in leicht“ (Kev 24.11.2026): Fr 27.11. Teaser, Sa 28.11. Launch, So 29.11. (1. Advent) Festmenü.
Info-Design wie B1–B6 (Baukasten aus tools/esn_produkt/esn_board.py), ein Bild je Beitrag, Ausgabe nach verkaufsseite/.
Kalorien laut Buch (Festtagskueche-in-leicht.pdf, 24.11.2026).
Aufruf: python3 festtag_launch.py [F1 F2 F3]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'esn_produkt'))
import esn_board as E
from PIL import Image
from playwright.sync_api import sync_playwright

V = '../../verkaufsseite/'; A = '../../archiv/fotos/'
NACHT = '#1E2A4A'; BORDEAUX = '#7A2236'
ROWS_CSS = '.ri{width:108px;height:108px;overflow:hidden}.ri img{max-width:none;max-height:none;width:108px;height:108px;object-fit:cover}.rw{padding:9px 0}.msg{font-size:27px;line-height:1.3}.mid{font-size:27px}.r1{font-size:32px}'
KC = lambda n: f'{n}<br><small>kcal</small>'

SPEC = {
 'F1': dict(out='Buch-Fr-Festtag-Teaser', hook='Morgen ist es so weit:', title=['MEIN NEUES', 'REZEPTBUCH'], size=96,
   secs=[dict(lab='37 REZEPTE FÜR WEIHNACHTEN & SILVESTER', col=NACHT, type='prod', d=[
      (V + 'festtag-putenbraten.jpg', 'Festtagsbraten', 'Putenbraten, Sauerbraten, Entenbrust'),
      (V + 'festtag-raclette.jpg', 'Raclette & Fondue', 'mit Guide für den leichten Abend'),
      (A + 'g11_G11Sliders.jpg', 'Silvester-Buffet', 'Mini-Burger, Laugenkonfekt & Co.')])],
   mid='Dazu ein Festtags-Planer mit Menüs<br><span>und einem Zeitplan für Heiligabend.</span>',
   msg='Morgen um 20:15 Uhr<br><span>zeige ich dir alles.</span>',
   css='.pc img{height:250px;width:100%;object-fit:cover;border-radius:12px}.p2{font-size:22px}.msg{font-size:30px;line-height:1.3}'),
 'F2': dict(out='Buch-Sa-Festtag-Launch', hook='Endlich da:', title=['FESTTAGSKÜCHE', 'IN LEICHT'], size=100,
   secs=[dict(lab='NEU: MEIN DRITTES REZEPTBUCH', col=NACHT, type='vs', d=dict(mid='ODER',
      l=dict(title='Nur das neue Buch', img=V + 'festtag-cover-gross.jpg', rows=[('', '37 Rezepte für die Feiertage', ''), ('', 'plus Festtags-Planer', ''), ('', 'Braten, Raclette, Buffet', '')], sum='9,99 €'),
      r=dict(title='Alle 3 im Trio', img=V + 'festtag-trio-covers.png', rows=[('', '109 Rezepte', ''), ('', 'alle 3 Bücher in einer PDF', ''), ('', 'du sparst 4,98 €', '')], sum='24,99 €')))],
   mid='Du hast schon mein Paket mit 2 Büchern?<br><span>Dann hol dir einfach die Festtagsküche für 9,99 €.</span>',
   msg='Sofort als PDF aufs Handy.<br><span>Link im 1. Kommentar 👇</span>',
   css='.vimg{height:300px;max-width:100%;object-fit:contain;margin:0 auto 6px;display:block}.vc.l .vimg{border-radius:8px;box-shadow:0 6px 16px rgba(0,0,0,.28)}.vc.l{background:#e8ebf3}.vc.r{background:#f6ecdf}.vc.l .vs{color:#1E2A4A}.vc.r .vs{color:#7A2236}.vsmid{font-size:24px;width:86px;height:86px}.vr2{justify-content:center;text-align:center}.vr2 .n{flex:none}.vh{margin-bottom:12px}.msg{font-size:27px;line-height:1.3}.mid{font-size:27px}'),
 'F3': dict(out='Buch-So-Festtag-Advent-Menue', hook='Zum 1. Advent:', title=['MEIN FESTMENÜ', 'IN LEICHT'], size=100,
   secs=[dict(lab='DREI GÄNGE, PRO PERSON', col=BORDEAUX, type='rows', d=[
      (V + 'festtag-kraftbruehe.jpg', 'Vorspeise', 'Rinderkraftbrühe mit Eierstich', KC(95)),
      (V + 'festtag-putenbraten.jpg', 'Hauptgang', 'Putenbraten mit Rotkohl & Klößen', KC(530)),
      (A + 'g34_G34Herrencreme.jpg', 'Dessert', 'Herrencreme mit Schokoraspeln', KC(190))])],
   mid='Zusammen 815 kcal pro Person.<br><span>Ein klassisches Festmenü hat schnell über 2.000.</span>',
   msg='Alle drei Rezepte stehen in meiner<br><span>„Festtagsküche in leicht“. Link im 1. Kommentar 👇</span>',
   css=ROWS_CSS.replace('width:108px;height:108px;overflow:hidden', 'width:150px;height:150px;overflow:hidden').replace('width:108px;height:108px;object-fit', 'width:150px;height:150px;object-fit') + '.rw{padding:16px 0}.r2{font-size:28px}'),
}

G = '/usr/share/fonts/truetype/google-fonts'; O = '/home/claude/ebook/fonts/gf/ofl'
E.CSS = (E.CSS.replace(f"{E.F}/anton/Anton-Regular.ttf", f"{O}/anton/Anton-Regular.ttf")
              .replace(f"{E.F}/kaushanscript/KaushanScript-Regular.ttf", f"{O}/kaushanscript/KaushanScript-Regular.ttf")
              .replace(f"{E.F}/poppins/Poppins-Bold.ttf", f"{G}/Poppins-Bold.ttf")
              .replace(f"{E.F}/poppins/Poppins-SemiBold.ttf", f"{G}/Poppins-Medium.ttf"))

if __name__ == '__main__':
    E.SPEC.update(SPEC)
    OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'verkaufsseite')
    tmp = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_f.html')
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        for k in (sys.argv[1:] or list(SPEC)):
            h = E.build(k).replace('src="../../', 'src="/home/claude/fitmitkev-bilder/esn/bilder/../../')
            open(tmp, 'w').write(h); pg.goto('file://' + tmp); pg.wait_for_timeout(600)
            top = pg.evaluate("()=>Math.round(document.querySelector('.top').getBoundingClientRect().bottom)")
            pg.evaluate(f"()=>{{document.getElementById('bd').style.top='{top+18}px'}}")
            bot = pg.evaluate("()=>Math.round(document.getElementById('bd').getBoundingClientRect().bottom)")
            free = 1180 - bot
            if free > 0: pg.evaluate(f"()=>{{document.getElementById('bd').style.top='{top+18+free//2}px'}}")
            print(k, 'Inhalt unten', bot, 'OK' if bot <= 1180 else 'ZU LANG')
            pg.screenshot(path=tmp + '.png'); Image.open(tmp + '.png').convert('RGB').save(f"{OUT}/{SPEC[k]['out']}.jpg", quality=92)
        b.close()
    for f in (tmp, tmp + '.png'):
        if os.path.exists(f): os.remove(f)
