# Count the occurrences of each word in a list of sentences.

from collections import defaultdict
import re

def count_word_occurrences(sentences):
    
    text = " ".join(sentences)
    
    words = re.findall(r'\w+', text.lower())     
    word_freq = defaultdict(int)
    
    
    for word in words:
        word_freq[word] += 1
    
    return dict(word_freq)


sentences = [
    "This is a sample sentence.",
    "It contains some words.",
    "The words are repeated to test the word counting functionality."
]

word_occurrences = count_word_occurrences(sentences)


for word, count in word_occurrences.items():
    print(f"{word}: {count}")
