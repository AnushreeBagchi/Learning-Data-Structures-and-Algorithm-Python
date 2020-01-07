def create_array(initial_size):
    arr = []
    for i in range(initial_size):
        arr.append(0)
    return arr
class Stack:
    def __init__(self, initial_size = 10):
        self.arr = create_array(initial_size)
        self.next_index = 0
        self.num_elements = 0
    def push(self, data):
        if self.next_index == len(self.arr):
            print("out of space. Increasing arr capacity")
            self.handle_capacity()
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1
    def handle_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range (2* len(old_arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value
    def size(self):
        return len(self.arr)
    def is_empty(self):
        return self.num_elements ==  0
    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        last_element = self.arr[self.num_elements-1]
        self.arr[self.num_elements-1] = 0
        self.num_elements -= 1
        self.next_index -= 1
        return  last_element




stack = Stack()
stack.push("a")
stack.push("b")
print(stack.pop())

print(stack.pop())
print(stack.pop())



        