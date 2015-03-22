# ### Set variable to string banana
# fruit = "banana"
# ### Set x to an index of the string
# x = fruit[2]

# print x


# ### Set variable to string banana
# fruit = "banana"
# ### Set variable to an integer
# n = 4
# ### Set the index to the variable minus a value
# x = fruit[n-4]

# print x


# ### Set variable to string banana
# fruit = "banana"

# ### Print the length of the variable
# print len(fruit) 


### Using a While loop
# ### Set variable to string banana
# fruit = "banana"
# ### Set variable to an initial value
# index = 0

# ### While the value of indexis less than the length of variable fruit
# while index < len(fruit):
# ### Set letter to the current index of variable fruit
    # letter = fruit[index]
# ### Print the current index number and the letter it corresponds
    # print index, letter
# ### Increment the index value by 1
    # index = index + 1
# ### Will continue to run through loop until the value of index is no longer < length of fruit


# ### Using a For loop
# ### Set variable to string banana
# fruit = "banana"
# ### For each index in the variable
# for letter in fruit:
# ### Print out each index
    # print letter
    
# ### Loops through the word variable and prints a count of the specified letter
# ### Set variable to a string
# word = "banana"
# ### Set variable to an integer value to keep count
# count = 0
# ### For each index in the word variable
# for letter in word:
# ### If the letter = an a
    # if letter == 'a':
    # ### Increment the count by 1
        # count = count + 1
# print count


# ### Slicing a string
# x = "McDonalds"
# ### First number is the start, second is the end. Will print out all indexes from start up to but not including end
# print x[3:6]
# print x[1:5]

# ### Using the In operator
# x = "Hockey"
# ### Prints out True or False if the letter is in the variable
# print 'c' in x
# print 'b' in x
# ### If the letter is in the variable
# if 'y' in x:
    # print "You bet!"
# else:
    # print "Nope!"

# ### Prints out the variable in all lower case letters    
# greet = 'Hello Bob'
# ### Use upper() for all upper case letters
# zap = greet.lower()
# print zap


# ### The dir option
# stuff = 'Hello World'
# ### Tells what type of variable it is
# print type(stuff)

# ### Gives you all the commands that can be used on this variable
# print dir(stuff)

# ### Print out the position of the first occurance of the substring. If not found prints out -1
# fruit = 'apple'
# pos = fruit.find('p')
# print pos

# ### Search and replace
# greet = 'Hello Bob'
# ###In the variable greet, replace the string Bob with Jane
# name = greet.replace('Bob','Jane')
# print name


# ### Stripping whitespace
# greet = '    Hello Bob  '
# ### Strips space starting from the left going right
# print greet.lstrip()
# ### Strips out space starting from right going left
# print greet.rstrip()
# ### Strips out all white space
# print greet.strip()

###Starts with
line = 'Please have a nice day'
### Determines if the variable starts with that string. CASE SENSATIVE!
print line.startswith('Please')
print line.startswith('p')

