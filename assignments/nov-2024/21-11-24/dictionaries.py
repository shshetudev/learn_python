# dictionaries are used to store data in key:value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# you can refer a dictionariy by its key name in its key:value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
# unlike sets and tuples, not only can the dictionaries items be removed and added, they can be changed too
# however like sets, there cannot be duplicate values in a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
# you can print the length of a dictionary by doing this
print(len(thisdict))
# the values in dictionaries can be of any data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
# to identify a dictionary...
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
# you can also make a dictionary using the dict() method
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
# you can access items of a dictionary by refering to its key name inside square brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# as an alternative, you can use the get() method
x = thisdict.get("model")
# this method will return all the keys present in the dictionary
x = thisdict.keys()
# contrary to that, this method will return all the values from the key:value in the dictionary
x = thisdict.values()
# this method will return each item in a dictionary as a tuple in a list
x = thisdict.items()
# you can check if a key exists by doing this
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
# you can change values in a dictionary by doing this 
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
# you can do the same using the update method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
# you can add a new item to a dictionary by assigning a new index key and a corresponding value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# the pop function removes a item from a dictionary by providing a index key
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# the del keyword can remove items from a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# the del keyword can also delete the entirety of a dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
# the clear method clears the dictionary but does not delete it
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
# you can loop through a dictionary by doing this
for x in thisdict:
  print(x)
# you can also print every value one by one in a dictionary by doing this
for x in thisdict:
  print(thisdict[x])
# you can also do the same by using the values() method
for x in thisdict.values():
  print(x)
# use the keys method to return all of the keys in a dictionary
for x in thisdict.keys():
  print(x)
# you can loop through both keys and values by using the item() method
for x, y in thisdict.items():
  print(x, y)
# you could make a copy of a dictionary with the copy method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# you could do the same with the dict() function
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# a dictionary can contain more dictionaries, this is called nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
# you can also do this by creating three dictionaries and then creating 1 dictionary that will contain the three
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
# you can access items from a nested dictionary
print(myfamily["child2"]["name"])
# you can loop through a nested dictionary by doing this
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])

