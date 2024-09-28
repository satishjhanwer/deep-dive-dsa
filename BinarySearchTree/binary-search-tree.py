# Class definition for a Binary Search Tree Node
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to insert nodes into the Binary Search Tree
def insert_bst(root, value):
    # If tree is empty, create a new node and return it
    if root is None:
        return BSTNode(value)

    # Recursively insert into the left or right subtree
    if value < root.value:
        root.left = insert_bst(root.left, value)
    elif value > root.value:
        root.right = insert_bst(root.right, value)

    return root


# Function to perform In-order traversal
def in_order_traversal_bst(root):
    if root:
        in_order_traversal_bst(root.left)
        print(root.value, end=" ")
        in_order_traversal_bst(root.right)


# Example usage:
# Creating a binary search tree
root_bst = BSTNode(10)
insert_bst(root_bst, 5)
insert_bst(root_bst, 20)
insert_bst(root_bst, 3)
insert_bst(root_bst, 7)
insert_bst(root_bst, 15)

print("In-order traversal of Binary Search Tree:")
in_order_traversal_bst(root_bst)
# Output: 3 5 7 10 15 20
