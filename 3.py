#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    l=0
    count = 0
    for i in range(l,len(c)):
        if l<len(c)-2 and c[l+2] == 0:
            l = l+2
            count = count + 1
        elif l<len(c)-1 and c[l+1] == 0:
            l = l+1
            count = count + 1
    return count



            


    

if __name__ == '__main__':
    
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)