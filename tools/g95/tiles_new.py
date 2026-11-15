# Neue Kacheln aus FLUX-Bildern mit weißem Hintergrund freistellen (wie tilex/build_tiles.cut_white) -> tiles_orig/<name>.png
import sys, os, numpy as np
from PIL import Image, ImageFilter, ImageDraw
from scipy import ndimage as ndi
D=os.path.dirname(os.path.abspath(__file__)); LIB=f"{D}/../tilex/tiles_orig"
def cut_white(path, target=150):
    im=Image.open(path).convert('RGB'); w,h=im.size
    fill=im.copy()
    for pt in [(0,0),(w-1,0),(0,h-1),(w-1,h-1),(w//2,0),(0,h//2),(w-1,h//2),(w//2,h-1)]:
        try: ImageDraw.floodfill(fill,pt,(255,0,255),thresh=40)
        except Exception: pass
    fa=np.asarray(fill); bg=(fa[:,:,0]==255)&(fa[:,:,1]==0)&(fa[:,:,2]==255)
    # weicher grauer Schlagschatten des Produktfotos: helle, farblose Pixel, die am Hintergrund hängen, gehören auch zum Hintergrund
    ia=np.asarray(im).astype(int); neutral=(ia.min(axis=2)>150)&((ia.max(axis=2)-ia.min(axis=2))<26)
    lab0,n0=ndi.label(bg|neutral)
    if n0: bg=np.isin(lab0,np.unique(lab0[bg]))&(lab0>0)
    obj=ndi.binary_fill_holes(~bg)
    lab,n=ndi.label(obj)
    if n>1:
        sizes=ndi.sum(obj,lab,range(1,n+1)); keep=[i+1 for i,s in enumerate(sizes) if s>=0.02*sizes.max()]; obj=np.isin(lab,keep)
    a=ndi.gaussian_filter(obj.astype(float),1.0)
    ys,xs=np.where(obj); y0,y1,x0,x1=ys.min(),ys.max(),xs.min(),xs.max()
    rgba=np.dstack([np.asarray(im),(a*255).astype(np.uint8)])
    t=Image.fromarray(rgba.astype(np.uint8),'RGBA').crop((max(0,x0-4),max(0,y0-4),x1+5,y1+5))
    s=target/max(t.width,t.height); t=t.resize((round(t.width*s),round(t.height*s)),Image.LANCZOS)
    pad=24; canvas=Image.new('RGBA',(t.width+2*pad,t.height+2*pad),(0,0,0,0))
    sh=Image.new('RGBA',canvas.size,(0,0,0,0)); alpha=Image.new('L',canvas.size,0); alpha.paste(t.split()[3],(pad+3,pad+10))
    alpha=alpha.filter(ImageFilter.GaussianBlur(7)).point(lambda v:int(v*0.45)); sh.paste((45,32,20,255),(0,0),alpha)
    canvas=Image.alpha_composite(canvas,sh); canvas.alpha_composite(t,(pad,pad)); return canvas
if __name__=='__main__':
    for p in sys.argv[1:]:
        name=os.path.splitext(os.path.basename(p))[0]; out=f"{LIB}/{name}.png"; cut_white(p).save(out); print(out, Image.open(out).size)
