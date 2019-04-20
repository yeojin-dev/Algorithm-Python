#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for __ in range(t):

        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        if k < (n // 2):
            result = k * 2 + 1
        else:
            result = (n - k - 1) * 2

        print(result)
