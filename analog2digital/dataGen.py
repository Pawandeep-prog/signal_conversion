import numpy as np
import matplotlib.pyplot as plt

class GenSin:
    def __init__(self):
        pass
    
    def generate(self, freq, amp, t_sec):
        x = np.linspace(0, t_sec, 10000)
        y = amp*np.sin(2*np.pi*freq*x)
        return (x, y)

    