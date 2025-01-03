class Solution:
    def firstUniqChar(self, s: str) -> int:
        # initialise an empty dict (python implements dictionary using hash table)
        # key = char, value = frequency
        freq = {}

        # iterate over the string and count frequency of each char
        for char in s:
            # if char not found return 0, add one
            freq[char] = freq.get(char, 0) + 1

        for idx, char in enumerate(s):
            # if character is unique (frequency = 1) return the index of the character
            if freq[char] == 1:
                return idx
            
        return -1

