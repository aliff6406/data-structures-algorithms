""" 
- if the value of the current node is greater than the top end range, search the left subtree
- if the value of the current node is less than the low end range, search the right subtree
- add the value of the current node and recursively find more nodes within the range in the left and right subtrees

Time Complexity: best case scenario - balanced bst = O(logn), worst case scenario - imbalanced bst = O(n)
Space Complexity: worst case scenario O(n)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # Base case
        if not root:
            return 0

        # If the current node's value is out of the range on the higher side
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        
        # If the current node's value is out of the range on the lower side
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        
        # Current node's value is in the range, include it and check both children
        return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)


if __name__ == "__main__":
    # Test using the examples provided
    example1 = TreeNode(10)
    example1.left = TreeNode(5)
    example1.left.left = TreeNode(3)
    example1.left.right = TreeNode(7)
    example1.right = TreeNode(15)
    example1.right.right = TreeNode(18)

    solution = Solution()
    print(solution.rangeSumBST(example1, 7, 15))  # Expected output: 32
