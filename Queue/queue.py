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
