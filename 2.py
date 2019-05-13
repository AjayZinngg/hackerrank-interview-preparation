#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def countingValleys(n, s):
    s = list(s)
    print(s)
    level = 0
    v = 0

    for i  in s:
        if i == 'U': level+=1
        if i == 'D': level-=1

        print(level)
        if (level == 0 and i == 'U'):
            v+=1
    
    return v

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)

    