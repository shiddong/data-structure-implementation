
# coding:utf-8
"""
循环单链表的操作（与单链表一致）

is_empty() 判断链表是否为空
length() 返回链表长度
travel() 遍历整个链表
add(item) 在链表头部添加元素
append(item) 在链表的尾部添加元素
insert(pos, item) 在指定位置插入元素
remove(item) 删除节点
search(item) 查找节点是否存在
"""


class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SinglyCycleLinkedList(object):
    """循环单链表"""
    def __init__(self, node=None):
        self._head = node
        # 判空，有头节点时需要将其next域指向自身
        if node:
            self._head.next = self._head

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """返回链表长度"""
        if self.is_empty():
            return 0
        curr = self._head
        length = 1   # 定义一个游标，用来移动遍历节点
        while curr.next != self._head:
            length += 1
            curr = curr.next
        return length

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        curr = self._head
        while curr.next != self._head:
            print(curr.elem, end=" ")
            curr = curr.next
        # 退出循环时，curr指向尾节点，但curr.next指向头节点，没有在循环体中打印尾节点的数据
        # 需要单独打印出尾节点的数据
        print(curr.elem)

    def add(self, item):
        """在链表头部添加元素 -> 头插法"""
        # 方案一，先遍历找到尾节点再处理
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            curr = self._head
            while curr.next != self._head:
                curr = curr.next
            # 退出循环，curr指向尾节点
            node.next = self._head
            self._head = node
            curr.next = self._head
        # 方案一，先在头部插入构造的node节点，之后不需要判断空链表的特殊情况
        # node = Node(item)
        # node.next = self._head
        # self._head = node
        # curr = node.next
        # while curr and curr.next != node.next:
        #     curr = curr.next
        # curr.next = node

    def append(self, item):
        """在链表的尾部添加元素 -> 尾插法"""
        node = Node(item)   # 根据数据元素构造节点
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            curr = self._head
            while curr.next != self._head:
               curr = curr.next
            node.next = curr.next
            curr.next = node

    def insert(self, pos, item):
        """
        在指定位置插入元素
        :param pos: (从0开始索引)
        :param item: 数据元素
        :return: None
        """
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            # 与单链表的逻辑一致
            pre = self._head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        # 可以使用两个游标pre和curr搜索，也可以只使用一个游标pre
        if self.is_empty():
            return
        pre, curr = None, self._head
        while curr.next != self._head:
            if curr.elem == item:
                # 先判断此节点是否为头节点
                if curr == self._head:
                    # 对于头节点，需要找到尾节点，改变其next域
                    # self._head = curr.next
                    rear = self._head
                    while rear.next != self._head:
                        rear = rear.next
                    # 退出循环，找到尾部
                    self._head = curr.next
                    rear.next = self._head
                else:
                    # 能够处理中间节点
                    pre.next = curr.next
                # 不再是break
                return
            else:
                pre = curr
                curr = curr.next
        # 退出循环，即找到尾节点，需要单独判断
        if curr.elem == item:
            if curr == self._head:
                # 链表只有一个节点, pre为None
                self._head = None
            else:
                pre.next = curr.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        curr = self._head
        while curr.next != self._head:
            if curr.elem == item:
                return True
            else:
                curr = curr.next
        # 单独处理尾节点
        if curr.elem == item:
            return True
        return False


if __name__ == '__main__':
    singly_cycle_linked_list = SinglyCycleLinkedList()
    print(singly_cycle_linked_list.is_empty())  # True
    print(singly_cycle_linked_list.length())  # 0

    singly_cycle_linked_list.append(10)
    singly_cycle_linked_list.add(-10)
    singly_cycle_linked_list.append(20)
    singly_cycle_linked_list.travel()  # -10 10 20
    singly_cycle_linked_list.insert(-1, 100)
    singly_cycle_linked_list.travel()  # 100 -10 10 20
    singly_cycle_linked_list.append(30)
    singly_cycle_linked_list.travel()  # 100 -10 10 20 30
    singly_cycle_linked_list.insert(3, 200)
    singly_cycle_linked_list.travel()  # 100 -10 10 200 20 30
    singly_cycle_linked_list.insert(6, 300)
    print(singly_cycle_linked_list.is_empty())  # False
    print(singly_cycle_linked_list.length())  # 7
    singly_cycle_linked_list.travel()  # 100 -10 10 200 20 30 300

    print(singly_cycle_linked_list.search(100))  # True
    print(singly_cycle_linked_list.search(500))  # False

    singly_cycle_linked_list.remove(100)
    singly_cycle_linked_list.travel()  # -10 10 200 20 30 300
    singly_cycle_linked_list.remove(10)
    singly_cycle_linked_list.travel()  # -10 200 20 30 300
    singly_cycle_linked_list.remove(300)
    singly_cycle_linked_list.travel()  # -10 200 20 30
