"""Implement a linked list class. Your class should be able to:
Append data to the tail of the list and prepend to the head
Search the linked list for a value and return the node
Remove a node
Pop, which means to return the first node's value and delete the node from the list
Insert data at some position in the list
Return the size (length) of the linked list"""
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        if self.head is None:
           self.head = DoublyNode(value)
           self.tail = self.head
           return
        self.tail.next = DoublyNode(value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
    def prepend(self, value):
        if self.head is None:
            self.head = DoublyNode(value)
            self.tail = self.head
            return
        self.head.previous = DoublyNode(value)
        self.head.previous.next = self.head
        self.head = self.head.previous
    def to_list(self):
        pyList = []
        node = self.head
        while node:
            pyList.append(node.value)
            node = node.next
        return pyList
    def search(self, value):
        if self.head is None:
            return
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
    def remove(self, value):
        if self.head is None:
            return
        node = self.head
        while node:
            if node.value == value:
                if node.previous is None:
                    self.head = node.next
                    return
                node.previous.next = node.next
                return 
            node = node.next
    def pop(self):
        if self.head is None:
            return
        node = self.head
        self.head = node.next
        return node.value
    def insert(self,value,pos):
        if pos == 0:
            self.prepend(value)
            return
        index = 0
        node = self.head
        while node.next and index <= pos:
            if(pos-1)==index:
                newNode = DoublyNode(value)
                newNode.next = node.next
                node.next = newNode
                return 
            index += 1
            node = node.next
        self.append(value)
    def size(self):
        length = 0
        node = self.head
        while node: 
            length += 1
            node = node.next
        return length
            
# Tests
# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"
    
# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
linked_list.append(3)
assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"

# Test remove
linked_list.remove(1)
assert linked_list.to_list() == [2, 1, 3, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4, 3], f"list contents: {linked_list.to_list()}"
linked_list.remove(3)
assert linked_list.to_list() == [2, 1, 4], f"list contents: {linked_list.to_list()}"
# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.to_list()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.to_list()}"


linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
print(linked_list.to_list())
linked_list.insert(5,2)
print(linked_list.to_list())
print(linked_list.size())