# Approach: One pass search
# Time Complexity: O(n)
def getSecondLargest(arr):
    n = len(arr)
    largest = -1
    secondLargest = -1

    for i in range(n):
        if(arr[i] > largest):
            secondLargest = largest
            largest = arr[i]

        elif(arr[i] < largest and arr[i] > secondLargest):
            secondLargest = arr[i]

    return secondLargest

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(getSecondLargest(arr))