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
