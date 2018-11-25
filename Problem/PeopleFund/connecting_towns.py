#!/bin/python3

import os
import sys
from functools import reduce


def connectingTowns(n, routes):
    return reduce(lambda x, y: (x*y) % 1234567, routes)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
