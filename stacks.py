# Implement a stack using a list
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

popped = stack.pop()
print("Popped Element:", popped)

print("Remaining Stack:", stack)

# Implement a stack Class
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):  # add an item to the top of the stack.
        self.items.append(item)
        
    def pop(self):   # remove and return the top item.
        if self.is_empty():
            return None   # Prevensts errors when popping an empty stack
        return self.items.pop()
    
    def peek(self):  # return the top item without removing it.
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):    # check if the stack is empty.
        return len(self.items) == 0
    
    def size(self):     # return the number of elements in the stack.
        return len(self.items)
    
# Test the stack :
stack = Stack()
stack.push(5)
stack.push(15)
stack.push(25)

print("Stack after pushing:", stack.items)

popped_items = stack.pop()  # remove the top element
print("Popped item:", popped_items)  [25]

print("Top item now:", stack.peek())  # peek the top element  [15]

print("Is the stack empty?", stack.is_empty())  # check if the stack is empty  [False]

print("Stack size:", stack.size())  # check stack size    [2]