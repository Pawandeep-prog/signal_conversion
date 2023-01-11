import matplotlib.pyplot as plt
from genCarrier import GenCarrier

class Digital2Analog:
    def __init__(self, data) -> None:
        self.data = data 
        self.genCarr = GenCarrier()
    
    def ASK(self, baud_rate):

        carrier_time = len(self.data)/baud_rate
        _x, _y = self.genCarr.genCarr(freq=4, t_sec=carrier_time)
        
        _init = 0

        to_chg = int(len(_y)/(carrier_time*baud_rate))

        for i in self.data:
            if(i=='0'):
                for i in range(to_chg):
                    try:
                        _y[_init] = 0
                        _init += 1
                    except:
                        break
            else:
                _init += to_chg

        plt.plot(_x, _y)
        plt.grid(which='both')
        plt.show()

    def FSK(self, baud_rate, fc, delta_f):
        _x = []
        _y = []

        _time = 1/baud_rate
        _st = 0
        for i in self.data:
            if( i == '1'):
                tmp_x, tmp_y = self.genCarr.genCarr(freq=(fc+delta_f), t_sec=_time, st=_st)
            else:
                tmp_x, tmp_y = self.genCarr.genCarr(freq=(fc-delta_f), t_sec=_time, st=_st)

            _x.extend(tmp_x)
            _y.extend(tmp_y)
            _st += _time

        plt.plot(_x, _y)
        plt.grid(which='both')
        plt.show()

    def PSK(self, baud_rate):
        _x = []
        _y = []

        _time = 1/baud_rate
        _st = 0

        fc = 2
        for i in self.data:
            if( i == '1'):
                tmp_x, tmp_y = self.genCarr.genCarr(freq=(fc), t_sec=_time, st=_st, phi=0)
            else:
                tmp_x, tmp_y = self.genCarr.genCarr(freq=(fc), t_sec=_time, st=_st, phi=180)

            _x.extend(tmp_x)
            _y.extend(tmp_y)
            _st += _time

        plt.plot(_x, _y)
        plt.grid(which='both')
        plt.show()