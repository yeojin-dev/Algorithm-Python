#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    time_strings = s.split(':')
    hour = int(time_strings[0])
    if time_strings[2][2:] == 'PM' and hour != 12:
        time_strings[0] = str(int(time_strings[0]) + 12)
    elif time_strings[2][2:] == 'AM' and hour == 12:
        time_strings[0] = '00'
    time_strings[2] = time_strings[2][:2]
    return ':'.join(time_strings)    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
