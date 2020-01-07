class Stack:
    def __init__(self):
        self.items =[]
    def push(self, value):
        self.items.append(value)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items) == 0

def equation_checker(equation):
    stack = Stack()
    for letter in equation:
        if len(equation) == 0:
            print("Pass an equaltion")
            return False
        if letter == "(":
            stack.push("(")
        elif letter == ")":
            if stack.size() == 0:
                print("Unbalanced equation")
                return False     
            stack.pop()
    if(stack.size() == 0):
        print("Balanced equation")
        return True
    else:
        print("Unbalanced equation")     
        return False

print ("Pass" if (equation_checker('((3^2 + 8)*(5/2))/(2+6)')) else "Fail")
print ("Pass" if not (equation_checker('((3^2 + 8)*(5/2))/(2+6))')) else "Fail")