# Board-Werkzeuge (Sicherung, Stand 9.11.2026)

Alles, was zum Bauen der Facebook-Rezeptboards im Original-Look nötig ist. Nach einem Reset des Arbeitsbereichs
reicht `git clone --depth 1 https://github.com/phj4t84dpj-byte/fitmitkev-bilder.git` und dieser Ordner.

- `tiles_orig/` – **die Original-Zutatenkacheln** (150 Stück, RGBA-PNG, Maßstab 2160er-Board), am 9.11.2026 aus den
  gesicherten Boards G78–G86 wieder ausgeschnitten (`tilex/`). `_index.json` = Herkunft, `_map_g87.json` = Zuordnung
  Rezept-Kachelname → Datei. Neue Kacheln: FLUX-Job (`g87/jobs_tiles87.py`), weißer Hintergrund, freistellen wie
  `tilex/build_tiles.py: cut_white()`.
- `g87/render87.py` – Renderer (Playwright/Chromium, 1080×1350 bei 2× → 2160×2700, XMP-KI-Kennzeichnung).
  Layout nach Kevs Quarkbällchen-Referenz: Kacheln links (Originalgröße ×1,2), Menge Poppins Bold 29 px,
  Name Poppins SemiBold 21 px, Hook Kaushan 60 px weiß mit Navy-Kontur, Titel Anton weiß mit blauer Kontur
  (#163b7d) und dunklem Schlagschatten (#0d1d42), „hat/haben pro … nur“ 34 px, kcal-Zeile 37 px rot (#c1202b),
  Pfeil, roter „-50 kg“-Badge, Vorher-Nachher-Foto (`render/vorher_nachher.jpg`), „@fitmitkev“.
  Pfade oben im Skript anpassen (`F` Schriften, `TL` Kacheln).
- `g87/g87_data.py` – Rezeptdaten-Muster (NUT/PIECE-Nährwerttabelle, `Z()`-Zutaten mit Kachelname, `macros4`).
- `g87/texte87.py` – Titel (kurz, „Höfliche Menschen“ jeder 3.), 1. Kommentar, Posting-Plan, `montag_posts.json`.
- `fonts/` – Anton, Kaushan Script, Poppins Bold/SemiBold (SIL Open Font License, `OFL.txt`).
- `tilex/` – Werkzeug, mit dem die Kacheln aus fertigen Boards zurückgeholt wurden (Hintergrund-Differenz,
  Zuordnung über `archiv/rezepte.json` bzw. OCR der Textspalte).
