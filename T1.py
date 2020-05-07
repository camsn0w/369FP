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
    inpt = relPrimeTable(inpt)
    for x in inpt:
        print("n =", x, " S\u2099=", end="{"), print(*inpt[x][0], sep=", ", end="}\n"),
        print("S\u2099=", inpt[x][1])
        print('Matrix: \n', np.matrix(genPnMatrix(x)))
        print("Determinant: ", round(np.linalg.det(genPnMatrix(x))))
        print("Determinant % {}: ".format(x), round(np.linalg.det(genPnMatrix(x))%4))
        print("{{x\u2081,x\u2082} ⊂ S\u2099| x\u2081+x\u2082 = n, |S\u2099(1,x\u2081)| = |S\u2099(x\u2082,n-1)|}")
        for i in range(int(len(inpt[x][0]) / 2)):
            x1 = inpt[x][0][int(i)]
            x2 = inpt[x][0][int((len(inpt[x][0]) - 1) - i)]
            print("{{x\u2081,x\u2082}} = {{{}, {}}}".format(x1, x2))
        print("_" * 60)


def relPrimeTable(inpt):
    sumDict = {}
    for x in inpt:
        sumDict.setdefault(x, [relPrime(x), sum(relPrime(x))])
    return sumDict


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
    return newlist


def bDetWork(num):
    inpt = genPnMatrix(num)
    det1 = np.linalg.det(inpt)
    det2 = np.linalg.det(inpt) % num
    print("n=", num, sep="")
    print("S\u2099", " = ", inpt, sep="")


def main():
    listoNums = [i for i in range(2, 26, 1)]
    printRelPrimeTable(listoNums)


if __name__ == '__main__':
    main()
