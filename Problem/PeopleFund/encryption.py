#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.replace(' ', '')
    length = len(s)
    L = math.ceil(math.sqrt(float(length)))
    slices = [s[i:i + L] for i in range(0, length, L)]
    print(slices)
    result = ''

    for i in range(L):
        for slice in slices:
            if i < len(slice):
                result += slice[i]
        result += ' '

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
