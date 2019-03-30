# coding:utf-8
'''
游标
'''

class Node(object):
    '''节点'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SinglyLinkedList(object):
    '''单链表'''
    def __init__(self, node = None):
        self._head = node

    def is_empty(self):
        '''判断链表是否为空'''
        return self._head == None

    def length(self):
        '''返回链表长度'''
        curr, length = self._head, 0   # 定义一个游标，用来移动遍历节点
        # while curr != None:
        while curr:
            length += 1
            curr = curr.next
        return length

    def travel(self):
        '''遍历整个链表'''
        curr = self._head
        while curr:
            print(curr.elem, end=" ")
            curr = curr.next
        print("")

    def add(self, item):
        '''在链表头部添加元素 -> 头插法'''
        node = Node(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        '''在链表的尾部添加元素 -> 尾插法'''
        node = Node(item)   # 根据数据元素构造节点
        if self.is_empty():
            self._head = node
        else:
            curr = self._head
            while curr.next:
               curr = curr.next
            curr.next = node

    def insert(self, pos, item):
        '''
        在指定位置插入元素
        :param pos: (从0开始索引)
        :param item: 数据元素
        :return: None
        '''
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            pre = self._head
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        '''删除节点'''
        # 可以使用两个游标pre和curr搜索，也可以只使用一个游标pre
        pre, curr = None, self._head
        while curr:
            if curr.elem == item:
                # 先判断此节点是否为头节点
                if curr == self._head:
                    self._head = curr.next
                else:
                    pre.next = curr.next
                break
            else:
                pre = curr
                curr = curr.next

    def search(self, item):
        '''查找节点是否存在'''
        curr = self._head
        while curr:
            if curr.elem == item:
                return True
            else:
                curr = curr.next
        return False

if __name__ == '__main__':
    singly_linked_list = SinglyLinkedList()
    print(singly_linked_list.is_empty())
    print(singly_linked_list.length())

    singly_linked_list.append(10)
    singly_linked_list.add(-10)
    singly_linked_list.append(20)
    singly_linked_list.insert(-1, 100)
    singly_linked_list.append(30)
    singly_linked_list.insert(3, 200)
    singly_linked_list.insert(6, 300)
    print(singly_linked_list.is_empty())
    print(singly_linked_list.length())
    singly_linked_list.travel()

    print(singly_linked_list.search(100))   # True
    print(singly_linked_list.search(500))   # False

    singly_linked_list.remove((100))
    singly_linked_list.travel()
    singly_linked_list.remove(10)
    singly_linked_list.travel()
    singly_linked_list.remove(300)
    singly_linked_list.travel()