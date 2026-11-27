# -*- coding: utf-8 -*-
# N3 – Nischenseiten ab Sa 28.11.2026 (Kev 27.11., 18:49: „ab morgen jeder unserer anderen Facebook Seiten 5 Rezepte“),
# je Seite 5 Rezepte am Tag um 9:00 · 12:00 · 15:00 · 17:30 · 20:00. Stil wie N2: Kuchenherz + Omas Kochtopf im Zettel-Stil,
# Heißluftheld im Board-Look mit gut sichtbarem Airfryer. Keine kcal, kein Abnehm-Bezug, kein Fitmitkev. Fotos: Higgsfield gpt_image_2_6, 4:5.
# Nicht wiederholt aus N1/N2 (15.–18.11.).
def Z(menge,name,tile): return dict(menge=menge,name=name,tile=tile)
ZEITEN=['09:00','12:00','15:00','17:30','20:00']
TAGE=['2026-11-28']
SEITEN={'KH':dict(name='Kuchenherz',blog='7766090',tag='#kuchenherz'),'HH':dict(name='Heißluftheld',blog='7766068',tag='#heißluftheld'),'OK':dict(name='Omas Kochtopf',blog='7766077',tag='#omaskochtopf')}
R=[]
def P(seite,tag,slot,key,name,ptitel,herz,zl,ex,aus,zeit,intro,schritte,frage,tags,prompt):
    R.append(dict(seite=seite,tag=tag,slot=slot,key=key,name=name,ptitel=ptitel,herz=herz,zl=zl,ex=ex,aus=aus,zeit=zeit,intro=intro,schritte=schritte,frage=frage,tags=tags,prompt=prompt,stil='zettel'))
def H(tag,slot,key,name,hook,titel,zutaten,ex,aus,zeit,intro,schritte,frage,tags,prompt):
    R.append(dict(seite='HH',tag=tag,slot=slot,key=key,name=name,hook=hook,titel=titel,zutaten=zutaten,ex=ex,aus=aus,zeit=zeit,intro=intro,schritte=schritte,frage=frage,tags=tags,prompt=prompt,stil='board'))

# =============================== KUCHENHERZ (Sa 28.11.) ===============================
P('KH',0,0,'KHNusszopf','Omas Nusszopf','Omas Nusszopf',['Saftige Nussfüllung!','Mit Zuckerguss obendrauf!','Perfekt zum Adventskaffee!'],
 ['500 g Mehl','250 ml Milch (lauwarm)','1 Würfel Hefe','80 g Butter','80 g Zucker','1 Ei','200 g gem. Haselnüsse','100 g Puderzucker'],['1 Prise Salz','für die Füllung: 100 ml Milch, 80 g Zucker, 1 TL Zimt','2–3 EL Wasser für den Guss'],
 '1 Zopf (ca. 16 Scheiben), Backblech','ca. 1 Std. + 1,5 Std. Gehzeit',
 'Weicher Hefeteig mit einer saftigen Haselnuss-Zimt-Füllung, geflochten und mit Zuckerguss überzogen. Der Duft zieht durchs ganze Haus.',
 ['Hefe in der lauwarmen Milch auflösen. Mit Mehl, Zucker, weicher Butter, Ei und Salz 10 Minuten zu einem glatten Teig kneten und abgedeckt 1 Stunde gehen lassen.',
  'Für die Füllung 100 ml Milch mit 80 g Zucker aufkochen, vom Herd nehmen, Haselnüsse und Zimt einrühren und abkühlen lassen.',
  'Den Teig zu einem Rechteck (ca. 40 × 30 cm) ausrollen, die Füllung darauf streichen und von der langen Seite aufrollen. Die Rolle längs halbieren, die beiden Stränge mit der Schnittfläche nach oben umeinanderschlingen und auf ein Backblech mit Backpapier legen. 30 Minuten gehen lassen.',
  'Bei 180 °C Ober-/Unterhitze 30–35 Minuten backen. Puderzucker mit Wasser verrühren und den noch warmen Zopf damit bestreichen.'],
 'Nusszopf: mit Zuckerguss oder lieber pur?','#nusszopf #hefeteig #advent #backen',
 'A long golden brown braided German nut yeast bread (Nusszopf) on a wooden board: two twisted dough strands with the cut side up, showing thick spiral swirls of dark brown ground hazelnut filling, drizzled with white sugar glaze, two thick slices cut in front showing the swirled nut filling inside the soft crumb.')
