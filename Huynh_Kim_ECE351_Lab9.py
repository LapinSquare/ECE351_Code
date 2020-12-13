# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 9                                                         #
# 10/26/20                                                      #
#                                                               #
#                                                               #
# ############################################################### 

import numpy as np
import math
import matplotlib . pyplot as plt
import scipy 
import scipy.fftpack
#from scipy.fftpack import fft, fftshift
from scipy import signal as sig 

freqq =100
steps = 1/freqq # Define step size
t = np . arange (0 , 2, steps ) #remove steps or rubbish :()
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


def my_fft(x, fs): #fs=freq
    N = len( x ) # find the length of the signal
    X_fft = scipy . fftpack . fft ( x ) # perform the fast Fourier transform (fft)
    X_fft_shifted = scipy . fftpack . fftshift ( X_fft ) # shift zero frequency components
    # to the center of the spectrum
    freq = np . arange ( - N /2 , N /2) * fs / N # compute the frequencies for the output
    # signal , (fs is the sampling frequency and
    # needs to be defined previously in your code
    X_mag = np .abs( X_fft_shifted ) / N # compute the magnitudes of the signal
    X_phi = np . angle ( X_fft_shifted ) # compute the phases of the signal
    # ----- End of user defined function ----- #
    #xmag, angle freq
    return X_mag, X_phi, freq

def my_fft_clean(x, fs): #fs=freq
    N = len( x ) # find the length of the signal
    X_fft = scipy . fftpack . fft ( x ) # perform the fast Fourier transform (fft)
    X_fft_shifted = scipy . fftpack . fftshift ( X_fft ) # shift zero frequency components
    # to the center of the spectrum
    freq = np . arange ( - N /2 , N /2) * fs / N # compute the frequencies for the output
    # signal , (fs is the sampling frequency and
    # needs to be defined previously in your code
    X_mag = np .abs( X_fft_shifted ) / N # compute the magnitudes of the signal
    X_phi = np . angle ( X_fft_shifted ) # compute the phases of the signal
    
    for k in range(len(X_mag)) :
        if (np.abs(X_mag[k])<1e-10):
            X_phi[k]=0
        
    # ----- End of user defined function ----- #
    #xmag, angle freq
    return X_mag, X_phi, freq

#%% TASK1
plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 1)
plt . plot (t,np.cos(2*np.pi*t))
plt . grid ()
plt . title ('TASK 1 : Normal Cosine')
plt . ylabel ('x(t)')
plt . xlabel('t(s)')

X_Mag, X_Phi, Freq=my_fft(np.cos(2*np.pi*t), freqq)   
plt . subplot (3 , 2 , 3)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 1 cos(2$\pi$t) Mag ')

plt . subplot (3 , 2 , 5)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 1 cos(2$\pi$t) Phi (Messy)')
plt . xlabel('f(Hz)')

#X_Mag, X_Phi, Freq=my_fft_clean(np.cos(2*np.pi*t), freqq)   
plt . subplot (3 , 2 , 4)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 1 cos(2$\pi$t) Mag ')
plt . xlim(-2, 2)

plt . subplot (3 , 2 , 6)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 1 cos(2$\pi$t) Phi')
plt . xlim(-2, 2)
plt . xlabel('f(Hz)')


#%% TASK2

plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 1)
plt . plot (t,5*np.sin(2*np.pi*t))
plt . grid ()
plt . title ('TASK 2 : Normal Sine')
plt . ylabel ('x(t)')
plt . xlabel('t(s)')

X_Mag, X_Phi, Freq=my_fft(5*np.sin(2*np.pi*t), freqq)   
plt . subplot (3 , 2 , 3)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 2 5sin(2$\pi$t) Mag')

plt . subplot (3 , 2 , 5)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 2 5sin(2$\pi$t) Phi (Messy)')
plt . xlabel('f(Hz)')

#X_Mag, X_Phi, Freq=my_fft_clean(5*np.sin(2*np.pi*t), freqq)   
plt . subplot (3 , 2 , 4)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 2 5sin(2$\pi$t) Mag')
plt . xlim(-2, 2)

plt . subplot (3 , 2 , 6)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 2 5sin(2$\pi$t) Phi')
plt . xlim(-2, 2)
plt . xlabel('f(Hz)')


#%% TASK3

plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 1)
plt . plot (t,(2*np.cos((2*np.pi*2*t)-2)+np.square(np.cos((2*np.pi*6*t)+3))))
plt . grid ()
plt . title ('TASK 3 : Cosine and Sine, 2cos((2$\pi$2t)-2)+np.square(cos((2$\pi$6*t)+3))')
plt . ylabel ('x(t)')
plt . xlabel('t(s)')

X_Mag, X_Phi, Freq=my_fft((2*np.cos((2*np.pi*2*t)-2)+np.square(np.cos((2*np.pi*6*t)+3))), freqq)   
plt . subplot (3 , 2 , 3)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 3 cos/sin Mag')

plt . subplot (3 , 2 , 5)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 3 cos/sin Phi (Messy)')
plt . xlabel('f(Hz)')

