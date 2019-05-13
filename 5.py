#!/bin/python3

def rotLeft(a, d):
    b = a[:]
    for i in range (0,len(a)):
        newLocation = (i + (len(a) - d)) % len(a)
        a[newLocation] = b[i]
    return a 

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)