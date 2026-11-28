# -*- coding: utf-8 -*-
# N4 – Nischenseiten So 29.11.2026 (1. Advent), je Seite 5 Rezepte um 9:00 · 12:00 · 15:00 · 17:30 · 20:00.
# je Seite 5 Rezepte am Tag um 9:00 · 12:00 · 15:00 · 17:30 · 20:00. Stil wie N2: Kuchenherz + Omas Kochtopf im Zettel-Stil,
# Heißluftheld im Board-Look mit gut sichtbarem Airfryer. Keine kcal, kein Abnehm-Bezug, kein Fitmitkev. Fotos: Higgsfield gpt_image_2_6, 4:5.
# Nicht wiederholt aus N1–N3.
def Z(menge,name,tile): return dict(menge=menge,name=name,tile=tile)
ZEITEN=['09:00','12:00','15:00','17:30','20:00']
TAGE=['2026-11-29']
SEITEN={'KH':dict(name='Kuchenherz',blog='7766090',tag='#kuchenherz'),'HH':dict(name='Heißluftheld',blog='7766068',tag='#heißluftheld'),'OK':dict(name='Omas Kochtopf',blog='7766077',tag='#omaskochtopf')}
R=[]
def P(seite,tag,slot,key,name,ptitel,herz,zl,ex,aus,zeit,intro,schritte,frage,tags,prompt):
    R.append(dict(seite=seite,tag=tag,slot=slot,key=key,name=name,ptitel=ptitel,herz=herz,zl=zl,ex=ex,aus=aus,zeit=zeit,intro=intro,schritte=schritte,frage=frage,tags=tags,prompt=prompt,stil='zettel'))
def H(tag,slot,key,name,hook,titel,zutaten,ex,aus,zeit,intro,schritte,frage,tags,prompt):
    R.append(dict(seite='HH',tag=tag,slot=slot,key=key,name=name,hook=hook,titel=titel,zutaten=zutaten,ex=ex,aus=aus,zeit=zeit,intro=intro,schritte=schritte,frage=frage,tags=tags,prompt=prompt,stil='board'))


# =============================== KUCHENHERZ (So 29.11.) ===============================
P('KH',0,0,'KHButterkuchen','Butterkuchen vom Blech','Omas Butterkuchen',['Mit Butterseen obendrauf!','Knusprige Mandeln!','Wie vom Bäcker!'],
 ['500 g Mehl','250 ml Milch (lauwarm)','1 Würfel Hefe','175 g Zucker','1 Ei','250 g Butter','100 g Mandelblättchen'],['1 Prise Salz','1 Pck. Vanillezucker'],
 '1 Blech (ca. 20 Stücke)','ca. 45 Min. + 1 Std. Gehzeit',
 'Weicher Hefeteig vom Blech mit kleinen Butterseen, Zucker und knusprigen Mandeln obendrauf. Ein Stück davon und der Sonntagskaffee ist perfekt.',
 ['Hefe in der lauwarmen Milch auflösen. Mit Mehl, 75 g Zucker, Ei, Salz und 75 g weicher Butter 8 Minuten zu einem glatten Teig kneten und abgedeckt 45 Minuten gehen lassen.',
  'Den Teig auf einem Backblech mit Backpapier ausrollen und weitere 15 Minuten gehen lassen. Dann mit den Fingern viele tiefe Mulden in den Teig drücken.',
  'Die restlichen 175 g Butter in Flöckchen in die Mulden setzen. 100 g Zucker mit Vanillezucker und Mandelblättchen mischen und darüberstreuen.',
  'Bei 200 °C Ober-/Unterhitze 15–20 Minuten goldbraun backen.'],
 'Butterkuchen: lieber frisch und warm oder am nächsten Tag?','#butterkuchen #blechkuchen #hefeteig #backen',
 'A sheet of German butter cake (Butterkuchen) on a baking tray, a golden yellow yeast dough with many small dimples filled with glossy melted butter and sugar, covered with golden toasted sliced almonds, cut into squares, two squares on a small plate in front showing the soft fluffy inside.')