#X_Mag, X_Phi, Freq=my_fft_clean((2*np.cos((2*np.pi*2*t)-2)+np.square(np.cos((2*np.pi*6*t)+3))), freqq)   
plt . subplot (3 , 2 , 4)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 3 cos/sin Mag')
plt . xlim(-2, 2)

plt . subplot (3 , 2 , 6)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 3 cos/sin Phi')
plt . xlim(-2, 2)
plt . xlabel('f(Hz)')

#%% TASK4
plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 1)
plt . plot (t,np.cos(2*np.pi*t))
plt . grid ()
plt . title ('TASK 4 : Normal Cosine')
plt . ylabel ('x(t)')
plt . xlabel('t(s)')

X_Mag, X_Phi, Freq=my_fft_clean(np.cos(2*np.pi*t), freqq)   
plt . subplot (3 , 2 , 3)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 4 cos(2$\pi$t) Mag ')

plt . subplot (3 , 2 , 5)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 4 cos(2$\pi$t) Phi (Clean)')
plt . xlabel('f(Hz)')

#X_Mag, X_Phi, Freq=my_fft_clean(np.cos(2*np.pi*t), freqq)   
plt . subplot (3 , 2 , 4)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 4 cos(2$\pi$t) Mag ')
plt . xlim(-2, 2)

plt . subplot (3 , 2 , 6)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 4 cos(2$\pi$t) Phi')
plt . xlim(-2, 2)
plt . xlabel('f(Hz)')




plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 1)
plt . plot (t,5*np.sin(2*np.pi*t))
plt . grid ()
plt . title ('TASK 4 : Normal Sine')
plt . ylabel ('x(t)')
plt . xlabel('t(s)')

X_Mag, X_Phi, Freq=my_fft_clean(5*np.sin(2*np.pi*t), freqq)   
plt . subplot (3 , 2 , 3)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 4 5sin(2$\pi$t) Mag ')

plt . subplot (3 , 2 , 5)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 4 5sin(2$\pi$t) Phi (Clean)')
plt . xlabel('f(Hz)')

#X_Mag, X_Phi, Freq=my_fft_clean(5*np.sin(2*np.pi*t), freqq)   
plt . subplot (3 , 2 , 4)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 4 5sin(2$\pi$t) Mag')
plt . xlim(-2, 2)

plt . subplot (3 , 2 , 6)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 4 5sin(2$\pi$t) Phi')
plt . xlim(-2, 2)
plt . xlabel('f(Hz)')




plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 1)
plt . plot (t,(2*np.cos((2*np.pi*2*t)-2)+np.square(np.cos((2*np.pi*6*t)+3))))
plt . grid ()
plt . title ('TASK 4 : Cosine and Sine: 2cos((2$\pi$2t)-2)+np.square(cos((2$\pi$6*t)+3))')
plt . ylabel ('x(t)')
plt . xlabel('t(s)')

X_Mag, X_Phi, Freq=my_fft_clean((2*np.cos((2*np.pi*2*t)-2)+np.square(np.cos((2*np.pi*6*t)+3))), freqq)   
plt . subplot (3 , 2 , 3)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 4 cos/sin Mag ')

plt . subplot (3 , 2 , 5)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 4 cos/sin Phi (Clean)')
plt . xlabel('f(Hz)')

#X_Mag, X_Phi, Freq=my_fft_clean((2*np.cos((2*np.pi*2*t)-2)+np.square(np.cos((2*np.pi*6*t)+3))), freqq)   
plt . subplot (3 , 2 , 4)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 4 cos/sin Mag')
plt . xlim(-2, 2)

plt . subplot (3 , 2 , 6)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 4 cos/sin Phi')
plt . xlim(-2, 2)
plt . xlabel('f(Hz)')


#%%TASK5

t = np . arange (0 , 16 , steps ) 

plt . figure ( figsize = (10 , 20) )
plt . subplot (3 , 1 , 1)
plt . plot (t,fourier(15, T, t))
plt . grid ()
plt . title ('TASK 5 : N=15 Fourier')
plt . ylabel ('x(t)')
plt . xlabel('t(s)')
#plt . xlim(-15, 15)

X_Mag, X_Phi, Freq=my_fft_clean(fourier(15, T, t), freqq)   
plt . subplot (3 , 2 , 3)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 5 Mag')
plt . xlim(-15, 15)

plt . subplot (3 , 2 , 5)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 5 Phi')
plt . xlim(-15, 15)
plt . xlabel('f(Hz)')

#X_Mag, X_Phi, Freq=my_fft_clean((2*np.cos((2*np.pi*2*t)-2)+np.square(np.cos((2*np.pi*6*t)+3))), freqq)   
plt . subplot (3 , 2 , 4)
plt . stem ( Freq , X_Mag ) # you will need to use stem to get these plots to be
plt . title ('TASK 5 Mag')
plt . xlim(-2, 2)

plt . subplot (3 , 2 , 6)
plt . stem ( Freq , X_Phi ) # correct , remember to label all plots appropriately
plt . title ('TASK 5 Phi')
plt . xlim(-2, 2)
plt . xlabel('f(Hz)')