def bubble(list_a):
    #We have to set an indexing length, if we access the last index we will throw an out of range error
    indexing_length = len(list_a) - 1
    #We use this variable in the control flow to break out of the loop when the list is sorted
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
    return list_a

print(bubble([3,6,32,6,7,1,4,3,6,7,8,34,6,324]))
