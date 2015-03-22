### Set variable smallest to None
smallest = None
print 'Before ', smallest
### For each value in the list
for n in [9, 41, 2, 24, 54, 17, 95, 6, 8]:
    ### If the value for smallest is set to None set it to the first value in the list
    if smallest is None:
        smallest = n
    ### If the value is smaller than the current smallest value
    elif n < smallest:
    ### Set smallest to the new value and print the smallest value and the current value
        smallest = n
    print smallest, n
    
print 'After ', smallest