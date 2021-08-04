# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name
# The values in dictionary items can be of any data type
# Duplicate values will overwrite existing values

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

# You can access the items of a dictionary by referring to its key name, inside square brackets
print(thisdict["brand"])
# The get() method also achieves this
x = thisdict.get("model")

# The keys() method will return a list of all the keys in the dictionary
# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list
# The above is also true for the values() and items() methods
# The values() method will return a list of all the values in the dictionary
# The items() method will return each item in a dictionary, as tuples in a list

# To determine if a specified key is present in a dictionary use the 'in' keyword

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument
# The argument must be a dictionary, or an iterable object with key:value pairs
thisdict.update({"year": 2021})

# Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict["color"] = "white"

# Removing Items
myDict = {
    "First Name": "Audrey",
    "Last Name": "Main",
    "Age": 20,
    "Major": "Game Design and Development",
    "Height": 160,  # cm
    "Blood Type": "A+"
}
print(myDict)
# The pop() method removes the item with the specified key name
myDict.pop("Age")
print(myDict)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
myDict.popitem()
print(myDict)
# The del keyword removes the item with the specified key name
del myDict["Height"]
print(myDict)
# The clear() method empties the dictionary
myDict.clear()
print(myDict)

# Looping Through a Dictionary
# When looping through a dictionary, the return values are the keys of the dictionary,
# but there are methods to return the values as well

# Print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)

# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)

# Copying a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1,
# because: dict2 will only be a reference to dict1,
# and changes made in dict1 will automatically also be made in dict2
# The copy() and dict() methods allow us to make copies
dict_1 = thisdict.copy()
dict_2 = dict(thisdict)

# Dictionaries have the capability to be nested, that is, a dictionary
# can contain other dictionaries
pet_1 = {"name": "Mei Mei", "species": "cat"}
pet_2 = {"name": "Chester", "species": "dog"}
myPets = {"Chester": pet_2, "Mei Mei": pet_1}

# Dictionary Methods

'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''