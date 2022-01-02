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


## Below, we have provided a list of tuples that consist of student names, final exam scores, and ‎se ‎or not they will pass the class. For some students, the tuple does not have a third element because it is unknown whether or not they will pass. Currently, the for loop does not work. Add a try/except clause so the code runs without an error - if there is no third element in the tuple, no changes should be made to the dictionary.

students = [('Timmy', 95, 'Will pass'), ('Martha', 70), ('Betty', 82, 'Will pass'), ('Stewart', 50, 'Will not pass'), ('Ashley', 68), ('Natalie', 99, 'Will pass'), ('Archie', 71), ('Carl', 45, 'Will not pass')]

passing = {'Will pass': 0, 'Will not pass': 0}
for tup in students:
    try:
        if tup[2] == 'Will pass':
            passing['Will pass'] += 1
        elif tup[2] == 'Will not pass':
            passing['Will not pass'] += 1
    except IndexError:
        continue


## Below, we have provided code that does not run. Add a try/except clause so the code runs without errors. If an element is not able to undergo the addition operation, the string ‘Error’ should be appended to plus_four.

nums = [5, 9, '4', 3, 2, 1, 6, 5, '7', 4, 3, 2, 6, 7, 8, '0', 3, 4, 0, 6, 5, '3', 5, 6, 7, 8, '3', '1', 5, 6, 7, 9, 3, 2, 5, 6, '9', 2, 3, 4, 5, 1]

plus_four = []

for num in nums:
    try:
        plus_four.append(num+4)
    except:
        plus_four.append("Error")