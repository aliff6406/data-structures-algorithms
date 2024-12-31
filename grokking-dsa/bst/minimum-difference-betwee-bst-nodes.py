""" 
- In-Order Traversal (left subtree > node > right subtree) approach

1. Perform in order traversal to create a list of sorted nodes
2. Find the minimum difference by comparing each pair in the list

Time Complexity: 
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # List to hold the values in order.
        self.nodes = []

    # time complexity = O(n), space complexity = O(n) in worst case scenario
    def inorderTraversal(self, node):
        """Helper function to perform the in-order traversal."""
        if not node:
            return
        self.inorderTraversal(node.left)   # Recursively visit the left subtree.
        # space complexity = O(n) - one element for each node
        self.nodes.append(node.val)        # Add the current node's value to the list.
        self.inorderTraversal(node.right)  # Recursively visit the right subtree.

    def minDiffInBST(self, root):
        # Clear the nodes list to ensure it's empty.
        self.nodes.clear()
        
        # First, perform the in-order traversal.
        self.inorderTraversal(root)

        # Find the minimum difference between each consecutive pair.
        min_diff = float('inf')
        # time complexity = O(n), 
        for i in range(1, len(self.nodes)):
            min_diff = min(min_diff, self.nodes[i] - self.nodes[i - 1])

        return min_diff

if __name__ == "__main__":
    # First test case
    example1 = TreeNode(4)
    example1.left = TreeNode(2)
    example1.left.left = TreeNode(1)
    example1.left.right = TreeNode(3)
    example1.right = TreeNode(6)

    # Second test case
    example2 = TreeNode(40)
    example2.right = TreeNode(70)
    example2.right.left = TreeNode(50)
    example2.right.right = TreeNode(90)

    solution = Solution()

    print(solution.minDiffInBST(example1))  # Expected output: 1
    print(solution.minDiffInBST(example2))  # Expected output: 10 (50-40)
