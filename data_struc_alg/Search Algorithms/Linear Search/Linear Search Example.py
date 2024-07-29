def linear_search(arr, target_val):
    for i in range(len(arr)):
        if arr[i] == target_val:
            return i
    return -1

arr = [3,6,6,43,2,1,2,4,5,6244,856,6534234,7645,456,74,324,763,456,2,4]
target_value = 43
result = linear_search(arr, target_value)

if result != -1:
    print("Value",target_value, "found at index ", result )
else:
    print("Value",target_value,"not found")