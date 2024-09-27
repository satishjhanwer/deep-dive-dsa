# Stack Variants

## 1. Simple/Basic Stack

- The stack that follows the **LIFO** (Last In First Out) principle.
- Basic operations: `push`, `pop`, `peek`, `isEmpty`.

## 2. Bounded Stack

- A **Bounded Stack** has a **fixed maximum size**.
- Once the stack is full, attempting to `push` another element results in a **Stack Overflow**.

### Example

```python
class BoundedStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, data):
        if len(self.stack) < self.capacity:
            self.stack.append(data)
        else:
            print("Stack Overflow")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack Underflow")
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity
```

## 3. Dynamic Stack

- A Dynamic Stack grows dynamically in size when it is full, unlike a Bounded Stack.
- Common in languages like Python where lists grow dynamically, so no fixed capacity is imposed.

## 4. Double-ended Stack (Deque)

- A Double-ended Stack or Deque (Double-ended Queue) allows elements to be pushed or popped from both ends.
- It combines the functionality of a stack and queue.
- Useful when you need both LIFO and FIFO behavior in the same structure.

```python
from collections import deque

stack = deque()

# Push to right (standard stack behavior)
stack.append(1)  # Push
stack.append(2)

# Pop from right
stack.pop()  # Pop -> 2

# Push to left (like queue behavior)
stack.appendleft(3)

# Pop from left
stack.popleft()  # Pop -> 3
```

## 5. Min Stack (with getMin)

- A Min Stack is a special stack that, in addition to standard stack operations, supports retrieving the minimum element in constant time O(1).
- It can be implemented using an additional stack that tracks the current minimum value.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Tracks the minimum values

    def push(self, data):
        self.stack.append(data)
        # Push the minimum value seen so far onto the min_stack
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return None
        # Pop from min_stack if we're removing the minimum element
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
```

## 6. Multi-stack

- A Multi-stack structure holds multiple stacks within the same data structure.
- It is useful in scenarios where you need to manage multiple independent stacks.

```python
class MultiStack:
    def __init__(self, stack_size, num_stacks=3):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack = [None] * (stack_size * num_stacks)
        self.sizes = [0] * num_stacks

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            print(f"Stack {stack_num} Overflow")
        else:
            index = self.index_of_top(stack_num)
            self.stack[index + 1] = value
            self.sizes[stack_num] += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            print(f"Stack {stack_num} Underflow")
            return None
        else:
            index = self.index_of_top(stack_num)
            value = self.stack[index]
            self.stack[index] = None
            self.sizes[stack_num] -= 1
            return value

    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0

    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.sizes[stack_num] - 1
```

## 7. Persistent Stack

- A Persistent Stack allows you to create a new version of the stack whenever you modify it, without altering the original version.
- This is useful in functional programming and undo/redo operations.
- Implemented using immutable data structures.

## 8. Circular Stack

- A Circular Stack allows wraparound behavior when reaching the end of the stack, and starts again from the beginning.
- Mainly used in specialized memory management systems.

## 9. Parallel Stack

- A Parallel Stack is designed to work in multi-threaded or parallel processing environments.
- It ensures thread-safe operations, meaning multiple threads can push/pop elements safely without data corruption.

## 10. Lazy Stack

- A Lazy Stack delays certain operations like memory allocation until absolutely necessary.
- It can be useful in systems where memory management is critical.

## Summary of Stack Variants

| Variant            | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| Basic Stack        | Standard LIFO structure with push, pop, peek.                 |
| Bounded Stack      | Stack with a fixed size, prone to overflow.                   |
| Dynamic Stack      | Grows dynamically with no fixed size.                         |
| Double-ended Stack | Allows pushing/popping from both ends (Deque).                |
| Min Stack          | Supports retrieving the minimum element in O(1) time.         |
| Multi-stack        | Manages multiple stacks within a single structure.            |
| Persistent Stack   | Maintains previous versions of the stack for undo operations. |
| Circular           | Stack Wraparound behavior at the end of the stack.            |
| Parallel           | Stack Safe for multi-threaded environments.                   |
| Lazy Stack         | Delays certain operations to optimize memory and performance. |
