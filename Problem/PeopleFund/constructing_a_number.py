#!/bin/python3

import math
import os
import random
import re
import sys


def canConstruct(a):
    sum_digits = 0
    for num in a:
        for digit in num:
            sum_digits += int(digit)
    return 'Yes' if sum_digits % 3 == 0 else 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = input().rstrip().split()

        result = canConstruct(a)

        fptr.write(result + '\n')

    fptr.close()
