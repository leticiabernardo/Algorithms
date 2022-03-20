#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insertion_sort(arr):
    for i in range(1, len(arr)):
        aux = arr[i]
        j = i
        while j > 0 and aux < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = aux
    return arr

arr = [66, 5, 9 , 1, 2, 8, 15, 5455, 42]
print(insertion_sort(arr))
