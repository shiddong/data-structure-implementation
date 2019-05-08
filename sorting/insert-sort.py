# coding:utf-8


def insert_sort(alist):
    """插入排序"""
    for i in range(1, len(alist)):
        j = i
        while j > 0:
            if alist[j] > alist[j-1]:
                break
            alist[j], alist[j-1] = alist[j-1], alist[j]
            j -= 1


if __name__ == "__main__":
    lis = [31, 17, 77, 20, 93]
    insert_sort(lis)
    print(lis)
