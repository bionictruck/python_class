### Lists are mutable (can be changed)

# ### Original list
# lotto = [2, 14, 22, 45, 65]
# print lotto
# ### Changing the item at id 2 to 28 from 22
# lotto[2] = 28
# print lotto

# ### Length function will show how many items are in the list
# x = ['apple', 'peach', 'banana']
# print len(x)


# ### The range function
# ### Returns a list of numbers starting at 0 and ending at one less than the parameter given
# print range(4)

# friends = ['John', 'Frank', 'Dean']
# ### Shows the length of the list
# print len(friends)
# ### Converts list to an integer value and uses that as the parameter for range
# ### Shows the index value of each friend in the list
# print range(len(friends))


# friends = ['Sammy', 'Frank', 'Dean']
# ### For each item in the range
# for i in range(len(friends)):
#     ### Set a variable friend for each item
#     friend = friends[i]
#     ### Print out  the message
#     print 'Happy New Year', friend


# ### Concatenate lists
# a = [1, 2, 3]
# b = [4, 5, 6]
# ### Set variable c to combine both the a and b lists
# c = a + b
# print c


# ### Slicing lists
# x = [1, 6, 55, 72, 4, 11, 54]

# print x[3:5]
# print x[2:]
# print x[:5]
# print x[:]



# ### List methods
# x = [1, 2, 3, 4]
# ### Determines what x is (list, int, etc)
# print type(x)
# ### Shows you the different methods that can be applied to x
# print dir(x)



# ### Adding to a list
# ### Create empty list
# x = []
# ### Add items to the list
# x.append('test')
# x.append(55)
# x.append('great')
# ### Print out the list
# print x


# #### Is something in a list?
# x = [12, 43, 'book', 'pizza', 66]
# ### Looks through the list and gives true or false if the item is in the list
# print 9 in x
# print 'book' in x


# ### Built in functions
# x = [3, 45, 23, 76, 18]

# print len(x)
# print min(x)
# print max(x)
# print sum(x)
# print sum(x)/len(x)



# ### Give an average for given numbers
# ### Create an empty list
# numlist = list()
# ### Create loop
# while True:
#     ### Assign give value to variable
#     inp = raw_input('Enter a number: ')
#     ### If done is entered, exit loop
#     if inp == 'done': break
#     ### Create variable value and assign the float of inp to it
#     value = float(inp)
#     ### Append the value to the list
#     numlist.append(value)

# ### Determine average by summing up the value and dividing by the number of values
# average = sum(numlist)/len(numlist)
# print 'Average:', average



# ### Strings and lists
# ### Create a string variable
# x = 'Hello there Bob'
# ### Using split() the string is broken up into a list
# y = x.split()
# print y
# print len(y)
# print y[2]


# ### Data seperated with characters other than spaces
# x = 'pizza;beer;cake'
# y = x.split()
# print y
# print len(y)
# ### By specifying the character to split on the list is returned as desired
# z = x.split(';')
# print z
# print len(z)


### Open the file
fhand = open('mbox-short.txt')
### For each line in the file
for line in fhand:
    ### Strip off the empty space at the end of each line
    line = line.rstrip()
    ### If the line does not start with 'From' skip to the next line
    if not line.startswith('From '): continue
    ### Split the line so each word is an item in a list
    words = line.split()
    ## print words ## shows the lists
    ### print the word at id 2
    print words[2]



