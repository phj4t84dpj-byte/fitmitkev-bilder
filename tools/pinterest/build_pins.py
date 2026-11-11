# Pinterest-Pins (1000x1500, 2:3) aus den Facebook-Boards G87-G90 + Titel, Beschreibung, Pinnwand, Zeitplan
import json, re, os, textwrap
from datetime import datetime, timedelta
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R='/home/claude/fitmitkev-bilder'; S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F=f'{S}/fonts/gf/ofl'; OUT='out'
NAVY=(18,33,63); RED=(193,32,43)
fA=lambda n: ImageFont.truetype(f'{F}/anton/Anton-Regular.ttf',n)
fP=lambda n: ImageFont.truetype(f'{F}/poppins/Poppins-Bold.ttf',n)
fS=lambda n: ImageFont.truetype(f'{F}/poppins/Poppins-SemiBold.ttf',n)
KURZ=json.load(open('kurz.json',encoding='utf-8'))
HOOK={'Weckmann':'Weckmann ohne Hefe und ohne Gehzeit.','MaulwurfBowl':'Maulwurfkuchen als Bowl nur für dich.','KokosMandelTiramisu':'Tiramisu mit Kokos und Mandeln als Bowl nur für dich.'}
SER=[('g87/montag_posts.json','G87'),('g88/dienstag_posts.json','G88'),('g89/mittwoch_posts.json','G89'),('g90/donnerstag_posts.json','G90')]
B_K='Leichte Kuchen & Desserts'; B_B='Bowls'; B_H='Herzhaft unter 500 kcal'; B_F='Frühstück'; B_W='Weihnachtsbäckerei'
FRUEH={'SpekOats','Quarkbroetchen','ZimtschneckenPancakes','BratapfelPorridge','KoernerBroetchen','Kaiserschmarrn','KaeseSchinkenWaffeln','NusseckenOats','Kaesebroetchen','Bauernfruehstueck','ZimtschneckenOats','Fruehstuecksbroetchen','StrammerMax'}
WEIH={'Zimtsterne','Engelsaugen','Kokosmakronen','Weckmann'}
TAGS={'BowlH':'#mealprep #kalorienarm #proteinreich',B_K:'#leichtbacken #kalorienarm #kuchenrezepte',B_B:'#kuchenbowl #kalorienarm #proteinreich',B_H:'#kalorienarmkochen #leichterezepte #familienessen',B_F:'#gesundesfrühstück #kalorienarm #proteinfrühstück',B_W:'#weihnachtsbäckerei #plätzchen #kalorienarm'}
def board(p):
    k=p['key']
    if 'Bowl' in k or k=='KokosMandelTiramisu': return B_B
    if k in FRUEH: return B_F
    if k in WEIH: return B_W
    return B_K if p['suess'] else B_H
def unit(p):
    m=re.search(r'kcal (pro \w+|die ganze Bowl)',p['text']); return m.group(1) if m else 'pro Portion'
def parse(fc):
    paras=fc.split('\n\n'); hook=paras[1].strip()
    steps=re.findall(r'^\d\. (.+)$',fc,flags=re.M)
    nw=re.search(r'Nährwerte (pro [^:]+): ca\. (\d+) kcal \| (\d+) g Eiweiß',fc)
    return hook,steps,nw
def first_sentence(t):
    m=re.match(r'(.+?[.!:])(\s|$)',t); return (m.group(1) if m else t).rstrip(':')+'.' if m and m.group(1).endswith(':') else (m.group(1) if m else t)
