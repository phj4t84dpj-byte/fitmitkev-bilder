# -*- coding: utf-8 -*-
"""Aus den ausgeschnittenen Original-Crops die Kachel-Bibliothek für den Renderer bauen:
   tiles_orig/<name>.png  (RGBA, Originalmaßstab 2160er-Board)  +  Zuordnung der G87-Kachelnamen."""
import json, os, glob, shutil, statistics
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as ndi
D=os.path.dirname(os.path.abspath(__file__))
LIB=f'{D}/tiles_orig'; os.makedirs(LIB,exist_ok=True)
meta=json.load(open(f'{D}/meta.json'))
# OCR-Crops (einzeln geprüft) ergänzen
for f in glob.glob(f'{D}/crops/*__G8[1-6]-*.png'):
    b=os.path.basename(f)[:-4]; name,rest=b.split('__'); board,i=rest.rsplit('_',1)
    im=Image.open(f); meta.append(dict(name=name,board=board,i=int(i),w=im.width,h=im.height))

def pick(name):
    c=[m for m in meta if m['name']==name and m['w']<=235 and m['h']<=235]
    if not c: return None
    unclipped=[m for m in c if not m.get('clip')]
    if unclipped: c=unclipped
    # größte Fläche = am wenigsten beschnitten (zusammengewachsene Doppel-Crops sind oben schon ausgefiltert)
    c.sort(key=lambda m:-(m['w']*m['h']))
    m=c[0]; return f"{D}/crops/{m['name']}__{m['board']}_{m['i']}.png"

names=sorted({m['name'] for m in meta})
index={}
for n in names:
    src=pick(n)
    if not src: continue
    dst=f'{LIB}/{n}.png'; shutil.copy(src,dst); index[n]=os.path.basename(src)
json.dump(index,open(f'{LIB}/_index.json','w'),ensure_ascii=False,indent=1)
print('Bibliothek:',len(index))

# Ketchup gibt es im Original nicht -> eigene Kachel (weißer Hintergrund) freistellen + Schatten wie im Original
def cut_white(path):
    im=Image.open(path).convert('RGB'); w,h=im.size
    from PIL import ImageDraw
    fill=im.copy()
    for pt in [(0,0),(w-1,0),(0,h-1),(w-1,h-1),(w//2,0),(0,h//2),(w-1,h//2),(w//2,h-1)]:
        try: ImageDraw.floodfill(fill,pt,(255,0,255),thresh=40)
        except Exception: pass
    fa=np.asarray(fill); bg=(fa[:,:,0]==255)&(fa[:,:,1]==0)&(fa[:,:,2]==255)
    obj=~bg
    obj=ndi.binary_fill_holes(obj)
    a=ndi.gaussian_filter(obj.astype(float),1.0)
    ys,xs=np.where(obj); y0,y1,x0,x1=ys.min(),ys.max(),xs.min(),xs.max()
    # auf Original-Kachelgröße bringen: Objektbreite ~150 px wie die Schalen im Original
    rgba=np.dstack([np.asarray(im),(a*255).astype(np.uint8)])
    t=Image.fromarray(rgba.astype(np.uint8),'RGBA').crop((x0-4,y0-4,x1+5,y1+5))
    s=150/max(t.width,t.height); t=t.resize((round(t.width*s),round(t.height*s)),Image.LANCZOS)
    # Schatten
    pad=24; canvas=Image.new('RGBA',(t.width+2*pad,t.height+2*pad),(0,0,0,0))
    sh=Image.new('RGBA',canvas.size,(0,0,0,0))
    alpha=Image.new('L',canvas.size,0); alpha.paste(t.split()[3],(pad+3,pad+10))
    alpha=alpha.filter(ImageFilter.GaussianBlur(7)).point(lambda v:int(v*0.45))
    sh.paste((45,32,20,255),(0,0),alpha)
    canvas=Image.alpha_composite(canvas,sh); canvas.alpha_composite(t,(pad,pad))
    return canvas
src=f'{D}/../g87/tiles/t_ketchup.jpg'
if os.path.exists(src):
    cut_white(src).save(f'{LIB}/ketchup.png'); print('ketchup eigene Kachel')

# Zuordnung G87-Kachelname -> Bibliotheksname
MAP={'apfel':'apfel','backpulver':'backpulver','bruehe':'rinderbruehe','dinkelmehl':'dinkelmehl','ei':'ei','erythrit':'erythrit',
 'frischkaese':'frischkaese_light','gurke':'salatgurke','gurken':'gewuerzgurken','gyrosgewuerz':'gyrosgewuerz','hack':'rinderhack',
 'haehnchen':'haehnchenbrust','haferflocken':'zarte_haferflocken','haselnuesse':'gemahlene_haselnuesse','honig':'honig','kakao':'backkakao',
 'kartoffeln':'kartoffeln','ketchup':'ketchup','kirschen':'sauerkirschen','kochschinken':'kochschinken','lasagneplatten':'lasagneplatten',
 'mandelblaettchen':'mandelblaettchen','milch':'milch','natron':'natron','nudeln':'nudeln','paprika':'paprika','puddingpulver':'vanillepudding_pulver',
 'quark':'magerquark','reibekaese':'reibekaese_light','reis':'reis','rosinen':'rosinen','salami':'salami','schokolade':'zartbitterschokolade',
 'senf':'senf','sesam':'sesam','skyr':'skyr','spekulatius':'spekulatius','tomaten':'passierte_tomaten','tomatenmark':'tomatenmark','zimt':'zimt',
 'zwiebel':'zwiebel','lebkuchengewuerz':'lebkuchengewuerz'}
missing=[k for k,v in MAP.items() if not os.path.exists(f'{LIB}/{v}.png')]
print('fehlt:',missing)
json.dump(MAP,open(f'{LIB}/_map_g87.json','w'),indent=1)
