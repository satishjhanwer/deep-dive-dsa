# LinkedList Code implementation

We will implement the following in a Singly Linked List:

- Basic Node and Linked List structure.
- Traversal.
- Insertion (beginning, end, and at a position).
- Deletion (beginning, end, and from a position).
- Searching for an element.
- Reversing the linked list.

## Basic Node and Linked List Structure

```python
# Basic structure of Node
class Node:
  def __init__(self, data):
    self.data = data  # Data part of the node
    self.next = None  # Pointer to the next node
```

```python
# Basic structure of LinkedList
class LinkedList:
  def __init__(self):
    self.head = None  # Initialize the list with no head (empty list)
```

## Traversal

```python
def traverse(self):
  if not self.head:
    print("The list is empty.")
    return
  current = self.head
  while current:
    print(current.data, end=" -> ")
    current = current.next
  print("None")
```

## Insertion (beginning, end, and at a position)

```python
# Insertion at the beginning
def insert_at_beginning(self, data):
  new_node = Node(data)
  new_node.next = self.head
  self.head = new_node

# Insertion at the end
def insert_at_end(self, data):
  new_node = Node(data)
  if not self.head:
    self.head = new_node
    return
  last = self.head
  while last.next:
    last = last.next
  last.next = new_node

# Insertion at a given position
def insert_at_position(self, data, position):
  if position == 0:
    self.insert_at_beginning(data)
    return
  new_node = Node(data)
  current = self.head
  for _ in range(position - 1):
    if current is None:
      raise Exception("Position out of bounds")
    current = current.next
  new_node.next = current.next
  current.next = new_node

```

## Deletion (beginning, end, and at a position)

```python
# Deletion at the beginning
def delete_at_beginning(self):
  if not self.head:
    print("The list is empty. No deletion performed.")
    return
  self.head = self.head.next

# Deletion at the end
def delete_at_end(self):
  if not self.head:
    print("The list is empty. No deletion performed.")
    return
  if not self.head.next:
    self.head = None
    return
  current = self.head
  while current.next.next:
    current = current.next
  current.next = None

# Deletion at a specific position
def delete_at_position(self, position):
  if not self.head:
    print("The list is empty. No deletion performed.")
    return
  if position == 0:
    self.delete_at_beginning()
    return
  current = self.head
  for _ in range(position - 1):
    if not current.next:
      raise Exception("Position out of bounds")
    current = current.next
  current.next = current.next.next


```

## Searching for an element

```python
def search(self, key):
  current = self.head
  position = 0
  while current:
    if current.data == key:
      print(f"Element {key} found at position {position}")
      return
    current = current.next
    position += 1
  print(f"Element {key} not found in the list.")
```

## Reversing the linked list

```python
def reverse(self):
  previous = None
  current = self.head
  while current:
    next_node = current.next
    current.next = previous
    previous = current
    current = next_node
  self.head = previous
```
