# -*- coding: utf-8 -*-
# ###############################################################
#                                                               #
# Kim Huynh                                                     #
# ECE351-51                                                     #
# Lab 12                                                        #
# 11/17/20                                                      #
#                                                               #
#                                                               #
# ############################################################### 

#Circuit: Parallel Bandpass 

import numpy as np
import math
import matplotlib . pyplot as plt
import scipy 
import scipy.fftpack
from scipy import signal as sig 
import pandas as pd
import control as con

freqq=1e6 #1MHz
R = 300 #160
C = 2.59e-7 #5e-6
L = 27e-3   #1405e-6
#steps = 1e3 # Define step size
steps=1
#w = np . arange (2*np.pi*1800 , 2*np.pi*2000 + steps , steps ) 
w = np . arange (10**0 , 10**5 + steps , steps ) 
#steps = 1e-5 # Define step size
#freqq = np . arange (1.8e3 , 2e3 + steps , steps ) 

#From lab 10.
def h_mag(w, R, C, L):
    return (w/(R*C))/ np.sqrt( (-w**2+1/(L*C))**2 + (w/(R*C))**2 )

def h_phi(w, R, C, L):
    return (np.pi/2)-np.arctan((w/(R*C))/(-w**2+1/(L*C)))

h_num= [1/(R*C), 0]
h_den= [1, 1/(R*C), 1/(L*C)]

#From handout.
def make_stem ( ax ,x ,y , color ='k', style ='solid', label ='', linewidths =2.5 ,** kwargs ) :
    ax . axhline ( x [0] , x [ -1] ,0 , color ='r')
    ax . vlines (x , 0 ,y , color = color , linestyles = style , label = label , linewidths =
                 linewidths )
    ax . set_ylim ([1.05* y . min () , 1.05* y . max () ])

#From lab 9.
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



# load input signal
df = pd . read_csv ('NoisySignal.csv')

t = df ['0']. values
sensor_sig = df ['1']. values

#%%1 noise
plt . figure ( figsize = (10 , 7) )
plt . plot (t , sensor_sig )
plt . grid ()
plt . title ('Noisy Input Signal ')
plt . xlabel ('Time [s]')
plt . ylabel ('Amplitude [V]')
plt . show ()

#%%2 entire band
Mag, Phi, Freq = my_fft_clean(sensor_sig, freqq)
fig , ax = plt . subplots ( figsize =(10 , 7) )
make_stem ( ax , Freq , Mag )
plt.xscale('log')
plt . title ('Unfiltered Noise FFT -Entire Band')
plt.grid(which = 'both')
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('X [V]')
plt.xlim([1e0, 100e3])
plt.ylim([0, 1.5])
plt . show ()

#%%3 passband
fig , ax = plt . subplots ( figsize =(10 , 7) )
make_stem ( ax , Freq , Mag )
#plt.xscale('log')
plt . title ('Unfiltered Noise FFT -Pass Band')
plt.grid(which = 'both')
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('X [V]')
plt.xlim([1790, 2010])
plt.ylim([0, 1.5])
plt . show ()

#%%4 lowband
fig , ax = plt . subplots ( figsize =(10 , 7) )
make_stem ( ax , Freq , Mag )
#plt.xscale('log')
plt . title ('Unfiltered Noise FFT -Low Band')
plt.grid(which = 'both')
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('X [V]')
plt.xlim([0, 1810])
plt.ylim([0, 1.5])
plt . show ()

#%%5 highband
fig , ax = plt . subplots ( figsize =(10 , 7) )
make_stem ( ax , Freq , Mag )
#plt.xscale('log')
plt . title ('Unfiltered Noise FFT -High Band')
plt.grid(which = 'both')
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('X [V]')
plt.xlim([1990, 10000])
plt.ylim([0, 1.5])
plt . show ()

#%%6 overall bode

plt . figure ( figsize = (10 , 20) )
sys = con . TransferFunction ( h_num , h_den )
_ = con . bode ( sys , 2*np.pi*w , dB = True , Hz = True , deg = True , Plot = True )
plt . title ('Filter Bode Plots')

#%%7 passband bode

plt . figure ( figsize = (10 , 20) )
sys = con . TransferFunction ( h_num , h_den )
_ = con . bode ( sys , 2*np.pi*np.arange(1.78e3, 2.02e3) , dB = True , Hz = True , deg = True , Plot = True )
plt . title ('Filter Bode Plots -Pass Band')

#%%8 lowband bode

plt . figure ( figsize = (10 , 20) )
sys = con . TransferFunction ( h_num , h_den )
_ = con . bode ( sys , 2*np.pi*np.arange(0, 1.78e3) , dB = True , Hz = True , deg = True , Plot = True )
plt . title ('Filter Bode Plots -Low Band')

#%%9 highband bode
plt . figure ( figsize = (10 , 20) )
sys = con . TransferFunction ( h_num , h_den )
_ = con . bode ( sys , 2*np.pi*np.arange(2e3, 10e5) , dB = True , Hz = True , deg = True , Plot = True )
plt . title ('Filter Bode Plots -High Band')

#%%10 filtered signal
b_num, b_den=sig . bilinear(h_num, h_den, freqq)
b_arr=sig . lfilter(b_num, b_den, sensor_sig)

plt . figure ( figsize = (10 , 20) )
plt . subplot (2 , 1 , 2)
plt . plot(t, b_arr)
plt . grid ()
plt . title ('Filtered Signal ')
plt . ylabel ('Amplitude [V]')
plt . xlabel('Time [s]')

#%%11 filtered entire band
Mag_Filt, Phi_Filt, Freq_Filt = my_fft_clean(b_arr, freqq)
fig, ax=plt . subplots(figsize = (10 , 7))
make_stem ( ax , Freq , Mag, label='Unfiltered' )
make_stem ( ax , Freq_Filt , Mag_Filt, color='b', style='dashed', label='Filtered' )
plt.xscale('log')
plt . title ('Filtered Signal FFT -Entire Band')
plt.grid(which = 'both')
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('X [V]')
plt.xlim([1e0, 100e3])
plt.ylim([0, 1.5])
plt . legend()
plt . show ()

#%%12 filtered passband
fig, ax=plt . subplots(figsize = (10 , 7))
make_stem ( ax , Freq , Mag, label='Unfiltered' )
make_stem ( ax , Freq_Filt , Mag_Filt, color='b', style='dashed', label='Filtered' )
plt . title ('Filtered Signal FFT -Pass Band')
plt.grid(which = 'both')
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('X [V]')
plt.xlim([1790, 2010])
plt.ylim([0, 1.5])
plt . legend()
plt . show ()

#%%13 filtered lowband
fig, ax=plt . subplots(figsize = (10 , 7))
make_stem ( ax , Freq , Mag, label='Unfiltered' )
make_stem ( ax , Freq_Filt , Mag_Filt, color='b', style='dashed', label='Filtered' )
plt . title ('Filtered Signal FFT -Low Band')
plt.grid(which = 'both')
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('X [V]')
plt.xlim([0, 1810])
plt.ylim([0, 1.5])
plt . legend()
plt . show ()

#%%14 filtered highband
fig, ax=plt . subplots(figsize = (10 , 7))
make_stem ( ax , Freq , Mag, label='Unfiltered' )
make_stem ( ax , Freq_Filt , Mag_Filt, color='b', style='dashed', label='Filtered' )
plt . title ('Filtered Signal FFT -High Band')
plt.grid(which = 'both')
plt . xlabel ('Frequency [Hz]')
plt . ylabel ('X [V]')
plt.xlim([1990, 10000])
plt.ylim([0, 1.5])
plt . legend()
plt . show ()