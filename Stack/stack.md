# Stack

## 1. What is a Stack?

A **Stack** is a linear data structure that follows the **LIFO (Last In First Out)** principle. This means the last element added to the stack is the first to be removed.

### Characteristics

- **LIFO**: The last element added is the first one to be removed.
- Operations are performed at one end called the **top** of the stack.
- Insertion and removal of elements happen at the **same end**, called the **top** of the stack.
- The opposite end is called the **bottom**, and no operations are allowed there.

### Analogy

Think of a stack of plates:

- The plate placed last on the top is removed first.

### Use Cases

- **Function call stack** in recursion.
- **Undo/Redo** functionality.
- **Balancing parentheses** or tags in compilers.
- **Backtracking algorithms**.

---

## 2. Terminology and Operations

- **Push**: Add an element to the top of the stack.
- **Pop**: Remove and return the top element.
- **Peek**: Get the top element without removing it.
- **isEmpty**: Check if the stack is empty.

### Push

Adds an element to the top of the stack.

- **Time Complexity**: O(1)

```python
def push(self, data):
    self.stack.append(data)
```

### Pop

Removes the topmost element from the stack.

- **Time Complexity**: O(1)

```python
def pop(self):
    if not self.is_empty():
        return self.stack.pop()
    else:
        print("Stack Underflow")
        return None
```

### Peek

Returns the topmost element without removing it.

- **Time Complexity**: O(1)

```python
def peek(self):
    if not self.is_empty():
        return self.stack[-1]
    else:
        return None
```

### isEmpty

Checks if the stack is empty.

- **Time Complexity**: O(1)

```python
def is_empty(self):
    return len(self.stack) == 0
```

## 3. Applications of Stack

- Function Call Stack: Used to store active function calls.
- Expression Evaluation: Converting infix expressions to postfix/prefix.
- Undo Mechanism: In word processors and text editors.

## 4. Detailed Example

Expression Evaluation: Stacks are used in evaluating arithmetic expressions in postfix notation.

Example:
Given postfix expression `23*54*+`, the stack is used to evaluate the expression as follows:

- Push `2`, `3` → Stack: [2, 3]
- Pop `3`, `2`, multiply → Push result `6` → Stack: [6]
- Push `5`, `4` → Stack: [6, 5, 4]
- Pop `4, 5`, multiply → Push result `20` → Stack: [6, 20]
- Pop `20, 6`, add → Push result `26` → Stack: [26]
- Result: `26`

## 5. Stack Implementation using Python List

Python’s list can be used as a stack because it supports both **append()** and **pop()** operations in O(1) time complexity.

```python
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
```

## 6. Stack Overflow and Underflow

- Stack Overflow: Occurs when attempting to push onto a full stack (not applicable in Python lists as they dynamically grow).
- Stack Underflow: Occurs when trying to pop from an empty stack.

```python
stack = Stack()
stack.pop() # Will raise "Stack Underflow" since the stack is empty.
```

## 7. Stack in Recursion

When a function is called recursively, the system stores the function call's state in the call stack. Once the recursive call is complete, the system pops the call stack and returns control to the previous function call.

## 8. Linked List based Stack

A stack can also be implemented using a linked list where the head of the linked list acts as the top of the stack.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    # Push element onto stack
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    # Pop element from stack
    def pop(self):
        if not self.is_empty():
            value = self.top.data
            self.top = self.top.next
            return value
        else:
            print("Stack Underflow")
            return None

    # Peek at the top element
    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            return None

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Display the stack
    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
```

## 9. Summary

- Stack: Follows LIFO (Last In, First Out) principle.
- Basic Operations: `push`, `pop`, `peek`, and `isEmpty` are performed in constant time O(1).
- Applications: Undo/redo, recursion, function call stack, expression evaluation.
