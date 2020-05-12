# Method for greatest common denominator
def gcd(a, n):
    if (a == 0):                                                # number has to be greater than 1
        return n 
    return gcd(n % a, a)                                        # number has to be relatively prime to n

# Method for Euler Phi function ϕ(n) of input
def eulerPhi(num):
    number = ""                                                 # string to append
    total = 0                                                   # result of Euler Phi function
    for i in range(1, num+1):                                   # has to start at 1
        if(gcd(i, num) == 1):                                   # calculate GCD of i in relation to input
            total += 1                                          # increment result
            number += (str(i) + ", ")                           # append the individual integers to string
    remove_last = number[:-2]                                   # remove last comma from string
    print("All values for ", i, ": ", remove_last, sep = "")    # print statement
    return total                                                # return result

# Main method
listOfNums = [i for i in range(2, 26)]
print("\n\n\nϕ(n) for n = 2, 3,..., 25:\n")
for i in range(2, 26):                                          # print all positive integers less than n
    print("ϕ(", i, ") = ", eulerPhi(i), "\n", sep = "")         # and relatively prime to n; value of ϕ(n)
