# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 2                                                        #
# 9/8/20                                                        #
#                                                               #
#                                                               #
# ############################################################### 

import numpy as np
import matplotlib . pyplot as plt

#plt.rcParams.update({ 'font.size' : 14}) # Set font size in plots

steps = 1e-2 # Define step size
t = np . arange (0 , 10 + steps , steps ) # Add a step size to make sure the
# plot includes 5.0. Since np. arange () only
# goes up to , but doesn ’t include the
# value of the second argument
print ('Number of elements : len(t) = ', len( t ) , '\ nFirst Element : t[0] = ', t [0] , '\ nLast Element : t[len(t) - 1] = ', t [len( t ) - 1])
# Notice the array might be a different size than expected since Python starts
# at 0. Then we will use our knowledge of indexing to have Python print the
# first and last index of the array . Notice the array goes from 0 to len () - 1

# --- User - Defined Function ---

# Create output y(t) using a for loop and if/ else statements
#def example1 ( t ) : # The only variable sent to the function is t
#    y = np . zeros ( t . shape ) # initialze y(t) as an array of zeros

#    for i in range (len ( t ) ) : # run the loop once for each index of t
#        if i < ( len( t ) + 1) /3:
#            y [ i ] = t [ i ]**2
#        else :
#            y [ i ] = np . sin (5* t [ i ]) + 2
#    return y # send back the output stored in an array

#y = example1 ( t ) # call the function we just created

def func1 ( t ) : # The only variable sent to the function is t
    y = np . zeros ( t . shape ) # initialze y(t) as an array of zeros

    for i in range (len ( t ) ) : # run the loop once for each index of t
        #if i < ( len( t ) + 1) /3:
           # y [ i ] = t [ i ]**2
        #else :
            y [ i ] = np . cos (t [ i ]) 
    return y # send back the output stored in an array 

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

def rampStepFunc ( t ) : # The only variable sent to the function is t
    #for i in range (len ( t ) ) : # run the loop once for each index of t
    return ramp(t) - ramp(t-3) + 5*step(t-3) - 2*step(t-6) - 2*ramp(t-6)

y = func1 ( t ) # call the function we just created

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (t , y )
plt . grid ()
plt . ylabel ('y(t) with Good Resolution ')
plt . title ('Cosine ')
plt.show()

#t = np . arange (0 , 5 + 0.25 , 0.25) # redefine t with poor resolution
y = ramp ( t )

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (t , y )
plt . xlim ([-5, 5])
plt . grid ()
plt . ylabel ('y(t)')
plt . title ('Ramp function')
plt.show()

y = step ( t )

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (t , y )
plt . xlim ([-5, 5])
plt . grid ()
plt . ylabel ('y(t)')
plt . title ('Step function')
plt.show()

t = np . arange (-5 , 10 + steps , steps )

y = rampStepFunc ( t )

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (t , y )
plt . grid ()
plt . ylabel ('y(t) ')
plt . title ('Combined function w/ step and ramp')
plt.show()

y = rampStepFunc ( -t )

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (t , y )
plt . grid ()
plt . ylabel ('y(t)')
plt . title ('Time reverse function w/ step and ramp (-t)')
plt.show()

y = rampStepFunc ( t-4 )

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (t , y )
plt . grid ()
plt . ylabel ('y(t)')
plt . title ('Time shift function w/ step and ramp (t-4)')
plt.show()

y = rampStepFunc ( -t-4 )

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (t , y )
plt . grid ()
plt . ylabel ('y(t) ')
plt . title ('Time shift function w/ step and ramp (-t-4)')
plt.show()

y = rampStepFunc ( t/2 )

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (t , y )
plt . grid ()
plt . ylabel ('y(t)')
plt . title ('Time scale function w/ step and ramp (t/2)')
plt.show()

y = rampStepFunc ( 2*t )

plt . figure ( figsize = (10 , 7) )
plt . subplot (2 , 1 , 1)
plt . plot (t , y )
plt . grid ()
plt . ylabel ('y(t) ')
plt . title ('Time scale function w/ step and ramp (2t)')
plt.show()

steps=1e-3   #1e-3
t = np.arange(-5, 10+steps, steps)
y = rampStepFunc(t)
dt = np.diff(t)
dy = np.diff(y, axis=0)/dt

plt . figure ( figsize = (10 , 7) )
plt . plot (t , y, '--', label='y(t)' )
plt . plot (t[range(len(dy))], dy, label='dy(t)/dt' )
plt . xlabel ('t ')
plt . ylabel ('y(t), dy(t)/dt')
plt . title ('Differential function w/ step and ramp')
plt.legend() 
plt . grid ()
plt.ylim([-2,10])
plt.show()

