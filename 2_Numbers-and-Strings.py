# Conversions
# Note: You cannot convert complex numbers into another number type
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a, type(a))
print(b, type(b))
print(c, type(c))

# Casting

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# strings can be formed using a matching pair of "" or ''
# You can assign a multiline string to a variable by using three quotes
sentence = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
"""
print(sentence)

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
word = "Supercalifragilisticexpialidocious"

print(word[0])
print(word[1])
print(word[2])

for letter in word:
    print(letter)

print(len(word))

if "list" in word:
    print("True")

# String formatting
