#Calculate the LCM and GCD of two numbers

import math

def gcd(a, b): 
    if (a == 0): 
        return b; 
    return gcd(b % a, a); 
def lcm(a, b): 
    return (a * b) // gcd(a, b); 

a = 12
b = 15

print("LCM of", a, "and", b, "is", lcm(a, b))
print("GCD of", a, "and", b, "is", gcd(a, b))
