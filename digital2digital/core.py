import numpy as np
import matplotlib.pyplot as plt
from constants import *
from utils import invert

class DigitalToDigital:
    def __init__(self, data):
        self.data = data

    def unipolarNRZ(self):
        _gen = []
        x = []
        init_ = 0
        for i in self.data:
            x.append(init_)
            init_ += WIDTH
            x.append(init_)
            if(i == '0'):
                _gen.append(0)
                _gen.append(0)
            else:
                _gen.append(1)
                _gen.append(1)
        
        print("plotting .....")
        print("please wait ....")

        plt.plot(x, _gen)
        plt.show()

    def polarNRZL(self):
        _gen = []
        x = []
        init_ = 0
        for i in self.data:
            x.append(init_)
            init_ += WIDTH
            x.append(init_)
            if(i == '0'):
                _gen.append(-1)
                _gen.append(-1)
            else:
                _gen.append(1)
                _gen.append(1)
        
        print("plotting .....")
        print("please wait ....")

        plt.plot(x, _gen)
        plt.show()

    def polarNRZI(self):
        _gen = []
        x = []
        init_ = 0
        _curr = 1
        for i in self.data:
            x.append(init_)
            init_ += WIDTH
            x.append(init_)
            if(i == '0'):
                _gen.append(_curr)
                _gen.append(_curr)
            else:
                _curr = invert(_curr)
                _gen.append(_curr)
                _gen.append(_curr)
        
        print("plotting .....")
        print("please wait ....")

        plt.plot(x, _gen)
        plt.show()

    def polarRZ(self):
        _gen = []
        x = []
        init_ = 0
        for i in self.data:
            x.append(init_)
            init_ += WIDTH//2
            x.append(init_)
            x.append(init_)
            init_ += WIDTH//2
            x.append(init_)
            if(i == '0'):
                _gen.append(-1)
                _gen.append(-1)
            else:
                _gen.append(1)
                _gen.append(1)
            _gen.append(0)
            _gen.append(0)
        
        print("plotting .....")
        print("please wait ....")

        plt.plot(x, _gen)
        plt.show()

    def bipolarAMI(self):
        _gen = []
        x = []
        init_ = 0
        _curr = 1
        for i in self.data:
            x.append(init_)
            init_ += WIDTH
            x.append(init_)
            if(i == '0'):
                _gen.append(0)
                _gen.append(0)
            else:
                _gen.append(_curr)
                _gen.append(_curr)
                _curr = invert(_curr)
        
        print("plotting .....")
        print("please wait ....")

        plt.plot(x, _gen)
        plt.show()

    def biphaseManchester(self):
        _gen = []
        x_axis = []
        _init = 0
        for i in self.data:
            x_axis.append(_init)
            _init += (WIDTH//2)
            x_axis.append(_init)
            x_axis.append(_init)
            _init += (WIDTH//2)
            x_axis.append(_init)

            if i == '0':
                _gen.append(-1)
                _gen.append(-1)
                _gen.append(1)
                _gen.append(1)
            else:
                _gen.append(1)
                _gen.append(1)
                _gen.append(-1)
                _gen.append(-1)

        plt.plot(x_axis, _gen)
        plt.show()

    def biphaseDifferentialManchester(self):
        _gen = []
        x_axis = []
        _init = 0
        _curr = 1
        for i in self.data:
            x_axis.append(_init)
            _init += (WIDTH//2)
            x_axis.append(_init)
            x_axis.append(_init)
            _init += (WIDTH//2)
            x_axis.append(_init)

            if i == '0':
                _curr = invert(_curr)
                _gen.append(_curr)
                _gen.append(_curr)
                _curr = invert(_curr)
                _gen.append(_curr)
                _gen.append(_curr)
            else:
                _gen.append(_curr)
                _gen.append(_curr)
                _curr = invert(_curr)
                _gen.append(_curr)
                _gen.append(_curr)

        plt.plot(x_axis, _gen)
        plt.show()


    def bipolarPseudoTernary(self):
        _gen = []
        x = []
        init_ = 0
        _curr = 1
        for i in self.data:
            x.append(init_)
            init_ += WIDTH
            x.append(init_)
            if(i == '0'):
                _gen.append(_curr)
                _gen.append(_curr)
                _curr = invert(_curr)
            else:
                _gen.append(0)
                _gen.append(0)
        
        print("plotting .....")
        print("please wait ....")

        plt.plot(x, _gen)
        plt.show()

