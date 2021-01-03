# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:13:19 2020

@author: anees
"""

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

def iterative_binary_search(data, target):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1
            
        return False
    
def binary_search(data, target):
    mid = len(data) // 2
    if target == data[mid]:
        return True
    elif len(data) <= 1:
        return False
    elif target < data[mid]:
        return binary_search(data[:mid], target)
    elif target > data[mid]:
        return binary_search(data[mid:], target)
    
        
hi = binary_search([1,2,4,5,6,7], 8)
print(hi)        
    