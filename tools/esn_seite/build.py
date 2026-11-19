# -*- coding: utf-8 -*-
# Baut die Prüfseite „ESN-Black-Week-Beiträge“: 11 Infobeiträge (P1–P11), unter jedem Bild ein Feld für Kevs Änderungswünsche (db-Sammlung „anmerkungen“).
import json, os, re
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/claude/fitmitkev-bilder"
WT = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
import datetime

posts = json.load(open(f"{D}/esn_produkt_posts.json"))
t = open(f"{REPO}/tools/gesn/ESN-persoenliche-Beitraege-Entwurf.txt").read()
i = t.index("4) SO 22.11., 12:00")
j = t.index("=====", i)
sec = t[i:j]
body = sec.split("-" * 20, 1)[1].lstrip("-").strip()
txt, fc = body.split("1. KOMMENTAR:")
p1 = dict(datum="2026-11-22", zeit="12:00", datei="ESN-P1-Einkaufszettel", text=txt.strip(), fc=fc.strip(), alt="Mein Einkaufszettel")
assert p1["text"].startswith("Werbung") and p1["fc"].startswith("Werbung:")
allp = [p1] + posts

data = []
for p in allp:
    num = re.match(r"ESN-(P\d+)-", p["datei"]).group(1)
    d = datetime.date.fromisoformat(p["datum"])
    slot = f"{WT[d.weekday()]} {d.day}.{d.month}. · {p['zeit']} Uhr"
    src = f"{REPO}/esn/posts/{p['datei']}.jpg"
    im = Image.open(src).convert("RGB").resize((1080, 1350), Image.LANCZOS)
    im.save(f"{D}/img/{num}.jpg", quality=88, optimize=True)
    data.append(dict(id=num, titel=p["alt"], slot=slot, bild=f"img/{num}.jpg", text=p["text"], fc=p["fc"]))
assert [x["id"] for x in data] == [f"P{n}" for n in range(1, 12)], [x["id"] for x in data]
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

html = open(f"{D}/vorlage.html").read().replace("/*__POSTS__*/[]", blob)
open(f"{D}/index.html", "w").write(html)
print("ok", len(data), sum(os.path.getsize(f"{D}/img/{x['id']}.jpg") for x in data) // 1024, "KB Bilder", len(html) // 1024, "KB Seite")
