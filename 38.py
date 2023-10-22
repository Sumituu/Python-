#Find the greatest common divisor (GCD) of two numbers

def gcd(a, b):
  
  while b != 0:
    a, b = b, a % b
  return a




a = 12
b = 15

gcd = gcd(a, b)

print("The greatest common divisor of {} and {} is {}".format(a, b, gcd))
