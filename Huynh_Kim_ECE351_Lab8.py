# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 8                                                         #
# 10/20/20                                                      #
#                                                               #
#                                                               #
# ############################################################### 

import numpy as np
import math
import matplotlib . pyplot as plt
import scipy 
from scipy import signal as sig 

steps = 1e-5 # Define step size
t = np . arange (0 , 20 + steps , steps ) 
T = 8

def ak(k):
    return 0 

def bk(k):
    return (2/(np.pi*k))*(-np.cos(k*np.pi)+1)

def fourier(n, T, t):
    sum=0
    for k in range(1,n+1):
        sum=sum+(bk(k)*np.sin(k*2*np.pi/T*t))
    return sum

print('a0='+str(ak(0)))
print('a1='+str(ak(1)))
print('b1='+str(bk(1)))
print('b2='+str(bk(2)))
print('b3='+str(bk(3)))
print('')

plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 1)
plt . plot (t,fourier(1, T, t))
plt . grid ()
plt . title ('N=1')
plt . ylabel ('y(t)')
plt . xlabel('t')

#plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 2)
plt . plot (t,fourier(3, T, t))
plt . grid ()
plt . title ('N=3')
plt . ylabel ('y(t)')
plt . xlabel('t')

plt . subplot (3 , 1 , 3)
plt . plot (t,fourier(15, T, t))
plt . grid ()
plt . title ('N=15')
plt . ylabel ('y(t)')
plt . xlabel('t')

plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 1)
plt . plot (t,fourier(50, T, t))
plt . grid ()
plt . title ('N=50')
plt . ylabel ('y(t)')
plt . xlabel('t')

#plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 2)
plt . plot (t,fourier(150, T, t))
plt . grid ()
plt . title ('N=150')
plt . ylabel ('y(t)')
plt . xlabel('t')

plt . subplot (3 , 1 , 3)
plt . plot (t,fourier(1500, T, t))
plt . grid ()
plt . title ('N=1500')
plt . ylabel ('y(t)')
plt . xlabel('t')