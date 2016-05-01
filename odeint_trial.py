# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:33:03 2016

@author: Vishwajeet
"""
import numpy as np
import scipy as sc
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def f(y, x):
    y0 = y[0]
    y1 = y[1]
    y2 = ((3*x+2)*y1 + (6*x-8)*y0)/(3*x-1)
    return y1, y2

# Initial conditions on y, y' at x=0
init = 2.0, 3.0
# First integrate from 0 to 2
x = np.linspace(0,2,100)
sol=odeint(f, init, x)
print sol
# Then integrate from 0 to -2
plt.plot(x, sol[:,0], color='b')
x = np.linspace(0,-2,100)
sol=odeint(f, init, x)
plt.plot(x, sol[:,0], color='b')

# The analytical answer in red dots
exact_x = np.linspace(-2,2,10)
exact_y = 2*np.exp(2*exact_x)-exact_x*np.exp(-exact_x)
plt.plot(exact_x,exact_y, 'o', color='r', label='exact')
plt.legend()

plt.show()