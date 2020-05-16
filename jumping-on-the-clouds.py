#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps=0
    i=0
    j=len(c)
    while i<j:
        if c[i]==0:
            if i<j-2 and c[i+2]==0:
                i+=2
            elif i<j-1 and c[i+1]==0:
                i+=0
            i+=1
            jumps+=1
        else:
            break
    return jumps

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 7 # int(input())

    c = [0,0,1,0,0,1,0] # list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    
    print(result)
    #assert result==4
    #fptr.write(str(result) + '\n')

    #fptr.close()
