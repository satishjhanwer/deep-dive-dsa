# Stack implementation in Python using List


class Stack:
    def __init__(self):
        self.stack = []

    # Push an element to the stack
    def push(self, data):
        self.stack.append(data)

    # Pop an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack Underflow")
            return None

    # Peek the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display the stack
    def display(self):
        print(self.stack)
