#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# recursive
def binary_search(arr, start, end, query):
    i = (start + end) // 2
    
    if start > end:
        return -1
    
    if arr[i] == query:
        return i
    
    if arr[i] < query:
        return binary_search(arr, i+1, end, query)
    else:
        return binary_search(arr, start, i-1, query)


# iterative
def iter_binary_search(arr, query):
    start = 0
    end = len(arr) - 1

    while start < end:
        i = (start + end) // 2

        if arr[i] == query:
            return i
        
        if arr[i] < query:
            start = i + 1
        else:
            end = i
    return -1


arr = [1, 3, 99, 565, 789, 5212]

# recursive
query = 99
index = binary_search(arr, 0, len(arr)-1, query)
if index >= 0:
    print(f'Found query {arr[index]} at index {index}')
else:
    print("Item not found")


# iterative
query = 565
index = iter_binary_search(arr, query)
if index >= 0:
    print(f'Found query {arr[index]} at index {index}')
else:
    print("Item not found")
