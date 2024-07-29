def insertion_sort(arr):
    if len(arr) > 1:
        for i in range(1, len(arr)):
            j = i #inner loop that starts at the index of the outer loop.
            while arr[j-1] > arr[j] and j > 0:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
    return arr

print(insertion_sort([1,5,2,4,78,8,3,4,2,9]))