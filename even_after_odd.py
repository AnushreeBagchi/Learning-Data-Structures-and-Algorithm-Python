class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def create_linked_list(self, input_list):
        self.head = None
        for value in input_list:
            if self.head is None:
                self.head = Node(value)
            else:
                node = self.head
                while node.next:
                    node =  node.next
                node.next =  Node(value)
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        node =  self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        self.tail = node.next
        self.tail.next = None

    def appendNode(self, inputnode):
        if self.head is None:
            self.head = inputnode
            return 
        node = self.head
        while node.next:
            node = node.next
        node.next = inputnode
        inputnode.next = None
    def remove(self, inputnode):
        if self.head is None:
            return
        node = self.head
        if node == inputnode:
            self.head = inputnode.next
            inputnode.next = None
            return
        while node.next != inputnode:
            node = node.next
        node.next = node.next.next
        inputnode.next = None

    def to_list(self):
        py_list = []
        node = self.head
        while node:
            py_list.append(node.value)
            node = node.next
        return py_list

linked_list = LinkedList()
linked_list.create_linked_list([1,2,3,4,5,6,7,8,9,10])
print(linked_list.to_list())

def even_after_odd(llist):
    evenll = LinkedList()
    oddll = LinkedList()
    node = llist.head
    evenll_node = evenll.head
    oddll_node = oddll.head
    while node:
        if node.value%2 == 0:
            nextPtr = node.next
            llist.remove(node)
            evenll.appendNode(node)
            node = nextPtr
        else:
            nextPtr = node.next
            llist.remove(node)
            oddll.appendNode(node)
            node = nextPtr 
        
    print(evenll.to_list())
    print(oddll.to_list())

even_after_odd(linked_list)
