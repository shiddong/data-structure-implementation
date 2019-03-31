"""
双链表的操作(操作基本上同单链表)：
is_empty() 判断链表是否为空
length() 返回链表的长度
travel() 遍历链表
add(item) 在链表的头部添加元素item
append(item) 在链表的尾部添加元素
insert(pos, item) 在指定位置添加
remove() 删除指定元素的节点
search(item) 查找节点是否存在

只有对链表进行添加/删除操作时与单链表有所不同，需要处理指向前驱节点的指针
所以，可以直接继承单链表的实现类SinglyLinkedList
"""


class Node(object):
    """双链表的节点定义"""
    def __init__(self, item):
        self.elem = item
        self.prev = None
        self.next = None


class DoubleLinedList(object):
    """双链表"""
    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """返回链表长度"""
        curr, length = self._head, 0   # 定义一个游标，用来移动遍历节点
        # while curr != None:
        while curr:
            length += 1
            curr = curr.next
        return length

    def travel(self):
        """遍历整个链表"""
        curr = self._head
        while curr:
            print(curr.elem, end=" ")
            curr = curr.next
        print("")

    def add(self, item):
        """在链表头部添加元素 -> 头插法"""
        node = Node(item)
        # 处理next，同单链表
        node.next = self._head
        self._head = node
        # 处理prev
        node.next.prev = node
        # node.prev = None  # 创建Node时(初始状态)已经为None了

    def append(self, item):
        """在链表的尾部添加元素 -> 尾插法"""
        node = Node(item)   # 根据数据元素构造节点
        if self.is_empty():
            self._head = node
        else:
            curr = self._head
            while curr.next:
                curr = curr.next
            curr.next = node
            node.prev = curr    # 需要多处理一个prev

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
            # 对于双向链表与单链表的不同之处在于它可以使用curr节点，直接遍历到pos位置
            # 而不用遍历到pos前一个位置
            curr = self._head
            count = 0
            # 找到当前的pos位置的节点，然后在该节点之前插入node节点
            while count < pos:
                count += 1
                curr = curr.next
            node = Node(item)
            # 处理next
            curr.prev.next = node
            node.next = curr
            # 处理prev
            node.prev = curr.prev
            curr.prev = node

    def remove(self, item):
        """删除节点"""
        # 此时只需要一个curr游标即可
        curr = self._head
        while curr:
            if curr.elem == item:
                if curr == self._head:
                    self._head = curr.next
                    # 判断链表是否只有一个节点
                    if curr.next:
                        curr.next.prev = None
                else:
                    curr.prev.next = curr.next
                    # 判断是否为最后一个节点
                    if curr.next:
                        curr.next.prev = curr.prev
                break
            else:
                curr = curr.next

    def search(self, item):
        """查找节点是否存在"""
        curr = self._head
        while curr:
            if curr.elem == item:
                return True
            else:
                curr = curr.next
        return False


if __name__ == '__main__':
    double_linked_list = DoubleLinedList()
    print(double_linked_list.is_empty())    # True
    print(double_linked_list.length())      # 0

    double_linked_list.append(10)
    double_linked_list.add(-10)
    double_linked_list.append(20)
    double_linked_list.travel()         # -10 10 20
    double_linked_list.insert(-1, 100)
    double_linked_list.travel()         # 100 -10 10 20
    double_linked_list.append(30)
    double_linked_list.travel()         # 100 -10 10 20 30
    double_linked_list.insert(3, 200)
    double_linked_list.travel()         # 100 -10 10 200 20 30
    double_linked_list.insert(6, 300)
    print(double_linked_list.is_empty())        # False
    print(double_linked_list.length())          # 7
    double_linked_list.travel()                 # 100 -10 10 200 20 30 300

    print(double_linked_list.search(100))  # True
    print(double_linked_list.search(500))  # False

    double_linked_list.remove(100)
    double_linked_list.travel()         # -10 10 200 20 30 300
    double_linked_list.remove(10)
    double_linked_list.travel()         # -10 200 20 30 300
    double_linked_list.remove(300)
    double_linked_list.travel()         # -10 200 20 30
