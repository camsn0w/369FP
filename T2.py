import math
import numpy as np
import T1 as T1


def EulerPhi(num):
    return len(T1.relPrime(num))

def main():
    print("ϕ(n) for n =", [i for i in range(2, 27, 1)])
    ep = [EulerPhi(i) for i in range(2, 27, 1)]
    print(ep)
    epMatrix = np.matrix([ep[r*5:(r+1)*5] for r in range(0,5)])
    print(epMatrix)


if __name__ == '__main__':
    main()