P('KH',0,1,'KHSchinkenhoernchen','Schinken-Käse-Hörnchen','Schinkenhörnchen',['Herzhaft und knusprig!','Ganz schnell gemacht!','Perfekt zum Brunch!'],
 ['1 Rolle Blätterteig','150 g Kochschinken','100 g Reibekäse','100 g Frischkäse','1 Ei','2 EL Sesam'],['Pfeffer','1 EL Schnittlauch'],
 '8 Hörnchen, Backblech','ca. 35 Minuten',
 'Knusprige Blätterteig-Hörnchen mit einer cremigen Füllung aus Schinken und Käse. Schnell gerollt und warm wie kalt ein Genuss.',
 ['Den Schinken fein würfeln und mit Frischkäse, Reibekäse, Schnittlauch und Pfeffer verrühren.',
  'Den Blätterteig ausrollen und in 8 Dreiecke schneiden. Auf die breite Seite jeweils etwas Füllung setzen und zur Spitze hin aufrollen.',
  'Die Hörnchen auf ein Backblech mit Backpapier legen, mit verquirltem Ei bestreichen und mit Sesam bestreuen. Bei 200 °C Ober-/Unterhitze 15–18 Minuten goldbraun backen.'],
 'Schinkenhörnchen: warm oder kalt am liebsten?','#schinkenhörnchen #blätterteig #fingerfood #backen',
 'Several golden brown flaky puff pastry croissant-shaped rolls sprinkled with sesame seeds on a wooden board, one cut in half in front showing a filling of pink ham cubes and melted creamy cheese.')
P('KH',0,2,'KHEierlikoerkuchen','Omas Eierlikörkuchen','Eierlikörkuchen',['Super saftig!','Mit Schokoguss!','Der Adventsklassiker!'],
 ['5 Eier','250 g Puderzucker','250 ml Öl','250 ml Eierlikör','125 g Mehl','125 g Speisestärke','1 Pck. Backpulver','100 g Zartbitterschoko'],['2 Pck. Vanillezucker','Butter und Mehl für die Form'],
 '1 Gugelhupf (ca. 16 Stücke)','ca. 1 Std. 15 Min.',
 'Der saftige Klassiker aus Omas Rezeptbuch: ein lockerer Gugelhupf mit Eierlikör und dunklem Schokoguss. Bleibt tagelang frisch.',
 ['Eier mit Puderzucker und Vanillezucker 5 Minuten schaumig schlagen. Öl und Eierlikör langsam unterrühren.',
  'Mehl, Speisestärke und Backpulver mischen und kurz unterrühren.',
  'Den Teig in eine gefettete und bemehlte Gugelhupfform (24 cm) füllen und bei 175 °C Ober-/Unterhitze ca. 60 Minuten backen (Stäbchenprobe).',
  'Auskühlen lassen, stürzen und mit der geschmolzenen Schokolade überziehen.'],
 'Eierlikörkuchen: mit Schokoguss oder mit Puderzucker?','#eierlikörkuchen #gugelhupf #advent #backen',
 'A tall golden yellow German eggnog bundt cake (Eierlikörkuchen) on a white cake plate, covered with a glossy dark chocolate glaze running down the ridges, one slice cut and lying on a small plate in front showing a fine moist pale yellow crumb.')
