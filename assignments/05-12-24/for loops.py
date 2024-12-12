# A for loop is used to iterate over a sequence like a list, tuple, set, or string

# Loop through each item in a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:  # x will take the value of each item in the list
    print(x)  # Print each fruit

# Loop through each character in a string (strings are iterable)
for x in "banana":  # x will take the value of each character in "banana"
    print(x)  # Print each character

# The break statement exits the loop before it finishes all iterations
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)  # Print each fruit
    if x == "banana":  # If x is banana, break the loop
        break

# The continue statement skips the current iteration and moves to the next
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":  # If x is banana, skip this iteration
        continue
    print(x)  # Print each fruit except banana

# The range() function generates a sequence of numbers, useful for looping a fixed number of times
for x in range(6):  # x will take values from 0 to 5
    print(x)  # Print each number

# You can specify a starting value and an increment for the range()
for x in range(2, 6):  # x will take values from 2 to 5
    print(x)  # Print each number

# You can also specify the increment (default is 1)
for x in range(2, 30, 3):  # x will take values from 2, 5, 8, ..., up to 29
    print(x)  # Print each number

# The else block in a for loop executes when the loop finishes (if not stopped by break)
for x in range(6):
    print(x)  # Print each number
else:
    print("Finally finished!")  # Print this after the loop finishes

# If the loop is stopped by a break statement, the else block is not executed
for x in range(6):
    if x == 3: break  # Exit the loop when x is 3
    print(x)  # Print each number
else:
    print("Finally finished!")  # This will NOT be printed because the loop was broken

# Nested loops: a loop inside another loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:  # Outer loop: for each adjective
    for y in fruits:  # Inner loop: for each fruit
        print(x, y)  # Print each combination of adjective and fruit

# The pass statement is used to avoid errors if a loop has no content
for x in [0, 1, 2]:
    pass  # Nothing happens, but no error occurs