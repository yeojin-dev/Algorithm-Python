#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    divisors = [x for x in range(1, n + 1) if n % x == 0]
    max_digit_sum = 0
    best = n
    for divisor in divisors:
        digit_sum = sum(int(n) for n in str(divisor))
        if max_digit_sum < digit_sum:
            max_digit_sum = digit_sum
            best = divisor
        elif max_digit_sum == digit_sum:
            if divisor < best:
                best = divisor
        else:
            continue
    print(best)
