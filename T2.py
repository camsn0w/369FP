import math
import numpy as np
import T1 as T1


def EulerPhi(num):
    return len(T1.relPrime(num))


def main():
    listoNums = [i for i in range(2, 26, 1)]
    print("ϕ(n) for n = 2, 3,..., 25")
    print([EulerPhi(i) for i in range(2, 26, 1)])
    #print(EulerPhi(6))


if __name__ == '__main__':
    main()

