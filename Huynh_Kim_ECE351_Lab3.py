# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 3                                                        #
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
t = np . arange (0 , 20 + steps , steps ) 
NN=len(t)
tExtend = np.arange(0, 2*t[NN-1], steps)


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
    return step(t-2)-step(t-9)

def func2( t ): 
    return np.exp(-t)*step(t) 

def func3( t ): 
    return ramp(t - 2)*(step(t - 2) - step(t - 3)) + ramp(4 - t)*(step(t - 3) - step(t - 4))

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
plt . ylim ([0, 1.2])
plt . grid ()
plt . subplot (3 , 1 , 2)
plt . plot (t , func2(t) )
plt . ylabel ('func2(t)')
plt . ylim ([0, 1.2])
plt . grid ()
plt . subplot (3 , 1 , 3)
plt . plot (t , func3(t) )
plt . ylabel ('func3(t)')
plt . ylim ([0, 1.2])
plt . grid ()
plt.show()

conv = convolution(func1(t),func2(t))*steps
convCheck = sig.convolve(func1(t), func2(t))*steps

plt . figure ( figsize = (10 , 7) )
plt . plot (tExtend , conv, label="User" )
plt . plot (tExtend , convCheck, label="Built-in" )
plt . ylim ([0, 1.2])
plt . grid ()
plt . legend()
plt . xlabel('t[s]')
plt . ylabel ('func1*func2')
plt . title ('Convolution: func1 and func2')
plt.show()

conv = convolution(func2(t),func3(t))*steps
convCheck = sig.convolve(func2(t), func3(t))*steps

plt . figure ( figsize = (10 , 7) )
plt . plot (tExtend , conv, label="User" )
plt . plot (tExtend , convCheck, label="Built-in" )
plt . ylim ([0, 1.2])
plt . grid ()
plt . legend()
plt . xlabel('t[s]')
plt . ylabel ('func2*func3')
plt . title ('Convolution: func2 and func3')
plt.show()

conv = convolution(func1(t),func3(t))*steps
convCheck = sig.convolve(func1(t), func3(t))*steps

plt . figure ( figsize = (10 , 7) )
plt . plot (tExtend , conv, label="User" )
plt . plot (tExtend , convCheck, label="Built-in" )
plt . ylim ([0, 1.2])
plt . grid ()
plt . legend()
plt . xlabel('t[s]')
plt . ylabel ('func1*func3')
plt . title ('Convolution: func1 and func3')
plt.show()


