'''
# The insertion sort algorithm below is unoptimal as all elements must shift down when the element from the unsorted part is removed
# and shifted up when the element is placed into the sorted part of the array
def insertionsort(array):
    n = len(array)

    for i in range(1, n):
        insert_index = i
        current_value = array.pop(i)

        for j in range(i-1, -1, -1):
            if array[j] > current_value:
                insert_index = j

        array.insert(insert_index, current_value)
'''

def insertionsort(array):
    n = len(array)

    for i in range(1, n):
        # insert_index = i
        current_value = array[i]
        j = i - 1 # start at index before the unsorted part of the array

        # for j in range(i-1, -1, -1):
        #     if array[j] > current_value:
        #         array[j+1] = array[j] # shift the element one up in memory (overrides the current_value in memory)
        #         insert_index = j
        #     else:
        #         break
        #     array[insert_index] = current_value

        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j] # shift the element one up in memory
            j -= 1

        array[j + 1] = current_value # insert the current value (value to be sorted) into the open space (+1 because we -1 at the start of the loop)


def main():
    array = [1, 5, 2, 3, 52, 15, 4]
    print(f"Unsorted array: {array}")
    insertionsort(array)
    print(f"Sorted array: {array}")

if __name__ == "__main__":
    main()
