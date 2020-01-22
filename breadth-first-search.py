from collections import deque
class Node:
    def __init__(self,value=None):
        self.value = value
        self.right = None
        self.left = None
    def set_value(self, value=None):
        self.value = value
    def get_value(self):
        return self.value
    def get_right_child(self):
        return self.right
    def get_left_child(self):
        return self.left
    def set_left_child(self, value):
        self.left = value
    def set_right_child(self, value):
        self.right = value
    def has_left_child(self):
        return self.left != None
    def has_right_child(self):
        return self.right != None

class Tree:
    def __init__(self, value=None):
        self.root = Node(value)
    def get_root(self):
        return self.root

class Queue:
    def __init__(self):
        self.q= deque()
    def enq(self, value):
        self.q.appendleft(value)
    def deq(self):
        return self.q.pop()
    def length(self):
        return len(self.q)
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

visit_order = list()
q = Queue()

node = tree.get_root()
q.enq(node)
while q.length()> 0:
    node = q.deq()
    visit_order.append(node.value)

    if node.has_left_child():
        q.enq(node.get_left_child())
    if node.has_right_child():
        q.enq(node.get_right_child())


print(visit_order)