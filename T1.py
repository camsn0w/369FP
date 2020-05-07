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
        print("n =",x, " S\u2099=",end="{"), print(*inpt[x][0],sep=", ",end="}\n"),#print("{",','.join(str(inpt[x][0])),"}")
        print("S\u2099=", inpt[x][1])
        print("{{x\u2081,x\u2082} ⊂ S\u2099| x\u2081+x\u2082 = n, 2|S\u2099(2,x\u2081)| = |S\u2099|, 2|S\u2099(x\u2082,n)| = |S\u2099| }")
        x1 = inpt[x][0][int(len(inpt[x][0]) / 2)-1]
        x2 = inpt[x][0][int(len(inpt[x][0])/2)]
        #x2 = inpt[x][0][int(len(inpt[x][0])/2+1)]
        #x2 = 1
        print("{{x\u2081,x\u2082}} = {{{}, {}}}".format(x1,x2))


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
    print("S\u2099", " = ",inpt,sep="")
    #print("Det P\u2099"," % ",num," = ", round(det2),sep="")

    #print("Row",len(inpt),"+ previous rows =",[sum(row[i] for row in inpt) for i in range(len(inpt[0]))])
    #print("Sum row:",len(inpt),sum(inpt[0]) * len(inpt[0]))



def main():
    listoNums = [i for i in range(2, 26, 1)]
    printRelPrimeTable(listoNums)
    #x = relPrimeTable(listoNums)
    #print(x)

    #bDetWork(13)


if __name__ == '__main__':
    main()
