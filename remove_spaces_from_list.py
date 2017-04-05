n = int(raw_input())
total = []
while n > 0:
    total.insert(0, n)
    n = n - 1
print(*total, sep='')
        
