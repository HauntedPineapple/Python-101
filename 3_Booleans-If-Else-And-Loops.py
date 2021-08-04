# Booleans - represent one of two values: True or False

# Almost any value is evaluated to True if it has some sort of content.
#   Any string is True, except empty strings.
#   Any number is True, except 0.
#   Any list, tuple, set, and dictionary are True, except empty ones.
# False values include empty values, such as (), [], {}, "", the number 0, the value None and, of course, False
# If you have an object that is made from a class with a __len__ function that returns 0 or False it evaluates to False

# Boolean operators
#   == Equal
#   != Not equal
#   >  Greater than
#   <  Less than
#   >= Greater than or equal to
#   <= Less than or equal to

# Logical Operators
#   'and' Returns True if both statements are true
#   'or'  Returns True if one of the statements is true
#   'not' Reverses the result, ex: returns False if the result is true

# Comparison
# If statements go in the order of if->elif(else if)->else
a = 3
b = 4
c = 5
if a == b:
    pass
elif c < b:
    pass
else:
    print("Hello")

# If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b:
    print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

# 'and' & 'or' are logical operators used to combine conditionals
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# While Loops - executes a set of statements as long as a condition is true
i = 1
while i < 6:
    print(i)
    i += 1

# 'break' - Allows us to exit the loop even if the condition is still true
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# 'continue' - Allows us to stop the current iteration and continue with the next
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# With the else statement we can run a block of code once when the condition no longer is true
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For Loops
# In Python, for loops are iterators that go through an iterable object (strings, lists, tuples, etc)
# They work much like foreach loops in other programming languages
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

# With the break statement we can stop the loop before it has looped through all the items:
for x in fruits:
    print(x)
    if x == "banana":
        break

# Range()
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number
# For example, range(6) returns the numbers 0-5
for x in range(6):
    print(x)

# It is possible to specify the starting value by adding a parameter:
for x in range(2, 6):
    print(x)

# It is possible to specify the increment value by adding a third parameter
for x in range(0, 10, 2):
    print(x)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished
# The else block will NOT be executed if the loop is stopped by a break statement
for x in range(2):
    print(x)
else:
    print("Finally finished!")