P('KH',0,1,'KHPizzaschnecken','Pizzaschnecken vom Blech','Pizzaschnecken',['Saftig und käsig!','Perfekt für Partys!','Warm und kalt lecker!'],
 ['400 g Mehl','220 ml Wasser (lauwarm)','½ Würfel Hefe','3 EL Olivenöl','150 g Tomatenmark','150 g Kochschinken','150 g Salami','200 g Reibekäse'],['1 TL Salz','1 TL Zucker','2 TL Oregano'],
 'ca. 16 Schnecken, Backblech','ca. 45 Min. + 1 Std. Gehzeit',
 'Pizzateig mit Tomate, Schinken, Salami und ganz viel Käse aufgerollt und in Scheiben gebacken. Die gehen auf jeder Feier als Erstes weg.',
 ['Hefe und Zucker im lauwarmen Wasser auflösen, mit Mehl, Olivenöl und Salz 8 Minuten zu einem glatten Teig kneten und 1 Stunde gehen lassen.',
  'Den Teig zu einem Rechteck (ca. 40 × 30 cm) ausrollen, mit Tomatenmark bestreichen, mit Oregano bestreuen und mit Schinken- und Salamiwürfeln sowie 150 g Käse belegen.',
  'Von der langen Seite aufrollen, in 16 Scheiben schneiden und auf ein Backblech mit Backpapier setzen. Mit dem restlichen Käse bestreuen und bei 200 °C Ober-/Unterhitze 20–25 Minuten goldbraun backen.'],
 'Pizzaschnecken: mit Salami oder lieber mit Schinken?','#pizzaschnecken #partyfood #fingerfood #backen',
 'Many round pizza pinwheel rolls baked close together on a baking tray, each a spiral of golden bread dough with red tomato, pink ham cubes and salami pieces, topped with golden melted bubbly cheese, one pinwheel lying in front on a small plate showing the spiral of filling from the top.')
P('KH',0,2,'KHFrankfurterKranz','Frankfurter Kranz','Frankfurter Kranz',['Der Sonntags-Klassiker!','Mit knusprigem Krokant!','Buttercreme wie früher!'],
 ['5 Eier','350 g Zucker','300 g Butter','250 g Mehl','1 Pck. Vanillepudding','500 ml Milch','150 g gehackte Mandeln','12 Belegkirschen'],['2 TL Backpulver','1 Pck. Vanillezucker','4 EL Johannisbeergelee','20 g Butter für den Krokant'],
 '16 Stücke, Kranzform 26 cm','ca. 2 Std. + Kühlzeit',
 'Lockerer Rührkuchen im Kranz, dazwischen Buttercreme und rotes Gelee, außen rundherum knuspriger Mandelkrokant. So stand er früher auf jeder Familienfeier.',
 ['Für den Teig 150 g weiche Butter mit 150 g Zucker und Vanillezucker cremig rühren, Eier einzeln unterrühren, Mehl und Backpulver unterheben. In eine gefettete Kranzform (26 cm) füllen und bei 175 °C Ober-/Unterhitze 35–40 Minuten backen. Auskühlen lassen und zweimal waagerecht durchschneiden.',
  'Puddingpulver mit 100 g Zucker und Milch nach Packungsangabe kochen, mit Frischhaltefolie abdecken und auf Zimmertemperatur abkühlen lassen. 150 g weiche Butter schaumig schlagen und den Pudding löffelweise unterrühren.',
  'Für den Krokant 20 g Butter mit 100 g Zucker hell karamellisieren, die Mandeln unterrühren, auf Backpapier abkühlen lassen und grob hacken.',
  'Den unteren Boden mit Gelee und Creme bestreichen, den zweiten Boden auflegen, Creme darauf, dann den dritten Boden. Rundherum mit Creme einstreichen, mit Krokant bestreuen, Tuffs aufspritzen und mit Kirschen belegen. 2 Stunden kalt stellen.'],
 'Frankfurter Kranz: lieber mit Kirsche oder ohne?','#frankfurterkranz #torte #kaffeeundkuchen #backen',
 'A classic German Frankfurter Kranz ring cake on a cake stand, completely covered with pale yellow buttercream and golden brown crunchy almond brittle crumbs all over, piped buttercream rosettes on top each topped with a bright red candied cherry, one slice cut out and placed on a small white plate in front showing three layers of pale sponge with buttercream and a thin red jam layer between them.')
