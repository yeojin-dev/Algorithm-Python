#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    point_alice = 0
    point_bob = 0
    for i in range(3):
        if a[i] > b[i]:
            point_alice += 1
        elif a[i] < b[i]:
            point_bob += 1
    return [point_alice, point_bob]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