P('KH',0,3,'KHSpritzgebaeck','Omas Spritzgebäck','Omas Spritzgebäck',['Zart und mürbe!','Mit Schoko-Spitzen!','Für die Plätzchendose!'],
 ['250 g Butter (weich)','125 g Zucker','1 Pck. Vanillezucker','1 Ei','375 g Mehl','100 g gem. Mandeln','150 g Zartbitterschoko'],['1 Prise Salz','2–3 EL Milch nach Bedarf'],
 'ca. 60 Stück, 2 Backbleche','ca. 1 Std.',
 'Zartes, mürbes Spritzgebäck als Kringel, S und Stangen, die Enden in Schokolade getaucht. Gehört bei Oma in jede Plätzchendose.',
 ['Butter mit Zucker, Vanillezucker und Salz cremig rühren, dann das Ei unterrühren.',
  'Mehl und Mandeln dazugeben und zu einem glatten, weichen Teig verrühren. Ist er zu fest, etwas Milch zugeben.',
  'Den Teig in einen Spritzbeutel mit großer Sterntülle füllen und Kringel, S-Formen und Stangen auf Backbleche mit Backpapier spritzen.',
  'Bei 180 °C Ober-/Unterhitze 10–12 Minuten hellgolden backen. Auskühlen lassen und die Enden in geschmolzene Schokolade tauchen.'],
 'Spritzgebäck: mit Schokolade oder ganz pur?','#spritzgebäck #plätzchen #weihnachtsbäckerei #backen',
 'Many pale golden German piped butter cookies (Spritzgebäck) shaped as rings, S-shapes and ridged sticks with star-shaped grooves, some ends dipped in dark chocolate, piled on a vintage plate and a few lying on the table in front.')
P('KH',0,4,'KHRotweinkuchen','Rotweinkuchen mit Schokolade','Rotweinkuchen',['Saftig und schokoladig!','Mit Zimt und Kakao!','Perfekt im Advent!'],
 ['250 g Butter','200 g Zucker','4 Eier','250 g Mehl','125 ml Rotwein','100 g Schokoraspel','2 EL Kakao','1 Pck. Backpulver'],['1 Pck. Vanillezucker','1 TL Zimt','Puderzucker zum Bestäuben'],
 '1 Kastenform 30 cm (ca. 16 Scheiben)','ca. 1 Std. 15 Min.',
 'Saftiger dunkler Rührkuchen mit Rotwein, Kakao, Zimt und Schokoraspeln. Duftet nach Advent und schmeckt nach zwei Tagen sogar noch besser.',
 ['Weiche Butter mit Zucker und Vanillezucker cremig rühren, die Eier einzeln unterrühren.',
  'Mehl, Kakao, Backpulver und Zimt mischen und abwechselnd mit dem Rotwein unterrühren. Die Schokoraspel unterheben.',
  'Den Teig in eine gefettete Kastenform (30 cm) füllen und bei 175 °C Ober-/Unterhitze 55–60 Minuten backen (Stäbchenprobe).',
  'Auskühlen lassen und mit Puderzucker bestäuben.'],
 'Rotweinkuchen: mit Puderzucker oder mit Schokoguss?','#rotweinkuchen #kastenkuchen #advent #backen',
 'A dark brown German red wine chocolate loaf cake (Rotweinkuchen) dusted with white powdered sugar on a wooden board, cut at the front with two slices lying in front showing a moist dark crumb speckled with chocolate shavings.')

# =============================== OMAS KOCHTOPF (So 29.11.) ===============================
P('OK',0,0,'OKWaffeln','Omas Waffeln mit heißen Kirschen','Omas Waffeln',['Knusprig und fluffig!','Mit heißen Kirschen!','Sonntags wie früher!'],
 ['125 g Butter (weich)','75 g Zucker','3 Eier','250 g Mehl','250 ml Milch','1 Glas Sauerkirschen','2 EL Speisestärke'],['1 Pck. Vanillezucker','1 TL Backpulver','1 Prise Salz','Puderzucker zum Bestäuben','etwas Öl fürs Waffeleisen','Schlagsahne zum Servieren'],
 'ca. 8 Waffeln','ca. 40 Minuten',
 'Goldbraune, fluffige Waffeln mit heißen Kirschen und Puderzucker. So hat Oma uns am Sonntag immer verwöhnt.',
 ['Butter mit Zucker, Vanillezucker und Salz cremig rühren, die Eier einzeln unterrühren. Mehl mit Backpulver mischen und abwechselnd mit der Milch unterrühren. 10 Minuten quellen lassen.',
  'Die Kirschen abtropfen lassen und den Saft auffangen. 6 EL Saft mit der Speisestärke glatt rühren. Den restlichen Saft aufkochen, die Stärke einrühren, 1 Minute köcheln lassen und die Kirschen unterheben.',
  'Das Waffeleisen leicht einfetten und nacheinander ca. 8 goldbraune Waffeln backen.',
  'Die Waffeln mit Puderzucker bestäuben und mit den heißen Kirschen und etwas Sahne servieren.'],
 'Waffeln: mit heißen Kirschen oder mit Puderzucker pur?','#waffeln #heißekirschen #sonntagsfrühstück #omasrezepte',
 'Two golden brown heart-shaped German waffles on a white plate dusted with powdered sugar, topped with a generous spoonful of hot glossy dark red sour cherries in thick cherry sauce, a dollop of whipped cream beside.')
