### Set variables largest and smallest to None
largest = None
smallest = None
bad_input = 'Invalid input'
while True:
    try:
    ### Enter a value and check that it is an integer
        num = raw_input("Enter a number: ")
        ### If the value is done, exit the loop
        if num == "done": 
            break
        n = int(num)
    except:
    ### If the value is other than done or an integer print invalid value and prompt again
        print 'Invalid input'
        continue
### Set largest equal to the first value entered        
    if largest is None:
        largest = n
    if smallest is None:
        smallest = n
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n


print "Maximum is", largest
print "Minimum is", smallest