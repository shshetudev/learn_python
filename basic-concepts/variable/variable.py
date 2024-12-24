# Creating variables
name = "Shahariar"
print(name)

# Casting
num_str = str(3)
int_num = int(3)
float_num = float(3)

print(num_str) # 3
print(int_num) # 3
print(float_num) # 3.0

# Get the type
print(type(num_str)) # <class 'str'>
print(type(int_num)) # <class 'int'>

# Case sensitive
a = 4
A = "Shabab"

print(a == A) # False

# Variable names, No: can not start with a number, case-sensitive, can not be any of the keywords
student_name = "Shabab" # Snake case -> Python standard/JS
# student-name = "Shabab" # Cabab case
studentName = "Shabab" # Camel case -> Java standard / JS / Python
StudentName = "Shabab" # Pascal case
_student_name = "Shabab" # JS: Private variables
studentname = "Shabab"
STUDENTNAME = "Shabab" # Final/Constant variable
studentname1 = "Shabab"

# Many values to multiple varialbles
orange, banana, mango = "Orange", "Banana", "Mango"
print(orange, banana, mango)

# One Value to multiple variables
nice_flower = red_flower = flower_with_throne = "Rose"
print(nice_flower, red_flower, flower_with_throne)

# Unpack a collection
birds = ["Magpie", "Robin", "Sparrow"] # Collection: List
bird1, bird2, bird3 = birds # Array destructing
print(bird1, bird2, bird3)

# Output variables: print() is used to output the variable
print(bird1+bird2+bird3) # String concatenation

print(10+5) # Addition

print(bird1 + str(10))

print(bird1, 10)

# Global variables
compliment = "Superb!"
def generateCompliments():
    print(compliment)

    global secondCompliment # Using global keyword
    secondCompliment = "Awesome"

generateCompliments() # Function call    
print(secondCompliment)