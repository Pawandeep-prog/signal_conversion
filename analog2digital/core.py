from utils import Utils
import numpy as np
class AnalogToDigital:
    def __init__(self, x, y, data_freq) -> None:
        self.x=x
        self.y=y
        self.data_freq = data_freq

    def sample(self, sample_freq, levels):
        sample_rate = 1/sample_freq
        sampled_time = np.arange(0, 2, sample_rate)
        samples = np.sin(2*np.pi*self.data_freq*sampled_time)

        max_amp = max(samples)
        min_amp = min(samples)

        delta = (max_amp - min_amp) / levels

        data = ""
        for i in samples:
            _ctr = 0
            _amp = min_amp
            while not((i>=_amp) and (i<=(_amp+delta))):
                _amp += delta 
                _ctr += 1
            
            data += bin(_ctr)[2:]+" "

        print("YOUR ANALOG SIGNAL DATA IS : ")
        print(data)
        Utils.plot_scatter(self.x, self.y, sampled_time, samples)

