# Python Program to move all zeros to the end (Naive Method)

# function to move all zeroes to the end
def pushZerosToEnd(arr):
    n = len(arr)
    temp = [0] * n  
    
    # to keep track of the index in temp[]
    j = 0

    # Copy non-zero elements to temp[]
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    # Fill remaining positions in temp[] with zeros
    while j < n:
        temp[j] = 0
        j += 1

    # Copy all the elements from temp[] to arr[]
    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)

    # Print the modified array
    for num in arr:
        print(num, end=" ")




        # Python Program to move all zeros to end using two traversals (Better Method)

# Function which pushes all zeros to end
def pushZerosToEnd(arr):
    
    # Count of non-zero elements
    count = 0  

    # If the element is non-zero, replace the element at
    # index 'count' with this element and increment count
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been shifted to
    # the front. Make all elements 0 from count to end.
    while count < len(arr):
        arr[count] = 0
        count += 1

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")


        # Python Program to move all zeros to end using one traversal (Expected Approach)

# Function which pushes all zeros to end of array
def pushZerosToEnd(arr):
    
    # Pointer to track the position for next non-zero element
    count = 0
    
    for i in range(len(arr)):
        
        # If the current element is non-zero
        if arr[i] != 0:
            
            # Swap the current element with the 0 at index 'count'
            arr[i], arr[count] = arr[count], arr[i]
            
            # Move 'count' pointer to the next position
            count += 1

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    pushZerosToEnd(arr)
    for num in arr:
        print(num, end=" ")