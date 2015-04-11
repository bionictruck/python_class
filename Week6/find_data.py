data = 'From steve.nass@something.uni.edu Sat Jan 5 05:16:21 2010'
### Find the position of the given substring and set it to atpos
atpos = data.find('@')
print atpos
### Find the position of the given substring starting from the previous substring variable
sppos = data.find(' ',atpos)
print sppos
### Set the variable host use slice to print out appos + 1 up to but no including sppos
host = data[atpos+1 : sppos]
print host