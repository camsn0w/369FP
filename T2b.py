import math

# Method for prime factors
def primeFactor(n):
    number = ""
    while n % 2 == 0:                               # Print the number of two's that divide n
        print(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):    # while i divides n , print i ad divide n 
        while n % i== 0: 
            print(int(i))
            n = n / i
    if n > 2:
        print(int(n))

# Main method
for i in range(2, 26):
    print("\nPrime factors of ", i, " are: ")       #print all prime factors of input
    primeFactor(i)
