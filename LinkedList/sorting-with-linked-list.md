# Sorting Algorithms for Linked Lists

## 1. Merge Sort on Linked List

**Overview:**

- **Merge Sort** is a divide-and-conquer algorithm that works efficiently with **Linked Lists** because it doesn't require random access like arrays.
- The linked list is split into two halves recursively, sorted individually, and then merged back in sorted order.

**Steps:**

- **Find the middle** of the linked list (using the slow and fast pointer method).
- **Recursively split** the linked list into halves until sub-lists contain only one node.
- **Merge** the two halves back in sorted order.

**Time Complexity:** O(n log n), where `n` is the number of nodes in the linked list.

### Example Implementation

```python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.value <= right.value:
        result = left
        result.next = merge_sorted_lists(left.next, right)
    else:
        result = right
        result.next = merge_sorted_lists(left, left.next)

    return result

def find_middle(head):
    if head is None:
        return head

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_sort_linked_list(head):
    if head is None or head.next is None:
        return head

    # Find middle of the list
    middle = find_middle(head)
    right_half = middle.next
    middle.next = None

    # Recursively split & sort
    left_sorted = merge_sort_linked_list(head)
    right_sorted = merge_sort_linked_list(right_half)

    # Merge sorted halves
    return merge_sorted_lists(left_sorted, right_sorted)

# Example usage:
def print_list(head):
    while head:
```

## 2. Insertion Sort on Linked List

**Overview:**

- Insertion Sort is simpler to implement on linked lists compared to arrays.
- In each iteration, the algorithm removes an element from the unsorted part and inserts it in the correct position in the sorted part of the list.

**Steps:**

- Start with the first node as the sorted list.
- Traverse the unsorted part, and insert each node into the correct position in the sorted part.
- Adjust pointers to maintain the linked list structure.

**Time Complexity:** O(n²), where n is the number of nodes in the list, because for each node, we may need to traverse the sorted part.

```python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def insertion_sort_linked_list(head):
    if not head or not head.next:
        return head

    sorted_list = None  # Start with an empty sorted list
    current = head

    while current:
        next_node = current.next  # Store next node to move ahead in unsorted list
        sorted_list = insert_in_sorted_order(sorted_list, current)
        current = next_node

    return sorted_list

def insert_in_sorted_order(sorted_list, node):
    # Insert node into sorted list in the correct position
    if not sorted_list or sorted_list.value >= node.value:
        node.next = sorted_list
        return node
    else:
        current = sorted_list
        while current.next and current.next.value < node.value:
            current = current.next
        node.next = current.next
        current.next = node

    return sorted_list

# Example usage:
def print_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Creating linked list: 4 -> 2 -> 1 -> 3
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

print("Original list:")
print_list(head)

# Sorting linked list
sorted_head = insertion_sort_linked_list(head)

print("Sorted list:")
print_list(sorted_head)

```