P('OK',0,1,'OKKassler','Kassler mit Sauerkraut und Püree','Omas Kassler',['Zart und saftig!','Mit Sauerkraut!','Dazu cremiges Püree!'],
 ['1 kg Kassler am Stück','1 Zwiebel','400 ml Brühe','800 g Sauerkraut','1 kg Kartoffeln','200 ml Milch','40 g Butter'],['2 Lorbeerblätter','5 Wacholderbeeren','1 TL Zucker','Salz, Muskat'],
 '4 Portionen','ca. 1 Std. 30 Min.',
 'Saftiger Kassler aus dem Ofen mit würzigem Sauerkraut und cremigem Kartoffelpüree. Ein echtes Sonntagsessen wie bei Oma.',
 ['Den Kassler in einen Bräter legen, die Zwiebel in Spalten dazugeben und 200 ml Brühe angießen. Zugedeckt bei 180 °C Ober-/Unterhitze ca. 60 Minuten garen.',
  'Das Sauerkraut mit 200 ml Brühe, Lorbeer, Wacholder und Zucker in einen Topf geben und zugedeckt 30 Minuten köcheln lassen.',
  'Die Kartoffeln schälen, in Salzwasser 20 Minuten weich kochen, abgießen und mit warmer Milch und Butter zu Püree stampfen. Mit Salz und Muskat würzen.',
  'Den Kassler in Scheiben schneiden und mit Sauerkraut, Püree und dem Bratensaft servieren.'],
 'Kassler: lieber mit Sauerkraut oder mit Grünkohl?','#kassler #sauerkraut #sonntagsessen #hausmannskost',
 'A plate with three thick juicy slices of pink smoked pork loin (Kassler) with a browned edge, a portion of pale golden sauerkraut and a big swirl of creamy mashed potatoes with a little melted butter, a little dark gravy over the meat.')
P('OK',0,2,'OKReibekuchen','Reibekuchen mit Apfelmus','Omas Reibekuchen',['Außen richtig knusprig!','Mit Apfelmus!','Wie auf dem Weihnachtsmarkt!'],
 ['1 kg Kartoffeln','1 Zwiebel','2 Eier','3 EL Mehl','1 TL Salz','Öl zum Braten','1 Glas Apfelmus'],['Pfeffer, Muskat'],
 'ca. 12 Stück','ca. 45 Minuten',
 'Goldbraune Reibekuchen mit knusprigem Rand, frisch aus der Pfanne und mit Apfelmus. Schmecken wie auf dem Weihnachtsmarkt.',
 ['Die Kartoffeln schälen und mit der Zwiebel fein reiben. In einem sauberen Küchentuch kräftig ausdrücken.',
  'Mit Eiern, Mehl, Salz, Pfeffer und Muskat zu einem Teig verrühren.',
  'Reichlich Öl in einer Pfanne erhitzen. Je 2 EL Teig hineingeben, flach drücken und von beiden Seiten 3–4 Minuten goldbraun und knusprig braten.',
  'Auf Küchenpapier abtropfen lassen und mit Apfelmus servieren.'],
 'Reibekuchen: mit Apfelmus oder mit Lachs und Schmand?','#reibekuchen #kartoffelpuffer #apfelmus #omasrezepte',
 'Several golden brown crispy German potato pancakes (Reibekuchen) with lacy crunchy edges stacked on a white plate, a small bowl of pale applesauce beside, one pancake in front showing the grated potato texture.')
