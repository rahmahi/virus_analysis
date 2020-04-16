#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 07:08:08 2020

@author: mahi
email: mrahamah@scholar.buruniv.ac.in
"""
import numpy as np
from scipy.interpolate import interp1d
from scipy import arange, array, exp
import matplotlib.pyplot as plt
def extrap1d(interpolator):
    xs = interpolator.x
    ys = interpolator.y

    def pointwise(x):
        if x < xs[0]:
            return ys[0]+(x-xs[0])*(ys[1]-ys[0])/(xs[1]-xs[0])
        elif x > xs[-1]:
            return ys[-1]+(x-xs[-1])*(ys[-1]-ys[-2])/(xs[-1]-xs[-2])
        else:
            return interpolator(x)

    def ufunclike(xs):
        return array(list(map(pointwise, array(xs))))

    return ufunclike

dataday = 48
nxtN = 2
nxtdy = np.arange(nxtN)
nxtdata = np.zeros(nxtN)

dt = np.loadtxt("data")
dy = np.arange(dataday)
np.savetxt("datafull.txt",np.vstack((dy,dt)).T)
data = np.loadtxt("datafull.txt")
day = data[:,0]
case = data[:,1]

f_i = interp1d(day, case)
f_x = extrap1d(f_i)

#print (f_x([48]))
for i in nxtdy:
    #print(f_x([dataday+i]))
    nxtdata[i] = f_x([dataday+i])
fcase = np.append(case,nxtdata)
fday = np.arange(1,dataday + nxtN +1)

plt.plot(fday,fcase)
plt.plot(day,case,'ro')
plt.show()