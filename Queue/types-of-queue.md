# Queue Variants

## 1. Simple Queue

A standard queue, where:

- Elements are inserted at the rear and removed from the front.
- Follows FIFO.

## 2. Circular Queue

In a **circular queue**, the last position is connected back to the first position, forming a circle.

### Key Features

- Efficient usage of space.
- The rear pointer wraps around when it reaches the end of the array.

### Operations

- **Enqueue**: Add elements to the rear, adjusting the rear pointer to wrap around if needed.
- **Dequeue**: Remove elements from the front, adjusting the front pointer to wrap around if needed.

### Circular Queue Example

```python
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  # Reset if only one element was there
        else:
            self.front = (self.front + 1) % self.size
        return data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Circular Queue:", end=" ")
            idx = self.front
            while idx != self.rear:
                print(self.queue[idx], end=" ")
                idx = (idx + 1) % self.size
            print(self.queue[self.rear])

# Example usage:
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()

cq.dequeue()
cq.display()
```

## 3. Priority Queue

In a priority queue, each element is assigned a priority, and elements are dequeued based on their priority rather than their order in the queue.

**Key Features:**

- Elements with higher priority are dequeued before elements with lower priority.
- If two elements have the same priority, they follow FIFO order.

**Operations:**

- Enqueue: Insert elements along with their priority.
- Dequeue: Remove the element with the highest priority.

```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data, priority):
        heapq.heappush(self.queue, (priority, data))  # Python's heapq is a min-heap, lower number has higher priority

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return heapq.heappop(self.queue)[1]  # Return the data with the highest priority

    def display(self):
        print("Priority Queue:", self.queue)

# Example usage:
pq = PriorityQueue()
pq.enqueue("task1", 2)
pq.enqueue("task2", 1)
pq.enqueue("task3", 3)

pq.display()
print("Dequeue:", pq.dequeue())
pq.display()
```

## 4. Deque (Double-Ended Queue)

A deque allows insertion and removal of elements from `both ends`. This makes it more versatile than a standard queue.

**Key Features:**

- Can function as both a queue (FIFO) and a stack (LIFO).
- Supports insertion and deletion from both the front and the rear.

**Operations:**

- `enqueue_front`: Insert an element at the front.
- `enqueue_rear`: Insert an element at the rear.
- `dequeue_front`: Remove an element from the front.
- `dequeue_rear`: Remove an element from the rear.

```python
class Deque:
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return len(self.deque) == 0

    def enqueue_front(self, data):
        self.deque.insert(0, data)  # Insert at the front

    def enqueue_rear(self, data):
        self.deque.append(data)  # Insert at the rear

    def dequeue_front(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.deque.pop(0)  # Remove from the front

    def dequeue_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return None
        return self.deque.pop()  # Remove from the rear

    def display(self):
        print("Deque:", self.deque)

# Example usage:
dq = Deque()
dq.enqueue_front(10)
dq.enqueue_rear(20)
dq.enqueue_front(5)
dq.display()

dq.dequeue_front()
dq.display()

dq.dequeue_rear()
dq.display()

```

## Time Complexity for Queue Operations

- `Enqueue`: O(1) (for a simple queue or circular queue)
- `Dequeue`: O(1) (for a simple queue or circular queue)
- `Peek`: O(1)
- `isEmpty`: O(1)
- `Priority Queue Operations`:
  - `Enqueue`: O(log n) (due to heap insertion)
  - `Dequeue`: O(log n) (due to heap extraction)

## Summary

- `Simple Queue`: Standard queue with FIFO.
- `Circular Queue`: A queue where the rear pointer wraps around to the front when it reaches the end of the array.
- `Priority Queue`: Elements are dequeued based on their priority.
- `Deque`: A double-ended queue that allows insertion and deletion from both the front and the rear.
