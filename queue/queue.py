# coding:utf-8
"""
队列具有的操作：
    Queue() 创建一个空的队列
    enqueue(item) 往队列中添加一个item元素
    dequeue() 从队列头部删除一个元素
    is_empty() 判断队列是否为空
    size() 返回队列的大小

说明：
使用列表实现队列，无论是在尾部入队、头部出队，还是在头部入队、尾部出队，
都会存在时间复杂度一个为O(1),另一个为O(n)的情况，所以这时应该根据入队还是出队的操作频繁度选择合适的方式
"""


class Queue():
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """往队列中添加一个item元素"""
        # self.__list.insert(0, item)
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)
        # return self.__list.pop()

    def is_empty(self):
        """判断队列是否为空"""
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(q.is_empty())
    print(q.size())

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

    print(q.is_empty())
    print(q.size())
