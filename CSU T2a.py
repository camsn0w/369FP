def gcd(a, b): 
    if (a == 0): 
        return b 
    return gcd(b % a, a) 

def eulerPhi(num):
    base = 1
    for i in range(2, num):
        if(gcd(i, num) == 1):
            base += 1
    return base

listoNums = [i for i in range(2, 26)]
print("\n\nϕ(n) for n = 2, 3,..., 25\n")

for n in range(2, 26): 
    print("ϕ(",n,") = ", eulerPhi(n), sep = "")

print("ϕ(n) for n = ", [i for i in range(2, 27, 1)])