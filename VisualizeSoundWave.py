# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 11:12:14 2021
Visualize Sound Wave
@author: mirac
"""


import wave
import numpy as np
import matplotlib.pyplot as plt

signal_wave = wave.open(r"C:\Users\mirac\CLT2.wav", 'r')
sample_rate = 999999
sig = np.frombuffer(signal_wave.readframes(sample_rate), dtype=np.int16)

sig = sig[:]

plt.figure(1)

plot_a = plt.subplot(211)
plot_a.plot(sig)
plot_a.set_ylabel('energy')

plot_b = plt.subplot(212)
plot_b.specgram(sig, NFFT=1024, Fs=sample_rate, noverlap=1)
plot_b.set_ylabel('Frequency')
plt.savefig('filename2.png', dpi=1200)
plt.show()
