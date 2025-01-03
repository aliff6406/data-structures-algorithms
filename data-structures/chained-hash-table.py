class Record:
    def __init__(self, key, title, placementInfo):
        self.key = key
        self.title = title
        self.placementInfo = placementInfo

class HashTable:
    def __init__(self, size):
        self.maxLength = size # max number of buckets
        self.buckets = [[] for _ in range(size)]

    def hashFunction(self, key):
        return key % self.maxLength

    def insert(self, item):
        index = self.hashFunction(item.key)

        for record in self.buckets[index]:
            if record.key == item.key:
                # key already exists in the chain, cannot insert
                return False 
        
        self.buckets[index].append(item)
        return True
    
    def search(self, key, returnedItem: Record):
        index = self.hashFunction(key)

        for record in self.buckets[index]:
            if record.key == key:
                returnedItem.key = record.key
                returnedItem.title = record.title
                returnedItem.placementInfo = record.placementInfo
                return True
            
        return False
    
    def delete(self, key):
        index = self.hashFunction(key)

        for i, record in enumerate(self.buckets[index]):
            if record.key == key:
                del self.buckets[index][i]
                return True
        
        return False
    
    def showTable(self):
        print("Index\tValue (key, title, placementInfo)")
        for i in range(self.maxLength):
            print(i, end="\t")
            if not self.buckets[i]:
                print("[EMPTY BUCKET]")
            else:
                for j, record in enumerate(self.buckets[i]):
                    if j > 0:
                        print("-->", end=" ")
                    print("({0}, {1}, {2})".format(record.key, record.title, record.placementInfo), end=" ")
                print()

def main():
    tableSize = 11
    hashTable = HashTable(tableSize)

    # insert initial book information
    hashTable.insert(Record(1701, "Internet of Things", "G1 Shelf"))
    hashTable.insert(Record(1712, "Statistical Analysis", "G1 Shelf"))
    hashTable.insert(Record(1718, "Grid Computing", "H2 Shelf"))
    hashTable.insert(Record(1735, "UML Modeling", "G1 Shelf"))
    hashTable.insert(Record(1752, "Professional Practices", "G2 Shelf"))

    # Display the hash table after initial insertions
    print("\nHash Table after initial insertions:")
    hashTable.showTable()

    # insert the following record
    hashTable.insert(Record(1725, "Deep Learning with Python", "C3 Shelf"))

    # Display the hash table after the last insertion
    print("\nHash Table inserting Book key 1725:")
    hashTable.showTable()

    # delete two records
    hashTable.delete(1701)
    hashTable.delete(1718)

    # Display the hash table after deletions
    print("\nHash Table after deleting 1701 and 1718:")
    hashTable.showTable()

if __name__ == "__main__":
    main()