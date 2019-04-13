# coding:utf-8


class Node(object):
    """
    定义节点
    """
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """
    二叉树
    """
    def __init__(self):
        self.root = None

    def add(self, item):
        """使用队列实现/层次遍历"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.lchild is None:
                curr_node.lchild = node
                return
            else:
                queue.append(curr_node.lchild)
            if curr_node.rchild is None:
                curr_node.rchild = node
                return
            else:
                queue.append(curr_node.rchild)

    def breath_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            print(curr_node.elem, end=" ")
            if curr_node.lchild is not None:
                queue.append(curr_node.lchild)
            if curr_node.rchild is not None:
                queue.append(curr_node.rchild)

    def pre_order(self, node):
        """先序遍历: 根 左 右（递归实现）"""
        if node is None:
            return
        print(node.elem, end=" ")
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, node):
        """中序遍历: 左 根 右（递归实现）"""
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.elem, end=" ")
        self.in_order(node.rchild)

    def post_order(self, node):
        """后序遍历: 左 右 根（递归实现）"""
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem, end=" ")

if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.add(10)
    tree.breath_travel()
    print(" ")
    tree.pre_order(tree.root)
    print(" ")
    tree.in_order(tree.root)
    print(" ")
    tree.post_order(tree.root)
