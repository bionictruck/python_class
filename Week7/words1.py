# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
	fh = open(fname)
except:
	print fname, "is not a valid file!"
	exit()
for words in fh:
	words = words.rstrip()
	print words.upper()