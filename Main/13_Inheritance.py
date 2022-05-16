# Inheritance allows us to define a class that inherits all the methods and properties from another class
# Parent class is the class being inherited from, also called the base class
# Child class is the class that inherits from another class, also called the derived class

# To inherit from a class, send the parent class as a parameter when creating the child class

class Person:    
  
        # __init__ is known as the constructor         
        def __init__(self, name, idnumber):   
                self.name = name
                self.idnumber = idnumber
        def display(self):
                print(self.name)
                print(self.idnumber)
  
# child class
class Employee( Person ):           
        def __init__(self, name, idnumber, salary, post):
                self.salary = salary
                self.post = post
  
                # invoking the __init__ of the parent class 
                Person.__init__(self, name, idnumber) 
  
                  
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")    
  
# calling a function of the class Person using its instance
a.display() 