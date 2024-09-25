# Linked List

A **Linked List** is a linear data structure where elements, called **nodes**, are linked using pointers. Each node contains:

1. **Data** – the value stored in the node.
2. **Next** – a pointer/reference to the next node in the sequence.

## Types of Linked Lists

### 1. Singly Linked List

- Each node points to the next node.
- The last node's `Next` points to `null` (or `None` in Python).

### 2. Doubly Linked List

- Each node points to both the next and the previous node.
- It allows traversal in both forward and backward directions.

## Basic Structure of a Singly Linked List Node

```python
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Reference to the next node
```

## Simple Representation of Linked List

```txt
Head -> [Data | Next] -> [Data | Next] -> ... -> None
```

- Head: Points to the first node of the list.
- None: Marks the end of the list.

## Pros and Cons of Linked Lists

### Memory Management

- Nodes are created dynamically, meaning memory is allocated as needed.
- Unlike arrays, where memory is allocated in a contiguous block, linked lists use non-contiguous memory.

### Pros

- **Dynamic Size**: Size can grow or shrink as needed.
- **Efficient Insertions/Deletions**: Insertions and deletions at any point are efficient.

### Cons

- **No Random Access**: Elements can’t be accessed directly by index (like in arrays); you must traverse the list.
- **Extra Memory**: Each node requires extra memory for storing pointers.

## Key Operations on Linked Lists

1. **Traversal**: Visiting all nodes one by one.
2. **Insertion**: Adding nodes at the beginning, end, or a specific position.
3. **Deletion**: Removing nodes from the beginning, end, or a specific position.
4. **Searching**: Finding a node with a specific value.
5. **Reversing**: Changing the direction of the list.

### 1. Traversal

- **Definition**: Starting from the `head`, visit each node one by one until reaching `None` (end of the list).
- **Time Complexity**: O(n), You need to visit each node once, starting from the `head` and going to the `end` (node with `next = None`).

### 2. Insertion

- **At the Beginning**:

  - Point the new node’s `next` to the current `head`.
  - Update the `head` to the new node.
  - **Time Complexity**: O(1)

- **At the End**:

  - Traverse the list to find the last node.
  - Set the last node’s `next` to the new node.
  - **Time Complexity**: O(n), Requires traversing the list to find the last node (O(n)), and then updating the last node’s `next` to the new node (O(1)).

- **At a Given Position**:

  - Traverse to the position where you want to insert the new node.
  - Adjust pointers to insert the node at the desired position.
  - **Time Complexity**: O(n), Requires traversing the list to find the last node (O(n)), and then updating the last node’s `next` to the new node (O(1)).

### 3. Deletion

- **From the Beginning**:

  - Update the `head` to point to the second node.
  - **Time Complexity**: O(1), Only requires moving the `head` pointer to the second node.

- **From the End**:

  - Traverse to the second-last node and set its `next` to `None`.
  - **Time Complexity**: O(n), Requires traversing the list to find the second-last node and updating its `next` to `None`.

- **From a Specific Position**:
  - Traverse to the node just before the one you want to delete.
  - Update its `next` pointer to skip the node to be deleted.
  - **Time Complexity**: O(n), You need to traverse the list to find the node just before the one to be deleted (O(n)) and update the pointers.

### 4. Searching

- **Definition**: Traverse through the list comparing each node’s data until the target is found or the end is reached.
- **Time Complexity**: O(n), You may need to traverse the entire list to find the target node, resulting in O(n) time in the worst case.

### 5. Reversing a Linked List

- **Definition**: Change the direction of the `next` pointers so that the last node becomes the `head` and the list is reversed.

- **Time Complexity**: O(n), You need to traverse each node once and reverse the pointers, which takes O(n) time.

### Summary Table

| Operation             | Time Complexity |
| --------------------- | --------------- |
| Traversal             | O(n)            |
| Insertion (Beginning) | O(1)            |
| Insertion (End)       | O(n)            |
| Insertion (Middle)    | O(n)            |
| Deletion (Beginning)  | O(1)            |
| Deletion (End)        | O(n)            |
| Deletion (Middle)     | O(n)            |
| Searching             | O(n)            |
| Reversing             | O(n)            |

### Key Points

- Inserting or deleting at the **beginning** is very fast (O(1)).
- Operations like insertion, deletion, or searching in the **middle or end** require traversal, making them O(n) in the worst case.

## Additional Key Points on Singly Linked Lists

## 1. Edge Cases to Consider

When working with linked lists, it's essential to handle a few common edge cases:

- **Empty List**: Operations like deletion, searching, or traversal should handle cases where the list is initially empty.
- **Single Node List**: Ensure operations like deletion, especially from the end or middle, work correctly when there's only one node.
- **Insertion/Deletion at Head or Tail**: Be careful when handling the first and last nodes, as these cases can often introduce bugs if not handled separately.

## 2. Linked List Variations

- **Circular Linked List**: The last node's `next` points back to the `head`, creating a circular structure. This can be useful for certain applications (e.g., round-robin scheduling).
- **Doubly Linked List**: Each node has an additional `prev` pointer, allowing traversal in both directions (forward and backward).

## 3. Linked List in Real-World Applications

- **Dynamic Memory Management**: In scenarios where you don’t know the size of data in advance, linked lists are often preferred over arrays.
- **Implementation of Stacks and Queues**: Linked lists are often used to implement these structures due to their efficient insertion/deletion capabilities.

## 4. Limitations of Singly Linked Lists

- **No Random Access**: Unlike arrays, linked lists don't support constant-time access to any element by index.
- **Extra Memory for Pointers**: Each node requires extra space for the pointer/reference to the next node.

## 5. Recursive Solutions

- Many operations on linked lists (e.g., reversal, searching) can also be solved using recursion. Recursion can simplify the logic, though it has a space overhead due to the call stack.

## 6. Detecting Cycles in Linked Lists

- A common problem is detecting if a linked list has a cycle (e.g., the `next` of a node points to an earlier node). This can be solved using **Floyd’s Cycle Detection Algorithm** (also known as the "tortoise and hare" algorithm).

## 7. Converting Between Linked Lists and Arrays

- **Linked List to Array**: You can traverse a linked list and store each node's data in an array.
- **Array to Linked List**: Similarly, you can iterate over an array and create a linked list from it.

## 8. Memory Management in Linked Lists

- Since memory for nodes is allocated dynamically, it’s important to properly manage memory, especially in languages like C/C++ where manual memory management (e.g., freeing nodes) is required. In Python, garbage collection takes care of this automatically.

---

### Final Thought

Linked lists are a great introduction to understanding **dynamic memory**, **pointer manipulation**, and **efficient insertion/deletion**. As you move forward, you'll likely encounter more advanced data structures, but linked lists will serve as a strong foundation.
