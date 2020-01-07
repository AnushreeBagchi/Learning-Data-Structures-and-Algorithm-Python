class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_element = 0
    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.num_element += 1
    def pop(self):
        if self.head is None:
            return None
        value =  self.head.value
        self.head = self.head.next
        self.num_element -=1
        return value
    def size(self):
        return self.num_element
    def is_empty(self):
        return self.num_element == 0
    def top(self):
        return self.head.value

def reverseStack(stack):
    new_stack = Stack()
    for e in range(stack.size()):
        poped_element = stack.pop()
        new_stack.push(poped_element)
    return new_stack

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack2 = reverseStack(stack1)


