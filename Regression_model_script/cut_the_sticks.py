#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(sticks, index):
    answer_set = []
    
    answer_set.append(index)
    
    end = False
    x = 0
    while(not end):
        cut_to_make = 0
        smallest = 1001
        for stick in sticks:
            if stick != 0 and smallest > stick:
                smallest = stick

        for index in range(0,len(sticks)):
            if sticks[index] > 0:
                sticks[index] = sticks[index] - smallest
            if sticks[index] > 0:
                cut_to_make += 1
                
                
        if cut_to_make == 0:
            end = True
        else:
            answer_set.append(cut_to_make)
            

            
    return answer_set

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr, n)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
