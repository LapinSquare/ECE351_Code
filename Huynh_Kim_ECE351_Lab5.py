# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 5                                                       #
# 9/29/20                                                        #
#                                                               #
#                                                               #
# ############################################################### 

import numpy as np
import matplotlib . pyplot as plt
import scipy 
from scipy import signal as sig

#plt.rcParams.update({ 'font.size' : 14}) # Set font size in plots

steps = 1e-5 # Define step size
t = np . arange (-10 , 10 + steps , steps ) 
NN=len(t)
tExtend = np.arange(2*t[0], 2*t[NN-1]+steps, steps)


def ramp ( t ) : # The only variable sent to the function is t
    y = np . zeros ( t . shape ) # initialze y(t) as an array of zeros

    for i in range (len ( t ) ) : # run the loop once for each index of t
        if t[ i ] < 0:
            y [ i ] = 0
        else :
            y [ i ] = t[ i ]
    return y # send back the output stored in an array

def step ( t ) : # The only variable sent to the function is t
    y = np . zeros ( t . shape ) # initialze y(t) as an array of zeros

    for i in range (len ( t ) ) : # run the loop once for each index of t
        if t[ i ] < 0:
            y [ i ] = 0
        else :
            y [ i ] = 1
    return y # send back the output stored in an array

def convolution( f1, f2 ): #user-defined convolution
    #Get correct length. 
    #Make dummy variables
    a = len(f1)
    b = len(f2) 
    f1Extend = np.append(f1, np.zeros((1, b-1))) #Start 1 instead of 0.
    f2Extend = np.append(f2, np.zeros((1, a-1))) 
    result = np.zeros(f1Extend.shape) #Extend with 0s. 
    
    for i in range(a+b-2): 
        result[i]=0 
        for j in range(a): 
            if(i-j+1>0): 
                try: #Make second start at one.
                    result[i] += f1Extend[j]*f2Extend[i-j+1] 
                except: #Dig out exception
                    print(i,j)
    return result


def sineImpulse(R, L, C, t):
    alpha = -1/(2*R*C)
    omega = 0.5*np.sqrt((1/(R*C))**2-4*(1/(np.sqrt(L*C)))**2 +0*1j)
    p = alpha+ omega
    g = (1/(R*C))*p
    g_mag = np.abs(g)
    g_deg = np.angle(g) 
    y = (g_mag/np.abs(omega)) * np.exp(alpha*t)*np.sin(np.abs(omega)*t+g_deg)*step(t) 
    return y 

t = np . arange (0 , 1.2e-3+steps , steps )
R = 1000
L = 0.027
C = (100e-9)
 
num=[(1/(R*C)), 0]
den= [1, (1/(R*C)), (1/(L*C)) ]
#tout=yout=sig.impulse((num, den), T=t)

plt . figure ( figsize = (10 , 20) )
plt . subplot (2 , 1 , 1)
plt . plot (t , sineImpulse(R, L, C, t), label="Hand calculated" )
plt . grid ()
plt . legend()
#plt . xlabel('t[s]')
plt . title ('Impulse h(t) - Hand calculated')
plt . ylabel ('h(t)')
plt . xlabel('t')

tout, yout=sig.impulse((num, den), T=t)

plt . subplot (2 , 1 , 2)
plt . plot (tout , yout, label="Python" )
plt . grid ()
plt . legend()
plt . xlabel('t')
plt . ylabel ('h(t)')
plt . title ('Impulse h(t) - Python generated')
plt.show()
    
num=[(1/(R*C)), 0]
den=[1, (1/(R*C)), ((1/np.sqrt(L*C))**2)]
tout, yout =sig.step((num, den), T=t)

plt . figure ( figsize = (10 , 20) )
plt . subplot (2 , 1 , 1)
plt . plot (tout, yout, label="Python" )
plt . grid ()
plt . legend()
#plt . xlabel('t[s]')
plt . ylabel ('H(s)')
plt . xlabel('s')
plt . title ('Final Value Theorem')