P('KH',0,3,'KHKokosmakronen','Omas Kokosmakronen','Omas Kokosmakronen',['Ganz einfach gemacht!','Knusprig und saftig!','Für die Plätzchendose!'],
 ['4 Eiweiß','200 g Zucker','250 g Kokosraspel','1 Pck. Vanillezucker','1 Prise Salz','Backoblaten (50 mm)','100 g dunkle Schokolade'],[],
 'ca. 40 Stück, Backblech','ca. 45 Minuten',
 'Kleine goldene Kokosberge, außen knusprig und innen saftig, mit einem Schokoboden. Omas Plätzchendose war ohne sie nie komplett.',
 ['Eiweiß mit Salz steif schlagen, dabei Zucker und Vanillezucker langsam einrieseln lassen, bis der Eischnee fest und glänzend ist.',
  'Die Kokosraspel vorsichtig unterheben. Mit zwei Teelöffeln kleine Häufchen auf die Oblaten setzen und auf ein Backblech mit Backpapier legen.',
  'Bei 150 °C Ober-/Unterhitze 20–25 Minuten backen, bis die Spitzen goldbraun sind. Auskühlen lassen, die Unterseiten in geschmolzene Schokolade tauchen und fest werden lassen.'],
 'Kokosmakronen: mit Schokoboden oder ohne?','#kokosmakronen #plätzchen #weihnachtsbäckerei #backen',
 'Many small golden toasted coconut macaroons shaped like little rough peaks, each sitting on a round white wafer with a dark chocolate base, piled on a vintage plate and a few lying on the table in front, one broken in half showing the moist white coconut inside.')
P('KH',0,4,'KHLebkuchenBlech','Omas Lebkuchen vom Blech','Lebkuchen vom Blech',['Saftig und würzig!','Mit Schokoguss!','Ganz schnell gemacht!'],
 ['375 g Mehl','250 g Honig','150 g Zucker','100 g Butter','2 Eier','2 TL Lebkuchengewürz','100 g gemahlene Mandeln','200 g dunkle Schokolade'],['1 Pck. Backpulver','2 EL Kakao','100 ml Milch','Mandeln oder bunte Streusel zum Verzieren'],
 'ca. 30 Stücke, Backblech','ca. 1 Std. + Abkühlen',
 'Saftiger Lebkuchen vom Blech mit Honig und Lebkuchengewürz, dick mit Schokolade überzogen. In 15 Minuten im Ofen und schmeckt nach ein paar Tagen in der Dose noch besser.',
 ['Honig, Zucker und Butter in einem Topf erwärmen, bis alles geschmolzen ist, und etwas abkühlen lassen.',
  'Mehl, Backpulver, Kakao, Lebkuchengewürz und Mandeln mischen. Mit der Honigmasse, den Eiern und der Milch zu einem glatten Teig verrühren.',
  'Auf ein Backblech mit Backpapier streichen und bei 180 °C Ober-/Unterhitze 15–20 Minuten backen. Auskühlen lassen, mit geschmolzener Schokolade bestreichen, nach Belieben verzieren und in Stücke schneiden.'],
 'Lebkuchen: lieber mit Schokolade oder mit Zuckerguss?','#lebkuchen #blechkuchen #weihnachtsbäckerei #backen',
 'Square pieces of soft dark brown German gingerbread sheet cake (Lebkuchen vom Blech) with a thick glossy dark chocolate coating on top, each piece decorated with a whole blanched almond, stacked on a wooden board, one piece in front on a small plate showing the soft spiced brown crumb from the side.')

