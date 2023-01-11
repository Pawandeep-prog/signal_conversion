import matplotlib.pyplot as plt 
from genSin import GenSin
import numpy as np

class Analog2Analog:
    def __init__(self, signal_freq, signal_time) -> None:
        self.genSin = GenSin()
        self.signal_x, self.signal_y = self.genSin.genSin(fq = signal_freq, t_sec=signal_time)
        self.carrier_x, self.carrier_y = self.genSin.genSin(fq = 15, t_sec=signal_time)

    def AM(self):

        plt.subplot(1, 3, 1)
        plt.plot(self.carrier_x, self.carrier_y)

        for i in range(len(self.signal_x)):
            self.carrier_y[i] *= self.signal_y[i]
        
        plt.title("amplitude modulation")
        plt.subplot(1, 3, 2)
        plt.plot(self.signal_x, self.signal_y)
        plt.subplot(1, 3, 3)
        plt.plot(self.carrier_x, self.carrier_y)
        plt.show()

    def FM(self):
        t = self.signal_x

        sig = self.signal_y

        fc = 10 
        k = 0.05
        phi = 2*np.pi*fc*t + k*np.cumsum(sig)
        sig_mod = np.sin(phi) 

        plt.title("frequency modulation")
        plt.plot(t, sig_mod)
        plt.plot(t, sig, c='r')

        plt.show()

    def PM(self):
        t = self.signal_x

        sig = self.signal_y

        fc = 10 
        k = 5
        phi = 2*np.pi*fc*t + k*sig
        sig_mod = np.sin(phi) 

        plt.title("phase modulation")
        plt.plot(t, sig_mod)
        plt.plot(t, sig, c='r')

        plt.show()
