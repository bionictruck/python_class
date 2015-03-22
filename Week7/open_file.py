# ### Set varible to use the open function (file name, r for read or w for write)
# handle = open('mbox-short.txt', 'r')

# print handle



# ### New line character \n indicates the start of a new line. Counts as 1 character
# stuff = 'Hello\nWorld!'
# print stuff
# print len(stuff)


# ### Shows the contents of the file
# xfile = open('mbox-short.txt', 'r')

# ### For each item in the file, print it out
# for source in xfile:
#     print source


# ### Count the number of lines in the file
# ### Set variables to open the file and set the initial count
# xfile = open('mbox-short.txt', 'r')
# count = 0

# ### Run the indented text once for each line in the file
# for line in xfile:
#     count = count+1

# print "Line Count:", count



# ### Read the entire file
# xfile = open('mbox-short.txt', 'r')
# ### Reads the entire file and return it as a string to a variable
# letter = xfile.read()
# ### Print out the length of that variable
# print len(letter)

# ### Prints out a slice of the file starting from the first character up to but not including 25
# print letter[:25]



# #### Searching through a file
# xfile = open('mbox-short.txt', 'r')
# ### For each line in the file
# for line in xfile:
#     ### Strips out the whitespace including \n from the end of each line
#     line = line.rstrip()
#     ### If the line starts with a string
#     if line.startswith('From:'):
#         ### Print that line
#         print line


# #### Skipping with continue
# xfile = open('mbox-short.txt', 'r')
# #### For each line in the file
# for line in xfile:
#     ### Strip out the white space
#     line = line.rstrip()
#     ### If the line does NOT start with the string skip it
#     if not line.startswith('From:'):
#         continue
#     ### Print out the lines that have not been skipped
#     print line



# #### Using in to select lines
# xfile = open('mbox-short.txt', 'r')
# for line in xfile:
#     line = line.rstrip()
#     ### If the line does not contain the string skip it continue through the file
#     if not '@uct.ac.za' in line:
#         continue
#     ### Print the line(s) that do contain the string
#     print line


# #### Prompt for a file name
# xname = raw_input('Which file ya want?: ')
# ### Open the file give in the prompt, if file is invalid print a message and exit the program
# try:
#     xfile = open(xname)
# except:
#     print 'This file cannot be opened:', xname
#     exit()
# count = 0
# ### For each line in the file
# for line in xfile:
#     ### If the file starts with the string
#     if line.startswith('Subject:'):
#         ### Increment the count
#         count = count+1
# ### Print out the number of lines that start with the string in the file
# print 'There were', count, 'Subject lines in', xname