# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 09:55:45 2016

@author: Vishwajeet
"""
import scipy
# Tube side Fluid- OIL (Hot Fluid)******
cps=1940.0         # J/kg-K
ds=0.06556         # kg/m^3
mus=1.046          # Pa-s
ko=0.01997         # W/m-K
Tins=45.0          # deg C
Touts=45.0         # deg C
ms=(8060.0/3600.0) # kg/s
lambs=1940.0       # J/Kg
Vs=ms/ds           # Volumetric flow rate,m^3/s
print 'volumetric flow rate of steam is ',Vs
print 'mass flow rate of steam is ',ms

# Shell side Fluid- Water (Cold Fluid)****
cpw=4.2            # J/kg-K
dw=1000.0          # kg/m^3
muw=0.001          # Pa-s
kw=0.64            # W/m-K
Tinw=25.0          # deg C
Toutw=40.0         # deg C

# ******Heat duty******
Q=(ms*cps*(Tins-Touts))+(ms*lambs)
print 'Heat duty (kW) is', Q

#***** Mass flowrate of Water******
mw=Q/(cpw*(Toutw-Tinw))
print 'mass flow rate of water in Kg/s is ',mw
#*****delT LM******
delT=(((Tins-Toutw)-(Touts-Tinw))/scipy.log((Tins-Toutw)/(Touts-Tinw)))
print 'delT LM',delT


'''#LMTD Correction factor For Multipasses
R=(Tinw-Toutw)/(Touts-Tins)
S=(Touts-Tins)/(Tinw-Tins)
print 'R,S-',R,     S
num=scipy.sqrt((R**2+1))*scipy.log(((1-S)/(1-R*S)))
den=(R-1)*scipy.log(((2-S*((R+1)-scipy.sqrt(R**2+1)))/(2-S*((R+1)+scipy.sqrt(R**2+1)))))
Ft=num/den
print 'LMTD Correction factor For Multipasses-',Ft

# assumption for U
Uass=1000.0       # J/(m^2*s*K)


#INITIAL GUESS********
F=1'''


#PARAMETERS CONSIDERED******
di=0.022       #m (inner Diameter)
do=0.024       #m (outer Diameter)
L=5*0.3048      #m (16 foot-Selected depending on available space)



n=1            #no of tube passes
def velocity(n):
    A=Q/(Uass*delT) #Heat transfer Area
    print A
    global N
    # Number of Tubes
    N1=A/(scipy.pi*do*L)
    N=round(N1)
   
    '''if n<>1:
        N=N/n
    # no of filled tubes'''

    # Cross flow Area
    Acs=N*scipy.pi*.25*(di)**2
    v=Vs/(Acs)
    return v

vel=velocity(n)

'''while vel<1 :
    F=Ft
    n=n+2
    vel=velocity(F,n)
print 'Number of passes-',n    
print 'Velocity-', vel'''

# *** CALCULATIONS OF SHELL SIDE DIMENSIONS ***
PT=1.5*do             #Pitch
Clr=0.5*do            #Clearance

""" Square Layout :Water is a dirty fluid """
""" For n=2 and Square Pitch """
K1=.156
n1=2.291
N=N*n                 #Total Number of Tubes
Dtb=do*(N/K1)**(1/n1) # Tube Bundle Diameter
print 'Tube Bundle Diameter-',Dtb
c=0.04                # Clearance=30-40 mm
 
Ds=Dtb+c 
print 'Shell Diameter',Ds

"""Baffle -Segmental Baffle (25% Baffle Cut)"""
Diabaffle=Ds-0.005      #Clearance of 4-6 mm
print 'Baffle Diameter',Diabaffle
Baffle_spacing=Ds       #Baffle_spacing: .2 Ds to Ds
print'Baffle spacing=',Baffle_spacing
tcs=(Ds*Clr*Baffle_spacing)/PT
print 'Cross flow area(Shell side)', tcs
vs=mw/(dw*tcs)          # Shell side velocity
print 'Shell side velocity',vs

'''Tube side hi calc''' 
print 'TUBE SIDE'
Ret=di*vel*doil/(muo)
print 'Re (Tube Side)',Ret
Prt=cpo*muo/ko
print 'Pr (Tube Side)',Prt
hi=.023*((Ret)**0.8)*((Prt)**.3)*ko/do
print 'Heat Transfer Coefficient(tube side)',hi
  
'''Shell Side ho calc'''
print 'SHELL SIDE'
De=4*(PT**2-scipy.pi*.25*do**2)/(scipy.pi*do)
print 'Equivalent Diameter',De
Res=De*vs*dw/muw
print 'Re (Shell Side)',Res
Prs=cpw*muw/kw
print 'Pr (Shell side)',Prs
ho=.023*((Res)**0.8)*((Prs)**.4)*kw/De
print 'Heat Transfer Coefficient(Shell side)',ho


""" COMPUTED U"""
U=1/((do**2/(di**2*hi))+(1/ho))
print 'U calculated'
print U

"""pressure drop calculations"""
print 'pressure drop calculations'

fs=0.046*Res**-.2
DeltaPshell=0.5*(fs*(dw*vs)**2*Ds*4)/(De)  
print 'Delta P shellside ' , DeltaPshell # Pa

ft=16/Ret
DeltaPtube1=0.5*(ft*(doil*vel)**2*L*18)/(di*doil/dw*muo/muw)  # straight pipe
DeltaPtube2=4*n*vel**2/(2*9.8)*doil
DeltaPtube=DeltaPtube1+DeltaPtube2
print 'Delta P tubeside ' , DeltaPtube # Pa'''

    
    







