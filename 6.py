#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    initialPositions = sorted(q)

    for i in range(0,len(q)):
        if q[i] != initialPositions[i] and q[i+1] < q[i]  


    print(initialPositions)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
