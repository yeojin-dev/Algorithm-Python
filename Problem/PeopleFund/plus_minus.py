#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    plus = minus = zero = 0
    for num in arr:
        if num > 0:
            plus += 1
        elif num < 0:
            minus += 1
        else:
            zero += 1
    length = len(arr)
    print(plus / length)
    print(minus / length)
    print(zero / length)

    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
