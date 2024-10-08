class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_node_present(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    # Recursively search in left and right subtrees
    return is_node_present(root.left, value) or is_node_present(root.right, value)
# Example usage:
# Create a binary tree
#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Example checks
print(is_node_present(root, 5))   # Output: True
print(is_node_present(root, 8))