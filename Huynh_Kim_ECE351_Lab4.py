# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 4                                                        #
# 9/15/20                                                        #
#                                                               #
#                                                               #
# ############################################################### 

import numpy as np
import matplotlib . pyplot as plt
import scipy 
from scipy import signal as sig

#plt.rcParams.update({ 'font.size' : 14}) # Set font size in plots

steps = 1e-2 # Define step size
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

def func1( t ): 
    return np.exp(2*t)*step(1-t) 

def func2( t ): 
    return step(t-2)-step(t-6) 

def func3( t ): 
    return np.cos((2*np.pi*0.25)*t)*step(t)

def calcFunc1( t ): 
    return 1/2*(np.exp(2*tExtend)*step(1-tExtend) + np.exp(2)*step(tExtend-1))

def calcFunc2( t ): 
    return (tExtend-2)*step(tExtend-2)-(tExtend-6)*step(tExtend-6)

def calcFunc3( t ): 
    return -1/(2*np.pi*0.25)*np.sin((2*np.pi*0.25)*tExtend)*step(tExtend)


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


plt . figure ( figsize = (10 , 7) )
plt . subplot (3 , 1 , 1)
plt . plot (t , func1(t) )
plt . ylabel ('func1(t)')
plt . title ('Three user defined functions')
plt . ylim ([0, 7])
plt . grid ()
plt . subplot (3 , 1 , 2)
plt . plot (t , func2(t) )
plt . ylabel ('func2(t)')
plt . ylim ([0, 1.2])
plt . grid ()
plt . subplot (3 , 1 , 3)
plt . plot (t , func3(t) )
plt . ylabel ('func3(t)')
plt . ylim ([-2, 3])
plt . grid ()
plt.show()

conv = convolution(func1(t),step(t))*steps
convCheck = sig.convolve(func1(t), step(t))*steps

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (tExtend , conv, label="User" )
plt . plot (tExtend , convCheck, label="Built-in" )
plt . ylim ([0, 5])
plt . grid ()
plt . legend()
#plt . xlabel('t[s]')
plt . ylabel ('func1*step')
plt . subplot (2 , 1 , 2)
plt . plot (tExtend , calcFunc1(t), label="Hand-calculated" )
plt . ylim ([0, 5])
plt . grid ()
plt . legend()
plt . xlabel('t[s]')
plt . ylabel ('func1*step')
plt . title ('Convolution: func1 ')
plt.show()

conv = convolution(func2(t),step(t))*steps
convCheck = sig.convolve(func2(t), step(t))*steps

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (tExtend , conv, label="User" )
plt . plot (tExtend , convCheck, label="Built-in" )
plt . legend()
plt . ylim ([0, 5])
plt . grid ()
#plt . xlabel('t[s]')
plt . ylabel ('func2*step')
plt . subplot (2 , 1 , 2)
plt . plot (tExtend , calcFunc2(t), label="Hand-calculated" )
plt . ylim ([0, 5])
plt . grid ()
plt . legend()
plt . xlabel('t[s]')
plt . ylabel ('func2*step')
plt . title ('Convolution: func2 ')
plt.show()

conv = convolution(func3(t),step(t))*steps
convCheck = sig.convolve(func3(t), step(t))*steps

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (tExtend , conv, label="User" )
plt . plot (tExtend , convCheck, label="Built-in" )
plt . ylim ([-1, 1])
plt . grid ()
plt . legend()
#plt . xlabel('t[s]')
plt . ylabel ('func3*step')
plt . subplot (2 , 1 , 2)
plt . plot (tExtend , calcFunc3(t), label="Hand-calculated" )
plt . ylim ([-1, 1])
plt . grid ()
plt . legend()
plt . xlabel('t[s]')
plt . ylabel ('func3*step')
plt . title ('Convolution: func3 ')
plt.show()




