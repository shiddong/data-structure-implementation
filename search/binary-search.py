# coding: utf-8


def binary_search(alist, item):
    def __binary_search(alist, first, last):
        if first >= last:
            return -1
        mid = (first + last) // 2
        if alist[mid] > item:
            return __binary_search(alist, first, mid-1)
        elif alist[mid] < item:
            return __binary_search(alist, mid+1, last)
        else:
            return mid

    return __binary_search(alist, 0, len(alist) - 1)


lis = [1, 3, 5, 6, 7, 10, 23, 32, 45, 50]
pos = binary_search(lis, 45)
print(pos)
