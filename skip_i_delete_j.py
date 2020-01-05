class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def create_linked_list(self, input_list):
        for data in input_list:
            if self.head is None:
                self.head = Node(data)
            else:
                node = self.head
                while node.next:
                    node = node.next
                node.next = Node(data)
    def to_list(self):
        py_list = []
        node = self.head
        while node:
            py_list.append(node.value)
            node = node.next
        return py_list
    def appendNode(self, inputnode):
        if self.head is None:
            self.head = inputnode
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = inputnode
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


linked_list = LinkedList()
linked_list.create_linked_list([1,2,3,4,5,6,7,8,9,10,11,12])
print(linked_list.to_list())

def skip_and_delete(llist, i, j):
    newll = LinkedList()
    node = llist.head
    while node:
        skip_count = 0
        delete_count = 0
        while skip_count != i :
            nextPtr = node.next
            if node:
                llist.remove(node)
                newll.appendNode(node)
                node = nextPtr
                skip_count += 1
            else:
                break
        while delete_count != j:
            if node:
                node = node.next
                delete_count += 1
            else:
                break
    return newll

newll = skip_and_delete(linked_list, 2, 3)
print(newll.to_list())