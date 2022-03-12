#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, low, high):
    pivot = arr[low]
    (i, j) = (low-1, high+1)
 
    while True:
        while True:
            i += 1
            if arr[i] >= pivot:
                break
        while True:
            j -= 1
            if arr[j] <= pivot:
                break
 
        if i >= j:
            return j
        swap(arr, i, j)


def quicksort(arr, low, high):
    if low >= high:
        return
    pivot = partition(arr, low, high)

    quicksort(arr, low, pivot)
    quicksort(arr, pivot+1, high)

 
arr = [3, 55, 2, 667, 4, 1, 99, 65, 45]
quicksort(arr, 0, len(arr)-1)
print(arr)
