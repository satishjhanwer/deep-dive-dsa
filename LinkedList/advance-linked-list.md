# Additional Concepts for Singly Linked List

## 1. **Floyd’s Cycle Detection Algorithm (Tortoise and Hare)**

- If you suspect that a linked list might have a **cycle** (where a node’s `next` pointer loops back to a previous node), you can use Floyd’s Cycle Detection Algorithm.
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

### Algorithm Explanation

- Use two pointers, `slow` and `fast`. `slow` moves one step at a time, while `fast` moves two steps.
- If the list has a cycle, `slow` and `fast` will eventually meet. If not, `fast` will reach the end (`None`).

```python
def detect_cycle(self):
    slow = self.head
    fast = self.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("Cycle detected in the linked list.")
            return True
    print("No cycle detected.")
    return False
```

## 2 Merge Two Sorted Linked Lists

- Merging two sorted linked lists into one sorted list is a common operation in linked list manipulation.
- Time Complexity: O(n + m), where n and m are the lengths of the two lists.

```python
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Append the remaining nodes
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next
```

## 3 Linked List as a Stack

- Linked lists can easily be used to implement a stack (LIFO – Last In First Out).
- Insertion and deletion at the head provide O(1) push and pop operations.

```python
def push(self, data):
    self.insert_at_beginning(data)

def pop(self):
    if self.is_empty():
        print("Stack underflow.")
        return
    value = self.head.data
    self.delete_at_beginning()
    return value
```

## 4 Linked List as a Queue

- Similarly, a singly linked list can be used to implement a queue (FIFO – First In First Out).
- Enqueue at the end and dequeue at the beginning both operate in O(1) time for insertion and O(1) for deletion at the head.

```python
def enqueue(self, data):
    self.insert_at_end(data)

def dequeue(self):
    if self.is_empty():
        print("Queue underflow.")
        return
    value = self.head.data
    self.delete_at_beginning()
    return value

```

## 5 Time-Space Trade-offs

- Singly linked lists have a time advantage in dynamic insertions/deletions but come with a space overhead due to the extra pointer (`next`).
- Doubly linked lists add an extra pointer (`prev`) to each node, allowing easier traversal and deletion from both directions, but at the cost of more memory.

## 6 Linked List sorting Algorithms

- Sorting a linked list using algorithms like Merge Sort is more efficient than Bubble Sort for larger lists.
- Merge Sort works well because it uses the divide-and-conquer technique, splitting the list into halves, sorting them, and merging them back.

```python
def merge_sort(self, head):
    if not head or not head.next:
        return head

    # Split the list into two halves
    middle = self.get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = self.merge_sort(head)
    right = self.merge_sort(next_to_middle)

    # Merge the sorted halves
    sorted_list = self.sorted_merge(left, right)
    return sorted_list
```
