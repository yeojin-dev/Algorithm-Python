#!/bin/python3

import os
import sys

from math import sqrt


def movingTiles(l, s1, s2, queries):
    result = list()
    speed = abs(s1 - s2)
    l = sqrt(2) * l
    for q in queries:
        result.append(
            max(0, ((l - sqrt(2 * q)) / speed))
        )
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
