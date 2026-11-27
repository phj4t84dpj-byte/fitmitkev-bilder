# Ranking „Die 10 besten Proteinquellen“ – Werte je 100 g (gerundet, übliche Nährwerttabellen; Linsen trocken gewogen).
# Reihenfolge von Kev festgelegt (28.11., 0:09: „rote Linsen bitte auf Platz 10 und Lachs auf Platz 9“). Reihenfolge hier = Reihenfolge im Video (Platz 10 → 1).
# (key, Anzeige-Name, gesprochen, Protein g, Protein gesprochen, kcal, kcal gesprochen, Zusatz, Platz, Platz gesprochen)
ITEMS = [
 ("linsen", "Rote Linsen", "rote Linsen", 25, "fünfundzwanzig", 330, "dreihundertdreißig", "trocken gewogen", 10, "zehn"),
 ("lachs", "Lachs", "Lachs", 20, "zwanzig", 200, "zweihundert", "", 9, "neun"),
 ("skyr", "Skyr", "Skyr", 11, "elf", 63, "dreiundsechzig", "", 8, "acht"),
 ("huettenkaese", "Hüttenkäse", "Hüttenkäse", 12, "zwölf", 95, "fünfundneunzig", "", 7, "sieben"),
 ("magerquark", "Magerquark", "Magerquark", 12, "zwölf", 67, "siebenundsechzig", "", 6, "sechs"),
 ("eier", "Eier", "Eier", 13, "dreizehn", 140, "hundertvierzig", "", 5, "fünf"),
 ("garnelen", "Garnelen", "Garnelen", 20, "zwanzig", 90, "neunzig", "", 4, "vier"),
 ("rinderhack", "Rinderhack mager", "mageres Rinderhack", 21, "einundzwanzig", 140, "hundertvierzig", "", 3, "drei"),
 ("haehnchen", "Hähnchenbrust", "Hähnchenbrust", 23, "dreiundzwanzig", 105, "hundertfünf", "", 2, "zwei"),
 ("thunfisch", "Thunfisch", "Thunfisch", 25, "fünfundzwanzig", 115, "hundertfünfzehn", "im eigenen Saft", 1, "eins"),
]
INTRO = "Die zehn besten Proteinquellen im Ranking – pro hundert Gramm."
OUTRO = "Welche isst du am liebsten?"


def text():
    """Sprechertext und Wort-Indizes je Eintrag (Platz-Wort, Protein-Zahl, kcal-Zahl)."""
    teile = [INTRO]; idx = []; n = len([w for w in INTRO.split() if w != "–"])
    for i, (k, name, gespr, p, pg, kc, kg, zus, pl, plg) in enumerate(ITEMS):
        if pl == 1:
            satz = f"Und Platz {plg}: {gespr}, {pg} Gramm bei nur {kg} Kalorien."
            a = n; pz = n + 3 + len(gespr.split()); kz = pz + 4
        else:
            satz = f"Platz {plg}: {gespr}, {pg} Gramm, {kg} Kalorien."
            a = n; pz = n + 2 + len(gespr.split()); kz = pz + 2
        w = [x for x in satz.split() if x != "–"]
        idx.append((a, pz, kz)); teile.append(satz); n += len(w)
    teile.append(OUTRO)
    return " ".join(teile), idx, n


if __name__ == "__main__":
    t, idx, o = text(); print(t); w = [x for x in t.split() if x != "–"]
    for (a, pz, kz) in idx: print(w[a], "|", w[pz], "|", w[kz])
    print(w[o])
