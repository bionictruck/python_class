### Set a variable, loops through a list, if the variable is greater than largest, print the largest number and the number just evaluated ###

# largest = -1
# print 'Before ', largest
# for n in [9, 41, 2, 24, 54, 17, 95, 6, 8]:
    # if n > largest:
        # largest = n
    # print largest, n
    
# print 'After ', largest

# ### Set Variable x
# x = 0
# print 'Before', x
# ### For each value of n in the list
# for n in [9, 41, 2, 24, 54, 17, 95, 6, 8]:
# ### Increment x by 1
    # x = x + 1
# ### Print out the current values of x and n
    # print x, n
# ### Print the total number of values in the list    
# print 'After', x

# ### Set variable x
# x = 0
# print 'Before', x
# ### for each value in the list
# for n in [23, 13, 7, 43, 9, 24]:
# ###  Add variable x and n, set to x
    # x = x + n
# ### Print the new value of x and the current n
    # print x, n
# ### Print the final value of x when the list is complete
# print 'After', x

# ### Set variables for count and sum
# count = 0
# sum = 0
# print 'Before', count, sum
# ### For each value in the list
# for value in [6, 87, 23, 15, 45, 7]:
    # ### Increment the count variable
    # count = count + 1
    # ### Take the current sum, add the next value and set that to new sum
    # sum = sum + value
    # ### print the current values for count, sum and value
    # print count, sum, value
# ### Print the count, sum and the average sum / count
# print 'After', count, sum, sum/count


# print 'Before'
# ### For each value in the list
# for value in [5, 10, 67, 43, 3, 12]:
# ### If the value is greater that 20 print large number
    # if value > 20:
        # print 'Large number', value
# print 'After'

### Set variable to False
found = False
print 'Before', found
### For each value in the list
for value in [4, 78, 25, 45, 9]:
### Loop through and if the value is found set found to True and exit loop
    if value == 25:
        found = True
        break
    print found, value
    
print 'After', found
