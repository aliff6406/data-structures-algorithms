""" 
Iterative approach

Time Complexity: O(n) - visits each node of the linked list exactly once
Space Complexity: O(1) - uses fixed number of extra variables, prev, current and nextNode,
    hence takes constant space (does not grow with input size (number of nodes in linked list))
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
           nextNode = current.next
           current.next = prev
           prev = current
           current = nextNode
        return prev
    
    @staticmethod
    def printList(head):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    head1 = Node(3, Node(5, Node(2)))
    Solution.printList(solution.reverseList(head1))  # Expected Output: 2 5 3
    
    # Test case 2
    head2 = Node(7)
    Solution.printList(solution.reverseList(head2))  # Expected Output: 7
    
    # Test case 3
    head3 = Node(-1, Node(0, Node(1)))
    Solution.printList(solution.reverseList(head3))  # Expected Output: 1 0 -1
