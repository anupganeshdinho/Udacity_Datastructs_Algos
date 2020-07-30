"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
telephone_full = []

a_string = "(080)"

for i in calls:
    # find if there is 080 present in caller
    if (i[0].find(a_string)) == 0:
        my_string = i[1]
        # First set for mobile numbers
        if my_string.startswith(('7', '8', '9')):
            telephone_full.append(my_string[:4])
        # Scam callers
        elif my_string.startswith('140'):
            telephone_full.append(140)
        else:
            # land line
            result = my_string.split(")")
            extra = ')'
            telephone_full.append(result[0] + extra)

# Remove duplicates
telephone_set = set(telephone_full)
# sort in lexicographic manner
telephone_sorted = sorted(telephone_set)

# print one after another as requested in sorted manner
print("The numbers called by people in Bangalore have codes:")

for j in telephone_sorted:
    print(j)

character = '(080)'
total = 0

# count number of calls to 080
for k in telephone_full:
    if k == character:
        total += 1

# calculate percentage and round it off to 2 decimal places
percentage = round(total * 100 / len(telephone_full), 2)

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))
