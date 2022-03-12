#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def partition(values, low, high):
    pivot = values[high]
    i = low - 1 
    for j in range(low, high):
        if values[j] < pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
    
    values[i+1], values[high] = values[high], values[i+1]
    return i + 1

def quick_sort(values, low, high):
    if low < high:
        idx_pivot = partition(values, low, high)
        quick_sort(values, low, idx_pivot-1)
        quick_sort(values, idx_pivot+1, high)
    return values

arr = [3, 55, 2, 667, 4, 1, 99, 65, 45]
print(quick_sort(arr, 0, len(arr)-1))
