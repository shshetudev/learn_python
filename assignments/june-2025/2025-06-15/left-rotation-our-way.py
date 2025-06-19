# Python implementation of left rotation of
# an array K number of times

# Function to leftRotate array multiple times


def leftRotate(arr, n, k):
    new_arr = []
    for i in range(k, n):
        new_arr.append(arr[i])

    for i in range(n - k - 1):
        new_arr.append(arr[i])
    return new_arr


# Driver code
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    n = len(arr)
    k = 2  # 2nd rotation: [5, 7, 9, 1, 3]
    print(leftRotate(arr, n, k))

    # Function Call
    # leftRotate(arr, n, k)
    #
    # k = 3
    #
    # # Function Call
    # leftRotate(arr, n, k)
    #
    # k = 4
    #
    # # Function Call
    # leftRotate(arr, n, k)