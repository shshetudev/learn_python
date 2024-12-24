# An iterator is an object that can be iterated upon, meaning you can loop through all its values.

# Iterator vs Iterable:
# - Iterable objects (like lists, tuples, dictionaries) can return an iterator.
# - The iterator implements the methods __iter__() and __next__().

# Example: Using iterators with a tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)  # Get an iterator from the tuple

# Using the next() method to get each value
print(next(myit))  # Output: apple
print(next(myit))  # Output: banana
print(next(myit))  # Output: cherry

# Example: Using iterators with a string
mystr = "banana"
myit = iter(mystr)  # Get an iterator from the string

# Using the next() method to get each character
print(next(myit))  # Output: b
print(next(myit))  # Output: a
print(next(myit))  # Output: n
print(next(myit))  # Output: a
print(next(myit))  # Output: n
print(next(myit))  # Output: a

# Looping through an iterator using a for loop
# The for loop automatically creates an iterator object and calls next() for each item.

# Example: Iterate through a tuple
for x in mytuple:
    print(x)  # Output: apple, banana, cherry

# Example: Iterate through a string
for x in mystr:
    print(x)  # Output: b, a, n, a, n, a

# Creating a custom iterator
# We need to implement the methods __iter__() and __next__() in a class.

class MyNumbers:
    def __iter__(self):
        self.a = 1  # Initialize the starting value
        return self  # Return the iterator object

    def __next__(self):
        x = self.a  # Get the current value
        self.a += 1  # Increment the value for the next iteration
        return x  # Return the value

# Create an iterator object
myclass = MyNumbers()
myiter = iter(myclass)  # Get an iterator from the class object

# Use next() to get the values from the iterator
print(next(myiter))  # Output: 1
print(next(myiter))  # Output: 2
print(next(myiter))  # Output: 3

# StopIteration
# If we want to stop the iteration after a certain number of values, we can raise StopIteration.

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:  # Stop the iteration after 20
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration  # Stop the iteration

# Create an iterator object
myclass = MyNumbers()
myiter = iter(myclass)

# Use a for loop to automatically handle the StopIteration exception
for x in myiter:
    print(x)  # Output: 1, 2, 3, ..., 20