# Queue

## 1. What is a Queue?

A **Queue** is a linear data structure that follows the **FIFO (First In First Out)** principle. This means the element added first is the first to be removed.

### Characteristics

- Insertion happens at one end, called the **rear**.
- Removal happens at the other end, called the **front**.

### Use Cases

- **Printer task scheduling**.
- **CPU scheduling** (round-robin scheduling).
- **Handling requests in web servers**.
- **Breadth-First Search (BFS)** in graphs.

---

## 2. Key Operations on Queue

- **Enqueue**: Add an element to the rear of the queue.
- **Dequeue**: Remove and return the front element.
- **Peek**: Get the front element without removing it.
- **isEmpty**: Check if the queue is empty.

---

## 3. Queue Implementation using Python List

A Python list can also be used to implement a queue, but using `pop(0)` for dequeue has O(n) time complexity. To optimize, we can use `collections.deque` which has O(1) operations for both `append()` and `popleft()`.

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Enqueue an element to the rear
    def enqueue(self, data):
        self.queue.append(data)

    # Dequeue an element from the front
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            print("Queue Underflow")
            return None

    # Peek at the front element without removing it
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display the queue
    def display(self):
        print(list(self.queue))
```

## 4. Time Complexity of Queue Operations

- Enqueue: O(1)
- Dequeue: O(1) with deque (O(n) with Python list)
- Peek: O(1)
- isEmpty: O(1)

## 5. Applications of Queue

- Task Scheduling: Managing processes in operating systems.
- Breadth-First Search (BFS): Traversing graphs.
- Simulations: Modeling queues in real-life systems like restaurants, call centers.
