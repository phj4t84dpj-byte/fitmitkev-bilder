# Instagram fitmitkevclips (Metricool-Marke 7765790, network instagram)

Kev 15.11.2026 per Dialog: jeden Tag die 3 stärksten Facebook-Rezepte vom Vortag (Reichweite), um 12:00 · 16:00 · 19:00, nur Rezepte (kein Buch-Hinweis, kein Link).
Beitrag = dasselbe Board (static.metricool.com-URL des Facebook-Beitrags), Text = Rezeptname – kcal-Hook, darunter der komplette 1. Kommentar vom Facebook-Beitrag (ohne Namenszeile), dann 8 Instagram-Hashtags (#fitmitkev zuletzt, nie #abnehmen). instagramData {"type":"POST","isAiGenerated":true}.
Je Tag eine Datei ig_<Datum>.json mit info, id, uuid.


## Ab 16.11. (Kev, 12:29): Top 3 als Karussell „Schritt für Schritt“
- 6 Slides (3:4, 1080 × 1440): 1 Hook mit fertigem Gericht · 4 Schritte · 6 Einkaufsliste im Notiz-Look mit Folgen-Leiste.
- Bilder: Qwen-Image-Edit-2511 über ZeroGPU (kostenlos, ~20 Bilder am Tag) im HF-Job, Basis = Kevs Hand mit Schüssel in seiner Küche (`fitmitkev-karussells/cheeseburger-taschen/roh/v2/base_A.jpg`), Pfannenschritte = Kevs Pfanne auf dem Bora-Herd (`misc/karussell_pfanne_kev.jpg`). Job-Muster `scripts/jobs_ig1.py` im Dataset `kevrsztorm/fitmitkev-bilder`, Ergebnisse `fitmitkev-karussells/ig-<Datum>/roh/`.
- Renderer `tools/instagram/karussell/ig_karussell.py <rezept.json>` (Beispiele sk.json, kh.json), Slides im Repo unter `instagram/karussell/`.
- Veröffentlichung automatisch, ohne Musik (Kev per Dialog). Caption: „Na, Hunger? <Hook>“ + Rezepttext, ohne „Schmeckt nach Sünde, zählt wie Salat“.
- Erste Karussells: 16.11. 16:00 Spekulatius-Kirsch im Glas (id 429938909), 19:00 Kalter Hund (id 429985851); 12:00 Hanuta-Bowl lief noch als Einzelbild.
- 17.11.: Montagszahlen fehlten bis 10:10 → Ersatz aus So 15.11. Platz 4–6: 12:00 Hefezopf (431185838), 16:00 Eiersalat (431185952), 19:00 Lahmacun (431186409). Bilder `jobs/jobs_ig2.py`; Rendern im Scratchpad-Ordner `ig/` (dort liegen die Schriften), Einkaufsliste max. 7 Zeilen, sonst stößt sie an die Folgen-Leiste.
- 18.11.: kein Morgen-Check gelaufen → um 11:30 aus Mo 16.11. Platz 1–3 gebaut: 13:00 Quarkbällchen (432642885), 16:00 Zitronenkuchen (432644943), 19:00 Mandarinen-Bowl (432643050). Bilder scripts/jobs_ig3.py. Morgen-Check ab jetzt per send_later für den Folgetag.
