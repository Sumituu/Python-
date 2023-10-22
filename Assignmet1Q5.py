#Write a Python program using loops for the Fibonacci sequence of n terms.

def generate_fibonacci(n):
   
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)

    return fib_sequence

n = int(input("Enter the number of Fibonacci terms to generate: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci Sequence (first", n, "terms):", fibonacci_sequence)
