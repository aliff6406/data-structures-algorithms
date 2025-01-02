# Definition for singly-linked list.
from typing import Optional

""" 
Iterative approach

Time complexity: O(n) each node in the linked list is visited exactly once
Space Complexity: O(1) fixed number of variable is used, in this case only current, hence constant space
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        # stop execution if there is no more next node
        while current and current.next: 
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head