def desc(p,b):
    hook,steps,nw=parse(p['fc'])
    if p['key'] in KURZ: steps=KURZ[p['key']]
    if b==B_B and not p['suess']: b='BowlH'
    nwt=f" {'P'+nw.group(1)[1:]} ca. {nw.group(2)} kcal und {nw.group(3)} g Eiweiß." if nw else ''
    tags=' '+TAGS[b]
    pre="Zutaten mit Mengen siehe Bild. So geht's: "
    hs=HOOK.get(p['key'],first_sentence(hook))+' '
    def S(st): return ' '.join(f'{i}. {x}' for i,x in enumerate(st,1))
    clean=[re.sub(r'\s*\([^)]*\)','',x).replace(' Ober-/Unterhitze','') for x in steps]
    for c in [hs+pre+S(steps)+nwt+tags, pre+S(steps)+nwt+tags, pre+S(steps)+nwt, pre+S(clean)+nwt+tags, pre+S(clean)+nwt]:
        if len(c)<=500: return c
    # Schritte 1 und 2 kürzen, Schritt 3 (Backzeit/Temperatur) bleibt ganz
    st=list(clean)
    while len(pre+S(st)+nwt)>500:
        i=0 if len(st[0])>=len(st[1]) else 1
        w=st[i].rstrip(' …').rsplit(' ',1)[0].rstrip(',;')
        st[i]=w+' …'
    return pre+S(st)+nwt
def pin_image(p,g):
    src=Image.open(f"{R}/boards/{p['media'].split('/')[-1]}").convert('RGB').resize((1000,1250),Image.LANCZOS)
    im=Image.new('RGB',(1000,1500),(233,219,199))
    # Kopfband: warmer Verlauf
    top=Image.new('RGB',(1000,250)); d=ImageDraw.Draw(top)
    for y in range(250):
        t=y/249; d.line([(0,y),(1000,y)],fill=(int(240-14*t),int(229-18*t),int(212-22*t)))
    im.paste(top,(0,0)); im.paste(src,(0,250))
    d=ImageDraw.Draw(im)
    name=p['alt'].replace(' nur für dich','')
    size=64
    while True:
        f=fP(size); lines=textwrap.wrap(name,width=max(8,int(1900/size)))
        if len(lines)<=2 and all(d.textlength(l,font=f)<=930 for l in lines): break
        size-=2
    lh=size*1.12; y0=(170-lh*len(lines))/2+12
    for i,l in enumerate(lines):
        d.text((500,y0+i*lh),l,font=f,fill=NAVY,anchor='mt')
    sub=f"nur {p['kcal']} kcal {unit(p)} · leicht & lecker"
    d.text((500,190),sub,font=fS(36),fill=RED,anchor='mt')
    return im
rows=[]
for f,g in SER:
    for p in json.load(open(f'{R}/tools/{f}',encoding='utf-8')):
        b=board(p); name=p['alt'].replace(' nur für dich','')
        title=f"{name} – nur {p['kcal']} kcal {unit(p)}"
        assert len(title)<=100,title
        fn=f"PIN-{g}-{p['key']}.jpg"
        if not os.path.exists(f'{OUT}/{fn}'): pin_image(p,g).save(f'{OUT}/{fn}',quality=90)
        rows.append(dict(serie=g,key=p['key'],name=name,kcal=p['kcal'],suess=p['suess'],board=b,title=title,desc=desc(p,b),file=fn))
# Zeitplan: 12 Pins/Tag ab Fr 13.11., Pinnwände gemischt, Abendspitze
TIMES=['07:05','09:10','11:15','12:40','14:05','15:30','17:05','18:20','19:35','20:30','21:25','22:15']
by={}
for r in rows: by.setdefault(r['board'],[]).append(r)
order=[]; keys=sorted(by,key=lambda k:-len(by[k]))
while any(by.values()):
    for k in keys:
        if by[k]: order.append(by[k].pop(0))
d0=datetime(2026,11,13)
for i,r in enumerate(order):
    day=d0+timedelta(days=i//12); r['date']=f"{day:%Y-%m-%d}T{TIMES[i%12]}:00"; r['n']=i+1
json.dump(order,open('pins.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
from collections import Counter
print(len(order),Counter(r['board'] for r in order)); print('max desc',max(len(r['desc']) for r in order),'max title',max(len(r['title']) for r in order))
print(order[0]['title']); print(order[0]['desc'])
