# Binary Tree

## 1. What is a Binary Tree?

- A **binary tree** is a data structure where each node has at most two children, referred to as the **left child** and the **right child**.
- It is used in many applications such as searching, sorting, and decision-making processes.

## 2. Key Terminologies

- **Node**: The basic unit of a tree containing data and links to its children.
- **Root**: The top node of the binary tree.
- **Leaf**: A node with no children.
- **Edge**: The connection between two nodes.
- **Depth**: The number of edges from the root to the node.
- **Height**: The number of edges from the node to the deepest leaf.
- **Parent**: A node that has one or more children.
- **Child**: A node that is the descendant of another node.

## 3. Types of Binary Trees

1. **Full Binary Tree**: Every node has 0 or 2 children.
2. **Perfect Binary Tree**: All internal nodes have two children, and all leaf nodes are at the same level.
3. **Complete Binary Tree**: All levels are filled except possibly the last level, and all nodes are as far left as possible.
4. **Balanced Binary Tree**: A tree where the difference in heights of the left and right subtrees is at most 1 for every node.
5. **Degenerate (Skewed) Binary Tree**: Each parent node has only one child (either left or right).

## 4. Binary Tree Traversal Methods

Traversal is the process of visiting all nodes in a tree in a specific order. There are four major types of traversal.

### 4.1 In-Order Traversal (Left, Root, Right)

- Process:

  1. Traverse the left subtree.
  2. Visit the root node.
  3. Traverse the right subtree.

```python
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)
```

### 4.2 Pre-Order Traversal (Root, Left, Right)

- Process:

  1. Visit the root node.
  2. Traverse the left subtree.
  3. Traverse the right subtree.

```python
def pre_order_traversal(node):
    if node:
        print(node.data, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)
```

### 4.3 Post-Order Traversal (Left, Right, Root)

- Process:

  1. Traverse the left subtree.
  2. Traverse the right subtree.
  3. Visit the root node.

```python
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")
```

### 4.4 Level-Order Traversal (Breadth-First)

- Process:

  1. Visit nodes level by level from left to right.
  2. Uses a queue to keep track of the nodes.

```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

## 5. Binary Tree Representation in Python

- Node Structure:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

- Simple Binary Tree:

```python
# Let's create the following binary tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
```

## 6. Applications of Binary Trees

- `Expression Trees`: Represent expressions where leaves are operands and internal nodes are operators.
- `Huffman Coding Tree`: Used for data compression.
- `Binary Search Tree (BST)`: A special binary tree used for efficient searching.

## 7. Time Complexity

- `Insertion`, `Deletion`, `Search` (in general binary tree): O(n), where n is the number of nodes.
- `Traversal` (In-order, Pre-order, Post-order, Level-order): O(n).

## 8. Advantages and Disadvantages

- Advantages:
  - `Flexible`: Can be used to implement other data structures such as BST, heaps, and tries.
  - `Efficient Traversals`: Recursive traversal is simple and natural to implement.
- Disadvantages:
  - `Memory Usage`: Each node requires additional storage for pointers to left and right children.
  - `Search time` in general is O(n) if the tree is not balanced.

## 9. Recursive vs Iterative Traversals

### 9.1 Recursive Traversal

- Recursive methods (In-order, Pre-order, Post-order) are more intuitive because they follow a natural structure for trees.
- **Advantage**: Simpler to write and understand.
- **Disadvantage**: Uses the system's call stack which may lead to a **stack overflow** if the tree is too deep.

### 9.2 Iterative Traversal

- Can avoid the system call stack by using an explicit stack (for DFS traversals).
- **Advantage**: No risk of stack overflow, more control over traversal.
- **Disadvantage**: Code can be slightly harder to understand compared to the recursive version.

### Iterative In-Order Traversal

```python
def iterative_in_order_traversal(root):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.value, end=" ")
        current = current.right
```

### Iterative Pre-Order Traversal

```python
def iterative_pre_order_traversal(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.value, end=" ")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### Iterative Post-Order Traversal

```python
def iterative_post_order_traversal(root):
    if not root:
        return
    stack1, stack2 = [root], []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        node = stack2.pop()
        print(node.value, end=" ")
```

## 10. Binary Tree Operations

### 10.1 Insert a Node

- Insert a node at the first available position in level order to maintain the tree structure.

```python
from collections import deque

def insert_node(root, value):
    new_node = TreeNode(value)
    if not root:
        return new_node

    queue = deque([root])
    while queue:
        node = queue.popleft()
        if not node.left:
            node.left = new_node
            return
        else:
            queue.append(node.left)
        if not node.right:
            node.right = new_node
            return
        else:
            queue.append(node.right)
```

### 10.2 Delete a Node

- Deletion in a binary tree involves three main cases:
  - `Node to delete is a leaf`: Simply remove the node.
  - `Node to delete has one child`: Replace the node with its child.
  - `Node to delete has two children`: Find the right-most node of the left subtree or left-most node of the right subtree to replace the deleted node.

```python
def delete_node(root, value):
    if not root:
        return None

    if root.value == value:
        if not root.left and not root.right:
            return None  # Node is a leaf, simply delete it
        if not root.left:
            return root.right  # Node has only right child
        if not root.right:
            return root.left  # Node has only left child
        # Node has two children
        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete_node(root.right, temp.value)
    elif value < root.value:
        root.left = delete_node(root.left, value)
    else:
        root.right = delete_node(root.right, value)

    return root

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current
```

## 11. Binary Tree Depth and Height

- Depth: The depth of a node is the number of edges from the root to that node.
- Height: The height of a node is the number of edges from that node to the deepest leaf.

```python
def height_of_tree(node):
    if not node:
        return -1  # Convention: height of empty tree is -1
    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)
    return max(left_height, right_height) + 1
```

## 12. Binary Tree Balance Check

- A binary tree is balanced if the height of the left and right subtree for every node differ by at most 1.

```python
def is_balanced(node):
    if not node:
        return True  # An empty tree is balanced

    left_height = height_of_tree(node.left)
    right_height = height_of_tree(node.right)

    if abs(left_height - right_height) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)
```

## 13. Binary Tree vs Binary Search Tree

**Binary Tree:**

- No specific order between node values.
- Any general structure.

**Binary Search Tree (BST):**

- For each node, all nodes in its left subtree have smaller values, and all nodes in its right subtree have larger values.
- Efficient for searching, insertion, and deletion.

## Conclusion

- Binary Trees provide a flexible and powerful structure for hierarchical data.
- Understanding tree traversals, node operations, and properties (like depth and height) is critical to solving many real-world problems.

**Common Interview Questions on Binary Tree:**

- How to check if two binary trees are identical?
- How to find the lowest common ancestor (LCA) of two nodes in a binary tree?
- How to convert a binary tree into its mirror tree?
- How to find the diameter (longest path) of a binary tree?
- How to serialize and deserialize a binary tree?
