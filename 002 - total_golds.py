"""
Split the string sentence into a list of words, then create a dictionary named 
word_counts that contains each word and the number of times it occurs.
"""
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
word_counts = {}

for v in sentence.split():
    if v not in word_counts:
        word_counts[v] = 0
        
    word_counts[v] += 1
print(word_counts)