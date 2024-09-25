# Doubly Linked List (DLL)

## 1. What is a Doubly Linked List?

A **Doubly Linked List** (DLL) is a type of linked list where each node contains three components:

- **Data**: The actual value stored in the node.
- **Next Pointer**: A reference to the next node in the list.
- **Prev Pointer**: A reference to the previous node in the list.

### DLL Node Structure

- Unlike a singly linked list (which only has a pointer to the next node), each node in a DLL has a pointer to both the **next** and **previous** nodes. This allows for **bi-directional traversal** of the list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node
```

## 2. Key Advantages of Doubly Linked List

- Bi-directional Traversal: You can traverse the list in both forward and backward directions.
- Efficient Deletion: Given a node, you can delete it efficiently without traversing the list to find the previous node (since each node has a prev pointer).
- Efficient Insertion: Insertion at both the head and the tail can be done efficiently.

## 3. Key Operations in Doubly Linked List

### Traversal

Traversal in both directions (forward and backward) is one of the main benefits of DLL.

```python
def traverse_forward(self):
    if not self.head:
        print("The list is empty.")
        return
    current = self.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def traverse_backward(self):
    if not self.head:
        print("The list is empty.")
        return
    current = self.head
    # Move to the last node
    while current.next:
        current = current.next
    # Traverse backward
    while current:
        print(current.data, end=" -> ")
        current = current.prev
    print("None")
```

### Insertion

There are three primary types of insertion in a doubly linked list:

- At the beginning.
- At the end.
- At a specific position.

#### Insertion At the Beginning

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node
```

#### Insertion At the End

```python
def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    last = self.head
    while last.next:
        last = last.next
    last.next = new_node
    new_node.prev = last
```

#### Insertion At a Specific Position

```python
def insert_at_position(self, data, position):
    if position == 0:
        self.insert_at_beginning(data)
        return
    new_node = Node(data)
    current = self.head
    for _ in range(position - 1):
        if not current:
            raise Exception("Position out of bounds")
        current = current.next
    new_node.next = current.next
    if current.next:
        current.next.prev = new_node
    current.next = new_node
    new_node.prev = current
```

### Deletion

Deletion is similar to insertion. There are three primary types of deletion in a doubly linked list:

- At the beginning.
- At the end.
- At a specific position.

#### Deletion At the Beginning

```python
def delete_at_beginning(self):
    if not self.head:
        print("The list is empty.")
        return
    if not self.head.next:
        self.head = None
        return
    self.head = self.head.next
    self.head.prev = None
```

#### Deletion At the End

```python
def delete_at_end(self):
    if not self.head:
        print("The list is empty.")
        return
    if not self.head.next:
        self.head = None
        return
    last = self.head
    while last.next:
        last = last.next
    last.prev.next = None
```

#### Deletion At a Specific Position

```python
def delete_at_position(self, position):
    if not self.head:
        print("The list is empty.")
        return
    if position == 0:
        self.delete_at_beginning()
        return
    current = self.head
    for _ in range(position):
        if not current:
            raise Exception("Position out of bounds")
        current = current.next
    if current.next:
        current.next.prev = current.prev
    if current.prev:
        current.prev.next = current.next
```

### Reversing the Doubly Linked List

Reversing a doubly linked list involves swapping the next and prev pointers of each node.

```python
def reverse(self):
    current = self.head
    prev_node = None
    while current:
        next_node = current.next
        current.next = prev_node
        current.prev = next_node
        prev_node = current
        current = next_node
    if prev_node:
        self.head = prev_node
```

## 4. Time Complexity of Operations

- Traversal: O(n) – since we need to visit every node.
- Insertion:
  - At the beginning or end: O(1).
  - At a specific position: O(n) – in the worst case.
- Deletion:
  - At the beginning or end: O(1).
  - At a specific position: O(n) – in the worst case.
- Reversal: O(n) – we must visit every node once.

## 5. Applications of Doubly Linked List

- Undo/Redo functionality: In text editors or browsers (where you can go back and forth between previous/next actions).
- Navigating between items in both directions: Music playlists or image galleries.
- Implementing certain data structures: Deques (double-ended queues), LRU Cache, etc.
