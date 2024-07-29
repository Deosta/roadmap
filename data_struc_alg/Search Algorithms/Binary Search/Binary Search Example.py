def binary_search(arr, target_val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target_val:
            return mid
        
        if arr[mid] < target_val:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

my_arr = ([3,52,4,5,6,77,3,5,5,433,22,5,3,2,7,8,9,3,45,6,43,53])
my_arr.sort()

my_target = 77

result = binary_search(my_arr, my_target)

if result != -1:
    print("Value",my_target,"found at index", result)
else:
    print("Target not found in array.")