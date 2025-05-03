# We will follow the sorting approach to find the second largest element in an array.
# Time Complexity: O(nlogn)

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34

# Time complexity of this algorithm: O(nlogn) = Log linear
def find_second_largest_element(arr):
    size = len(arr)  # O(1) = Constant time complexity

    arr.sort()  # O(nlogn) = Log linear time complexity

    for i in range(size - 2, -1, -1):  # O(n) = Linear time complexity, handles n operations, eg: 12, 35, 1, 10, 34, 1 = number of inputs(n)
        if arr[i] != arr[size - 1]:  # O(1) = Constant time complexity, handles with 1 operation, eg: 10 != 5 -> true
            return arr[i] # O(1)
    return -1 # O(1)

# Time complexity calculation:
# = O(1) + O(nlogn) + O(n) + O(1) + O(1) + O(1)
# = O(nlogn) + (O(n) + 4O(1))
# = (O(nlogn) + O(n))
# = O(nlogn)


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1] # n = 6
    # arr = [10, 10, 10]
    # arr = [-1, -5, -7]
    # arr = [0, 0, 0]
    # arr = [10, 5, 10]
    print(find_second_largest_element(arr))



    # 10 10 10 [sorted]
    # largest: 15
