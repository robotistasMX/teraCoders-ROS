#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    suma=arr[0][0]+arr[0][0+1]+arr[0][0+2]+arr[0+1][0+1]+arr[0+2][0]+arr[0+2][0+1]+arr[0+2][0+2]
    for x in range(4):
        for y in range(4):
            suma_aux=arr[x][y]+arr[x][y+1]+arr[x][y+2]+arr[x+1][y+1]+arr[x+2][y]+arr[x+2][y+1]+arr[x+2][y+2]
            if suma_aux > suma:
                suma=suma_aux
    return suma 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

