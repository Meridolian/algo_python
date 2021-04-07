import math
import numpy as np


def compare(time: int):
    hz = 0.0000001
    instruction = float(time) / hz

    print("Nombre d'instruction possible :", instruction)
    print("log(n) :", np.log10(instruction))
    print("n :", instruction)
    print("n log(n) :", instruction * math.log10(instruction))
    print("n² :", instruction**2)
    print("2^n :", 2**instruction)


if __name__ == '__main__':
    print("Pour 1 seconde")
    compare(1)
    print("Pour 1 minute")
    compare(60)
    print("Pour 1 heure")
    compare(3600)
    print("Pour 1 journée")
    compare(3600*24)
