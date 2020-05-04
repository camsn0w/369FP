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
        print("n = ",x, ", Coprimes < n: ", inpt[x][0],sep="")
        print("S\u2099=", inpt[x][1])


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

def bDetWork(num):
    inpt = genPnMatrix(num)
    det1 = np.linalg.det(inpt)
    det2 = np.linalg.det(inpt) % num
    print("n=",num,sep="")
    print("Det P\u2099", " = ",round(det1),sep="")
    print("Det P\u2099"," % ",num," = ", round(det2),sep="")

    print("Row",len(inpt),"+ previous rows =",[sum(row[i] for row in inpt) for i in range(len(inpt[0]))])



def main():
    listoNums = [i for i in range(2, 30, 1)]
    #printRelPrimeTable(listoNums)
    bDetWork(9)


if __name__ == '__main__':
    main()
