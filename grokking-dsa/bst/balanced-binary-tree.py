""" 
- Depth-First Search (DFS) approach

1. recursively compute the height of both the left and right subtree
2. if the difference between the height is greater than 1 at any node, return -1 (imbalanced)
3. -1 propogates up

Time Complexity: O(n) each node is visited exactly once
Space Complexity: worst case scenario - O(n) if tree is imbalanced
"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depth(self, node):
        # If node is None, return depth as 0
        if not node:
            return 0

        # Calculate depth of left child
        leftDepth = self.depth(node.left)
        if leftDepth == -1:
            return -1

        # Calculate depth of right child
        rightDepth = self.depth(node.right)
        if rightDepth == -1:
            return -1

        # Check if the current node is unbalanced
        if abs(leftDepth - rightDepth) > 1:
            return -1

        # Return depth of the current subtree
        return max(leftDepth, rightDepth) + 1

    def isBalanced(self, root):
        return self.depth(root) != -1

if __name__ == "__main__":
    # Test example 1
    example1 = TreeNode(3)
    example1.left = TreeNode(9)
    example1.right = TreeNode(20)
    example1.right.left = TreeNode(15)
    example1.right.right = TreeNode(7)

    # Test example 2
    example2 = TreeNode(1)
    example2.left = TreeNode(2)
    example2.left.left = TreeNode(3)
    example2.left.left.left = TreeNode(4)
    example2.right = TreeNode(5)

    solution = Solution()
    print(solution.isBalanced(example1))  # Expected output: true
    print(solution.isBalanced(example2))  # Expected output: false
