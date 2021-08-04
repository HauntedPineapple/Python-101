# Functions are defined using the 'def' keyword
def helloWorld():
    print("Hello World!")
helloWorld()

# Docstrings are optional, but helpful for documenting what a function does
# It goes after the function header and is denoted by opening and closing """s or '''s and can be multiline

def sayGoodbye():
    """Prints out a goodbye"""
    print("Goodbye World!")

# Arguments/Parameters are specified after the function name,
# inside the parentheses, and separated by commas
def sayHello(name):
    print("Hello", name)
fname = input("What is your name? ")
sayHello(fname)

# Python functions allow for default arguments, and must go at the end
# of the list of parameters
def greet(name, msg="Good morning!"):

    print("Hello", name + ', ' + msg)
fname = input("What is your name? ")
greet(fname)

# If you do not know how many arguments that will be passed into your function,
# add a '*' before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly
def greetMult(*names):
    for name in names:
        print("Hello", name)


greetMult("Audrey", "Chester", "Mei Mei")

# The 'return' keyword is used, as always, to return data
def addNums(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum
print(addNums(1,2,3,4,5,6,7))

# We can call other functions inside of a function
def recursive_factorial(n):
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)
print(recursive_factorial(7))