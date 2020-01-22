class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def create_linked_list(self, inputlist):
        for data in inputlist:
            if self.head is None:
                self.head = Node(data)
                self.tail = self.head
            else:
                self.tail.next = Node(data)
                self.tail = self.tail.next
    def to_list(self):
        py_list = []
        node = self.head
        while node:
            py_list.append(node.value)
            node = node.next
        return py_list
    def appendNode(self, input_node):
        if self.head is None:
            self.head = input_node
            self.tail = self.tail
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = input_node
        input_node.next = None
    def removeNode(self, input_node):
        if self.head is None:
            return
        node =  self.head
        while node.next != input_node:
            node = node.next
        node.next = node.next.next
        input_node.next = None
    def getPrevious(self, input_node):
        node = self.head
        if self.head == input_node:
            return
        while node.next != input_node:
            node =  node.next
        previous_node = node
        return previous_node
linked_list = LinkedList()
linked_list.create_linked_list([1,2,3,4,5,6,7,8,9])   

def swap_nodes(llist, i, j):
    left_index_prev = None
    right_index_prev = None
    left_index_next = None
    right_index_next = None
    left_index_node = None
    right_index_node = None
    counter = 0
    node = llist.head
    while node:
        if counter == i:
            left_index_prev = llist.getPrevious(node)
            left_index_next = node.next
            left_index_node = node
        elif counter == j:
            right_index_prev = llist.getPrevious(node)
            right_index_next = node.next
            right_index_node = node
        node = node.next
        counter += 1

    llist.removeNode(left_index_node)
    llist.removeNode(right_index_node)
    
    if right_index_prev == left_index_node: #if swaping nodes next to each other
        right_index_node.next = left_index_node
    else:
        right_index_node.next = left_index_next
        right_index_prev.next = left_index_node

    left_index_node.next = right_index_next
    left_index_prev.next = right_index_node

swap_nodes(linked_list,0,4)
print(linked_list.to_list())
 