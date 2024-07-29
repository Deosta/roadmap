#left and right are indexes that determine the part of the array that we want to sort. At the start, we want to sort the whole array so left = 0 and right = len(array)
def quick_sort(arr, left, right):
    #if the len of the subarray to sort is 1, we don't do anything with that array. if left is less than right, the sub array contains 2 or more elements.
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)
    return arr

#returns the index of the pivot element after the first iteration of quicksort
def partition(arr, left, right):
    i = left
    j = right -1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i

arr = [3,73,4,2,12,66,4,32,63546,23,1]
print(quick_sort(arr, 0, len(arr) -1))