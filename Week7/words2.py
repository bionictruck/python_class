# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
count = 0
x = 0
try:
    fh = open(fname)
except:
    print fname, "is not a valid file."
    exit()
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = float(line[20:])+x
    count = count + 1

print "Average spam confidence:", x / count