def findLeft(lst,num):
    left = []
    for i in range(1,len(lst)):
        if lst[i]<=num:
            left.append(lst[i])
    return left

def findRight(lst,num):
    right = []
    for i in range(1,len(lst)):
        if lst[i]>num:
            right.append(lst[i])
    return right

def quicksort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    # no need 2 lines below 
    # elif len(lst) == 2:
    #     return lst if lst[0]<lst[1] else lst[::-1]
    num = lst[0]
    left = findLeft(lst,num) # see sample code which simplifies this func
    right = findRight(lst,num)
    
    return quicksort(left)+[num]+quicksort(right)

print(quicksort([1,9,2,8,7,4,9,9]))