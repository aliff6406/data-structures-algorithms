def radixsort(array):
    radix_array = [[], [], [], [], [], [], [], [], [], []]
    max_value = max(array)
    exp = 1 # initialise to 1 to start with the least significant digit

    while max_value // exp > 0:
        while len(array) > 0:
            num = array.pop() # pop last element in array
            radix_index = (num // exp) % 10 # num // exp = floor division to make num into radix we want to focus on, % 10 to get the remainder (last digit)
            radix_array[radix_index].append(num)

        for bucket in radix_array:
            while len(bucket) > 0:
                num = bucket.pop()
                array.append(num)

        exp *= 10


def main():
    array = [1, 6, 7, 232, 54, 32, 18, 3, 4, 45, 5]
    print(f"Unsorted array: {array}")
    radixsort(array)
    print(f"Sorted array: {array}")

if __name__ == "__main__":
    main()
