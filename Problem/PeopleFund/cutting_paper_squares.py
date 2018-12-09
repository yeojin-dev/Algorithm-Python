#!/bin/python3

import math
import os
import random
import re
import sys


def solve(n, m):
    if n == 1:
        return m - 1
    if m == 1:
        return n - 1
    if n < m:
        n, m = m, n
    return ((n - 1) * m) + m - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