P('OK',0,3,'OKKaesespaetzle','Käsespätzle mit Röstzwiebeln','Omas Käsespätzle',['Schön käsig!','Mit Röstzwiebeln!','Alles aus einer Pfanne!'],
 ['500 g Spätzle (frisch)','250 g Bergkäse','3 Zwiebeln','40 g Butter','100 ml Sahne','1 Bund Schnittlauch'],['Salz, Pfeffer, Muskat'],
 '4 Portionen','ca. 35 Minuten',
 'Cremige Käsespätzle mit würzigem Bergkäse und goldbraunen Röstzwiebeln, alles aus einer Pfanne. Einfach, schnell und richtig gemütlich.',
 ['Die Zwiebeln in feine Ringe schneiden und in der Hälfte der Butter bei mittlerer Hitze 15 Minuten goldbraun rösten. Herausnehmen.',
  'Die Spätzle in der restlichen Butter in einer großen Pfanne 5 Minuten anbraten.',
  'Sahne und geriebenen Käse dazugeben und unter Rühren schmelzen lassen, bis alles cremig ist. Mit Salz, Pfeffer und Muskat abschmecken.',
  'Mit den Röstzwiebeln und Schnittlauch bestreut servieren.'],
 'Käsespätzle: mit Röstzwiebeln oder mit Speck?','#käsespätzle #spätzle #pfannengericht #hausmannskost',
 'A rustic cast iron pan filled with creamy German cheese spaetzle (Käsespätzle) with stringy melted cheese, topped with a generous heap of golden brown crispy fried onion rings and fresh chopped chives, a portion on a plate in front.')
P('OK',0,4,'OKHuehnersuppe','Omas Hühnersuppe','Omas Hühnersuppe',['Wärmt von innen!','Mit Nudeln und Gemüse!','Wie bei Oma!'],
 ['1 Suppenhuhn (1,5 kg)','2 Karotten','1 Stange Lauch','¼ Knollensellerie','1 Zwiebel','150 g Suppennudeln','1 Bund Petersilie'],['2 Lorbeerblätter','5 Pfefferkörner','2 TL Salz','2,5 l Wasser'],
 '6 Portionen','ca. 2 Std. 30 Min.',
 'Goldene Hühnersuppe mit zartem Fleisch, Gemüse und feinen Nudeln, langsam gekocht wie bei Oma. Genau das Richtige für kalte Abende.',
 ['Das Huhn mit dem Wasser, der halbierten Zwiebel, Lorbeer, Pfefferkörnern und Salz aufkochen. Bei kleiner Hitze 2 Stunden leise köcheln lassen und den Schaum abschöpfen.',
  'Das Huhn herausnehmen und die Brühe durch ein Sieb gießen. Das Fleisch von den Knochen lösen und klein zupfen.',
  'Karotten, Lauch und Sellerie klein schneiden und in der Brühe 10 Minuten garen. Die Suppennudeln dazugeben und nach Packungsangabe mitkochen.',
  'Das Fleisch zurück in die Suppe geben, abschmecken und mit gehackter Petersilie servieren.'],
 'Hühnersuppe: mit Nudeln oder mit Reis?','#hühnersuppe #suppe #omasrezepte #hausmannskost',
 'A deep white soup plate filled with golden clear German chicken noodle soup with thin soup noodles, pieces of tender chicken meat, orange carrot slices, green leek rings and chopped fresh parsley, a soup pot blurred behind.')

