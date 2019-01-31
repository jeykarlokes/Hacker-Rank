#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    
    current_level = 0
    valley_count  = 0

    for direction in s:
        if direction == 'U':
            current_level += 1
        elif direction == 'D':
            current_level -= 1
        if current_level == 0 and direction == 'U':
            valley_count += 1
    
    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')ey_count

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
