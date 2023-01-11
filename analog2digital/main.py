from dataGen import GenSin
from core import AnalogToDigital

generator = GenSin()

x, y = generator.generate(freq=2, amp=1, t_sec=2)

a2d = AnalogToDigital(x, y, data_freq=2)

a2d.sample(sample_freq=5, levels=4)