# =============================== OMAS KOCHTOPF (Sa 28.11.) ===============================
P('OK',0,0,'OKQuarkkeulchen','Omas Quarkkeulchen','Omas Quarkkeulchen',['Knusprig und weich!','Mit Zimt und Zucker!','Dazu Apfelmus!'],
 ['500 g Kartoffeln (gekocht)','250 g Magerquark','100 g Mehl','2 Eier','60 g Zucker','50 g Rosinen','Butter zum Braten','Zimt und Zucker'],['1 Pck. Vanillezucker','1 Prise Salz','Apfelmus zum Servieren'],
 '4 Portionen (ca. 12 Stück)','ca. 40 Minuten',
 'Kleine goldene Küchlein aus Kartoffeln und Quark, in Butter gebraten und in Zimtzucker gewälzt. Ein sächsischer Klassiker, den Oma aus den Kartoffeln vom Vortag gemacht hat.',
 ['Die am Vortag gekochten Kartoffeln pellen und fein reiben oder durch die Presse drücken.',
  'Mit Quark, Mehl, Eiern, Zucker, Vanillezucker, Salz und Rosinen zu einem formbaren Teig verkneten. Mit bemehlten Händen 12 flache Küchlein formen.',
  'In reichlich Butter bei mittlerer Hitze von jeder Seite 3–4 Minuten goldbraun braten, in Zimt und Zucker wenden und mit Apfelmus servieren.'],
 'Quarkkeulchen: mit Apfelmus oder mit Zucker pur?','#quarkkeulchen #omasrezepte #hausmannskost #süßeküche',
 'Golden brown round flat fried potato and quark pancakes (Saxon Quarkkeulchen) dusted with cinnamon sugar, raisins visible inside, stacked on a white plate, a small bowl of pale apple sauce beside, one cut in half showing the soft pale inside with raisins.')
P('OK',0,1,'OKKartoffelsalat','Kartoffelsalat mit Würstchen','Omas Kartoffelsalat',['Wie an Heiligabend!','Mit Gurke und Ei!','Dazu Wiener Würstchen!'],
 ['1,5 kg Kartoffeln','4 Eier','6 Gewürzgurken','1 Zwiebel','200 g Mayonnaise','150 g Joghurt','100 ml Gurkenwasser','8 Wiener Würstchen'],['1 TL Senf','Salz, Pfeffer','Schnittlauch'],
 '4–6 Portionen','ca. 45 Min. + 1 Std. Ziehzeit',
 'Cremiger Kartoffelsalat mit Ei, Gewürzgurken und Zwiebeln, dazu heiße Wiener. In vielen Familien gibt es genau das an Heiligabend, und es schmeckt jedes Mal wie früher.',
 ['Festkochende Kartoffeln in der Schale 20–25 Minuten kochen, pellen, etwas abkühlen lassen und in Scheiben schneiden. Eier 10 Minuten hart kochen, abschrecken und würfeln.',
  'Gurken und Zwiebel fein würfeln. Mayonnaise, Joghurt, Gurkenwasser und Senf verrühren und mit Salz und Pfeffer würzen.',
  'Alles vorsichtig mischen und mindestens 1 Stunde durchziehen lassen. Die Würstchen in heißem (nicht kochendem) Wasser 8 Minuten ziehen lassen und mit dem Salat und Schnittlauch servieren.'],
 'Kartoffelsalat: mit Mayo oder mit Essig und Öl?','#kartoffelsalat #würstchen #omasrezepte #hausmannskost',
 'A large rustic bowl of creamy German potato salad with sliced potatoes, chopped egg, diced pickles and chives, two Vienna sausages lying on a plate in front next to a serving of the potato salad, a small dish of mustard beside.')
P('OK',0,2,'OKBratapfel','Bratäpfel mit Vanillesoße','Omas Bratäpfel',['Duftet nach Weihnachten!','Mit Nuss-Marzipan-Füllung!','Dazu warme Vanillesoße!'],
 ['4 Äpfel (z. B. Boskop)','50 g Marzipan','40 g gehackte Haselnüsse','30 g Rosinen','1 TL Zimt','20 g Butter','500 ml Milch','1 Pck. Vanillesoßenpulver'],['2 EL Zucker für die Soße'],
 '4 Stück, Auflaufform','ca. 45 Minuten',
 'Ofenwarme Äpfel mit einer Füllung aus Marzipan, Nüssen, Rosinen und Zimt, dazu Vanillesoße. Wenn die in der Küche schmoren, ist Advent.',
 ['Die Äpfel waschen, Deckel abschneiden und das Kerngehäuse großzügig ausstechen.',
  'Marzipan klein würfeln und mit Haselnüssen, Rosinen und Zimt mischen. In die Äpfel füllen, Deckel aufsetzen, in eine gefettete Auflaufform stellen und Butterflöckchen darauf verteilen.',
  'Bei 180 °C Ober-/Unterhitze 25–30 Minuten backen, bis die Äpfel weich sind. Inzwischen die Vanillesoße mit Milch und Zucker nach Packungsangabe kochen und warm dazu servieren.'],
 'Bratapfel: mit Vanillesoße oder mit Eis?','#bratapfel #advent #omasrezepte #weihnachten',
 'Four whole baked red apples with slightly wrinkled glossy skin in a white ceramic baking dish, each with its lid set on top and a filling of marzipan, chopped hazelnuts and raisins bulging out, one apple served on a plate in front in a pool of warm pale yellow vanilla custard sauce, a cinnamon stick beside.')
