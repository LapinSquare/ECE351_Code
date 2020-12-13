# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 6                                                       #
# 10/6/20                                                        #
#                                                               #
#                                                               #
# ############################################################### 

import numpy as np
import matplotlib . pyplot as plt
import scipy 
from scipy import signal as sig

#plt.rcParams.update({ 'font.size' : 14}) # Set font size in plots

steps = 1e-5 # Define step size
t = np . arange (0 , 10 + steps , steps ) 
#t = np . arange (0 , 1.2e-3+steps , steps )

def step ( t ) : # The only variable sent to the function is t
    y = np . zeros ( t . shape ) # initialze y(t) as an array of zeros

    for i in range (len ( t ) ) : # run the loop once for each index of t
        if t[ i ] < 0:
            y [ i ] = 0
        else :
            y [ i ] = 1
    return y # send back the output stored in an array

def func1(t): 
    return (0.5+np.exp(-6*t)-0.5*np.exp(-4*t))*step(t)

def func2(s): #H(s)
    return (s**2+(6*s)+12)/((s+6)(s+4)) 

def cosMethod(r, p, t): 
    alpha=np.real(p)
    omega=np.imag(p)
    return np.abs(r)*np.exp(alpha*t)*np.cos(omega*t+np.angle(r))*step(t)

plt . figure ( figsize = (10 , 20) )
plt . subplot (2 , 1 , 1)
plt . plot (t , func1(t), label="Hand calculated" )
plt . grid ()
plt . legend()
#plt . xlabel('t[s]')
plt . title ('Impulse h(t) - Hand calculated')
plt . ylabel ('h(t)')
plt. xlim(0,2)
plt. ylim([0,1])
plt . xlabel('t')

num=[1, 6, 12]
den=[1, 10, 24]
tout, yout =sig.step((num, den), T=t)

#plt . figure ( figsize = (10 , 20) )
plt . subplot (2 , 1 , 2)
plt . plot (tout, yout, label="Python" )
plt . grid ()
plt . legend()
#plt . xlabel('t[s]')
plt . ylabel ('H(s)')
plt . xlabel('s')
plt. xlim(0,2)
plt. ylim([0,1])
plt . title ('H(s) with step')

num=[1, 6, 12]
den=[1, 10, 24, 0]
r, p, _ = sig.residue(num, den)
print('First part')
print('r='+str(r))
print('')
print('p='+str(p))


num=[25250]
den=[1, 18, 218, 2036, 9085, 25250, 0]
r, p, _ = sig.residue(num, den)
print('')
print('Second part')
print('r='+str(r))
print('')
print('p='+str(p))
#print('')
#print('k='+str(k))


t = np . arange (0 , 4.5 + steps , steps ) 
result=0
for i in range(len(r)):
    result+=cosMethod(r[i], p[i], t)
    
plt . figure ( figsize = (10 , 20) )
plt . subplot (2 , 1 , 1)
plt . plot (t , result)
plt . grid ()
#plt . legend()
#plt . xlabel('t[s]')
plt . title ('Residue with cosine method')
plt . ylabel ('y(t)')
#plt. xlim(0,4.5)
#plt. ylim([0,1.2])
plt . xlabel('t')

num=[25250]
den=[1, 18, 218, 2036, 9085, 25250]
tout, yout =sig.step((num, den), T=t)
plt . subplot (2 , 1 , 2)
plt . title ('Residue with step')
plt . plot (tout, yout, label="Python" )
plt . grid ()
plt . ylabel ('y(t)')
plt . xlabel('t')