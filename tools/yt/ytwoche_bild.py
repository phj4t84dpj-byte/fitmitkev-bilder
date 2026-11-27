# -*- coding: utf-8 -*-
"""YouTube-Reihe ab Mo 30.11.2026 (Kev 27.11.: 14 Links, „Ab montag jeden Tag 1“, gewohnter Stil, Dialog: „Bild ohne Zutatenliste“).
Aufbau wie yt/Facebook_Langos.jpg / Facebook_Kloesse.jpg: oben das Thumbnail, unten dunkles Feld – hier ohne Zutaten, nur Name,
Werte aus Thumbnail bzw. Videotitel und rote Leiste „Ganzes Video – Link im 1. Kommentar“. Keine erfundenen Zahlen.
Aufruf: python3 ytwoche_bild.py <thumb-ordner (mit Retusche)> <ausgabe-ordner> [ids…]"""
import sys, os, base64, io
from PIL import Image
from playwright.sync_api import sync_playwright
S='/tmp/claude-0/-home-claude/62a14d94-6bfc-5e5c-b2da-15988fbe030e/scratchpad'; F=f"{S}/fonts/gf/ofl"
# id: (Dateiname, Name, Unterzeile, Karten [(oben, Zahl, Einheit, unten)])
D={
'jbviLMbSITg':('Ofenblech','Ofenblech mit Hähnchen &amp; Kürbis','Mit Kichererbsen – alles auf einem Blech',[('',"100",'g','Eiweiß auf dem ganzen Blech')]),
'gVKFErcJpCc':('SpekulatiusCheesecake','Spekulatius-Cheesecake','Cremig, mit Spekulatius-Streuseln',[('UNTER',"200",'kcal','pro Stück')]),
'-srhq33xMGY':('CheeseburgerTaschen','Cheeseburger-Taschen','Saftiges Hack und Käse im Teig',[('',"365",'kcal','pro Tasche'),('',"27",'g','Eiweiß')]),
'TZUXs6jSD3c':('SpaetzlePfanne','Spätzle-Pfanne','Mit Pilzen und Erbsen in cremiger Soße',[('',"80",'g','Eiweiß in der ganzen Pfanne')]),
'w-dmnnDt7jw':('ProteinKuchen','3 Protein-Kuchen','Kirsch · Zitrone · Apfel',[('UNTER',"500",'kcal','pro Kuchen'),('ÜBER',"30",'g','Eiweiß')]),
'HjmsgKJlWzg':('AirfryerDrei','3 Airfryer-Rezepte','Herzhaft und süß aus der Heißluftfritteuse',[('UNTER',"300",'kcal','je Rezept')]),
'nrhnicOIdVM':('Lahmacun','Lahmacun','Dünn, knusprig, mit würzigem Hack',[('UNTER',"200",'kcal','pro Stück')]),
'0mFJBHReQq8':('ButterChicken','Butter Chicken mit Reis','Cremig wie beim Inder',[('UNTER',"600",'kcal','pro Portion')]),
'yyekUrb68mI':('Pizza','Pizza mit Gemüse','Mit Brokkoli und Mais',[('',"87",'g','Eiweiß')]),
'HDrF1P3y8X0':('AirfryerPide','Pide &amp; gefüllte Paprika','Beides aus der Heißluftfritteuse',[('UNTER',"300",'kcal','je Rezept')]),
'Qjecnj9RH10':('OrangeChicken','Orange Chicken mit Reis','Mit Paprika, Brokkoli und Sesam',[('',"500",'kcal','pro Portion')]),
'7MlDFtuRUHg':('FrostaTest','5 Frosta-Gerichte im Test','Diätretter oder Kalorienfalle?',[]),
}
src,dst=sys.argv[1],sys.argv[2]; ids=sys.argv[3:] or list(D)
def b64(im):
    b=io.BytesIO(); im.save(b,'JPEG',quality=93); return base64.b64encode(b.getvalue()).decode()
