"""
Data types: 
-----------
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

greetings = "Hello World" # text type

# Numeric type
int_num = 42
float_num = 3.14
complex_num = 2+3j

############ Sequence type
# list
print("Printing list: ")
my_num_list = [1,2,3,4,5] # list -> iterate through loop(for, while)
for number in my_num_list:
    print(number)

# tuple
print("Printing tuples: ")
my_tuple = (1,2,3,4,5)
for tuple in my_tuple:
    print(tuple)
  
# range
print("Printing range: ")
my_range = range(5)
for range_num in my_range:
    print(range_num)  

############# Mapping type (key: value): O(1)
print("Printing dictionary: ")
my_dictionary = {"name": "Shabab", "country": "BD", "age": 30} 
for key, value in my_dictionary.items():
        print(f"{key}: {value}")

######## Set type

# set
print("Printing set: ")
my_set = {1, 2, 3, 4, 5} # Never allows duplicate value, and shows in sorted order
my_set.add(6)
for set_num in my_set:
     print(set_num)

# frozen set
print("Printing frozen range: ")
frozen_set = frozenset({1, 2, 3, 4, 5})
for fr_set_num in frozen_set:
     print(fr_set_num)