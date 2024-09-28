# Class definition for a Binary Tree Node
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to insert nodes into the Binary Tree
def insert_binary_tree(root, value):
    # If tree is empty, create a new node and return it
    if root is None:
        return BinaryTreeNode(value)

    # Use a queue to do level order traversal and find the first empty position
    queue = [root]
    while queue:
        current = queue.pop(0)

        # Insert on the left
        if current.left is None:
            current.left = BinaryTreeNode(value)
            return root
        else:
            queue.append(current.left)

        # Insert on the right
        if current.right is None:
            current.right = BinaryTreeNode(value)
            return root
        else:
            queue.append(current.right)


# Function to perform In-order traversal
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)


# Example usage:
# Creating a binary tree
root_bt = BinaryTreeNode(1)
insert_binary_tree(root_bt, 2)
insert_binary_tree(root_bt, 3)
insert_binary_tree(root_bt, 4)
insert_binary_tree(root_bt, 5)

print("In-order traversal of Binary Tree:")
in_order_traversal(root_bt)
# Output: 4 2 5 1 3
