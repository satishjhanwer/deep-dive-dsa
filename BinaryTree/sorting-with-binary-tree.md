# Sorting with Binary Tree

## 1. Binary Tree Sort (Using Binary Search Tree)

**Algorithm Overview:**

- A **Binary Search Tree (BST)** can be used to sort an array by inserting elements into the tree and then performing an **in-order traversal**. The in-order traversal of a BST will give the elements in sorted order.

**Steps:**

1. Insert all elements of the array into a **Binary Search Tree**.
2. Perform an **in-order traversal** to retrieve the sorted elements.

**Time Complexity:**

- **Best Case**: O(n log n) – when the tree is balanced.
- **Worst Case**: O(n²) – when the tree becomes skewed (unbalanced).

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Insert into BST
def insert_into_bst(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root

# In-order traversal for sorting
def in_order_traversal(node, result):
    if node:
        in_order_traversal(node.left, result)
        result.append(node.value)
        in_order_traversal(node.right, result)

# Tree Sort
def tree_sort(arr):
    if not arr:
        return []

    root = None
    for value in arr:
        root = insert_into_bst(root, value)

    result = []
    in_order_traversal(root, result)
    return result

# Example Usage
arr = [7, 4, 9, 1, 5, 6]
sorted_arr = tree_sort(arr)
print("Sorted Array:", sorted_arr)
Sorted Array: [1, 4, 5, 6, 7, 9]
```

## 2. Heap Sort (Special Case of Binary Tree)

**Algorithm Overview:**

- `Heap Sort` is a comparison-based sorting technique based on a `Binary Heap` data structure.
- A `Binary Heap` is a complete binary tree, and it can be either a `Max Heap` (root node is the largest) or a `Min Heap` (root node is the smallest).
- Heap Sort uses a `Max Heap` to repeatedly remove the largest element and place it at the end of the array.

**Steps:**

- Build a `Max Heap` from the unsorted array.
- Repeatedly extract the maximum element from the heap and place it at the end of the sorted portion of the array.

**Time Complexity:**

- O(n log n) for all cases (best, average, worst).

```python
# Max-Heapify function
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Heap Sort function
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Example Usage
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Sorted Array:", arr)
Sorted Array: [5, 6, 7, 11, 12, 13]
```