P('OK',0,3,'OKHackbraten','Omas Hackbraten','Omas Hackbraten',['Mit Ei in der Mitte!','Mit dunkler Soße!','Dazu Kartoffelpüree!'],
 ['1 kg Hackfleisch','2 Brötchen (vom Vortag)','2 Zwiebeln','2 Eier','3 Eier (hart gekocht)','1 EL Senf','400 ml Fleischbrühe','200 g Sahne'],['1 TL Paprikapulver','Salz, Pfeffer','1 EL Speisestärke','Kartoffelpüree zum Servieren'],
 '6 Portionen, Bräter','ca. 1,5 Std.',
 'Saftiger Hackbraten mit hart gekochten Eiern in der Mitte und einer dunklen Rahmsoße aus dem Bräter. Mit Kartoffelpüree das Sonntagsessen schlechthin.',
 ['Brötchen in Wasser einweichen und gut ausdrücken. Zwiebeln fein würfeln. Hack mit Brötchen, Zwiebeln, 2 Eiern, Senf, Paprika, Salz und Pfeffer gut verkneten.',
  'Die Hälfte des Hackteigs in einem Bräter zu einem Laib formen, die gepellten Eier der Länge nach daraufsetzen, mit dem restlichen Teig umhüllen und gut verschließen.',
  'Bei 200 °C Ober-/Unterhitze 20 Minuten braten, dann die Brühe angießen und weitere 40 Minuten braten, dabei ab und zu begießen.',
  'Den Braten herausnehmen, den Bratensaft mit Sahne aufkochen, mit Speisestärke binden und abschmecken. Den Hackbraten in Scheiben schneiden und mit Soße und Kartoffelpüree servieren.'],
 'Hackbraten: mit Ei in der Mitte oder ohne?','#hackbraten #sonntagsessen #omasrezepte #hausmannskost',
 'A German meatloaf (Hackbraten) with a dark brown roasted crust in a dark roasting pan, two thick slices cut in front showing the juicy minced meat with a whole halved hard-boiled egg in the middle, served on a plate with creamy mashed potatoes and dark brown gravy.')
P('OK',0,4,'OKGaensekeule','Gänsekeule mit Rotkohl und Klößen','Omas Gänsekeule',['Das Festessen!','Mit knuspriger Haut!','Rotkohl und Klöße dazu!'],
 ['4 Gänsekeulen','2 Äpfel','2 Zwiebeln','1 TL Beifuß','500 ml Geflügelbrühe','1 Glas Rotkohl','8 Kartoffelklöße','2 EL Speisestärke'],['Salz, Pfeffer','1 Lorbeerblatt'],
 '4 Portionen, Bräter','ca. 2,5 Std.',
 'Knusprige Gänsekeulen aus dem Ofen mit einer kräftigen Soße, dazu Rotkohl und Klöße. Das Festessen, auf das sich die ganze Familie jedes Jahr freut.',
 ['Die Keulen mit Salz, Pfeffer und Beifuß einreiben und mit der Hautseite nach oben in einen Bräter legen. Äpfel und Zwiebeln grob würfeln und dazugeben.',
  'Brühe angießen, Lorbeer dazu und bei 160 °C Ober-/Unterhitze 2 Stunden schmoren, dabei ab und zu mit dem Bratensaft begießen.',
  'Die letzten 20 Minuten auf 220 °C stellen, damit die Haut knusprig wird. Inzwischen Rotkohl erwärmen und die Klöße nach Packungsangabe garen.',
  'Den Bratensaft durch ein Sieb gießen, entfetten, aufkochen und mit angerührter Speisestärke binden. Keulen mit Soße, Rotkohl und Klößen servieren.'],
 'Was gibt es bei euch an Weihnachten: Gans, Ente oder Braten?','#gänsekeule #weihnachtsessen #omasrezepte #festessen',
 'A festive plate with a roasted goose leg with crispy glossy golden brown skin, a portion of glossy red braised red cabbage and two round pale potato dumplings, dark brown gravy poured over the dumplings, the roasting pan with more goose legs blurred behind.')

