#!/bin/python3

from math import ceil


def lowestTriangle(base, area):
    return ceil((area * 2) / base)


base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
