class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
    def createLinkedList(self, inputList):
        self.head = None
        self.tail = None
        for value in inputList:
            if self.head is None:
                self.head = Node(value)
                self.tail = self.head
            else:
                self.tail.next = Node(value)
                self.tail = self.tail.next
    def appendValue(self, value):
        if self.head is None:
            self.head = Node(value)
            return 
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    def appendNode(self, input_node):
        if self.head is None:
            self.head = input_node
            input_node.next = None
            return 
        node = self.head
        while node.next:
            node = node.next
        node.next = input_node

    def to_list(self):
        pyList = []
        if self.head :
            node = self.head
            while node:
                pyList.append(node.value)
                node = node.next
        return pyList

# merging sorted linked lists
def merge(llist1, llist2):
    newllist =  LinkedList()
    if llist1 is None: 
        return llist2
    elif llist2 is None:
        return llist1
    llist1_node = llist1.head
    llist2_node = llist2.head
    while llist1_node is not None or llist2_node is not None:
        if llist1_node is None:
            newllist.appendNode(llist2_node)
            llist2_node = llist2_node.next
        elif llist2_node is None:
            newllist.appendNode(llist1_node)
            llist1_node = llist1_node.next
        elif llist1_node.value <= llist2_node.value:
            newllist.appendNode(llist1_node)
            llist1_node = llist1_node.next
        else:
            newllist.appendNode(llist2_node)
            llist2_node = llist2_node.next
        
    return newllist

llistA = LinkedList()
llistA.appendValue(1)
llistA.appendValue(2)
llistA.appendValue(3)
llistA.appendValue(4)
llistA.appendValue(5)


llistB = LinkedList()
llistB.appendValue(21)
llistB.appendValue(31)
llistB.appendValue(41)
llistB.appendValue(51)

llistC = LinkedList()
llistC.appendValue(121)
llistC.appendValue(131)
llistC.appendValue(141)
llistC.appendValue(151)

llistMain = LinkedList()
llistMain.appendValue(llistA)
llistMain.appendValue(llistB)
llistMain.appendValue(llistC)

ll = None
node = llistMain.head
while node.next:
    nextMainNode = node.next
    if ll == None:
        ll = merge(node.value, node.next.value)
    else:
        ll = merge(ll, node.next.value)

    node = nextMainNode    