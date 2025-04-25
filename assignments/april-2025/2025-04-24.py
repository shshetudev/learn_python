# Lists in Python can hold different types of items and grow in size automatically.
a = [1, "Hello", [3.14, "world"]]
a.append(2)  # Add a number to the list
print(a)  # Output: [1, 'Hello', [3.14, 'world'], 2]

# NumPy arrays are great for math and big data.
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr * 2)  # Multiply each item by 2 (Output: [2 4 6 8])

# 2D NumPy array (like a matrix)
arr2d = np.array([[1, 2], [3, 4]])
print(arr2d * 2)  # Multiply each item by 2 (Output: [[2 4] [6 8]])

# Python arrays: Better for large, same-type data. 
import array as arr

a = arr.array('i', [1, 2, 3])
print(a[0])  # Get the first item (Output: 1)

a.append(5)  # Add an item to the array
print(a)  # Output: array('i', [1, 2, 3, 5])

# Loop through the array and print each item
for i in range(0, 3):
    print(a[i], end=" ")  # Output: 1 2 3

# Insert an item at a specific position
a.insert(1, 4)
print("\nAfter insertion:", *a)  # Output: 1 4 2 3 5

# Access items using their position (index)
print(a[0])  # Output: 1
print(a[3])  # Output: 3

# Remove items using remove() and pop()
arr = arr.array('i', [1, 2, 3, 1, 5])
arr.remove(1)  # Remove the first 1
print(arr)  # Output: array('i', [2, 3, 1, 5])

arr.pop(2)  # Remove item at position 2
print(arr)  # Output: array('i', [2, 3, 5])

# Slicing the array to get specific parts
a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(a[3:8])  # Get items from position 3 to 7 (Output: [4, 5, 6, 7, 8])
print(a[5:])   # Get items from position 5 to the end (Output: [6, 7, 8, 9, 10])
print(a[:])    # Get the whole array (Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Find the position of an item in the array
arr = arr.array('i', [1, 2, 3, 1, 2, 5])
print(arr.index(2))  # First 2 is at position 1 (Output: 1)
print(arr.index(1))  # First 1 is at position 0 (Output: 0)

# Change an item in the array by its position
arr[2] = 6
print(arr)  # Output: array('i', [1, 2, 6, 1, 2, 5])

arr[4] = 8
print(arr)  # Output: array('i', [1, 2, 6, 1, 8, 5])

# Count how many times an item shows up in the array
arr = arr.array('i', [1, 2, 3, 4, 2, 5, 2])
print("Count of 2:", arr.count(2))  # Output: 3

# Reverse the array
arr.reverse()
print("Reversed array:", *arr)  # Output: 5 8 1 6 2 5 2 4 3 2 1

# Add multiple items to the array
a = arr.array('i', [1, 2, 3, 4, 5])
a.extend([6, 7, 8, 9, 10])
print(a)  # Output: array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])