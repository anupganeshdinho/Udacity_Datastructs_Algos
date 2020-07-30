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

# create a set
telephone = []
k = 0

# add phone numbers using append function
for i in texts:

    telephone.append(texts[k][0])
    telephone.append(texts[k][1])
    k = k + 1

k = 0
for i in calls:

    telephone.append(calls[k][0])
    telephone.append(calls[k][1])
    k = k + 1

unique = set(telephone)
print("There are {} different telephone numbers in the records.".format(len(unique)))
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
