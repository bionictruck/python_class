from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    total = []
    while n > 0:
        total.insert(0, n)
        n = n - 1
    ### The * removes [{, and sep = removes the spaces
    print(*total, sep='')
        
