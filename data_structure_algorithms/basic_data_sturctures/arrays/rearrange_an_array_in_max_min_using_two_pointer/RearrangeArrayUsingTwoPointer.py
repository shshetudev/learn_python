def rearrange_an_array_in_max_min_using_two_pointer(arr):
    size = len(arr)

    l = 0
    h = size-1
    rearranged_array = []

    # 0 < 6
    # 1 < 5
    # 2 < 4
    # 2 < 4
    # 3 <= 3
    # 3 <= 2
    while l <= h:
        rearranged_array.append(arr[h]) # [7] -> [7,1,6] -> [7,1,6,2,5,3,4]
        h = h - 1 # 5 -> 4 -> 3 -> 2
        if h > l: # 2 > 3
            rearranged_array.append(arr[l]) # [7,1] -> [7,1,6,2] -> [7,1,6,2,5,3]
            l = l + 1 # 1 -> 2 -> 3
    return rearranged_array


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(rearrange_an_array_in_max_min_using_two_pointer(arr)) # {7, 1, 6, 2, 5, 3, 4}