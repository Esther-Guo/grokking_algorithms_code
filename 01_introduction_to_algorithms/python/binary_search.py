def binary_search(low,high,lst,num):
    mid = int((low+high)/2)
    if high-low<0:
        return None
    if lst[mid]>num:
        high = mid-1
    elif lst[mid]<num:
        low = mid+1
    else:
        pos = mid
        return pos
    pos = binary_search(low,high,lst,num)
    return pos
lst = [1,2,5,6,8,9,10,12,14,15,16,18,19]
n = len(lst)
low = 0
high = n-1
num = 21
#pos = binary_search(low,high,lst,num)
print(binary_search(low,high,lst,num))