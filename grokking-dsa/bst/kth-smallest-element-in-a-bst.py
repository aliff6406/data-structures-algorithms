from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def __init__(self):
        self.count = 0
        self.result = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal
        """ 
        MY ANSWER:
        time complexity: O(k) stops execution once kth smallest element is found

        space complexity: O(1) we are only using two extra variables count and result which take linear space
        """
        def traverse(node, k):
            if node and self.count != k:
                self.kthSmallest(node.left, k)
                self.count += 1
                if self.count == k:
                    self.result = node.val
                self.kthSmallest(node.right, k)

        traverse(root, k)
        return self.result