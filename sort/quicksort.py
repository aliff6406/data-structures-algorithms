def partition(array, low, high):
    pivot = array[high] # pivot value = last element of array
    i = low - 1 # i initialised to index before first element

    # iterate through sub-array
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    # place pivot at the right index -> swap index i + 1 and pivot
    array[i+1], array[high] = array[high], array[i+1]

    # return new index of pivot which is where the partition is between the new sub arrays
    return i + 1
    
def quicksort(array, low=0, high=None):
    # if high is not initialised, set it to last index of array
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

def main():
    array = [1, 6, 7, 232, 54, 32, 18, 3, 4, 45, 5]
    print(f"Unsorted array: {array}")
    quicksort(array)
    print(f"Sorted array: {array}")

if __name__ == "__main__":
    main()
