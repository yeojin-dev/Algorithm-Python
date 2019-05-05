#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    formating = '%a %d %b %Y %H:%M:%S %z'
    delta = int((datetime.strptime(t1, formating) - datetime.strptime(t2, formating)).total_seconds())
    return abs(delta)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()
