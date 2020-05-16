#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=0
    v=0
    for ele in s:
        if ele=='U':
            level+=1
        if ele=='D':
            level-=1
        if (level==0 and ele=='U'):
            v+=1
    return(v)
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 12 #8#int(input())

    s = 'DDUUDDUDUUUD' #'UDDDUDUU'#input()

    result = countingValleys(n, s)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
