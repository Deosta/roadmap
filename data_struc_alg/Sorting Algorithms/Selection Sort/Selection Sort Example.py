def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_min_inx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_min_inx]:
                cur_min_inx = j
        arr[i], arr[cur_min_inx] = arr[cur_min_inx], arr[i]
    return arr

print(selection_sort([5,23,663,2,32,673,6422,4]))
