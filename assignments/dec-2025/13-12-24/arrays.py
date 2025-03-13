# Arrays are used to store multiple values in a single variable.
# In Python, we typically use lists as arrays, though to work with true arrays, you would need to import a library like NumPy.

# Example: Create a list (array) containing car names
cars = ["Ford", "Volvo", "BMW"]

# What is an Array?
# An array (list) holds multiple values under a single variable name.
# Instead of having separate variables like:
# car1 = "Ford"
# car2 = "Volvo"
# car3 = "BMW"
# You can use an array to store them all in one place.

# Accessing Array Elements
# You refer to an array element using its index number. Indexing starts from 0.
# Example: Get the value of the first array item
x = cars[0]  # x will be "Ford"

# Example: Modify the value of the first array item
cars[0] = "Toyota"  # Now, cars[0] will be "Toyota"

# The Length of an Array
# Use the len() method to find the number of elements in the array.
x = len(cars)  # x will be 3 because there are 3 elements in the cars list

# Looping Through Array Elements
# Use a for loop to loop through all elements in the array
for x in cars:
    print(x)  # Prints each car in the cars list

# Adding Array Elements
# Use the append() method to add an element to the end of the array
cars.append("Honda")  # Now the cars list will be ["Toyota", "Volvo", "BMW", "Honda"]

# Removing Array Elements
# Use the pop() method to remove an element by index
cars.pop(1)  # Removes the element at index 1 ("Volvo")

# Use the remove() method to remove an element by value
# cars.remove("Volvo")  # Removes the first occurrence of "Volvo"

# Array Methods
# Python provides several built-in methods for working with lists (arrays)

# append() - Adds an element at the end of the list
cars.append("Ford")

# clear() - Removes all elements from the list
cars.clear()  # cars will be an empty list

# copy() - Returns a copy of the list
new_cars = cars.copy()

# count() - Returns the number of times a specified value appears in the list
count = cars.count("Ford")

# extend() - Adds elements from another list (or any iterable) to the end of the current list
cars.extend(["BMW", "Honda"])

# index() - Returns the index of the first occurrence of a specified value
index = cars.index("BMW")  # Finds the index of "BMW"

# insert() - Adds an element at a specific position in the list
cars.insert(1, "Mercedes")  # Inserts "Mercedes" at index 1

# pop() - Removes an element at the specified position
cars.pop(0)  # Removes the first element from the list

# remove() - Removes the first occurrence of a specified value
cars.remove("Honda")  # Removes "Honda" from the list

# reverse() - Reverses the order of the list
cars.reverse()  # The list is now reversed

# sort() - Sorts the list
cars.sort()  # The list will now be sorted alphabetically