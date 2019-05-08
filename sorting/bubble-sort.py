# coding:utf-8


def bubble_sort(alist):
    """
    冒泡排序
    先描述内部循环，再描述外部循环
    """
    for n in range(0, len(alist) - 1):
        count = 0
        for i in range(0, len(alist) - n - 1):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
            # 使用count优化，在没有交换时表示已经处于已排序状态
            if count == 0:
                return

def bubble(lis):
    for i in range(len(lis) - 1, 0, -1):
        switch_count = 0
        for j in range(0, i - 1):
            if lis[j] > lis[j+1]:
                switch_count += 1
                lis[j], lis[j+1] = lis[j+1], lis[j]
        if switch_count == 0:
            return


if __name__ == "__main__":
    lis = [54, 26, 101, 93, 23, 34, 1010]
    #bubble_sort(lis)
    bubble(lis)
    print(lis)

