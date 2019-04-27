#!/bin/python3

import math
import os
import sys

# Complete the solve function below.
def solve(coordinates):
    x = list()
    y = list()

    for c in coordinates:
        x.append(c[0])
        y.append(c[1])

    return max(
        max(x) - min(x),
        max(y) - min(y),
        math.sqrt(max(abs(max(x)), abs(min(x)))**2 + max(abs(max(y)), abs(min(y)))**2)
    )


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    fptr.write(str(result) + '\n')

    fptr.close()
