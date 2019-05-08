#coding:utf-8


def selection_sort(alist):
    """选择排序"""
    for i in range(0, len(alist) - 1):
        min_index = i
        # 选择
        for j in range(i + 1, len(alist)):
            if alist[min_index] > alist[j]:
                min_index = j
        # 交换
        alist[i], alist[min_index] = alist[min_index], alist[i]


if __name__ == "__main__":
    lis = [31, 17, 77, 20, 93]
    selection_sort(lis)
    print(lis)

