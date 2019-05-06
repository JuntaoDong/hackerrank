#!/bin/python3

import os
import sys

def timeConversion(s):
    mark = s[-2:]
    time = s[:-2]
    if mark == 'AM':
        if time[:2] == '12':
            return '00'+time[2:]
        return time
    else:
        if time[:2] == '12':
            return time
        return str(int(time[:2])+12)+time[2:]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
