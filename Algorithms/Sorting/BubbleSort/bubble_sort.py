#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def bubble_sort(arr):
    length = len(arr)

    for i in range(length):
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

test = [2, 7, 99, 40, 23, 27, 44, 678, 33, 8, 5]

print(bubble_sort(test))