# =============================== HEISSLUFTHELD (Sa 28.11.) ===============================
H(0,0,'HHZimtschnecken','Zimtschnecken aus dem Airfryer','Fertig in 12 Minuten:',['ZIMT-','SCHNECKEN'],
 [Z('1 Rolle','Blätterteig','blaetterteig'),Z('40 g','Butter','butter'),Z('50 g','Zucker','zucker'),Z('2 TL','Zimt','zimt'),Z('80 g','Puderzucker','puderzucker'),Z('1–2 EL','Milch','milch')],[],
 '10 Stück','ca. 25 Minuten',
 'Knusprige Zimtschnecken aus Blätterteig mit Zuckerguss, ganz ohne Hefe und ohne Warten. Der Airfryer macht sie in 12 Minuten goldbraun.',
 ['Den Blätterteig ausrollen, mit geschmolzener Butter bestreichen und mit Zucker und Zimt bestreuen.',
  'Von der langen Seite aufrollen, in 10 Scheiben schneiden und mit etwas Abstand in den Korb mit Backpapier legen.',
  'Im Airfryer bei 180 °C 10–12 Minuten goldbraun backen. Puderzucker mit Milch verrühren und über die warmen Schnecken träufeln.'],
 'Zimtschnecken: mit Guss oder ohne?','#zimtschnecken #airfryer #heißluftfritteuse #backen',
 'Golden brown flaky puff pastry cinnamon rolls with visible cinnamon sugar spirals, drizzled with white sugar glaze, sitting in the basket and on a plate in front, one roll in front showing the spiral from the top.')
H(0,1,'HHFrikadellen','Frikadellen aus dem Airfryer','Ohne Spritzen und Fett:',['FRIKA-','DELLEN'],
 [Z('500 g','Hackfleisch','hackfleisch'),Z('1 Stück','Brötchen vom Vortag','broetchen_vom_vortag'),Z('1 Stück','Zwiebel','zwiebel'),Z('1 Stück','Ei','ei'),Z('1 TL','Senf','senf'),Z('1 TL','Paprikapulver','paprikapulver'),Z('1 EL','Petersilie','petersilie'),Z('1 TL','Salz','salz')],['Pfeffer'],
 '8 Stück','ca. 30 Minuten',
 'Saftige Frikadellen wie bei Oma, aber ohne Fettspritzer in der Küche. Im Airfryer werden sie rundherum braun und bleiben innen schön saftig.',
 ['Das Brötchen einweichen und gut ausdrücken, die Zwiebel fein würfeln.',
  'Hack mit Brötchen, Zwiebel, Ei, Senf, Paprika, Petersilie, Salz und Pfeffer verkneten und 8 flache Frikadellen formen.',
  'Im Airfryer bei 190 °C 14–16 Minuten garen und nach der Hälfte wenden.'],
 'Frikadellen: warm mit Kartoffelsalat oder kalt mit Senf?','#frikadellen #airfryer #heißluftfritteuse #hausmannskost',
 'Juicy round golden brown German meat patties (Frikadellen) with a browned crust, some in the basket and three on a plate in front with a small dish of mustard, one patty cut in half showing the juicy minced meat inside.')