# =============================== HEISSLUFTHELD (So 29.11.) ===============================
H(0,0,'HHQuarkbroetchen','Quarkbrötchen aus dem Airfryer','Ohne Hefe, ohne Warten:',['QUARK-','BRÖTCHEN'],
 [Z('250 g','Magerquark','magerquark'),Z('250 g','Dinkelmehl','dinkelmehl'),Z('1 Pck.','Backpulver','backpulver'),Z('1 Stück','Ei','ei'),Z('3 EL','Milch','milch'),Z('1 TL','Salz','salz'),Z('2 EL','Kürbiskerne','kuerbiskerne')],['Butter zum Bestreichen'],
 '6 Brötchen','ca. 25 Minuten',
 'Frische Brötchen am Sonntagmorgen, ganz ohne Hefe und ohne Gehzeit. Im Airfryer werden sie in 15 Minuten außen knusprig und innen weich.',
 ['Quark, Ei, 2 EL Milch und Salz verrühren. Mehl und Backpulver dazugeben und kurz zu einem glatten Teig verkneten.',
  'Mit bemehlten Händen 6 Brötchen formen, mit der restlichen Milch bestreichen und mit Kürbiskernen bestreuen.',
  'Mit etwas Abstand in den Korb mit Backpapier legen und im Airfryer bei 170 °C 14–16 Minuten goldbraun backen.'],
 'Quarkbrötchen: mit Butter und Marmelade oder herzhaft?','#quarkbrötchen #airfryer #heißluftfritteuse #frühstück',
 'Six round golden brown homemade quark bread rolls with a cross cut on top, sprinkled with green pumpkin seeds, sitting in the basket and on a wooden board in front, one roll cut open showing the soft white crumb with a little butter.')
H(0,1,'HHCevapcici','Cevapcici aus dem Airfryer','Wie vom Grill:',['CEVAPCICI','MIT AJVAR'],
 [Z('500 g','Rinderhack','rinderhack'),Z('1 Stück','Zwiebel','zwiebel'),Z('2 Zehen','Knoblauch','knoblauch'),Z('1 TL','Paprikapulver','paprikapulver'),Z('1 TL','Salz','salz'),Z('½ TL','Natron','natron'),Z('4 EL','Ajvar','ajvar')],['Pfeffer','Zwiebelringe zum Servieren'],
 '16 Stück','ca. 30 Minuten',
 'Würzige Hackröllchen wie vom Grill, ganz ohne Rauch und Fettspritzer. Mit Ajvar und Zwiebeln wie im Balkan-Restaurant.',
 ['Zwiebel und Knoblauch sehr fein würfeln. Mit Hack, Paprika, Salz, Pfeffer und Natron gründlich verkneten.',
  'Mit nassen Händen 16 fingerdicke Röllchen formen und nebeneinander in den Korb legen.',
  'Im Airfryer bei 200 °C 10–12 Minuten garen und nach der Hälfte wenden. Mit Ajvar und Zwiebelringen servieren.'],
 'Cevapcici: mit Pommes oder mit Reis?','#cevapcici #airfryer #heißluftfritteuse #schnelleküche',
 'Many browned juicy minced meat rolls (cevapcici) with a few dark roasted marks, some in the basket and several on a plate in front with a small bowl of red ajvar pepper relish and raw onion rings.')
H(0,2,'HHSchokokuchen','Schokokuchen aus dem Airfryer','In 25 Minuten fertig:',['SCHOKO-','KUCHEN'],
 [Z('100 g','Butter','butter'),Z('80 g','Zucker','zucker'),Z('2 Stück','Eier','eier'),Z('100 g','Mehl','mehl'),Z('2 EL','Backkakao','backkakao'),Z('1 TL','Backpulver','backpulver'),Z('80 ml','Milch','milch'),Z('50 g','Zartbitterschokolade','zartbitterschokolade')],['Puderzucker zum Bestäuben'],
 '1 kleine Springform (18 cm)','ca. 35 Minuten',
 'Saftiger kleiner Schokokuchen für den Sonntagskaffee, ganz ohne den großen Ofen anzuheizen. Passt in eine 18-cm-Form direkt in den Airfryer.',
 ['Butter mit Zucker cremig rühren und die Eier einzeln unterrühren.',
  'Mehl, Kakao und Backpulver mischen und abwechselnd mit der Milch unterrühren. Die gehackte Schokolade unterheben.',
  'Den Teig in eine gefettete kleine Springform (18 cm) füllen und in den Korb stellen. Im Airfryer bei 160 °C 22–25 Minuten backen (Stäbchenprobe). Auskühlen lassen und mit Puderzucker bestäuben.'],
 'Schokokuchen: mit Puderzucker oder mit Sahne?','#schokokuchen #airfryer #heißluftfritteuse #backen',
 'A small round moist dark chocolate cake dusted with white powdered sugar on a plate in front of the basket, one slice cut out and lying beside it showing the moist dark crumb with melted chocolate pieces.')
