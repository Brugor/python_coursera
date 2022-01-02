## Create an empty list called resps. Using the list percent_rain, for each percent, if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, otherwise, add the string ‘Nice day!’ to resps. Note: if you’re sure you’ve got the problem right but it doesn’t pass, then check that you’ve matched up the strings exactly.

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = []
for rain in percent_rain:
    if rain > 90:
        resps.append("Bring an umbrella.")
    elif rain > 80:
        resps.append("Good for the flowers?")
    elif rain > 50:
        resps.append("Watch out for clouds!")
    else:
        resps.append("Nice day!")


## str1 = "I love python"
# HINT: what's the accumulator? That should go here.

chars = []
for c in str1:
    chars.append(c)
# chars = [char for char in str1]


## The print statements at the end of program ac10_5_5 above pick out the specific keys ‘t’ and ‘s’. Generalize that to print out the occurrence counts for all of the characters. To pass the unit tests, your output must use the same format as the original program above.

f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0

    letter_counts[c] = letter_counts[c] + 1

# Write a loop that prints the letters and their counts
for k, v in letter_counts.items():
    print("{}:{}" .format(k, v))


## Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value

product = "iphone and android phones"
lett_d = {}
for char in product:
    if char not in lett_d:
        lett_d[char] = 0
    lett_d[char] += 1
    
max_value = max(lett_d, key=lett_d.get)