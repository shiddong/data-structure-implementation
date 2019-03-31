# coding:utf-8

"""
栈结构的实现

栈具有的操作：
    Stack() 创建一个新的空栈
    push(item) 向栈顶压入一个元素
    pop() 弹出栈顶元素
    peek() 返回栈顶元素
    is_empty() 判断栈是否为空
    size() 返回栈的元素个数
"""


class Stack():
    """栈结构"""

    def __init__(self):
        # 私有成员
        self.__list = []

    def push(self, item):
        """添加一个元素item到栈顶"""
        self.__list.append(item)    # 添加到列表尾部的时间复杂度为O(1)，添加到头部的时间复杂度为O(n)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        return None

    def is_empty(self):
        """判断栈顶元素是否为空"""
        # return self.__list == []
        return not self.__list

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print(s.is_empty())
    print(s.peek())
    print(s.size())

    print(s.pop())
    print(s.pop())
    print(s.pop())

    print(s.is_empty())
    print(s.peek())
    print(s.size())
