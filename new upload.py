# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 8:10:30 2016

@author: Vishwajeet
"""
import numpy
import scipy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import scipy.optimize as opt
import pylab
# Tube side Fluid-(Steam)******
cps=1940.0         # J/kg-K
ds=1.12            # kg/m^3
mus=1.046          # Pa-s
ks=0.01997         # W/m-K
Tins=45.0          # deg C
Touts=45.0         # deg C
ms=(8060.0/3600.0) # kg/s
lambs=1940.0       # KJ/Kg
R=8.314            #J/kg.k
Vs=(ms*R*Tins)/(0.018*1000)           # Volumetric flow rate,m^3/s
print 'volumetric flow rate of steam is ',Vs
print 'mass flow rate of steam is ',ms
# Shell side Fluid- Water (Cold Fluid)****
cpw=4.2            # KJ/kg-K
dw=993.0           # kg/m^3
muw=0.0008         # Pa-s
kw=0.571           # W/m-K
Tinw=25.0          # deg C
'''From trial.py using LMTD approach, lets take the value of water flow rate, area of heat transfer and U as the same'''
mw=68.9435626102   # kg/s
print 'mass flow rate of water is ',mw
U=1697.72
A=267.61
n=20
Tcguess=n*[Tinw]
T0=numpy.array(Tcguess)
print T0
#PARAMETERS CONSIDERED******
di=0.016       #m (inner Diameter)
do=0.019       #m (outer Diameter)
L=16*0.3048      #m (16 foot-Selected depending on available space)
print'the length of pipe',L
n=1            #no of tube passes
Nt= 920        # no. of tube passes.
# constant term in the integral is
const=(scipy.pi*U*Nt)/(mw*cpw)
print 'the constant term is ',const
def rk4( f, Tinw, x ):
    """Fourth-order Runge-Kutta method to solve T' = f(x,t) with T(x[0]) = Tinw.

    USAGE:
        T = rk4(f, Tinw, x)

    INPUT:
        f     - function of x and t equal to dT/dx.  
        Tinw    - the initial condition(s).  Specifies the value of T when
                x = x[0].  Can be either a scalar or a list or NumPy array
                if a system of equations is being solved.
        x     - list or NumPy array of x values to compute solution at.
                x[0] is the the initial condition point, and the difference
                h=x[i+1]-x[i] determines the step size h.

    OUTPUT:
        T     - NumPy array containing solution values corresponding to each
                entry in T array.  If a system is being solved, T will be
                an array of arrays.
    """
    
    n = len( x )
    T = numpy.array( [ T0 ] * n )
    f=-(const)*(Tinw-T)
    for i in xrange( n - 1 ):
        h = x[i+1] - x[i]
        k1 = h * f( T[i], x[i] )
        k2 = h * f( T[i] + 0.5 * k1, x[i] + 0.5 * h )
        k3 = h * f( T[i] + 0.5 * k2, x[i] + 0.5 * h )
        k4 = h * f( T[i] + k3, x[i+1] )
        T[i+1] = T[i] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0
        x=0.0
        T=Tinw

    return T
    print T