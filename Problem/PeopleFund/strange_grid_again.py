#!/bin/python3

import os
import sys
import math


def strangeGrid(r, c):
    odds = [1, 3, 5, 7, 9]
    evens = [0, 2, 4, 6, 8]
    c = odds[c - 1] if r % 2 == 0 else evens[c - 1]
    r = math.ceil(r / 2) - 1
    return r * 10 + c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()

    r = int(rc[0])

    c = int(rc[1])

    result = strangeGrid(r, c)

    fptr.write(str(result) + '\n')

    fptr.close()
