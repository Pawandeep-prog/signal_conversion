import numpy as np 
class GenSin:
    def __init__(self) -> None:
        pass

    def genSin(self, fq, t_sec):
        x = np.arange(0, t_sec, 0.001)
        y = np.sin(x*2*np.pi*fq)

        return x, y
