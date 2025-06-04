# O(n^2)
def move_all_zeros_to_the_end(arr):
    # iterate through the array -> check if the element is zero -> If it is zero then remove it and append it to the end of the array
    size = len(arr)
    for i in range(size):
        if arr[i] == 0:
            arr.remove(0)
            arr.append(0)
    return arr


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    # arr = [10, 20, 30]
    # arr = [0, 0]
    print(move_all_zeros_to_the_end(arr))
