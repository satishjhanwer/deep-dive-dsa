# Binary Search Tree (BST)

## 1. Definition

A **Binary Search Tree (BST)** is a binary tree where each node follows these properties:

- The left subtree contains only nodes with values **less than** the node's value.
- The right subtree contains only nodes with values **greater than** the node's value.
- Both the left and right subtrees are also BSTs.

## 2. Properties of BST

- **Ordered Structure**: Nodes are stored in a sorted manner, making it easy to perform searches.
- **Dynamic Size**: A BST can grow or shrink as needed, unlike arrays that have a fixed size.
- **Efficiency**: Average time complexity for search, insert, and delete operations is **O(log n)**, but can degrade to **O(n)** in the worst case (e.g., if the tree is skewed).

## 3. Common Operations

### 3.1 Insertion

- To insert a new node, start at the root and recursively find the correct position.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root
```

### 3.2 Search

- To search for a value, traverse the tree based on the value's comparison with the current node.

```python
def search_bst(root, value):
    if not root or root.value == value:
        return root
    if value < root.value:
        return search_bst(root.left, value)
    return search_bst(root.right, value)
```

## 3.3 Deletion

- To delete a node:

1. `Leaf Node`: Simply remove it.
2. `Node with One Child`: Replace it with its child.
3. `Node with Two Children`: Find the in-order successor (smallest in the right subtree) or in-order predecessor (largest in the left subtree) and replace it.

```python
def delete_bst(root, value):
    if not root:
        return root
    if value < root.value:
        root.left = delete_bst(root.left, value)
    elif value > root.value:
        root.right = delete_bst(root.right, value)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # Node with two children
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete_bst(root.right, temp.value)
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node
```

## 4. Traversal Methods

### 4.1 In-Order Traversal

- Yields values in sorted order.

```python
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=" ")
        in_order_traversal(node.right)
```

### 4.2 Pre-Order Traversal

- Useful for creating a copy of the tree.

```python
def pre_order_traversal(node):
    if node:
        print(node.value, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
```

### 4.3 Post-Order Traversal

- Useful for deleting the tree.

```python
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=" ")
```

## 5. Height of BST

- Height of a BST is the number of edges on the longest downward path between the root and a leaf node.

```python
def height_bst(node):
    if not node:
        return -1
    left_height = height_bst(node.left)
    right_height = height_bst(node.right)
    return max(left_height, right_height) + 1
```

## 6. Balancing the BST

- A balanced BST ensures that the height remains logarithmic. If a BST becomes unbalanced, operations degrade to `O(n)`.
- `Self-balancing BSTs` like `AVL Trees` or `Red-Black Trees` maintain balance automatically during insertions and deletions.

## 7. Applications of BST

- Implementing dynamic sets and lookup tables.
- Used in databases and memory management.
- Facilitates efficient searching and sorting operations.

## Conclusion

Binary Search Trees (BST) are fundamental data structures that provide efficient means for data organization, retrieval, and manipulation. Understanding BST operations and their complexities is crucial for optimizing performance in various applications.

**Common Interview Questions on Binary Tree:**

- How to find the lowest common ancestor (LCA) in a BST?
- How to validate if a tree is a BST?
- How to find the k-th smallest/largest element in a BST?
- How to convert a sorted array into a balanced BST?
