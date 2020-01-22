# post-order traversal

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

class State:
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
    def get_node(self):
        return self.node
    def get_visited_left(self):
        return self.visited_left
    def get_visited_right(self):
        return self.visited_right
    def set_visited_left(self):
        self.visited_left = True
    def set_visited_right(self):
        self.visited_right = True


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

class Stack:
    def __init__(self):
        self.list = list()
    def push(self, value):
        self.list.append(value)
    def pop(self):
        return self.list.pop()
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
    def is_empty(self):
        return len(self.list) == 0

     
def pre_order_traversal_with_stack(tree):
    stack = Stack()
    visit_order = list()
    node = tree.get_root()
    state = State(node)
    stack.push(state)
    visit_order.append(node.get_value())
    count = 0
    while (node):
        count+=1  
        if node.has_left_child() and not state.get_visited_left():
            state.set_visited_left()
            node = node.get_left_child()
            state = State(node)
            stack.push(state)
            visit_order.append(node.get_value())
        elif node.has_right_child() and not state.get_visited_right():
            state.set_visited_right()
            node = node.get_right_child()
            state = State(node)
            stack.push(state)
            visit_order.append(node.get_value())
        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None
    return visit_order
def pre_order_traversal_with_recursion(tree):
    node = tree.get_root()
    visit_order = list()
    def traverse(node):
        if node:
            # visit
            visit_order.append(node.get_value())
            # traverse left
            traverse(node.get_left_child())
            # traverse right
            traverse(node.get_right_child())
    traverse(node)
    return visit_order
def inorder_traversal_with_recursion(tree):
    node = tree.get_root()
    visit_order = list()
    def traverse(node):
        if node:
            # traverse left
            traverse(node.get_left_child())
            # visit
            visit_order.append(node.get_value())
            # traverse right
            traverse(node.get_right_child())
    traverse(node)
    return visit_order
def post_order_traversal_with_recusrion(tree):
    node = tree.get_root()
    visit_order = list()
    def traversal(node):
        if node:
            # traverse left
            traversal(node.get_left_child())
            # traverse right
            traversal(node.get_right_child())
            # visit
            visit_order.append(node.get_value())
    traversal(node)
    return visit_order


print(post_order_traversal_with_recusrion(tree))




