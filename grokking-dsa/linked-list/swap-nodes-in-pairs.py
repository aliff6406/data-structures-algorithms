# Definition for singly-linked list.
from typing import Optional
""" 
Iterative approach

Time Complexity: O(n/2) = O(n) nodes are visited in pairs, execution time grows linearly with input size
Space Complexity: O(1) constant space as a fixed number of variables is used i.e. dummy, previous, firstNode and secondNode
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        previous = dummy

        while head and head.next:
            firstNode = head
            secondNode = head.next

            firstNode.next = secondNode.next
            secondNode.next = firstNode
            previous.next = secondNode

            head = firstNode.next
            previous = firstNode

        return dummy.next
