class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def appendValue(self, value):
        if self.head is None:
            self.head = Node(value)
            return 
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
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
            
def merge(llist1, llist2):
    merged = LinkedList()
    if llist1 is None:
        return llist2
    elif llist2 is None:
        return llist1
    llist1_node = llist1.head
    llist2_node = llist2.head
    while llist1_node is not None or llist2_node is not None:
        if llist1_node is None:
            nextPtr = llist2_node.next
            llist2.remove(llist2_node)
            merged.appendNode(llist2_node)
            llist2_node = nextPtr
        elif llist2_node is None:
            nextPtr = llist1_node.next
            llist1.remove(llist1_node)
            merged.appendNode(llist1_node)
            llist1_node = nextPtr
        elif llist1_node.value <= llist2_node.value:
            nextPtr = llist1_node.next
            llist1.remove(llist1_node)
            merged.appendNode(llist1_node)
            llist1_node = nextPtr
        else: 
            nextPtr = llist2_node.next
            llist2.remove(llist2_node)
            merged.appendNode(llist2_node)
            llist2_node = nextPtr
    return merged

def test():
    llist1 = LinkedList()
    llist1.appendValue(1)
    llist1.appendValue(12)
    llist1.appendValue(31)
    llist1.appendValue(41) 

    llist2 = LinkedList()
    llist2.appendValue(10)
    llist2.appendValue(30)
    llist2.appendValue(40)

    llist3 = LinkedList()
    llist3.appendValue(5)
    llist3.appendValue(11)
    llist3.appendValue(15)

    mainList = LinkedList()
    mainList.appendValue(llist1)
    mainList.appendValue(llist2)
    mainList.appendValue(llist3)

    node = mainList.head
    flattendList = LinkedList()
    while node:
       flattendList = merge(flattendList, node.value)
       node = node.next
test()




