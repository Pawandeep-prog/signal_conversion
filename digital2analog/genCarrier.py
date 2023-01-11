import numpy as np

class GenCarrier:
    def __init__(self) -> None:
        pass

    def genCarr(self, freq, t_sec, st=0, phi=0):
        x = np.arange(st, st+t_sec, 0.001)
        y = np.sin(x*freq*2*np.pi + phi)
        return x ,y 