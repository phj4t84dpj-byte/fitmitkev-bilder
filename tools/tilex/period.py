# -*- coding: utf-8 -*-
"""Reihen über die Periodizität der Kachelspalte finden (ohne Zutatenliste)."""
import numpy as np
from scipy import ndimage as ndi
from tilex import X0, Y0, Y1, HI

def rows_by_period(diff, tx1):
    hard=(diff[Y0:Y1,X0:tx1]>HI)
    prof=ndi.gaussian_filter1d(hard.sum(1).astype(float),2)
    on=np.where(prof>0.5)[0]
    if len(on)<50: return []
    yf,yl=int(on[0]),int(on[-1])
    p=prof-prof.mean()
    lags=list(range(120,470)); ac=np.array([(p[:-lag]*p[lag:]).mean() for lag in lags])
    mx=ac.max(); pitch=None
    for i in range(1,len(ac)-1):
        if ac[i]>=ac[i-1] and ac[i]>=ac[i+1] and ac[i]>=0.55*mx:
            pitch=lags[i]; break
    if pitch is None: pitch=lags[int(np.argmax(ac))]
    span=yl-yf
    n=int(round((span+15)/pitch))
    n=max(1,min(8,n))
    if n==1: return [[yf+Y0,yl+Y0]]
    # Teilungspunkte: gleichmäßig zwischen yf und yl, dann aufs lokale Minimum schieben
    cuts=[]
    for k in range(1,n):
        s=yf+(span)*(k/n)
        lo=int(max(yf+20,s-30)); hi=int(min(yl-20,s+30))
        seg=prof[lo:hi+1]
        cuts.append(lo+int(np.argmin(seg)))
    bounds=[yf]+cuts+[yl+1]
    rows=[]
    for a,b in zip(bounds[:-1],bounds[1:]):
        sub=hard[a:b]; ys=np.where(sub.sum(1)>0)[0]; xs=np.where(sub.sum(0)>0)[0]
        if len(ys)==0 or len(xs)==0: rows.append([a+Y0,b+Y0,X0,tx1]); continue
        rows.append([a+int(ys.min())+Y0,a+int(ys.max())+1+Y0,int(xs.min())+X0,int(xs.max())+1+X0])
    return rows
