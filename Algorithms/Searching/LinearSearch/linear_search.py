#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def linear_search(arr, query):
    for i, val in enumerate(arr):
        if val == query:
            return i
    return -1

arr = [3, 6, 588, 5, 22, 1, 9]
query = 5

index = linear_search(arr, query)
if (index >= 0):
    print(f'Found item {arr[index]} at index {index}')
else:
    print("Item not found")
