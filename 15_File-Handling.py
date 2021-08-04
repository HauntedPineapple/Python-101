# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# "rt" is the default, so
import os
a = open("Syntax.txt")
# is the same as
b = open("Syntax.txt", "rt")
# Note: Make sure the file exists, or else you will get an error.

# It is good practice to always close files when you are done with them
a.close()
# Note: In some cases, due to buffering, changes made to a file may not show until you close the file.

# File Reading
# The read() method reads the whole file
print(b.read())

# You can also specify how many characters from the file you wish to read
b = open("Syntax.txt")
print(b.read(3))

# You can return one line by using the readline() method
b = open("Syntax.txt")
print(b.readline())
# After calling the readline() method, the line moves to the next,
# so by calling readline() again, our code will read the second line
print(b.readline())
# By looping through the lines of the file, you can read the whole file, line by line
for x in b:
    print(x)

b.close()

# File Writing
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# File Creation
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist

f = open("demofile.txt", "w")
f.close()

# File Deletion
# To delete a file, you must import the OS module, and run its os.remove() function
os.remove("demofile.txt")
# To avoid getting an error, you might want to check if the file exists before you try to use it
if os.path.exists("demofile.txt"):
    pass
else:
    print("The file does not exist")

# To delete an entire folder, use the os.rmdir() method
# You can only delete EMPTY folders, though

# How to get the number of lines in a text file
file = open('Syntax.txt')
count = 0

content = file.read()
lineList = content.split("\n")

for i in lineList:
    if i:
        count += 1

print('There are', count, 'lines in the file')