#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max = min = scores[0]
    max_change = min_change = 0
    for score in scores[1:]:
        if score > max:
            max = score
            max_change += 1
        elif score < min:
            min = score
            min_change += 1            
    return [max_change, min_change]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

