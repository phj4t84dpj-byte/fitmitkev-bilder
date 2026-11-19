# Prüfseite „ESN-Black-Week-Beiträge“ (19.11.2026)

Kev wollte alle ESN-Black-Week-Infobeiträge (P1–P11) auf einer Seite sehen und direkt unter jedem Bild schreiben, was anders sein soll.

- Seite: https://claude.ai/artifact/Wp6rMK53G8j7hi8TVUFEZe (privat, nur Kev)
- Kevs Anmerkungen liegen in der Datenbank der Seite, Sammlung `anmerkungen`, je Beitrag ein Dokument `P1` … `P11` mit `text`, `ok` (true = „Passt so“) und `stand`. Auslesen mit dem Werkzeug ArtifactData (`list`, Sammlung `anmerkungen`).
- Bauen: `build.py` neben `vorlage.html` und `esn_produkt_posts.json` (aus `tools/esn_produkt/produkt_texte.py`) legen, Ordner `img/` anlegen, ausführen; ergibt `index.html` und `img/P1.jpg` … `img/P11.jpg` (1080 × 1350). Veröffentlichen mit denselben Dateipfaden, Fähigkeit `db`.
- Nach Änderungen an einem Board: Bild neu rendern, `build.py` laufen lassen, Seite neu veröffentlichen. Die Anmerkungen bleiben erhalten.
