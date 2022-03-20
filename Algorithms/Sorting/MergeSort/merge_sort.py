def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]
        mergeSort(left)
        mergeSort(right)
  
        i = 0
        j = 0
        aux = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[aux] = left[i]
                i += 1
            else:
                arr[aux] = right[j]
                j += 1
            aux += 1
  
        while i < len(left):
            arr[aux] = left[i]
            i += 1
            aux += 1
  
        while j < len(right):
            arr[aux] = right[j]
            j += 1
            aux += 1


if __name__ == '__main__':
    arr = [66, 5, 9 , 1, 2, 8, 15, 42]
    mergeSort(arr)
    print(arr)
