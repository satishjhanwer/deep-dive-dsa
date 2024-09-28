# Advanced Concepts in Binary Search Trees (BST)

## 1. BST Variants

There are several types of Binary Search Trees optimized for different scenarios:

### 1.1 Self-Balancing Binary Search Trees

In practice, BSTs can become **unbalanced**, leading to performance degradation. **Self-balancing trees** ensure that the tree remains balanced, keeping the height close to **O(log n)**.

#### a) AVL Tree

- Named after its inventors, **Adelson-Velsky and Landis**.
- It is a **self-balancing BST** where the difference in height between left and right subtrees (balance factor) is at most 1.
- Every insertion and deletion operation ensures that the tree remains balanced by performing **rotations**.

#### b) Red-Black Tree

- Another type of **self-balancing BST**.
- Each node has an additional bit representing "color" (Red or Black), which helps maintain balance without strictly enforcing height conditions.
- Operations are performed to maintain the following properties:
  1. Every node is either red or black.
  2. The root is always black.
  3. No two red nodes can be adjacent.
  4. Every path from a node to its descendant NULL nodes must have the same number of black nodes.

#### c) Splay Tree

- A **self-adjusting BST** where recently accessed elements are moved to the root via rotations.
- This helps optimize **frequently accessed elements**, making access to those nodes faster.
- Does not strictly balance the tree, but improves average access time.

### 1.2 Treaps

- A hybrid of a **Binary Search Tree (BST)** and a **Heap**.
- Each node has both a **key** and a **priority**:
  1. The keys follow the **BST property**.
  2. The priorities follow the **Max-Heap property**.
- Useful in applications where both ordered and priority-based access are required.

---

## 2. Advanced Operations

### 2.1 Finding Lowest Common Ancestor (LCA) in BST

The **Lowest Common Ancestor (LCA)** of two nodes `n1` and `n2` in a BST is the node that is an ancestor of both `n1` and `n2`, and the deepest one.

**Algorithm:**

1. Start from the root node.
2. If both `n1` and `n2` are greater than the root, then LCA lies in the **right subtree**.
3. If both `n1` and `n2` are smaller than the root, then LCA lies in the **left subtree**.
4. Otherwise, the root is the LCA.

**Example:**

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_lca_bst(root, n1, n2):
    # Base case
    if not root:
        return None

    # If both nodes are smaller than the current node, move to the left subtree
    if n1 < root.value and n2 < root.value:
        return find_lca_bst(root.left, n1, n2)

    # If both nodes are larger than the current node, move to the right subtree
    if n1 > root.value and n2 > root.value:
        return find_lca_bst(root.right, n1, n2)

    # Otherwise, the current node is the lowest common ancestor
    return root

# Example usage:
# Create a sample BST
root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(4)
root.left.right = TreeNode(12)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)

lca = find_lca_bst(root, 10, 14)
print(f"LCA of 10 and 14 is: {lca.value}")  # Output: LCA of 10 and 14 is: 12
```

### 2.2 Validating if a Tree is a BST

To check if a given binary tree is a valid BST, you can use the in-order traversal method, or ensure that each node satisfies the BST properties recursively.

**Recursive Validation:**

The value of the node must be greater than the maximum value of the left subtree and smaller than the minimum value of the right subtree.

```python
def is_valid_bst(node, min_value=float('-inf'), max_value=float('inf')):
    # An empty tree is a valid BST
    if not node:
        return True

    # Check the value of the current node
    if not (min_value < node.value < max_value):
        return False

    # Recursively check the left and right subtrees
    return (is_valid_bst(node.left, min_value, node.value) and
            is_valid_bst(node.right, node.value, max_value))

# Example usage:
is_bst = is_valid_bst(root)
print(f"Is the tree a valid BST? {'Yes' if is_bst else 'No'}")
```

### 2.3 K-th Smallest Element in a BST

The K-th smallest element can be found using in-order traversal, which visits nodes in increasing order.

```python
def kth_smallest_bst(root, k):
    def in_order(node):
        if node:
            yield from in_order(node.left)
            yield node.value
            yield from in_order(node.right)

    # Generator to traverse the tree
    gen = in_order(root)

    # Traverse the tree until we reach the k-th element
    for _ in range(k - 1):
        next(gen)
    return next(gen)

# Example usage:
k = 3
kth_smallest = kth_smallest_bst(root, k)
print(f"The {k}-th smallest element is: {kth_smallest}")  # Output: The 3-th smallest element is: 10
```

### 2.4 BST to Sorted Doubly Linked List

You can convert a BST into a sorted doubly linked list by performing an in-order traversal and modifying the node pointers.

```python
def bst_to_doubly_linked_list(root):
    def convert(node):
        nonlocal prev, head
        if not node:
            return

        # Convert left subtree
        convert(node.left)

        # Adjust pointers
        if prev:
            prev.right = node
            node.left = prev
        else:
            head = node  # The first node becomes the head of the linked list

        # Update prev to the current node
        prev = node

        # Convert right subtree
        convert(node.right)

    prev, head = None, None
    convert(root)
    return head

# Example usage:
dll_head = bst_to_doubly_linked_list(root)

# Print the sorted doubly linked list
current = dll_head
while current:
    print(current.value, end=" <-> " if current.right else "\n")
    current = current.right
```

### 2.5 Balancing a BST

If you have an unbalanced BST, you can balance it by:

- Performing an in-order traversal to get the sorted elements.
- Rebuilding the tree from the sorted elements into a balanced BST.

```python
def in_order_traversal(node, elements):
    if node:
        in_order_traversal(node.left, elements)
        elements.append(node.value)
        in_order_traversal(node.right, elements)

def build_balanced_bst(sorted_elements):
    if not sorted_elements:
        return None

    mid = len(sorted_elements) // 2
    node = TreeNode(sorted_elements[mid])

    # Recursively build left and right subtrees
    node.left = build_balanced_bst(sorted_elements[:mid])
    node.right = build_balanced_bst(sorted_elements[mid + 1:])
    return node

def balance_bst(root):
    elements = []
    in_order_traversal(root, elements)
    return build_balanced_bst(elements)

# Example usage:
balanced_root = balance_bst(root)
print("BST balanced.")
```

## 3. Time Complexity of BST Operations

| Operation | Average Case | Worst Case (Skewed Tree) |
| --------- | ------------ | ------------------------ |
| Search    | O(log n)     | O(n)                     |
| Insert    | O(log n)     | O(n)                     |
| Delete    | O(log n)     | O(n)                     |

**Space Complexity:** O(n) for storing the tree.

## 4. When to Use a BST

BST is useful when you need to:

- Perform dynamic insertions and deletions.
- Frequently search for elements.
- Maintain sorted order for elements.
- However, if the tree is unbalanced, a Self-Balancing Tree (like AVL or Red-Black Trees) is preferred, as they guarantee better performance.

## 5. Applications of BST

- Databases: BSTs are used in databases for indexing and maintaining sorted data.
- Memory Management: BSTs can help manage memory allocation efficiently.
- Set and Map Implementations: Common data structures like sets and maps (in C++ STL and Java) use BST-based trees.
- Sorting Algorithms: Trees like Heap (a form of binary tree) are used in Heap Sort and Priority Queues.

## Conclusion

Binary Search Trees (BST) are powerful structures for ordered data. By understanding both basic and advanced concepts, such as self-balancing and efficient tree manipulations, you can optimize tree-based algorithms and applications.
