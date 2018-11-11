#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_value = -64
    for x in range(4):
        for y in range(4):
            temp = (arr[x][y] + arr[x][y + 1] + arr[x][y + 2] + arr[x + 1][y + 1]
                + arr[x + 2][y] + arr[x + 2][y + 1] + arr[x + 2][y + 2])
            max_value = temp if temp > max_value else max_value
    return max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
