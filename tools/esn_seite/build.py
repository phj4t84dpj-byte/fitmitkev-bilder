# -*- coding: utf-8 -*-
# Baut die Prüfseite „ESN-Black-Week-Beiträge“: alle Beiträge ab Sa 21.11. in der geplanten Reihenfolge –
# 5 persönliche (K1–K5, Kevs Fotos) und die Infobeiträge (P1–P11 ohne P5). Unter jedem Bild ein Feld für Kevs Änderungswünsche
# (db-Sammlung „anmerkungen“, je Beitrag ein Dokument mit text, ok, erledigt, stand).
import json, os, re, glob, datetime
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/claude/fitmitkev-bilder"
WT = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
ENT = open(f"{REPO}/tools/gesn/ESN-persoenliche-Beitraege-Entwurf.txt").read()

def abschnitt(kopf):
    i = ENT.index(kopf); j = ENT.index("=====", i)
    body = ENT[i:j].split("-" * 20, 1)[1].lstrip("-").strip()
    txt, fc = body.split("1. KOMMENTAR:")
    assert txt.strip().startswith("Werbung") and fc.strip().startswith("Werbung:"), kopf
    return txt.strip(), fc.strip()

def slot(datum, zeit):
    d = datetime.date.fromisoformat(datum)
    return f"{WT[d.weekday()]} {d.day}.{d.month}. · {zeit} Uhr"

for f in glob.glob(f"{D}/img/*.jpg"): os.remove(f)
def bild(src, name, breit):
    im = Image.open(src).convert("RGB")
    h = round(im.height * breit / im.width)
    im.resize((breit, h), Image.LANCZOS).save(f"{D}/img/{name}.jpg", quality=88, optimize=True)
    return dict(src=f"img/{name}.jpg", w=breit, h=h)

data = []
# Infobeiträge
p1t, p1fc = abschnitt("4) SO 22.11., 12:00")
info = [dict(datum="2026-11-22", zeit="12:00", datei="ESN-P1-Einkaufszettel", text=p1t, fc=p1fc, alt="Mein Einkaufszettel")] + json.load(open(f"{REPO}/tools/esn_produkt/esn_produkt_posts.json"))
for p in info:
    num = re.match(r"ESN-(P\d+)-", p["datei"]).group(1)
    data.append(dict(id=num, art="info", titel=p["alt"], slot=slot(p["datum"], p["zeit"]), wann=p["datum"] + "T" + p["zeit"],
                     bilder=[bild(f"{REPO}/esn/posts/{p['datei']}.jpg", num, 1080)], text=p["text"], fc=p["fc"]))
# Persönliche Beiträge mit Kevs Fotos
# K1 und K2 seit 19.11. (Kev: „auch im Info-Design, nur ein Bild pro Beitrag“) als Board aus esn_board.py
K = [("K1", "2) SA 21.11., 11:00", "2026-11-21", "11:00", "Ankündigung: Das nehme ich selbst", "ESN-K1-Ankuendigung", ""),
     ("K2", "3) SO 22.11., 6:10", "2026-11-22", "06:10", "Start-Tag: Heute um 12 Uhr geht's los", "ESN-K2-Start", ""),
     ("K3", "5) FR 27.11., 18:30", "2026-11-27", "18:30", "Black Friday: mein Vorrat", ["Kev-Riegel-6-Sorten-schraeg"], "Im Text fehlt noch, was du selbst bestellt hast. Schreib es mir hier ins Feld."),
     ("K4", "6) MI 2.12., 6:10", "2026-12-02", "06:10", "Letzter Tag: nur noch bis 17:30 Uhr", ["Kev-Riegel-angeschnitten"], ""),
     ("K5", "7) MI 2.12., 15:30", "2026-12-02", "15:30", "Erinnerung: noch 2 Stunden", ["Kev-Isoclear-3-Glaeser-schraeg"], "")]
for kid, kopf, datum, zeit, titel, fotos, hinweis in K:
    txt, fc = abschnitt(kopf)
    if isinstance(fotos, str):
        bs = [bild(f"{REPO}/esn/posts/{fotos}.jpg", kid, 1080)]; art = "info"
    else:
        bs = [bild(f"{REPO}/esn/bilder/kev/{f}.jpg", kid + ("abc"[i] if len(fotos) > 1 else ""), 1280) for i, f in enumerate(fotos)]; art = "persoenlich"
    data.append(dict(id=kid, art=art, titel=titel, slot=slot(datum, zeit.lstrip("0")), wann=datum + "T" + zeit, bilder=bs, text=txt, fc=fc, hinweis=hinweis))
data.sort(key=lambda x: x["wann"])
ids = [x["id"] for x in data]
assert len(ids) == 15 and "P5" not in ids, ids
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
html = open(f"{D}/vorlage.html").read().replace("/*__POSTS__*/[]", blob)
open(f"{D}/index.html", "w").write(html)
files = sorted(os.path.basename(f) for f in glob.glob(f"{D}/img/*.jpg"))
json.dump({f"img/{f}": f"img/{f}" for f in files}, open(f"{D}/_files.json", "w"))
print("Reihenfolge:", " ".join(f"{x['id']}({x['slot']})" for x in data))
print(len(files), "Bilder", sum(os.path.getsize(f"{D}/img/{f}") for f in files) // 1024, "KB ·", len(html) // 1024, "KB Seite")
