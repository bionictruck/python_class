### Tuples
# x = ('John', 'Sally', 'Frank')
# print x[2]

# y = (1, 8, 4, 3)
# print y
# print max(y)

# for num in y:
#     print num

### Tuples are immutable and cannot be edited
### Cannot sort tuples
### Cannot append
### Cannot reverse

### Assign to two variable, can either use or leave out left paranthesis
# (x, y) = (45, 78)
# print x
# print y

# ### Create a dictionary
# d = dict()
# d['jay'] = 5
# d['reno'] = 6
# ### Use the items function to create a list of two tuples
# tups = d.items()
# print tups

# ### Loops through the list
# for k, v in tups:
#     ### Print the first item in the each tuple in the list
#     print k


### Tuples are comparable
### Compares each number, if they are equal, moves to the next. After all numbers compared prints true or false
# print (5, 6, 7) < (5, 6, 8)
### The sooner in the alphabet is the "less" than value
# print ('Butch', 'Fletch') < ('Karen', 'Reno')


# #### A list of tuples CAN be sorted
# ### Create a dictionary
# x = {'a':5, 'b':6, 'c':10}
# ### Create list of tuples that have a key:value relationship
# t = x.items()
# print t
# ### sorts by keys
# t.sort()
# print t


# #### Shorter version of the previous
# ### Create a dictionary
# x = {'a':5, 'b':6, 'c':10}
# ### Create and sort list of tuples that have a key:value relationship
# t = sorted(x.items())
# print t

# for k, v in sorted(x.items()):
#     print k, v

# #### Sort by values instead of keys
# ### Create dictionary
# x = {'a':2, 'b':8, 'c':5}
# ### Create empty list
# tmp = list()
# ### For each key:value pair in the dictionary
# for k, v in x.items():
#     ### Append them in reverse (value:key) in the list from lowest to highest
#     tmp.append( (v, k) )
# print tmp
# ### Sorts the list in reverse (from highest to lowest)
# tmp.sort(reverse=True)
# print tmp

# ### Open the document
# fhand = open('romeo.txt')
# ### Create an empty dictionary
# counts = dict()
# ### for each line in the documents
# for line in fhand:
#     ### Create words by splitting the line
#     words = line.split()
#     ### For each word
#     for word in words:
#         ### Increment the count for each word as it is found.
#         ### Set the word as the key and the count as the value
#         counts[word] = counts.get(word, 0) + 1

# print counts
# ### Create an empty list
# lst = list()
# ### For each key:value pair in the count dictionary
# for k, v in counts.items():
#     ### append them to the list as value:key pairs
#     lst.append( (v, k) )
# ### Sort the list to go from highest to lowest
# lst.sort(reverse=True)
# ### for the first 10 value:key pairs in the list
# for v, k in lst[:10] :
#     ### print out the key and it's value (word and counts)
#     print k, v


# counts = {'apple':4, 'peach':18, 'cranberries':22, 'banana':4}
# print sorted( [ (v,k) for k,v in counts.items() ] )

