# Konzept 2 – Zubereitung oben, fertiges Gericht unten (9.11.2026)

Muster nach Kevs Oktober-Beispielen: oben Hände mitten im Zubereitungsschritt, unten das fertige Gericht groß,
schmale weiße Trennlinie, kleines Label (Rezeptname in Kaushan + kcal in Rot), „@fitmitkev“ dezent unten rechts.
Auf Kevs Wunsch zusätzlich Variante mit Zutaten-Kachelspalte links (compose_tiles).

- Fotos: FLUX.1-dev über HF-Job `scripts/jobs_k2.py` (Dataset kevrsztorm/fitmitkev-bilder), je Rezept top 1152x640 + bot 1152x768,
  4 Seeds, Kevs helle Küche (Anthrazit-Platte, weiße Fronten). Für die Kachel-Variante die Zubereitung mit Form/Topf in der rechten Bildhälfte prompten.
- `compose.py`: compose(key, top, bot, out) bzw. compose_tiles(...) – Pfade: fonts/gf/ofl, tilex/tiles_orig, g87/g87_data.py (Rezeptdaten).
- Muster: `misc/k2/`. Entscheidung von Kev stand am 9.11. mittags noch aus (Vorschlag: 2–3 Beiträge am Dienstag testen).
