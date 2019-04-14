#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    return sorted(reversed(list(set(arr))), key=arr.count)[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
