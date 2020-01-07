class Queue:
    def __init__(self, initial_size= 10):
        self.arr = [0 for _ in range(initial_size)]
        self.front_index = -1
        self.next_index = 0
        self.queue_size = 0
    def size(self):
        return self.queue_size
    def is_empty(self):
        return self.queue_size == 0
    def enqueue(self, value):
        if self.queue_size == len(self.arr):
            self.handle_capacity()
        self.arr[self.next_index] = value
        self.queue_size += 1
        if self.front_index == -1:
            self.front_index = 0
        self.next_index = (self.next_index+1) % len(self.arr)
    def dequeue(self):
        if self.queue_size == 0:
            self.next_index = 0
            self.front_index = -1
            return None
        value = self.arr[self.front_index]
        self.queue_size -= 1
        self.front_index = (self.front_index+1)%len(self.arr)
        return value
    def handle_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2*len(self.arr))]
        index = 0
        for i in range(self.front_index, len(self.arr)):
            self.arr[index] = old_arr[i]
            index += 1
        for i in range(0, self.front_index):
            self.arr[index] = old_arr[i]
            index += 1
        self.front_index = 0
        self.next_index = index

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print ("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print ("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print ("Pass" if (q.dequeue() == 2) else "Fail")
print ("Pass" if (q.dequeue() == 3) else "Fail")
print ("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print ("Pass" if (q.size() == 1) else "Fail")
    
        

        

        
