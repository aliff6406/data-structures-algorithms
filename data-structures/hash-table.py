""" 
Naive implementation of a hash table data structure. We use the modular hashing.
"""

class Record:
    def __init__(self, key=-1, title="", placementInfo=""):
        self.key = key
        self.title = title
        self.placementInfo = placementInfo

class HashTable:
    def __init__(self, size):
        # python convention, prefix with _ (underscore) to denote private field
        self.maxLength = size
        self.length = 0
        self.HTArray = [Record() for _ in range(size)]

    def hashFunction(self, key):
        return key % self.maxLength


    def insert(self, item):
        if self.length == self.maxLength:
            print("Hash table is full. Cannot insert the key value pair.")
            return False
        
        index = self.hashFunction(item.key)
        self.HTArray[index] = item
        self.length += 1
        return True
    
    # Time complexity: O(1)
    def search(self, key, returnedItem):
        index = self.hashFunction(key)
        if self.HTArray[index].key == -1:
            return False
        returnedItem.key = self.HTArray[index].key
        returnedItem.title = self.HTArray[index].title
        returnedItem.placementInfo = self.HTArray[index].placementInfo
        return True
    
    # Time complexity: O(1)
    def delete(self, key):
        index = self.hashFunction(key)
        if self.HTArray[index].key == key:
            self.HTArray[index].key = -1
            self.length -+ 1
            return True
        return False
    
