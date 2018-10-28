#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    letter_dict = dict()
    for letter in s:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
            
    frequencies = list(letter_dict.values())
    frequency_set = set(frequencies)

    max_freq = max(frequencies)
    min_freq = min(frequencies)

    if (max_freq == min_freq
            or (max_freq - min_freq == 1 and frequencies.count(max_freq) == 1)
            or (min_freq == 1 and frequencies.count(min_freq) == 1 and len(set(frequencies)) == 2)):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
