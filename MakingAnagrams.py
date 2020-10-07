#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    freq = dict()
    count = 0
    for char in a:
        if char in freq:
            freq[char]+=1
            count +=1
        else:
            freq[char]=1
            count +=1
        
    for char in b:
        if char in freq:
            freq[char]-=1
            if freq[char]==0:
                freq.pop(char)
            count-=1
        else:
            count+=1            
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
