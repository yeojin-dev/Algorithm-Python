#!/bin/python3

import os
import sys

#
# Complete the restaurant function below.
#
def restaurant(l, b):
    def gcd(l, b):
        if l < b:
            l, b = b, l
        return b if l % b == 0 else gcd(b, l % b)
    k = gcd(l, b)
    return (l // k) * (b // k)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()

        l = int(lb[0])

        b = int(lb[1])

        result = restaurant(l, b)

        fptr.write(str(result) + '\n')

    fptr.close()
