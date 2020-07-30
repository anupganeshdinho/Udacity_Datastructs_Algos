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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

caller = set()
receiver = set()
text_inbound = set()
text_outbound = set()
marketing = set()

# create list of telephone numbers - callers and receivers
for i in calls:
    caller.add(i[0])
    receiver.add(i[1])

# create list of texters
for i in texts:
    text_inbound.add(i[1])
    text_outbound.add(i[0])

# if the caller not present in texters or receiver then must be telemarketer
for i in caller:
    if i not in receiver and i not in text_inbound and i not in text_outbound:
        marketing.add(i)

# lexicographic sort
marketing_sorted = sorted(marketing)

print("These numbers could be telemarketers: ")
for j in marketing_sorted:
    print(j)
