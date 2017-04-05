n = int(input("Enter a number: "))
total = []
while n > 0:
    total.insert(0, n)
    n -= 1
print(*total, sep='')