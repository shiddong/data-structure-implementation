# coding:utf-8


def quick_sort(alist, first, last):
    if first >= last:
        return
    pivot_value = alist[first]
    low, high = first, last
    while low < high:
        # high左移
        while low < high and alist[high] >= pivot_value:
            high -= 1
        alist[low] = alist[high]

        # low右移
        while low < high and alist[low] < pivot_value:
            low += 1
        alist[high] = alist[low]

    # 退出循环时low==high
    alist[low] = pivot_value
    # 对左端数列排序
    quick_sort(alist, first, low - 1)
    # 对右端数列排序
    quick_sort(alist, low + 1, last)

lis = [31, 17, 77, 20, 93, 101, 110, 102, 104,1010, 999,23]
quick_sort(lis, 0, len(lis)-1)
print(lis)