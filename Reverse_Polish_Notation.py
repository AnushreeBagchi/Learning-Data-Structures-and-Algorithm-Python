class Node:
    def __init__(self, value):
        self.value =  value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0
    def push(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1
    def pop(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        self.num_elements -=1
        return value
    def size(self):
        return self.num_elements
    def is_empty(self):
        return self.num_elements == 0
    def top(self):
        if self.head is None: 
            return None
        return self.head.value

def evaluate_post_fix(input_list):
    stack = Stack()
    for element in input_list:
        if element == '+':
            second = stack.pop()
            first = stack.pop()
            stack.push(first + second)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            stack.push(first-second)
        elif element == '*':
            second = stack.pop()
            first = stack.pop()
            stack.push(first*second)
        elif elemnt == '/'
            second = stack.pop()
            first = stack.pop()
            stack.push(int(first/second))
        else:
            stack.push(int(element))

stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
print(stack.top())
