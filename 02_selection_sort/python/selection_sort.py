def findSmallest(lst):
    min = 9999
    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
    return min

lst = [3,5,2,6,9,9,10]
sorted_lst = []
while(len(lst)):
    min = findSmallest(lst)
    sorted_lst.append(min)
    lst.remove(min)
print(sorted_lst)