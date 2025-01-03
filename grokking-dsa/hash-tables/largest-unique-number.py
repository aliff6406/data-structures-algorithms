""" 
Time Complexity: traverse list A = O(n), traverse dict freq = O(n), O(n) + O(n) = O(n)
Space Complexity: O(n) in the worst case, the hashmap will have an entry for each unique number in the array
    worse case scenario is when each element in the list is unique.
"""

from typing import List


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1

        freq = {}

        for num in A:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            if freq[num] == 1:
                maxUnique = max(maxUnique, num)
        
        return maxUnique