import math
import numpy as np


def relPrime(num):
    if num <= 2:
        if num == 1:
            return [0]
        if num == 2:
            return [1]
        return []
    result = []
    for x in range(1, num):
        if math.gcd(num, x) == 1:
            result.append(x)
    return result


def printRelPrimeTable(inpt):
    for x in inpt:
        print(x, "Coprimes:", inpt[x][0])
        print("Sum:", inpt[x][1])


def relPrimeTable(inpt):
    sumDict = {}
    for x in inpt:
        sumDict.setdefault(x, [relPrime(x), sum(relPrime(x))])
    return sumDict
    # printRelPrimeTable(sumDict)


def c1(inpt):
    for x in inpt:
        print("n =", x)
        print("Sum =", inpt[x][1])
        val = inpt[x][1] % int(x)
        print("Sum % n =", val)


# Builds matrix shown in B for a given int
def genPnMatrix(num):
    inpt = relPrime(num)
    newlist = [inpt[x:] + inpt[:x] for x in range(0, len(inpt))]
    print(np.matrix(newlist))
    return newlist


def main():
    listoNums = [i for i in range(2, 30, 1)]
    genPnMatrix(9)
    # print(relPrimeTable(listoNums))
    # c1(relPrimeTable(listoNums))


if __name__ == '__main__':
    main()
