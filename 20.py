#Write a program to find the roots of a quadratic equation.

import math

def quadratic_roots(a, b, c):


  discriminant = b**2 - 4 * a * c

  if discriminant > 0:
   
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2

  elif discriminant == 0:
    
    root = -b / (2 * a)
    return root, root

  else:
    
    root1 = (-b + math.sqrt(-discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(-discriminant)) / (2 * a)
    return root1, root2



a = 1
b = 2
c = 3

roots = quadratic_roots(a, b, c)

print("The roots of the quadratic equation are:", roots)
