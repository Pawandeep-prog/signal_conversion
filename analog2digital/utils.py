import matplotlib.pyplot as plt
class Utils:
    def __init__(self) -> None:
        pass
    def plot(x, y):
        plt.plot(x, y)
        plt.grid(True, which='both')
        plt.show()

    def plot_scatter(x, y, a, b):
        plt.plot(x, y)
        plt.grid(True, which='both')
        plt.scatter(a, b, c='r')
        plt.show()