from core import Digital2Analog


d2a = Digital2Analog("10110101")

d2a.ASK(baud_rate=2)
d2a.FSK(baud_rate=2, fc=10, delta_f=3)
d2a.PSK(baud_rate=2)
