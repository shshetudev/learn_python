# Python program to rearrange an array in minimum
# maximum form

# Function to rearrange the array elements alternately
def rearrange(arr):
    n = len(arr)
    temp = [0] * n

    # Indexes of smallest and largest elements
    small, large = 0, n - 1

    # To indicate whether we need to copy remaining
    # largest or remaining smallest at next position
    flag = True

    # Store result in temp[]
    for i in range(n):
        if flag:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1
        flag = not flag

    # Copy temp[] to arr[]
    for i in range(n):
        arr[i] = temp[i]


# Driver code
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)

print("Original Array")
for x in arr:
    print(x, end=" ")

rearrange(arr)

print("\nModified Array")
for x in arr:
    print(x, end=" ")