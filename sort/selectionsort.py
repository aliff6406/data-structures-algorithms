
def selectionsort(array):
    n = len(array)

    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j

        '''
        # Not optimised as all elements preceding the removed element has to be shifted one space down
        # and all elements must be shifted one space up when inserting the value at the start of the array
        '''
        # min_value = array.pop(min_index)
        # array.insert(i, min_value)
        
        # Solution: Swap min value and first value of the array
        array[min_index], array[i] = array[i], array[min_index]


def main():
    array = [1, 5, 2, 3, 52, 15, 4]
    print(f"Unsorted array: {array}")
    selectionsort(array)
    print(f"Sorted array: {array}")

if __name__ == "__main__":
    main()
