# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:07:20 2021

@author: ek672
"""

import params as p
import main_function as main
#import main_function as main

M=p.M

dt1=p.dt
# Length of the run in time steps
tmax = p.tmax
#surface gravity
g=p.g
#radiative time scale in Earth days
taurad=p.taurad
#drag time scale in Earth days
taudrag=p.taudrag
#mean geopotential height. In hot Jupiter case, Phibar is the flat nightside thickness
Phibar=p.Phibar
#the difference in radiative-equilibrium thickness between the substellar point and the nightside
DPhieq=p.DPhieq

#rotation rate of the planet, radians per second
omega=p.omega
#planetary radius, meters
a=p.a
#angle for test cases 1 and 2, radians
a1=p.a1
#test case, number
test=p.test

#colorbar settings for plotting
minlevel=p.minlevel
maxlevel=p.maxlevel

#forcing flag
forcflag=p.forcflag
#hyperviscosity filter flag
diffflag=p.diffflag

#continuation flag
contflag=p.contflag
#flag to save
saveflag=p.saveflag
#save frequency
savefreq=p.savefreq

#flag for anti-aliasing filter as in Hack and Jakob (1992) eq. (4.4)
modalflag=p.modalflag
# if modalflag==1:
alpha=p.alpha

plotflag=p.plotflag
plotfreq=p.plotfreq

K6=p.K6


k1= 0.0002#0.0002
k2vec=[0.0004]#[0.182606]
#k2vec=[1*10**(-2),2*10**(-2)]
#k2vec=[0.0002]
# for i in range(len(k2vec)):

#     k2=k2vec[i]
    #print(k2)
    #main.main(M,dt1,tmax,g,taurad,taudrag,Phibar,DPhieq,omega,a,a1,test,minlevel, maxlevel, forcflag,diffflag,modalflag,alpha,plotflag, plotfreq,contflag,saveflag,savefreq,k1,k2,pressure,Cp,R,sigmaSB)
    #main.main(M,dt1,tmax,Phibar, omega, a, test=p.test, DPhieq=DPhieq, plotflag=plotflag, plotfreq=plotfreq, minlevel=6.4, maxlevel=6.8, saveflag=1, savefreq=150, k1=k1, k2=k2,taudrag=p.taudrag, taurad=p.taurad,R=p.R, diffflag=p.diffflag)
main.main(M,dt1,tmax,Phibar, omega, a, test=p.test, DPhieq=p.DPhieq, plotflag=p.plotflag, forcflag=p.forcflag, plotfreq=p.plotfreq, minlevel=p.minlevel, maxlevel=p.maxlevel, saveflag=p.saveflag, savefreq=p.savefreq, taudrag=p.taudrag, taurad=p.taurad, diffflag=p.diffflag,g=p.g,alpha=p.alpha,K6=K6,expflag=p.expflag,custompath="C:/Users/ek672/Documents/testdata/",contflag=0,contTime=0,timeunits='minutes')
#check if k1, k2 are overwritten when params are called in main_function



