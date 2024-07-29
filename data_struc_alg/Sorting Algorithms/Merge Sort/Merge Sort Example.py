def merge_sort(list_a):
    #if the len of the list is 1, we don't need to split it any further
    if len(list_a) > 1:
        left_list = list_a[:len(list_a)//2]
        right_list = list_a[len(list_a)//2:]


        #recursive work
        merge_sort(left_list)
        merge_sort(right_list)



        #merging work
        i = 0 #left_list index
        j = 0 #right_list index
        k = 0 #merged array index
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list_a[k] = left_list[i]
                i += 1
            else:
                list_a[k] = right_list[j]
                j += 1
            k += 1
        
        while i < len(left_list):
            list_a[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list_a[k] = right_list[j]
            j += 1
            k += 1
    return list_a

print(merge_sort([4,2123,566,32,1]))