H(0,3,'HHKartoffelgratin','Kartoffelgratin aus dem Airfryer','Cremig und goldbraun:',['KARTOFFEL-','GRATIN'],
 [Z('800 g','Kartoffeln','kartoffeln'),Z('200 ml','Sahne','sahne'),Z('100 ml','Milch','milch'),Z('100 g','Reibekäse','reibekaese'),Z('1 Zehe','Knoblauch','knoblauch'),Z('1 TL','Salz','salz'),Z('10 g','Butter','butter')],['Pfeffer, Muskat'],
 '4 Portionen','ca. 45 Minuten',
 'Cremiges Kartoffelgratin mit goldener Käsekruste, das perfekt in den Airfryer passt. Schmeckt als Beilage oder einfach pur mit einem Salat.',
 ['Kartoffeln schälen und in dünne Scheiben hobeln. Eine ofenfeste Form, die in den Korb passt, mit Butter fetten und mit Knoblauch ausreiben.',
  'Sahne und Milch mit Salz, Pfeffer und Muskat verrühren. Die Kartoffelscheiben einschichten, mit der Sahnemilch übergießen und mit Käse bestreuen.',
  'Mit Alufolie abgedeckt im Airfryer bei 160 °C 25 Minuten garen, dann ohne Folie bei 180 °C 10–12 Minuten goldbraun überbacken.'],
 'Kartoffelgratin: als Beilage oder als Hauptgericht?','#kartoffelgratin #airfryer #heißluftfritteuse #beilage',
 'A small round ceramic baking dish of creamy potato gratin with thin layered potato slices and a bubbling golden brown cheese crust, one portion served on a plate in front showing the creamy layers.')
H(0,4,'HHBackfisch','Backfisch aus dem Airfryer','Wie an der Nordsee:',['BACK-','FISCH'],
 [Z('4 Stück','Kabeljaufilets','kabeljau'),Z('50 g','Mehl','mehl'),Z('2 Stück','Eier','eier'),Z('100 g','Semmelbrösel','semmelbroesel'),Z('2 EL','Öl','oel'),Z('1 TL','Salz','salz'),Z('1 Stück','Zitrone','zitrone')],['Pfeffer','Remoulade zum Dippen'],
 '4 Stück','ca. 25 Minuten',
 'Knuspriger Backfisch wie an der Fischbude am Hafen, aber ohne Fett-Bad und ohne Fischgeruch in der ganzen Wohnung. Dazu Remoulade und Zitrone.',
 ['Die Fischfilets trocken tupfen und mit Salz und Pfeffer würzen.',
  'Nacheinander in Mehl, verquirlten Eiern und Semmelbröseln wenden und rundherum dünn mit Öl bepinseln.',
  'In den Korb legen und im Airfryer bei 200 °C 10–12 Minuten goldbraun garen, nach der Hälfte vorsichtig wenden. Mit Zitronenspalten und Remoulade servieren.'],
 'Backfisch: mit Remoulade oder mit Kartoffelsalat?','#backfisch #airfryer #heißluftfritteuse #fisch',
 'Four golden brown crispy breaded fish fillets with a crunchy breadcrumb coating, two in the basket and two on a plate in front with lemon wedges and a small bowl of creamy remoulade, one fillet broken open showing flaky white fish inside.')
