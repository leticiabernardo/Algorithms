#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def shell_sort(arr):
    arr_size = len(arr)
    interval = arr_size // 2
    while interval > 0:
        j = interval
        while j < arr_size:
            aux = arr[j]
            k = j
            while k >= interval and aux < arr[k-interval]:
                arr[k] = arr[k-interval]
                k -= interval

            arr[k] = aux
            j += 1
        interval //= 2


arr = [7, 4, 15, 10, 9, 2]
shell_sort(arr)
print(arr)
