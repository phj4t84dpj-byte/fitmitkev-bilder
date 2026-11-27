# -*- coding: utf-8 -*-
# Test Kev 27.11., 20:32: „für die 3 Seiten jeweils 1 kurzes Rezeptvideo für Samstag und wir prüfen wie es funktioniert“.
# Je Seite 1 Reel (Higgsfield seedance_2_5, 15 s, 9:16, 720p, ohne Ton), Sa 28.11. 18:45, zusätzlich zu den 5 Bildbeiträgen.
import json
R=[
dict(seite='KH',blog='7766090',tag='#kuchenherz',name='Omas Spritzgebäck',emo='😍',
 text="Omas Spritzgebäck in 15 Sekunden 😍 Rezept im 1. Kommentar ⤵️\n\n#spritzgebäck #plätzchen #weihnachtsbäckerei #backen #kuchenherz",
 intro="Zartes Spritzgebäck mit Schokolade, so wie bei Oma aus der Plätzchendose. Mit dem Spritzbeutel ganz einfach gemacht.",
 aus="ca. 60 Stück, 2 Backbleche",zeit="ca. 1 Std.",
 zut=["250 g Butter (weich)","120 g Puderzucker","1 Pck. Vanillezucker","1 Ei","1 Prise Salz","375 g Mehl","150 g Zartbitterschokolade"],
 schritte=["Butter mit Puderzucker, Vanillezucker und Salz cremig schlagen, das Ei unterrühren und das Mehl kurz unterkneten.",
  "Den Teig in einen Spritzbeutel mit großer Sterntülle füllen und kleine Rosetten und kurze Stangen auf Backbleche mit Backpapier spritzen.",
  "Bei 180 °C Ober-/Unterhitze 10–12 Minuten hell goldgelb backen und auskühlen lassen.",
  "Die Plätzchen zur Hälfte in geschmolzene Schokolade tauchen und auf Backpapier fest werden lassen."],
 frage="Spritzgebäck: mit Schokolade oder ohne?"),
dict(seite='OK',blog='7766077',tag='#omaskochtopf',name='Omas Kartoffelpuffer',emo='🤤',
 text="Omas Kartoffelpuffer – knusprig wie früher 🤤 Rezept im 1. Kommentar ⤵️\n\n#kartoffelpuffer #reibekuchen #omasrezepte #hausmannskost #omaskochtopf",
 intro="Außen knusprig, innen weich und dazu Apfelmus: Kartoffelpuffer wie bei Oma, frisch aus der Pfanne.",
 aus="4 Portionen (ca. 12 Stück)",zeit="ca. 40 Minuten",
 zut=["1 kg Kartoffeln (mehligkochend)","1 Zwiebel","2 Eier","3 EL Mehl","1 TL Salz","Pfeffer, Muskat","Öl zum Braten","Apfelmus zum Servieren"],
 schritte=["Kartoffeln schälen und mit der Zwiebel fein reiben. Die Masse in einem sauberen Küchentuch kräftig ausdrücken.",
  "Mit Eiern, Mehl, Salz, Pfeffer und etwas Muskat verrühren.",
  "Reichlich Öl in einer Pfanne erhitzen, je 2 EL Teig hineingeben, flach drücken und von jeder Seite 3–4 Minuten goldbraun und knusprig braten.",
  "Kurz auf Küchenpapier abtropfen lassen und mit Apfelmus servieren."],
 frage="Kartoffelpuffer: mit Apfelmus oder mit Zucker?"),
dict(seite='HH',blog='7766068',tag='#heißluftheld',name='Mozzarella-Sticks aus dem Airfryer',emo='😋',
 text="Mozzarella-Sticks aus dem Airfryer – schau dir diesen Käse an 😋 Rezept im 1. Kommentar ⤵️\n\n#mozzarellasticks #airfryer #heißluftfritteuse #fingerfood #heißluftheld",
 intro="Außen knusprig, innen ganz viel geschmolzener Käse: Mozzarella-Sticks ohne Fritteuse, in 8 Minuten aus dem Airfryer.",
 aus="ca. 16 Stück",zeit="ca. 20 Min. + 30 Min. Kühlzeit",
 zut=["250 g Mozzarella (am Stück, fest)","50 g Mehl","2 Eier","100 g Semmelbrösel","1 TL Paprikapulver","1 Prise Salz","1 EL Öl","Tomatensoße zum Dippen"],
 schritte=["Den Mozzarella in dicke Sticks schneiden. Semmelbrösel mit Paprika und Salz mischen.",
  "Die Sticks nacheinander in Mehl, verquirlten Eiern und Semmelbröseln wenden – für eine extra knusprige Hülle Ei und Brösel noch einmal wiederholen. 30 Minuten ins Gefrierfach legen, damit der Käse beim Backen nicht ausläuft.",
  "Mit etwas Öl einsprühen und im Airfryer bei 200 °C 6–8 Minuten goldbraun backen. Sofort mit Tomatensoße servieren."],
 frage="Mozzarella-Sticks: mit Tomatensoße oder mit Knoblauch-Dip?"),
]
posts=[]
for r in R:
    fc=f"{r['name']}\n\n{r['intro']}\n\nZutaten ({r['aus']}):\n"+"\n".join("• "+z for z in r['zut'])+"\n\nSo geht's:\n"+"\n".join(f"{i}. {s}" for i,s in enumerate(r['schritte'],1))+f"\n\nZeit: {r['zeit']}\n\nGuten Appetit! 😋\n\n{r['frage']}"
    assert not any(w in (r['text']+fc).lower() for w in ('kcal','abnehm','fitmitkev'))
    posts.append(dict(seite=r['seite'],blog=r['blog'],name=r['name'],date='2026-11-28T18:45:00',text=r['text'],fc=fc))
json.dump(posts,open('reels_samstag_posts.json','w'),ensure_ascii=False,indent=1)
with open('Reels-Nischenseiten-Samstag.txt','w') as f:
    for p in posts: f.write(f"===== Sa 28.11. 18:45 · {p['seite']} · {p['name']} (Reel)\n\nTITEL:\n{p['text']}\n\n1. KOMMENTAR:\n{p['fc']}\n\n\n")
print('ok')
