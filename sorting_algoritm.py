def linear_search(list, element):
    n = len(list)
    for i in range(0, n):
        if list[i] == element:
            return i
    return -1


def binary_search(list,start,end,element):
    if end>=start:
        mid=(start+end)//2
        if list[mid]==element:
            return mid
        elif list[mid]>element:
            return binary_search(list,start,mid-1,element)
        elif list[mid]<element:
            return binary_search(list,mid+1,end,element)
    else:
        return -1


list = [1, 4, 7, 45, 98, 987, 1234, 7654]

mid = len(list) // 2

search_element = 45

print(binary_search(list, 0, len(list), search_element))
print(linear_search(list, search_element))
# if element is present in the list then return index of that element else return -1
