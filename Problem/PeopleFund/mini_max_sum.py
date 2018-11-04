#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_value = min(arr)
    max_value = max(arr)
    sum = 0
    for num in arr:
        sum += num
    print('{} {}'.format(sum - max_value, sum - min_value))

    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
