fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.strip()
    words = line.split()
    for i in words:
        if i not in lst:
            lst.append(i)
            lst.sort()


print lst