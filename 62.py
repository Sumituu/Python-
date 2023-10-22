# Reverse the order of words in a sentence
# Function to reverse the order of words in a sentence
def reverse_words(sentence):
    
    words = sentence.split()

   
    reversed_words = words[::-1]

    
    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence


my_sentence = "The quick brown fox"


reversed_sentence = reverse_words(my_sentence)

print("Original Sentence:", my_sentence)
print("Reversed Sentence:", reversed_sentence)
