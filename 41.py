#Calculate the nth term of an arithmetic progression.

def nth_term_of_ap(a1, n, d):
    if n < 1:
        return None  
    else:
        return a1 + (n - 1) * d

# Example usage:
a1 = 3  
n = 6 
d = 2   

nth_term = nth_term_of_ap(a1, n, d)

if nth_term is not None:
    print(f"The {n}th term of the arithmetic progression is: {nth_term}")
else:
    print("Invalid input. n should be a positive integer.")
