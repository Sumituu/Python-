# Count the number of vowels and consonants in a string.

def count_vowels_and_consonants(string):
    
    vowels = 0
    consonants = 0

    
    vowel_set = set("AEIOUaeiou")

    for char in string:
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


input_string = "Hello, World!"
vowels, consonants = count_vowels_and_consonants(input_string)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
