# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 8:10:30 2016

@author: Vishwajeet
"""

import numpy as np
import scipy
from scipy.integrate import odeint
import matplotlib.pyplot as plt
'''ort scipy.optimize as opt
import pylab'''


# Tube side Fluid-(Steam)******

cps=1940.0         # J/kg-K
ds=1.12            # kg/m^3
mus=1.046          # Pa-s
ks=0.01997         # W/m-K
Tins=45   # deg C
Touts=45.0         # deg C
ms=(8060.0/3600.0) # kg/s
lambs=1940.0       # KJ/Kg
R=8.314            #J/kg.k

print "-----------------------------"

print 'mass flow rate of steam is: \t',ms


# ******Heat duty******

Q=(ms*cps*(Tins-Touts))+(ms*lambs)
print "-----------------------------"
print 'Heat duty (kW) is: \t', Q


# Shell side Fluid- Water (Cold Fluid)****
cpw=4.2            # KJ/kg-K
dw=993.0           # kg/m^3
muw=0.0008         # Pa-s
kw=0.571           # W/m-K
Tinw=25.0          # deg C

print "-----------------------------"
# Assumed value of Overall heat transfer coefficient

U=[200,300,400,500,600]
print'Assumed value of Overall heat transfer coefficient\t',U 
print "---------------------------------------------"

T0=25.00001


#PARAMETERS CONSIDERED******

di=0.012       #m (inner Diameter)
do=0.016       #m (outer Diameter)
L=16*0.3048      #m (16 foot-Selected depending on available space)
L=[8*0.3048,12*0.3048,16*0.3048,20*0.3048,24*0.3048]

print'the length of pipe:\t\t\t\t\t',L
print "----------------------------------------------"

n=1            #no of tube passes
Nt= 400        # no. of tube passes.

# constant term in the integral is
const=[]
for i in range(5):
    const.append((scipy.pi*U[i]*Nt*do)/(Q))
print 'the constant term is \t\t\t\t',const


def CounterCurrentTemp(T,x,const):
    dtdx=const*((Tins-T)/(T-Tinw))
    return dtdx
    
def CoCurrentTemp(T,x):
    dtdx=const*((Tins-T)/(T-Tinw))
    return dtdx
    
print '______________________________________________________'    
print '----Below is the Temperature for Inlet and Outlet----'
print '---------------------------------------------------------'
print "For different values of overall heat transfer coefficient"
print '---------------------------------------------------------'
profile=[]
LengthPiece=[]
Label=['Length=8ft','Length=12ft','Length=16ft','Length=20ft','Length=24ft']
color=['r','g','b','y','m']
for i in range(5):
    LengthPiece.append(np.linspace(0,L[i],15))
    profile.append(odeint(CounterCurrentTemp,T0,LengthPiece[i],args=(const[i],)))
       
    print "For Type", i+1,":"   
    print "Inlet Temp:", round(profile[i][0][0],2),"degree Celsius"
    print "Outlet Temp:", round(profile[i][-1][0],2), "degree Celsius"
    print '------------------------------------'
    plt.figure(1)    
    plt.plot(LengthPiece[i],profile[i], '-', color=color[i], label=Label[i])
    plt.axvline(x=LengthPiece[i][-1],color='black')
    plt.xlabel('length(in meter)')
    plt.ylabel('temperature(degree C)')
    plt.show()
    plt.pause(0.5)    
    plt.legend()

print "For value of overall heat transfer coefficient: 200"
print '---------------------------------------------------------'
profile=[]
for i in range(5):
    LengthPiece.append(np.linspace(0,L[i],15))
    profile.append(odeint(CounterCurrentTemp,T0,LengthPiece[i],args=(const[0],)))
       
    print "For Type", i+1,":"   
    print "Inlet Temp:", round(profile[i][0][0],2),"degree Celsius"
    print "Outlet Temp:", round(profile[i][-1][0],2), "degree Celsius"
    print '------------------------------------'
    plt.figure(2)
    plt.plot(LengthPiece[i],profile[i], '-', color=color[i], label=Label[i])
    plt.axvline(x=LengthPiece[i][-1],color='black')
    plt.xlabel('length(in meter)')
    plt.ylabel('temperature(degree C)')
    plt.show()
    plt.pause(0.5)    
    plt.legend()    
    
