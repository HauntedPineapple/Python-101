# Create a class using the 'class' keyword
class Dog:
    pass
    # The 'pass' keyword is often used as a placeholder indicating where code will eventually go
    # It allows you to run this code without Python throwing an error

# All classes have a function called __init__(), which is always called when the class is being instantiated
# The properties that all objects must have are defined in __init__()
# Every time a new object is created, __init__() sets the initial state of the object by
# assigning the values of the object’s properties, it can be thought of as the constructor
# __init__() takes any number of parameters, but the first parameter will always be a variable called 'self'
# When a new class instance is created, the instance is automatically passed to the self parameter in
# __init__() so that new attributes can be defined on the object.
# Attributes created in __init__() are called instance attributes
# An instance attribute’s value is specific to a particular instance of the class
# Class attributes are attributes that have the same value for all class instances
# You can define a class attribute by assigning a value to a variable name outside of __init__()


class Player:
    """
    docstrings can also be used with classes
    """
    # Class Attribute
    species = "Human"

    def __init__(self, name, level, xPos, yPos):
        self.name = name  # string
        self.level = level  # int
        self.xPosition = xPos  # int
        self.yPosition = yPos  # int

    # Instance methods are functions that are defined inside a class and can only be called from an instance of that class
    # The 'self' parameter is a reference to the current instance of the class, 
    # and is used to access variables that belongs to the class
    # It does not have to be named 'self' , you can call it whatever you like, 
    # but it has to be the first parameter of any function in the class
    def moveVertically(self, change):
        '''
        Postive input indicates moving up,
        Negative input indicates moving down
        '''
        self.yPosition += change

    def moveHorizontally(self, change):
        '''
        Postive input indicates moving right,
        Negative input indicates moving left
        '''
        self.xPosition += change

    def move(self, xChange, yChange):
        self.xPosition += xChange
        self.yPosition = yChange

    # Here we are overriding the dunder method "__str__", which
    # outputs the object in a string format
    # By overriding it, we can customize how the object is printed out
    def __str__(self):
        return f"{self.name} is at ({self.xPosition}, {self.yPosition})"

myPlayer = Player("Audrey", 5, 0, 0)

# You can access attributes using dot notation:
playerLevel = myPlayer.level
print("Level:", playerLevel)

print(myPlayer)
myPlayer.moveHorizontally(1)
print(myPlayer)

# You can delete objects or properties using the 'del' keyword
del myPlayer.level
del myPlayer