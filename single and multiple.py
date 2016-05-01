# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 16:19:12 2016

@author: Yogi...!
"""

import numpy as np
from scipy.optimize import fsolve
print ("select the no. of stages. 1.Single stage  2. Two stage")
Z= raw_input("enter the choice: ")
Z=float(Z)
if Z==1:
    
    # SINGLE STAGE ADSORPTION
    #S_s: kg adsorbent
    #x_0: (kg solute)/(kg adsorbent)
    #L_s: kg solvent
    #y_0: (kg solute)/(kg solvent)
    #L_s*y_0+S_s*x_0=L_s*y_1+S_s*x_1
    #rearranging- L_s(y_1-y_0)=S_s(x_0-x_1)
    #y=m*x^n 
    #for an example of single stage adsorption.
    #(adsorption of polysubstituted phenol on activated carbon using single stage)
    

    m=raw_input("enter the value of m: ")
    n=raw_input("enter the value of n: ")
    L_s=raw_input("enter the value of solvent in kg: ")
    y_0=raw_input("enter the amount of pollutant in solvent in ppm: ")
    y_1=raw_input("enter the desired amount of pollutant at the output : ")
    x_0=raw_input("enter the amount of pollutant in adsorbent initially: ")
    m=float(m)
    n=float(n)
    L_s=float(L_s)
    y_0=float(y_0)
    y_1=float(y_1)
    x_0=float(x_0)
    x_1=(y_1*1/m)**(1/n) # where x_1 is in mg/g and y_1 is in ppm (GIVEN RELATIONSHIP)
    
    print "Amount of pollutant in adsorbent is:", x_1
    
    S_s=L_s*(y_1-y_0)/((x_0-x_1))
    print S_s
    print "Amount of adsorbent required for desired output in Kg:", S_s
else:
   # TWO STAAGE ADSSORPTION
   #S_s1: kg adsorbent at stage 1
   #S_s2: kg of adsorbent at stage 2
   #x_0: (kg solute)/(kg adsorbent)...amount of pollutant in adsorbent
   #L_s: kg solvent
   #y_0: (kg solute)/(kg solvent)...amount of pollutant in solvent
   #y_1: (kg of solute)/(kg of solvent)...amount of pollutant after first stage
   #y_2: (kg of solute)/(kg of solvent )...amount of polluant after second stage
   #L_s(y_0-y_1)=S_s1(x_1-x_0)...component balance and re-arrangement of stage 1
   #L_s(y_1-y_2)=S_s2(x_2-x_1)...component balance and re-arrangement of stage 2
   #for two stage operation (y_1/y_2)^1/n-(1/n)*(y_0/y_1)=1-1/n...to find out y1
   #S_s1+S_s2=L_s((y_1-y_0)/(x_0-x_1) + (y_2-y_1)/(x_0-x_2))...ST
   #(adsorption of polysubstituted phenol on activated carbon using double stage)
   m=raw_input("enter the value of m: ")
   n=raw_input("enter the value of n: ")
   L_s=raw_input("enter the value of solvent in kg: ")
   y_0=raw_input("enter the amount of pollutant present in solvent in ppm: ")
   y_2=raw_input("enter the desired amount of pollutantb at the output of stage 2 : ")
   x_0=raw_input("enter the amount of pollutant in adsorbent initially: ")
   m=float(m)
   n=float(n)
   L_s=float(L_s)
   y_0=float(y_0)
   y_2=float(y_2)
   x_0=float(x_0)
   
   def fun (u):
    return (u/y_2)**(1/n)-(1/n)*(y_0/u)-(1-1/n)
   y_1=fsolve(fun,3.5)
   #print y_1
   x_1=(y_1/m)**(1/n)
   #print x_1
   x_2=(y_2/m)**(1/n)
   #print x_2
   ST=L_s*((y_1-y_0)/(x_0-x_1) + (y_2-y_1)/(x_0-x_2))
   print "Minimum total amount of adsorbent requred for both the stages for desired output:", ST
                
    
        
    
    
            
            
    
    
    
    
    
    