os.makedirs(dst,exist_ok=True)
with sync_playwright() as pw:
    br=pw.chromium.launch(); pg=br.new_page(viewport={'width':1080,'height':1350},device_scale_factor=1)
    for vid in ids:
        datei,name,sub,karten=D[vid]
        top=b64(Image.open(f"{src}/{vid}.jpg").convert('RGB'))
        if karten:
            kt=''.join(f'<div class="k">{f"<div class=ko>{o}</div>" if o else ""}<div class="kz">{z}<span> {e}</span></div><div class="ku">{u}</div></div>' for o,z,e,u in karten)
        else:
            kt='<div class="k frage"><div class="kz2">Welches lohnt sich –<br>und welches nicht?</div></div>'
        lang=len(name.replace('&amp;','&'))>20
        HTML=f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-SemiBold.ttf');font-weight:600}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Bold.ttf');font-weight:700}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-Medium.ttf');font-weight:500}}
@font-face{{font-family:P;src:url('{F}/poppins/Poppins-ExtraBold.ttf');font-weight:800}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:#1f1d1b;font-family:P;color:#fff;position:relative;overflow:hidden}}
.top{{position:absolute;left:0;top:0;width:1080px;height:608px;background:url(data:image/jpeg;base64,{top}) center/cover}}
.top:after{{content:'';position:absolute;left:0;right:0;bottom:0;height:60px;background:linear-gradient(to bottom,rgba(31,29,27,0),#1f1d1b)}}
.inh{{position:absolute;left:48px;right:48px;top:632px}}
.pill{{display:inline-flex;align-items:center;gap:10px;background:#2b2825;border-radius:30px;padding:8px 20px 8px 14px;font-weight:700;font-size:20px;letter-spacing:2px;color:#e8e2da}}
.pill i{{display:inline-block;width:34px;height:24px;border-radius:7px;background:#e3261f;position:relative}}
.pill i:after{{content:'';position:absolute;left:13px;top:6px;border-left:11px solid #fff;border-top:6px solid transparent;border-bottom:6px solid transparent}}
h1{{font-weight:800;font-size:{68 if lang else 82}px;color:#ffd400;line-height:1.05;margin-top:16px;letter-spacing:.5px}}
.sub{{font-weight:500;font-size:28px;color:#d8d2ca;margin-top:8px}}
.ks{{display:flex;gap:20px;margin-top:26px}}
.k{{flex:1;background:#2b2825;border-radius:22px;padding:18px 28px 20px}}
.ko{{font-weight:700;font-size:19px;letter-spacing:3px;color:#b9b2a8}}
.kz{{font-weight:800;font-size:78px;line-height:1}} .kz span{{color:#ffd400;font-size:44px}}
.ku{{font-weight:600;font-size:24px;color:#e8e2da;margin-top:6px}}
.kz2{{font-weight:800;font-size:44px;line-height:1.15}}
.cta{{position:absolute;left:48px;right:48px;bottom:36px;height:128px;border-radius:22px;background:#e3261f;display:flex;align-items:center;justify-content:space-between;padding:0 34px;box-shadow:0 8px 20px rgba(0,0,0,.35)}}
.c1{{font-weight:700;font-size:20px;letter-spacing:3px;color:#ffe9a8}}
.c2{{font-weight:800;font-size:44px;line-height:1.1}}
.c3{{font-weight:800;font-size:64px}}
.hand{{position:absolute;left:48px;bottom:182px;font-weight:600;font-size:22px;color:#9e978d}}
</style></head><body>
<div class="top"></div>
<div class="inh"><div class="pill"><i></i>{"VIDEO" if not karten else "REZEPTVIDEO"} AUF YOUTUBE</div>
<h1>{name}</h1><div class="sub">{sub}</div><div class="ks">{kt}</div></div>
<div class="hand">Mehr Videos auf meinem YouTube-Kanal · @fitmitkev</div>
<div class="cta"><div><div class="c1">▸ GANZES VIDEO</div><div class="c2">Link im 1. Kommentar</div></div><div class="c3">👇</div></div>
</body></html>"""
        hp=f'{S}/ytw/_b.html'; open(hp,'w').write(HTML); pg.goto('file://'+hp); pg.wait_for_timeout(300)
        r=pg.evaluate("()=>({inh:document.querySelector('.inh').getBoundingClientRect().bottom,hand:document.querySelector('.hand').getBoundingClientRect().top})")
        if r['inh']>r['hand']-10: print('ZU HOCH',vid,r)
        out=f"{dst}/YT-{datei}.jpg"; pg.screenshot(path=out.replace('.jpg','.png'))
        Image.open(out.replace('.jpg','.png')).convert('RGB').save(out,quality=93); os.remove(out.replace('.jpg','.png')); print('ok',out)
    br.close()
