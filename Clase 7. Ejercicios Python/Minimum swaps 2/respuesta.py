#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    global n
    var =0
    for i in range(n):
        if arr[i] == i+1: pass
        else:
            min_idx = i
            while arr[min_idx] !=  arr[arr[min_idx]-1]:
                arr[arr[min_idx]-1], arr[min_idx] = arr[min_idx], arr[arr[min_idx]-1]
                var=var+1
    return var

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

