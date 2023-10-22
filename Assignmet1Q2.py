#Create a Python function that accepts a list of numbers as input and returns the sum of all even numbers.

def sum_even_numbers(numbers):
    
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num

    return even_sum


numbers = [1, 2, 3, 4, 5, 6]
result = sum_even_numbers(numbers)
print("Sum of even numbers:", result)
