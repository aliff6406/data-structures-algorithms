# Definition for a binary tree node.
from typing import Optional

""" 
Recursive approach:
1. if root1 or root2 is null, return the other tree root node
2. if neither are null, create a new node with the sum of their values
3. Recursively set the children nodes by calling mergeTrees on both trees' left and right children
4. return the new root

n and m are the number of nodes in the respective trees
Time Complexity: O(min(n,m)) each node is visited exactly once
Space Complexity: O(min(n,m)) we are creating a new node for each node in the original trees
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        # if both root1 and root2 are null, newNode will also be null
        newNode = TreeNode(root1.val + root2.val)

        newNode.left = self.mergeTrees(root1.left, root2.left)
        newNode.right = self.mergeTrees(root1.right, root2.right)

        return newNode