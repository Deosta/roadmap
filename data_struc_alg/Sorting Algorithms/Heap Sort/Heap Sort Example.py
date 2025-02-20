def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def sift_down(lst, i, upper):
    while (True):
        l, r = i*2+1, i*2+2
        if max(l,r) < upper:
            if lst[i] >= max(lst[l], lst[r]):
                break
            elif lst[l] > lst[r]:
                swap(lst, i, l)
                i = l
            else:
                swap(lst, i , r)
                i = r
        elif l < upper:
            if lst[l] > lst[i]:
                swap(lst, i ,l)
                i = l
            else:
                break
        elif r < upper:
            if lst[r] > lst[i]:
                swap(lst,i,r)
                i = r
            else:
                break
        else:
            break

def heapsort(lst):
    for j in range(len(lst)-2//2, -1, -1):
        sift_down(lst, j, len(lst))
    
    for end in range(len(lst)-1, 0, -1):
        swap(lst, 0, end)
        sift_down(lst, 0, end)

lst = [5,16,8,14,20,63,6743,23,2]
heapsort(lst)
print(lst)