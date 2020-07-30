"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# using dictionary instead of 2 for loops
mydict = {}

for i in calls:
    # caller
    if i[0] not in mydict.keys():
        mydict[i[0]] = int(i[3])
    else:
        mydict[i[0]] += int(i[3])
    # receiver
    if i[1] not in mydict.keys():
        mydict[i[1]] = int(i[3])
    else:
        mydict[i[1]] += int(i[3])

max_time = 0

# iterate through the dictionary to find the max time.
for key in mydict:
    if max_time < int(mydict[key]):
        final_phone = key
        max_time = int(mydict[key])
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(final_phone, max_time));

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
