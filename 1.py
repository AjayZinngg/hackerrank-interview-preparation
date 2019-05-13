#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def sockMerchant(n, ar):
    count = 0
    counter = Counter(ar)
    r = dict(counter)
    for i in r.values():
        if(i/2 > 0):
            count+=int(i/2)
    return int(count)
        



if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    