#!/bin/python3

import math
import os
import sys

# Complete the solve function below.
def solve(n):
    sum_digits = sum(int(digit) for digit in list(str(n)))
    
    factor_digits = list()
    factor = 2

    while n > 1:
        if n % factor == 0:
            factor_digits += list(str(factor))
            n /= factor
        else:
            factor += 1

    sum_factors = sum(int(digit) for digit in factor_digits)

    return int(sum_digits == sum_factors)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = solve(n)

    fptr.write(str(result) + '\n')

    fptr.close()
