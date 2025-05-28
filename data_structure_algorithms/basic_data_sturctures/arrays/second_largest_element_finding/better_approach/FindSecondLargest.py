# Time complexity = O(n)
def getSecondLargest(arr):
    n = len(arr)
    # dummy largest and second largest value
    largest = -1
    secondLargest = -1

    # largest
    for i in range(n):
        if (arr[i] > largest):
            largest = arr[i]

    # second largest
    for i in range(n):
        if (arr[i] > secondLargest and arr[i] != largest):
            secondLargest = arr[i]

    return secondLargest


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))
