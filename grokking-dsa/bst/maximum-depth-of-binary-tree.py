""" 
- Depth-First Search (DFS) approach

1. Begin at the root node and traverse down each branch, keeping track of the current branch.
2. The depth increases by one each time we move to a child node.
3. If a node is a leaf (no children), compare its depth with the current max depth and update if necessary.
4. Recursively apply this process to each node's left and right children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if node is null, return 0
        if not root:
            return 0
        
        # Recursively calculate left subtree depth
        leftDepth = self.maxDepth(root.left)
        
        # Recursively calculate right subtree depth
        rightDepth = self.maxDepth(root.right)

        # Return the maximum of left and right subtree depth plus 1 for the current node
        return 1 + max(leftDepth, rightDepth)

if __name__ == "__main__":
    solver = Solution()

    # Example 1
    root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print(solver.maxDepth(root1)) # Expected output: 3

    # Example 2
    root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    print(solver.maxDepth(root2)) # Expected output: 3

    # Example 3
    root3 = TreeNode(1, TreeNode(2, TreeNode(4) , TreeNode(7, None, TreeNode(9))), TreeNode(3))
    print(solver.maxDepth(root3)) # Expected output: 4