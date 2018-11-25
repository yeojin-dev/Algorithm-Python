#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(n, c):
    result = i = 0
    while i < n - 1:
        if i != n - 2 and c[i + 2] == 0:
            i += 2
        elif c[i + 1] == 0:
            i += 1
        result += 1
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
