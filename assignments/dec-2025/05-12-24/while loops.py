# Python has two types of loops: while loops and for loops

# The while loop executes a block of code as long as a condition is True
i = 1
while i < 6:  # As long as i is less than 6, the loop will run
    print(i)  # Print the current value of i
    i += 1  # Increment i to avoid an infinite loop

# The break statement allows us to exit the loop early if a certain condition is met
i = 1
while i < 6:
    print(i)  # Print the current value of i
    if i == 3:  # If i equals 3, exit the loop
        break
    i += 1  # Increment i to avoid an infinite loop

# The continue statement skips the current iteration and moves to the next one
i = 0
while i < 6:
    i += 1  # Increment i
    if i == 3:  # If i equals 3, skip this iteration
        continue
    print(i)  # Print the current value of i (will not print when i is 3)

# The else statement can be used to execute code after the loop ends, once the condition is False
i = 1
while i < 6:
    print(i)  # Print the current value of i
    i += 1  # Increment i
else:  # Once the while loop condition is no longer true (i >= 6), this block executes
    print("i is no longer less than 6")