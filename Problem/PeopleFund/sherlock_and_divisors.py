#!/bin/python3

import math
import os
import sys

#
# Complete the divisors function below.
#
def divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0 and i % 2 == 0:
            count += 1
        if n % (n // i) == 0 and (n // i) % 2 == 0:
            count += 1
        if i == n // i and i % 2 == 0 and n % i == 0:
            count -= 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = divisors(n)

        fptr.write(str(result) + '\n')

    fptr.close()
