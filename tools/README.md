# Board-Werkzeuge (Stand 11.11.2026)

Alles, was zum Bauen der Facebook-Rezeptboards im Original-Look nötig ist. Nach einem Reset des Arbeitsbereichs:

    git clone --depth 1 https://github.com/phj4t84dpj-byte/fitmitkev-bilder.git
    python3 fitmitkev-bilder/tools/einrichten.py <arbeitsordner>

`<arbeitsordner>` liegt außerhalb des Repos (z. B. der Scratchpad der Session). `einrichten.py` legt die Ordner so an,
wie die Skripte sie erwarten (Schriften unter `fonts/gf/ofl/…`, Kacheln unter `tilex/tiles_orig/`, je Serie `assets/`,
`raw/`, `hero/`, `out/`), und kopiert die Serien g87–g90 hinein. Geprüft am 11.11.2026: ein Board aus dem frisch
eingerichteten Ordner stimmt mit dem veröffentlichten überein.

Braucht Python mit Pillow, numpy, OpenCV (`cv2`), scipy und Playwright mit Chromium.

## Neueste Serie: `g90/` (Vorlage für die nächste – kopieren und 90 → 91 umbenennen)

1. `g90_data.py` – Rezepte (`R`-Liste: key, Hook, Titelzeilen, Zutaten mit Kachelname, Vergleichswert, Hashtags).
   Die Nährwert-Tabellen kommen aus `g89_data.py` ← `g88_data.py` ← `g87_data.py`. Die Prüfungen am Dateiende
   (höchstens 8 Kacheln, Hauptgerichte ≤ 500 kcal, Hashtag-Zahl je Beitrag) laufen bei jedem Import.
2. `jobs_g90.py`, `jobs_g90b.py` – Bild-Prompts (FLUX.1-dev über Hugging-Face-Jobs, 1024 × 1280) und Prompts für neue
   Zutaten-Kacheln. Prompts nur positiv formulieren – Verneinungen erzeugen das Verneinte.
3. `grab.py Name=Kennung …` – angehängte Bilder nach `raw/` kopieren (Zuordnung nur über die Kennung aus der
   Tool-Ausgabe). Die Auswahl je Rezept steht in `hero/_auswahl.json` (im Repo: `auswahl.json`).
4. `prep.py [Key …]` – gewähltes Bild spiegeln, verkleinern, verschieben (Tabelle `T`: `mirror`, `s`, `dx`, `dy`,
   `cl`, `soft`); schreibt `hero/<Key>.jpg` und `hero/_meta.json`.
5. `zones.py [Key …]` – Vorschau mit den festen Board-Zonen (`out/_zonen_<n>.jpg`): rot = Kachelspalte und Titel,
   blau = Badge und Foto, grün = Pfeil. Erst rendern, wenn jedes Gericht frei liegt.
6. `render90.py [Key …]` – Boards 2160 × 2700 nach `out/G90-<Key>.jpg` (Playwright/Chromium, Freisteller über
   `foodcut.py`, KI-Kennzeichnung per XMP). Meldet, wenn der Pfeil eine Beschriftung berührt oder die Kachelspalte
   überläuft; `ORDER` ändert die Kachel-Reihenfolge nur auf dem Board.
7. `sheet90.py` – Kontaktbögen (nie nach `boards/` kopieren). `texte90.py` – Titel, 1. Kommentar, Uhrzeiten,
   Posting-Plan, `out/donnerstag_posts.json`.
8. `payload.py <von> <bis>` – Planungsdaten je Beitrag. `verify_metricool.py` – gleicht die angelegten Beiträge
   Feld für Feld mit dem Plan ab und schreibt die id-Liste.
9. `tiles_new.py` – neue Zutaten-Kacheln freistellen (weißer Hintergrund → RGBA, Schatten entfernt).

Die Rohbilder liegen nicht hier, sondern im Hugging-Face-Dataset `kevrsztorm/fitmitkev-bilder` (Ordner `g90/`).

## Der Look (Renderer)

Playwright/Chromium, 1080 × 1350 bei 2× → 2160 × 2700. Layout nach Kevs Quarkbällchen-Referenz: Kacheln links
(Originalgröße × 1,2; bei 8 Reihen × 1,1), Menge Poppins Bold 29 px, Name Poppins SemiBold 21 px, Hook Kaushan 60 px
weiß mit Navy-Kontur, Titel Anton weiß mit blauer Kontur (#163b7d) und dunklem Schlagschatten (#0d1d42),
„hat/haben pro … nur“ 34 px, kcal-Zeile 37 px rot (#c1202b) mit durchgestrichenem Vergleichswert, Pfeil,
roter „-50 kg“-Badge, Vorher-Nachher-Foto, „@fitmitkev“. Das Gericht liegt als oberste Ebene über den Verläufen.

Feste Zonen (CSS-px): Kachelspalte 0–430 × 0–765 · Titel 380–1080 × 0–612 · Badge 100–291 × 890–951 ·
Foto 43–323 × 968–1256 · Pfeil 296–436 × 588–688. Frei für das Gericht: rechts ab x ≈ 330 und unter y ≈ 650.

## Übrige Ordner

- `tiles_orig/` – Zutaten-Kacheln (154 Stück, RGBA-PNG, Maßstab des 2160er-Boards). 147 wurden am 9.11.2026 aus
  den gesicherten Boards G78–G86 wieder ausgeschnitten (`tilex/`, Herkunft in `_index.json`), 7 sind neu erzeugt
  (ketchup, kokosraspel, eierlikoer, loeffelbiskuit, banane, gnocchi, vollkornbrot).
  `_map_g87.json` = Zuordnung Rezept-Kachelname → Datei.
- `fonts/` – Anton, Kaushan Script, Poppins Bold/SemiBold (SIL Open Font License, `OFL.txt`).
- `render/vorher_nachher.jpg` – das Vorher-Nachher-Foto für die Boards.
- `tilex/` – Werkzeug, mit dem die Kacheln aus fertigen Boards zurückgeholt wurden (Hintergrund-Differenz,
  Zuordnung über `archiv/rezepte.json` bzw. OCR der Textspalte).
- `g87/`–`g89/` – frühere Serien; g87 ist der erste Renderer nach dem Neuaufbau, g89 brachte `prep.py`.
- `k2/` – Muster für ein zweiteiliges Board (Zubereitung oben, Gericht unten). `styles/` – Farb- und
  Schriftvarianten, nicht in Gebrauch.
