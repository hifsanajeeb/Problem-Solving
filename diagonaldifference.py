#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    length = len(arr[0]);
    leftDiagonalSum=0;
    rightDiagonalSum=0;
    for i in range(length):
        leftDiagonalSum += arr[i][i];
        rightDiagonalSum += arr[i][length-i-1]  # same result with         rightDiagonalSum += arr[length-i-1][i]
    return abs(rightDiagonalSum - leftDiagonalSum)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
