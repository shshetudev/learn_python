# sets are used to store multiple values in a single python variable
thisset = {"apple", "banana", "cherry"}
print(thisset)
# displaying how their cannot be duplicate values in a set
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# the values true, and 1 cannot be in the same set as python considers them duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
# same applies for false, and 0
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# you could find the length of a set by doing these lines of code
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# sets have 3 different data types
set1 = {"apple", "banana", "cherry"} # string
set2 = {1, 5, 7, 9, 3} # integers
set3 = {True, False, False} # booleans
# an example of a set with all three data types
set1 = {"abc", 34, True, 40, "male"}
# to check if something is a set or not, run these lines of code
myset = {"apple", "banana", "cherry"}
print(type(myset))
# you could loop through a set by doing something like this
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
# to check if a item is present in a set
  thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# to check if an item is not present in a set
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
# once a set is created, you cannot change any of its items but rather add them with this method
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# you can also add items from another set into a different set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# you can also add items from a list into a set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
# as you can add items, you can also review items from a set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# you can do the same with the discard method
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# you can remove a random item from a set using the pop method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)
# you can remove all items from a set using the clear method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# you can delete a set with the del function
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
# loop through sets wiith these lines of code
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
# you can merge 2 sets with the union feature
  set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# this can also be substituted for the | feature
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
# you can also merge more than 2 sets together
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)