# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 10                                                        #
# 11/3/20                                                       #
#                                                               #
#                                                               #
# ############################################################### 

import numpy as np
import math
import matplotlib . pyplot as plt
import scipy 
import scipy.fftpack
from scipy import signal as sig 
import control as con

steps = 1e3 # Define step size
t = np . arange (0 , 20 + steps , steps ) 
w = np . arange (10**3 , 10**6 + steps , steps ) 
R = 1000
C = 100e-9
L = 27e-3

def h_mag(w, R, C, L):
    return (w/(R*C))/ np.sqrt( (-w**2+1/(L*C))**2 + (w/(R*C))**2 )

def h_phi(w, R, C, L):
    return (np.pi/2)-np.arctan((w/(R*C))/(-w**2+1/(L*C)))

x=h_phi(w, R, C, L)
for k in range(len(w)) :
    if (x[k]>(np.pi/2)): #>90
        x[k]=x[k]-np.pi  #180

h_num= [1/(R*C), 0]
h_den= [1, 1/(R*C), 1/(L*C)]

#%% PART 1

plt . figure ( figsize = (10 , 20) )
plt . subplot (2 , 1 , 1)
plt . semilogx(w, h_mag(w, R, C, L))
plt . grid ()
plt . title ('Task 1 Mag')
plt . ylabel ('h(w)')
plt . xlabel('w')

plt . subplot (2 , 1 , 2)
plt . semilogx(w, x)
plt . grid ()
plt . title ('Task 1 Phase')
plt . ylabel ('h(w)')
plt . xlabel('w')


freq, mag, phase = sig . bode((h_num, h_den), w)
plt . figure ( figsize = (10 , 20) )
plt . subplot (2 , 1 , 1)
plt . semilogx(freq, mag)
plt . grid ()
plt . title ('Task 2 Mag')
plt . ylabel ('h(w)')
plt . xlabel('w')

plt . subplot (2 , 1 , 2)
plt . semilogx(freq, phase)
plt . grid ()
plt . title ('Task 2 Phase')
plt . ylabel ('h(w)')
plt . xlabel('w')

plt . figure ( figsize = (10 , 20) )
plt . title ('Bode plots')
sys = con . TransferFunction ( h_num , h_den )
_ = con . bode ( sys , w , dB = True , Hz = True , deg = True , Plot = True )

#%% PART 2

#x(t) = cos(2π · 100t) + cos(2π · 3024t) + sin(2π · 50000t)
def func2(t):
    return np.cos(2*np.pi*100*t) + np.cos(2*np.pi*3024*t) + np.sin(2*np.pi*50000*t)

steps = 1/(50000*2*np.pi) #fs=largest frequency.
t = np . arange (0 , 0.01 + steps , steps ) 

plt . figure ( figsize = (10 , 20) )
plt . subplot (2 , 1 , 1)
plt . plot(t, func2(t))
plt . grid ()
plt . title ('Part 2 Plot')
plt . ylabel ('x(t)')
plt . xlabel('t')

b_num, b_den=sig . bilinear(h_num, h_den, 50000*2*np.pi)
b_arr=sig . lfilter(b_num, b_den, func2(t))

plt . subplot (2 , 1 , 2)
plt . plot(t, b_arr)
plt . grid ()
plt . title ('Part 2 Plot, filtered')
plt . ylabel ('y(t)')
plt . xlabel('t')

