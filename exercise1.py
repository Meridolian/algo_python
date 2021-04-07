import numpy as np
import matplotlib.pyplot as plt
import math


def curves(n: int):
    plt.plot(np.array([math.log(i) for i in range(1, n)]))
    plt.plot(np.array([i for i in range(1, n)]))
    plt.plot(np.array([i * math.log(i) for i in range(1, n)]))
    plt.plot(np.array([i**2 for i in range(1, n)]))
    plt.plot(np.array([2**i for i in range(1, n)]))
    plt.legend(["log(i)", "i", "i * log(i)", "i**2", "2**i"])
    plt.show()


if __name__ == '__main__':
    curves(8)
