import math


def relPrime(num):
    if num <= 2:
        if num == 1:
            return [0]
        if num == 2:
            return [1]
        return []
    result = []
    for x in range(1,num):
        if math.gcd(num,x) == 1:
            result.append(x)
    return result

def printRelPrimeTable(inpt):
    for x in inpt:
        print(x,"Sum:",inpt[x][1])

def relPrimeTable(inpt):
    sumDict = {}
    for x in inpt:
        sumDict.setdefault(x,[relPrime(x), sum(relPrime(x))])
    printRelPrimeTable(sumDict)






def main():
    listoNums = [i for i in range(2,16,1)]
    #numNums = (int(input("How many numbers? ")))
    print(relPrimeTable(listoNums))


if __name__ == '__main__':
    main()
