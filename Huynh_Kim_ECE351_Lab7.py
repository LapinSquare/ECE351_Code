# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 7                                                      #
# 10/13/20                                                        #
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

def step ( t ) : # The only variable sent to the function is t
    y = np . zeros ( t . shape ) # initialze y(t) as an array of zeros

    for i in range (len ( t ) ) : # run the loop once for each index of t
        if t[ i ] < 0:
            y [ i ] = 0
        else :
            y [ i ] = 1
    return y # send back the output stored in an array

def eqG(s): 
    return (s+9)/((s+4)*(s-8)*(s+2))
def eqA(s): 
    return (s+4)/((s+3)*(s+1))
def eqB(s): 
    return (s+14)*(s+12) 
#def totalEq(s): 
#    return ((s+9)*(s+3)*(s+1))/((s+4)*((s+4)*(s-8)*(s+2)+(s+9)*(s+14)*(s+12)))

G_den=sig.convolve([1,-6,-16], [1, 4])
G_num=[1,9]
A_num=[1,4]
#A_den=sig.convolve([1,3], [1, 4])
A_den=[1,4,3]
B_num=[1, 26, 168]
B_den=[1]
test=convolution([1,-6,-16], [1, 4])
#print('User-defined convolution'+str(test))
#print('Python convolve'+str(G_den))
#print('')


#num=[1, 9]
#den=[1, -2, -40, -64]
z, p, _=sig.tf2zpk(G_num, G_den) #G
print('Eq G:')
print('zeroes='+str(z))
print('poles='+str(p))
print('')

#num=[1, 4]
#den=[1, 4, 3]
z, p, _=sig.tf2zpk(A_num, A_den) #A
print('Eq A:')
print('zeroes='+str(z))
print('poles='+str(p))
print('')

#num=[1, 26, 168] 
#den=[1]
b=np.roots(B_num) #B
print('Eq B:')
print('roots(zeroes)='+str(b))
print('')

num = sig . convolve (G_num , A_num)
den = sig . convolve ([1,4,3] , G_den )
t = np . arange (0 , 2 + steps , steps ) 
tout, yout =sig.step((num, den))
plt . figure ( figsize = (10 , 20) )
plt . plot (tout, yout)
plt . grid ()
plt . title ('Step response (Open loop), part 1')
plt . ylabel ('y(t)')
plt . xlabel('t')



numTot= sig.convolve(A_num, G_num)
denTot= sig.convolve(G_den+sig.convolve(B_num, G_num), A_den)
zTot, pTot,_=sig.tf2zpk(numTot, denTot)
print('Closed loop:')
print('numerator='+str(numTot))
print('denominator='+str(denTot))
print('zeroes='+str(zTot))
print('poles='+str(pTot))
print('')

tout, yout =sig.step((numTot, denTot))
plt . figure ( figsize = (10 , 20) )
plt . plot (tout, yout)
plt . grid ()
plt . title ('Total Step response (closed loop), part 2')
plt . ylabel ('y(t)')
plt . xlabel('t')


