#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def order_numbers(arr):
    return

def radix_sort(arr):
    max_number = max(arr)
    measure = 1

    i = 0
    while i < len(str(max_number)):
        for i, _ in enumerate(arr):
            print(arr[i]//measure % 10)

        measure *= 10
        i += 1


arr = [7, 4, 15, 10, 9, 2]
radix_sort(arr)
print(arr)