def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1): # n-i-1 because after each outer loop iter. the largest value is already placed at the end (no need to compare it again)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def main():
    array = [1, 5, 2, 3, 52, 15, 4]
    print(f"Unsorted array: {array}")
    bubblesort(array)
    print(f"Sorted array: {array}")

if __name__ == "__main__":
    main()

