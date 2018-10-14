#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    diagonal_right_to_left = 0
    diagonal_left_to_right = 0
    length = len(arr)

    for i in range(length):
        diagonal_right_to_left += arr[i][length - 1 - i]
        diagonal_left_to_right += arr[i][i]

    return abs(diagonal_right_to_left - diagonal_left_to_right)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
