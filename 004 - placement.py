""" Create a dictionary called d that keeps track of all the characters in the string 
placement and notes how many times each character was seen. Then, find the key with the 
lowest value in this dictionary and assign that key to min_value.
"""

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = {}

for c in placement:
    if c not in d:
        d[c] = 0
        
    d[c] += 1
    
min_value = min(d, key=d.get)