from random import randint

def binary_search(v, search, init=0, end=0):
    if end >= init:
        midpoint = (end + init) // 2
        if v[midpoint] == search:
            return True
        elif v[midpoint] > search:
            return binary_search(v, search, init, midpoint-1)
        else:
            return binary_search(v, search, midpoint+1, end)
    else:
        return False

size = 1000

l = [randint(0,size) for i in range(size)]

l.sort()

print(l)

print(binary_search(l, 26, init=0, end=len(l)-1))