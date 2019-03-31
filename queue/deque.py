"""
双端队列的操作

Deque() 创建一个空的双端队列
add_front(item) 从队头加入一个item元素
add_rear(item) 从队尾加入一个item元素
remove_front() 从队头删除一个元素
remove_rear() 从队尾删除一个元素
is_empty() 判断双端队列是否为空
size() 返回双端队列的大小

说明：
基本实现同队列
将list的头尾顺序对应双端队列的头尾
"""


class Deque():
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """从队头加入一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """从队尾加入一个item元素"""
        self.__list.append(item)

    def remove_front(self):
        """从队头删除一个元素"""
        return self.__list.pop(0)

    def remove_rear(self):
        """从队尾删除一个元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断双端队列是否为空"""
        return self.__list == []

    def size(self):
        """返回双端队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    q = Deque()
    q.add_front(10)
    q.add_rear(20)
    q.add_front(30)
    q.add_rear(40)

    print(q.is_empty())
    print(q.size())

    print(q.remove_front())
    print(q.remove_rear())

    print(q.is_empty())
    print(q.size())
