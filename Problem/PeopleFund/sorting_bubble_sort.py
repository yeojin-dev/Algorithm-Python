#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(a):
    length = len(a)
    count = 0

    for i in range(length - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                count += 1
                a[j], a[j + 1] = a[j + 1], a[j]

    print('Array is sorted in {} swaps.\nFirst Element: {}\nLast Element: {}'.format(count, a[0], a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
