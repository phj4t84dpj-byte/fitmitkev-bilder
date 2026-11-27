# 10 Proteinquellen, Werte je 100 g (gerundet, übliche Nährwerttabellen; Linsen trocken gewogen)
# (key, Anzeige-Name, gesprochen, Protein g, Protein gesprochen, kcal, kcal gesprochen, Zusatz)
ITEMS = [
 ("skyr", "Skyr", "Skyr", 11, "elf", 63, "dreiundsechzig", ""),
 ("magerquark", "Magerquark", "Magerquark", 12, "zwölf", 67, "siebenundsechzig", ""),
 ("huettenkaese", "Hüttenkäse", "Hüttenkäse", 12, "zwölf", 95, "fünfundneunzig", ""),
 ("eier", "Eier", "Eier", 13, "dreizehn", 140, "hundertvierzig", ""),
 ("lachs", "Lachs", "Lachs", 20, "zwanzig", 200, "zweihundert", ""),
 ("garnelen", "Garnelen", "Garnelen", 20, "zwanzig", 90, "neunzig", ""),
 ("rinderhack", "Rinderhack mager", "Mageres Rinderhack", 21, "einundzwanzig", 140, "hundertvierzig", ""),
 ("haehnchen", "Hähnchenbrust", "Hähnchenbrust", 23, "dreiundzwanzig", 105, "hundertfünf", ""),
 ("thunfisch", "Thunfisch", "Thunfisch", 25, "fünfundzwanzig", 115, "hundertfünfzehn", "im eigenen Saft"),
 ("linsen", "Rote Linsen", "Und rote Linsen", 25, "fünfundzwanzig", 330, "dreihundertdreißig", "trocken gewogen"),
]
INTRO = "Zehn Proteinquellen – alle Werte pro hundert Gramm."
OUTRO = "Welche ist dein Favorit?"


def text():
    """Sprechertext und Wort-Indizes je Eintrag (Name, Protein-Zahl, kcal-Zahl)."""
    teile = [INTRO]; idx = []; n = len([w for w in INTRO.split() if w != "–"])
    for i, (k, name, gespr, p, pg, kc, kg, zus) in enumerate(ITEMS):
        satz = f"{gespr}: {pg} Gramm{' Protein' if i == 0 else ''}, {kg} Kalorien."
        if zus == "trocken gewogen": satz = satz[:-1] + " – trocken gewogen."
        w = [x for x in satz.split() if x != "–"]
        a = n; pz = n + len(gespr.split()); kz = pz + (3 if i == 0 else 2)
        idx.append((a, pz, kz)); teile.append(satz); n += len(w)
    teile.append(OUTRO); idx_outro = n
    return " ".join(teile), idx, idx_outro


if __name__ == "__main__":
    t, idx, o = text(); print(t); w = [x for x in t.split() if x != "–"]
    for (a, pz, kz) in idx: print(w[a], "|", w[pz], "|", w[kz])
    print(w[o])
