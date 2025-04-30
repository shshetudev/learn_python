# We will follow the sorting approach to find the second largest element in an array.
# Time Complexity: O(nlogn)

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34

def find_second_largest_element(arr):
    size = len(arr)  # 6

    arr.sort()  # [1, 1, 10, 12, 34, 35] -> We have to find out the number that is less than 35

# range[1, -1] -> [1, 0] start at: 1st index and end at: 0th index
# 1st iteration: i = 1
    # 2nd interation: i = 1-1 = 0
     # 3rd iteration: i = 0 - 1 -> loop breaks
    for i in range(size - 2, -1, -1):  # [4, -1, -1] -> start from: 4th index, end at: 0th index, decrementing by 1 (Backward traversal)
        if arr[i] != arr[size - 1]:  # 34 != 35
            return arr[i]  # Second largest element
    return -1  # If no second-largest element is found


if __name__ == "__main__":
    # arr = [12, 35, 1, 10, 34, 1]
    # arr = [10, 10, 10]
    # arr = [-1, -5, -7]
    # arr = [0, 0, 0]
    arr = [10, 5, 10]
    print(find_second_largest_element(arr))



    # 10 10 10 [sorted]
    # largest: 15
