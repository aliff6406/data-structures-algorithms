def countsort(array):
    max_value = max(array)
    count = [0] * (max_value + 1) # initialise count array (+1 because 0 to max)

    while len(array) > 0:
        num = array.pop(0) # pop the first element of the array
        count[num] += 1 # increment the value index in the count array

    for i in range(len(count)):
        while count[i] > 0:
            array.append(i)
            count[i] -= 1

    return array

def main():
    array = [1, 6, 7, 232, 54, 32, 18, 3, 4, 45, 5]
    print(f"Unsorted array: {array}")
    array = countsort(array)
    print(f"Sorted array: {array}")

if __name__ == "__main__":
    main()