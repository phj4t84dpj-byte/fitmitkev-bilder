# -*- coding: utf-8 -*-
"""Texte (Beitrag + 1. Kommentar) der YouTube-Reihe 30.11.–13.12.2026, täglich 15:00. Schreibt ytwoche_posts.json und
die Textdatei für Kev. Kein „abnehmen“, keine erfundenen Zutaten: das Rezept steht im Video, der Kommentar verlinkt es."""
import json, sys
R='https://raw.githubusercontent.com/phj4t84dpj-byte/fitmitkev-bilder/{c}/yt/{b}'
P=[  # datum, id, bild, name, beitrag (2 Sätze), hashtags, frage
('2026-11-30','jbviLMbSITg','YT-Ofenblech.jpg','Ofenblech mit Hähnchen und Kürbis',
 'Hähnchen, Kürbis und Kichererbsen auf einem Blech 🤤 100 g Eiweiß auf dem ganzen Blech.','Einmal schnippeln, ab in den Ofen, fertig.',['#ofenblech','#kürbis'],'Kürbis aus dem Ofen: Ja oder nein?'),
('2026-12-01','gVKFErcJpCc','YT-SpekulatiusCheesecake.jpg','Spekulatius-Cheesecake',
 'Spekulatius-Cheesecake unter 200 kcal pro Stück 😍','Cremig, mit knusprigen Spekulatius-Streuseln – perfekt für die Adventszeit.',['#spekulatius','#cheesecake'],'Spekulatius oder lieber Lebkuchen?'),
('2026-12-02','-srhq33xMGY','YT-CheeseburgerTaschen.jpg','Cheeseburger-Taschen',
 'Cheeseburger-Taschen mit 365 kcal und 27 g Eiweiß 🍔','Saftiges Hack und geschmolzener Käse im knusprigen Teig.',['#cheeseburger','#fastfood'],'Burger lieber klassisch oder als Tasche?'),
('2026-12-03','TZUXs6jSD3c','YT-SpaetzlePfanne.jpg','Spätzle-Pfanne mit Pilzen und Erbsen',
 'Spätzle-Pfanne mit Pilzen und Erbsen 😋 80 g Eiweiß in der ganzen Pfanne.','Cremig, schnell und alles aus einer Pfanne.',['#spätzle','#pfanne'],'Spätzle: selbst gemacht oder aus dem Kühlregal?'),
('2026-12-04','w-dmnnDt7jw','YT-ProteinKuchen.jpg','3 Protein-Kuchen: Kirsch, Zitrone, Apfel',
 '3 Kuchen, jeder unter 500 kcal und mit über 30 g Eiweiß 🥰','Kirsch, Zitrone und Apfel – such dir deinen Favoriten aus.',['#kuchen','#proteinkuchen'],'Welcher wäre dein Favorit: Kirsch, Zitrone oder Apfel?'),
('2026-12-05','HjmsgKJlWzg','YT-AirfryerDrei.jpg','3 Airfryer-Rezepte unter 300 kcal',
 '3 Rezepte aus der Heißluftfritteuse, jedes unter 300 kcal 🤗','Herzhaft und süß – alle drei schnell gemacht.',['#airfryer','#heißluftfritteuse'],'Hast du schon eine Heißluftfritteuse?'),
('2026-12-06','nrhnicOIdVM','YT-Lahmacun.jpg','Lahmacun',
 'Lahmacun unter 200 kcal pro Stück 🤤','Dünn, knusprig und mit würzigem Hack – wie vom Imbiss.',['#lahmacun','#türkischeküche'],'Lahmacun mit oder ohne Salat?'),
('2026-12-07','0mFJBHReQq8','YT-ButterChicken.jpg','Butter Chicken mit Reis',
 'Butter Chicken mit Reis unter 600 kcal 😍','Cremig wie beim Inder, nur leichter.',['#butterchicken','#curry'],'Isst du gern indisch?'),
('2026-12-08','yyekUrb68mI','YT-Pizza.jpg','Pizza mit Gemüse',
 'Pizza mit 87 g Eiweiß 😋','Mit Brokkoli und Mais – und trotzdem richtig Pizza.',['#pizza','#pizzaliebe'],'Was gehört für dich auf die perfekte Pizza?'),
('2026-12-09','HDrF1P3y8X0','YT-AirfryerPide.jpg','Pide und gefüllte Paprika aus dem Airfryer',
 'Pide und gefüllte Paprika aus der Heißluftfritteuse, jedes unter 300 kcal 🥰','Beides schnell gemacht, beides mit überbackenem Käse.',['#airfryer','#pide'],'Pide oder gefüllte Paprika: Was machst du zuerst?'),
('2026-12-10','Qjecnj9RH10','YT-OrangeChicken.jpg','Orange Chicken mit Reis',
 'Orange Chicken mit Reis für 500 kcal 🤗','Mit Paprika, Brokkoli und Sesam – wie vom Asia-Imbiss.',['#orangechicken','#asiatisch'],'Asia-Imbiss oder lieber selbst kochen?'),
('2026-12-11','_QwmE8IggaY','Facebook_Langos.jpg','Lángos wie vom Weihnachtsmarkt',
 'Lángos wie vom Weihnachtsmarkt, unter 400 kcal pro Stück 🎄','Aus dem Ofen, ohne Hefe und ohne Fritteuse – in drei Sorten.',['#langos','#weihnachtsmarkt'],'Lángos klassisch, süß oder mit Pesto?'),
('2026-12-12','lEpsQPmeOZM','Facebook_Kloesse.jpg','Überbackene Klöße mit Hack und Käse',
 'Überbackene Klöße mit Hack und Käse 🤤 395 kcal und 33 g Eiweiß pro Portion.','Aus fertigem Kloßteig, alles in einer Form.',['#klöße','#kloßteig'],'Klöße mit Käse überbacken: schon mal probiert?'),
('2026-12-13','7MlDFtuRUHg','YT-FrostaTest.jpg','5 Frosta-Gerichte im Test',
 'Diätretter oder Kalorienfalle? Ich habe 5 Frosta-Gerichte getestet 👀','Eins hat mich richtig überrascht – und eins hat 700 kcal.',['#tiefkühlkost','#frosta'],'Welches Fertiggericht isst du am liebsten?'),
]
c=sys.argv[1] if len(sys.argv)>1 else 'COMMIT'
out=[]; txt=['YOUTUBE-REIHE 30.11.–13.12.2026 – täglich 15:00 Uhr (Facebook)\n']
for d,vid,bild,name,s1,s2,tags,frage in P:
    rezept=vid!='7MlDFtuRUHg'
    text=f"{s1}\n\n{s2} {'Wie ich es mache, zeige ich dir Schritt für Schritt im Video.' if rezept else 'Alle Ergebnisse siehst du im Video.'}\n\nLink zum Video im 1. Kommentar ⤵️\n\n{' '.join(tags+['#fitmitkev'])}"
    fc=f"Hier geht's zum ganzen Video: https://youtu.be/{vid}\n\n{name}\n\n{'Zutaten und Zubereitung zeige ich dir Schritt für Schritt im Video.' if rezept else 'Welches Gericht mich überzeugt hat und welches nicht, siehst du im Video.'}\n\nBleib satt! 💪\nKev\n\n{frage}"
    ordner='yt' 
    out.append({'datum':f'{d}T15:00:00','id':vid,'name':name,'text':text,'fc':fc,'media':R.format(c=c,b=bild),'alt':name})
    txt.append(f"\n==================== {d} 15:00 – {name} ====================\nBild: {bild}\n\n--- BEITRAGSTEXT ---\n{text}\n\n--- 1. KOMMENTAR ---\n{fc}\n")
    assert 'abnehm' not in (text+fc).lower(), name
json.dump(out,open('ytwoche_posts.json','w'),ensure_ascii=False,indent=1)
open('YouTube-Reihe-Texte.txt','w').write(''.join(txt)); print(len(out),'Beiträge')
