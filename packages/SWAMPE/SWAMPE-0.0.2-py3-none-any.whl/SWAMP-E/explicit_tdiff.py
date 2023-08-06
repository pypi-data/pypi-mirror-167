# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:35:48 2020

@author: ek672
"""

import numpy as np

#local imports
import spectral_transform as st
import filters



## PHI tstep
def phi_timestep(etam0,etam1,deltam0,deltam1,Phim0,Phim1,I,J,M,N,Am,Bm,Cm,Dm,Em,Fm,Gm,Um,Vm,Pmn,Hmn,w,tstepcoeff1,tstepcoeff2,mJarray,narray,PhiFM,dt,a,K4,Phibar,taurad,taudrag,forcflag,diffflag,sigma,sigmaPhi,test,t):
    
    Phicomp1=st.fwd_leg(Phim0, J, M, N, Pmn, w)
    
    Phicomp2prep=np.multiply(tstepcoeff1,np.multiply((1j)*mJarray,Cm))
    Phicomp2=st.fwd_leg(Phicomp2prep, J, M, N, Pmn, w)
    
    Phicomp3prep=np.multiply(tstepcoeff1,Dm)
    Phicomp3=st.fwd_leg(Phicomp3prep, J, M, N, Hmn, w)
    
    Phicomp4=2*dt*Phibar*st.fwd_leg(deltam1, J, M, N, Pmn, w)
    
    Phimntstep=Phicomp1-Phicomp2+Phicomp3-Phicomp4

    if forcflag==1:
        Phiforcing=st.fwd_leg(2*dt*PhiFM, J, M, N, Pmn, w)
        Phimntstep=Phimntstep+Phiforcing
        
    
    if diffflag==1:
        Phimntstep=filters.diffusion(Phimntstep, sigmaPhi)    
    
    newPhimtstep=st.invrs_leg(Phimntstep, I,J, M, N, Pmn)
    newPhitstep=st.invrs_fft(newPhimtstep, I)

    
    return Phimntstep,newPhitstep

def delta_timestep(etam0,etam1,deltam0,deltam1,Phim0,Phim1,I,J,M,N,Am,Bm,Cm,Dm,Em,Fm,Gm,Um,Vm,Pmn,Hmn,w,tstepcoeff1,tstepcoeff2,mJarray,narray,PhiFM,dt,a,K4,Phibar,taurad,taudrag,forcflag,diffflag,sigma,sigmaPhi,test,t):
    deltacomp1=st.fwd_leg(deltam0, J, M, N, Pmn, w)
    
    deltacomp2prep=np.multiply(np.multiply(tstepcoeff1,(1j)*mJarray),Bm)
    deltacomp2=st.fwd_leg(deltacomp2prep, J, M, N, Pmn, w)
    

    deltacomp3prep=np.multiply(tstepcoeff1,Am)

    deltacomp3=st.fwd_leg(deltacomp3prep, J, M, N, Hmn, w)
    

    deltacomp4prep=np.multiply(tstepcoeff2,Phim1+Em)
    deltacomp4=st.fwd_leg(deltacomp4prep, J, M, N, Pmn, w)
    
    deltacomp4=np.multiply(narray,deltacomp4)
    
    #deltamntstep=deltacomp1+deltacomp2+deltacomp3+deltacomp4
    deltamntstep=deltacomp1#+deltacomp2+deltacomp4

    if forcflag==1:

        deltaf1prep=np.multiply(np.multiply(tstepcoeff1,(1j)*mJarray),Um)/taudrag
        deltaf1=st.fwd_leg(deltaf1prep, J, M, N, Pmn, w)
        
        deltaf2prep=np.multiply(tstepcoeff1,Vm)/taudrag
        deltaf2=st.fwd_leg(deltaf2prep, J, M, N, Hmn, w)
        
        deltaf3prep=np.multiply(np.multiply(tstepcoeff1,(1j)*mJarray),Fm)
        deltaf3=st.fwd_leg(deltaf3prep, J, M, N, Pmn, w)
        
        deltaf4prep=np.multiply(tstepcoeff1,Gm)
        deltaf4=st.fwd_leg(deltaf4prep, J, M, N, Hmn, w)
        
        deltaforcing=-deltaf1+deltaf2+deltaf3-deltaf4
        deltamntstep=deltamntstep+deltaforcing
        
    
    if diffflag==1:
        deltamntstep=filters.diffusion(deltamntstep, sigma)

    newdeltamtstep=st.invrs_leg(deltamntstep, I,J, M, N, Pmn)
    newdeltatstep=st.invrs_fft(newdeltamtstep, I)
    return deltamntstep,newdeltatstep


def eta_timestep(etam0,etam1,deltam0,deltam1,Phim0,Phim1,I,J,M,N,Am,Bm,Cm,Dm,Em,Fm,Gm,Um,Vm,Pmn,Hmn,w,tstepcoeff1,tstepcoeff2,mJarray,narray,PhiFM,dt,a,K4,Phibar,taurad,taudrag,forcflag,diffflag,sigma,sigmaPhi,test,t):

    etacomp1=st.fwd_leg(etam0, J, M, N, Pmn, w)

    etacomp2prep=np.multiply(np.multiply(tstepcoeff1,(1j)*mJarray),Am)
    etacomp2=st.fwd_leg(etacomp2prep, J, M, N, Pmn, w)
    
    etacomp3prep=np.multiply(tstepcoeff1,Bm)
    etacomp3=st.fwd_leg(etacomp3prep, J, M, N, Hmn, w)
    
    
    
    etamntstep=etacomp1-etacomp2+etacomp3
    
    if forcflag==1:
        
        etaf1prep=np.multiply(np.multiply(tstepcoeff1,(1j)*mJarray),Vm)/taudrag
        etaf1=st.fwd_leg(etaf1prep, J, M, N, Pmn, w)
        
        etaf2prep=np.multiply(tstepcoeff1,Um)/taudrag
        etaf2=st.fwd_leg(etaf2prep, J, M, N, Hmn, w)
        
        etaf3prep=np.multiply(np.multiply(tstepcoeff1,(1j)*mJarray),Gm)
        etaf3=st.fwd_leg(etaf3prep, J, M, N, Pmn, w)
        
        etaf4prep=np.multiply(tstepcoeff1,Fm)
        etaf4=st.fwd_leg(etaf4prep, J, M, N, Hmn, w)
        
        etaforcing=-etaf1+etaf2+etaf3+etaf4
    
        etamntstep=etamntstep+etaforcing

    
    if diffflag==1:
        etamntstep=filters.diffusion(etamntstep, sigma)
    
    newetamtstep=st.invrs_leg(etamntstep, I,J, M, N, Pmn)
    newetatstep=st.invrs_fft(newetamtstep, I)
    return etamntstep,newetatstep
