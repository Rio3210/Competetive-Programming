#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    noOfswaps=0
    for i in range(len(a)-1):
        for j in range(0,len(a)-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
                noOfswaps+=1
    print("Array is sorted in {} swaps.".format(noOfswaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a)-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
