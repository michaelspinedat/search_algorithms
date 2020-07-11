#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:37:13 2020

@author: michael
"""

import math

"""
code to linearly search.  
Returns either the index of the location in the array,
or -1 if the array did not contain the targetValue
"""
def linear_search(numbers, target):
    for index in range(0, len(numbers)):
        if numbers[index] == target:
            return index
    return -1

"""
Iterative Binary Search Function 
Returns either the index of the location in the array,
or -1 if the array did not contain the targetValue
"""

def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1
    
    while low <= high:
        index = math.floor((low + high) / 2)
        if numbers[index] == target:
            return index
        elif numbers[index] < target:
            low = index + 1            
        else:
            high = index - 1
    return -1

primes = [2, 3, 5, 7, 11, 13, 17, 
          19, 23, 29, 31, 37, 41, 
          43, 47, 53, 59, 61, 67, 
          71, 73, 79, 83, 89, 97]

print(linear_search(primes, 97))
print(binary_search(primes, 41))
