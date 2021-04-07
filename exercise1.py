import numpy as np
import matplotlib.pyplot as plt
import math


def curves(n: int):
    x = np.array([math.log(n), n, n * math.log(n), n**2, 2**n])
    plt.plot(n, n)
    plt.show()


if __name__ == '__main__':
    curves(5)
