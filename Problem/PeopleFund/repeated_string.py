#!/bin/python3

import math
import os
import random
import re
import sys


def repeatedString(s, n):
    a_count = s.count('a')
    length = len(s)
    return a_count * (n // length) + (s[:(n % length)].count('a'))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