H(0,2,'HHQuarkbaellchen','Quarkbällchen aus dem Airfryer','Ohne Fritteuse:',['QUARK-','BÄLLCHEN'],
 [Z('250 g','Magerquark','magerquark'),Z('250 g','Mehl','mehl'),Z('80 g','Zucker','zucker'),Z('2 Stück','Eier','eier'),Z('1 Pck.','Backpulver','backpulver'),Z('1 Pck.','Vanillezucker','vanillezucker'),Z('30 g','Butter','butter'),Z('1 TL','Zimt','zimt')],['50 g Zucker zum Wälzen'],
 'ca. 20 Stück','ca. 30 Minuten',
 'Fluffige Quarkbällchen wie vom Bäcker, ganz ohne Frittierfett. Noch warm in Zimtzucker wälzen und sofort genießen.',
 ['Quark, Zucker, Vanillezucker und Eier verrühren. Mehl und Backpulver dazugeben und zu einem weichen Teig verrühren.',
  'Mit bemehlten Händen ca. 20 walnussgroße Kugeln formen und mit Abstand in den Korb mit Backpapier legen.',
  'Im Airfryer bei 170 °C 10–12 Minuten goldbraun backen. In geschmolzener Butter schwenken und in Zimtzucker wälzen.'],
 'Quarkbällchen: mit Zimtzucker oder mit Puderzucker?','#quarkbällchen #airfryer #heißluftfritteuse #backen',
 'Round golden brown quark balls rolled in cinnamon sugar, heaped in the basket and on a plate in front, one ball broken open showing the fluffy pale yellow inside.')
H(0,3,'HHSchnitzel','Schnitzel aus dem Airfryer','Knusprig ohne Fett-Bad:',['SCHNITZEL','PANIERT'],
 [Z('4 Stück','Schweineschnitzel','schweineschnitzel'),Z('2 Stück','Eier','eier'),Z('50 g','Mehl','mehl'),Z('100 g','Semmelbrösel','semmelbroesel'),Z('2 EL','Öl','oel'),Z('1 TL','Salz','salz'),Z('1 Stück','Zitrone','zitrone')],['Pfeffer'],
 '4 Stück','ca. 30 Minuten',
 'Goldene, knusprige Schnitzel mit Panade wie aus der Pfanne, aber ohne Fett-Bad und ohne Spritzer. Mit einer Scheibe Zitrone wie im Gasthaus.',
 ['Die Schnitzel flach klopfen, mit Salz und Pfeffer würzen.',
  'Nacheinander in Mehl, verquirlten Eiern und Semmelbröseln wenden und beidseitig dünn mit Öl bepinseln.',
  'Im Airfryer bei 200 °C 10–12 Minuten goldbraun garen, nach der Hälfte wenden und mit Zitronenspalten servieren.'],
 'Schnitzel: mit Pommes oder mit Kartoffelsalat?','#schnitzel #airfryer #heißluftfritteuse #hausmannskost',
 'Two golden brown crispy breaded pork schnitzels with a wavy crunchy breadcrumb coating, one in the basket and one on a plate in front with a lemon wedge and a sprig of parsley, the schnitzel cut to show the tender white meat inside.')
H(0,4,'HHFlammkuchen','Flammkuchen aus dem Airfryer','In 8 Minuten fertig:',['FLAMM-','KUCHEN'],
 [Z('4 Stück','Tortilla-Wraps','tortilla'),Z('200 g','Schmand','schmand'),Z('125 g','Speckwürfel','speck'),Z('2 Stück','Zwiebeln','zwiebeln'),Z('1 Bund','Schnittlauch','schnittlauch'),Z('1 Prise','Salz','salz')],['Pfeffer, Muskat'],
 '4 Stück','ca. 20 Minuten',
 'Hauchdünner Flammkuchen mit Schmand, Speck und Zwiebeln, mit Tortilla-Wraps als Boden. Kein Teig, kein Warten und in 8 Minuten knusprig aus dem Airfryer.',
 ['Schmand mit Salz, Pfeffer und etwas Muskat glatt rühren. Zwiebeln in feine Ringe schneiden.',
  'Die Wraps dünn mit Schmand bestreichen und mit Zwiebeln und Speck belegen.',
  'Nacheinander im Airfryer bei 200 °C 6–8 Minuten knusprig backen und mit Schnittlauch bestreuen.'],
 'Flammkuchen: klassisch mit Speck oder mit Lachs?','#flammkuchen #airfryer #heißluftfritteuse #schnelleküche',
 'A thin crispy round flatbread with golden brown edges, spread with white sour cream and topped with thin onion rings, crispy bacon cubes and fresh chopped chives, cut into wedges, one round flatbread in the basket and one on a wooden board in front.')
