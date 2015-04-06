name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
address = []
handle = open(name,'r')
for line in handle:
    lines = line.rstrip()
    if not lines.startswith('From '): continue
    words = lines.split()
    address.append(words[1])

count = dict()
for addy in address:
    count[addy] = count.get(addy,0) + 1
bigaddy = None
bigcount = None
for addy,count in count.items():
    if bigcount is None or count > bigcount:
        bigaddy = addy
        bigcount = count

print bigaddy, bigcount