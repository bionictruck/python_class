#### Open a file
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
### For each line in the file
for line in handle:
    ### If the the line doesn't start with From, skip it
    if not line.startswith('From '): continue
    ### Split the line up into words
    words = line.split()
    ### Create a word variable which splits the time at the :
    word = words[5].split(':')
    ### Create an hour variable which takes the first value of word
    hour = word[0]
    ### Add or increments the hour keys in the count dictionary
    count[hour] = count.get(hour, 0) + 1
### Create an empty time list
time = list()
### For each key:value pair in count, append them as tuples to the time list
for k, v in count.items():
    time.append( [k, v] )
### Sort the tuples from smallest to largest based on the key
time.sort()
for k, v in time:
    print k, v


        

