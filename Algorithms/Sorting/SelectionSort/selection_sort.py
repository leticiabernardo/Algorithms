#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def selection_sort(arr):
    i = 0
    while i < len(arr) - 1:
        pivot = arr[i]
        
        j = i + 1
        while j < len(arr):
            if pivot > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                break
            j += 1

        if len(arr) - 1 == j:
            i += 1
        

arr = [3, 8, 5, 4, 89, 54, 2]
selection_sort(arr)
print(arr)
