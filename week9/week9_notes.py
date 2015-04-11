# #### Dictionaries

# #### Creates a dictionary called purse
# purse = dict()
# ### Adds keys to purse with values
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# ### prints out the entire dictionary purse
# print purse
# ### prints out one specific value from the dictionary
# print purse['candy']
# #### Adds to the value for that specific key
# purse['candy'] = purse['candy'] + 2
# print purse


# test = dict()
# #### Printing out a key before it exists will give an error
# print test['grape']
# ### Looks in the dictionary for the key and prints true or fales
# print 'grape' in test

# ### Creates a dictionary called counts
# counts = dict()
# ### Creates a list called names
# names = ['jay', 'karen', 'karen', 'fletch', 'reno', 'jay']
# ### For each value (name) in the list
# for name in names:
#     ### If the name doesn't exist in the counts dictionary
#     if name not in counts:
#         ### Add that name as key with the value 1 to the count
#         counts[name] = 1
#     else:
#         #### If the name already exists, add 1 to the value for it
#         counts[name] = counts[name] + 1
# print counts



# #### Same as above code but a shorter if/else statement using Get
# ### Creates a dictionary called counts
# counts = dict()
# ### Creates a list called names
# names = ['jay', 'karen', 'karen', 'fletch', 'reno', 'jay', 'karen']
# ### For each value (name) in the list
# for name in names:
#     #### Add name to the dictionary, add 1 if already exists, print out a 0 (default value) if it can't be found
#     counts[name] = counts.get(name,0) + 1
# print counts


# ### Create an empty dictionary called counts
# counts = dict()
# print 'Enter a line of text: '
# ### User entered text is stored as a variable called line
# line = raw_input('')
# #### Create a words variable using the split function on line
# words = line.split()
# ### Shows the words as a list
# print 'Words: ', words

# print 'Counting...'
# ### For each word in the words list
# for word in words:
#     ### Add the word from the list to the dictionary, if it already exists add 1 to the value
#     counts[word] = counts.get(word,0) + 1
# ### Print out the dictionary counts
# print 'Counts', counts



# ### Creates a dictionary called counts
# counts = {'jay' : 5, 'fletch' : 3, 'reno' : 4, 'karen' : 8}
# ### For each key in the dictionary counts
# for key in counts:
#     ### Print the key and the value of that key in the dictionary counts
#     print key, counts[key]


# ### Retrieving lists of keys and values
# ### Creates a dictionary called counts
# counts = {'jay' : 5, 'fletch' : 3, 'reno' : 4, 'karen' : 8}
# #### Prints out the keys in the dictionary as a list
# print list(counts)
# print counts.keys()
# ### prints out the values in the dictionary
# print counts.values()
# ### Prints out the key:value pairs
# print counts.items()


# ### Two Iteration variables
# ### Creates a dictionary called counts
# counts = {'jay' : 5, 'fletch' : 3, 'reno' : 4, 'karen' : 8}
# #### For each key AND value in the counts dictionary
# for name,num in counts.items():
#     #### Print the key:value pair
#     print name,num


###Enter the name of a file
name = raw_input("Enter file: ")
###Open that file for read, assign to handle
handle = open(name, 'r')
### Assign all the text in handle to variable text
text = handle.read()
### Split the text and assign it to a list called words
words = text.split()

### Create an empty dictionary
counts = dict()
### For each words in the list words
for word in words:
    ### Add the word to the dictionary, add 1 if it already exists
    counts[word] = counts.get(word,0) + 1

### Set variables for the biggest word and count to None
bigcount = None
bigword = None
### For each word (key) and it's count (value) in the dictionary counts
for word,count in counts.items():
    ### If largest so far is None or current count is larger
    if bigcount is None or count > bigcount:
        ### Assign that word to bigword
        bigword = word
        ### Assign that count to bigcount
        bigcount = count

print bigword, bigcount