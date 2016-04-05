# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:10:21 2016

@author: Vishwajeet
"""

import scipy
# Tube side Fluid- OIL (Hot Fluid)******
cps=1940.0         # J/kg-K
ds=1.12            # kg/m^3
mus=1.046          # Pa-s
ko=0.01997         # W/m-K
Tins=45.0          # deg C
Touts=45.0         # deg C
ms=(8060.0/3600.0) # kg/s
lambs=1940.0       # KJ/Kg
R=8.314
Vs=(ms*R*Tins)/(0.018*1000)           # Volumetric flow rate,m^3/s
print 'volumetric flow rate of steam is ',Vs
print 'mass flow rate of steam is ',ms

# Shell side Fluid- Water (Cold Fluid)****
cpw=4.2            # KJ/kg-K
dw=993.0          # kg/m^3
muw=0.0008          # Pa-s
kw=0.571            # W/m-K
Tinw=25.0          # deg C
Toutw=40.0         # deg C

# ******Heat duty******
Q=(ms*cps*(Tins-Touts))+(ms*lambs)
print 'Heat duty (kW) is', Q

#***** Mass flowrate of Water******
mw=(Q)/(cpw*(Toutw-Tinw))
print 'mass flow rate of water in Kg/s is ',mw
#*****delT LM******
delT=(((Tins-Toutw)-(Touts-Tinw))/scipy.log((Tins-Toutw)/(Touts-Tinw)))
print 'delT LM',delT

#PARAMETERS CONSIDERED******
di=0.016       #m (inner Diameter)
do=0.019       #m (outer Diameter)
L=16*0.3048      #m (16 foot-Selected depending on available space)
Uass=1500.0       # J/(m^2*s*K)
n=1            #no of tube passes

Ah=(Q*1000)/(Uass*delT) #Heat transfer Area
print Ah
A1=(scipy.pi*do*L) # area of one tube
print A1
N1=Ah/A1
print N1
P=0
for i in range(0,100):
    while (P < N1):
        P = P + 1
    N1 = P
print N1   
# Cross flow Area
Act=(scipy.pi/16)*(do**2)*(N1)
#tube velocity
vt=mw/(dw*Act)
print 'tube velocity',vt

'''pitch and tube bundle diameter'''
print 'pitch and tube bundle diameter'
Pt=1.25*do
print Pt
a=0.158
b=2.263
Dtb=do*(N1/a)**(1/b)
print Dtb
# no. of tubes in centre row
Nr=Dtb/Pt
print Nr
#no. of tubes in vertical row
Nract=(2*Nr)/3
print 'number of tubes in vertical row are ', Nract 

'''Tube side hi calc''' 
print 'TUBE SIDE'
# film heat transfer coefficient on tube side
hi=4200*(0.5+0.02*(do-di))*vt**0.8*di**-0.2     # formula from literature
print 'Heat Transfer Coefficient(tube side)',hi

'''Shell Side ho calc'''
print 'SHELL SIDE'
# wall temperature estimation
kcond=4250  # W/m^2.C .... From literature assumed value.
Tw=Touts-(((Tins-Tinw)*Uass)/kcond)
print 'wall temperature',Tw
# condensate loading on horizontal tube,
CL=ms/(N1*L)
print CL
# Heat transfer coefficient in condensation is 
ho=(0.00075*kw*(dw*(dw-ds))*9.81)/((muw*CL)**(1/3)*Nract**(1/6))   # formula from literature
print 'Heat Transfer Coefficient(Shell side)',ho
# thermal conductivity of tube wall material ,
ku=50
'''Overall heat transfer coefficient'''
print  'Overall heat transfer coefficient  U'
U=1/((1/ho)+((do/di)*(1/hi))+(scipy.log(do/di)/(2*scipy.pi*ku*L)))
print 'U calculated',U