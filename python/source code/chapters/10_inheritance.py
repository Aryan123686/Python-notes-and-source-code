# Inheritance is a way of creating new class from an existing class

'''
Sometimes we want to make many classes with stored same information
as the previous one but with little changes in it.We can do this by using 
inheritance
'''
'''
class Employee: # Base Class or parent class
    # Code
    pass
    
class Programmer(Employee): # Child class or derived class
    # code
    pass

This means that all the methods and attributes of class Employee will come in 
class Programmer
'''

# Types of inheritance

# 1. single inheritance

'''
                    Base Class
                        |
                        |
                    derived class
'''

# example of single inheritance
'''
class employee():
    pass

class programmer(employee):
    pass
'''

# 2. multi inheritance

'''
            Parent1             Parent2
                |                   |
                |___________________|
                            |
                            |
                        Derived class
'''
'''
class Employee():
    pass

class Coder:
    pass

class Programmer(Employee, Coder):
    pass
'''

# 3. Multilevel inheritance

'''
                    Parent Class
                        |
                        |
                    Child Class1
                        |
                        |
                    Child Class 2
'''
'''
class Programmer():
    pass

class Coder(Programmer):
    pass

class Employee(Coder):
    pass
'''

# super() method 

'''
Super method is used to access the methods of the super class(base class) in derived class
A method in a base class can be called in a derived class
'''
'''
class Emp():
    def __init__(self, name, id, town):
        self.name = name
        self.id = id
        self.town = town
        
class Freelance(Emp):
    def __init__(self, name, id, town, emails):
        super().__init__(id, name, town)
        self.emails = emails
        
aryan2 = Freelance("Aryan", "103", "Buxar", "KKK@gmails")
print(aryan2.name, aryan2.id, aryan2.emails)
'''

# Class Method

'''
Class Method
---------------------------------
A class method is a method which is bound to class and not he object of the class
If we want a method to print only class attribute and ignore the object attribute
then we can use class method
'''
'''
class Num:
    a = 18
    
    @classmethod
    def no(cls): # we need to use cls parameter to use class attributes
        print(f"The number is {cls.a}")
        
num1 = Num()
num1.a = 7
num1.no()
'''

# property decrators

# Property method defines as a method but we can use it as an attribute
'''
@property decorator is a built-in decorator in Python which is helpful in defining
the properties effortlessly without manually calling the inbuilt function
property(). Which is used to return the property attributes of a class from 
the stated getter, setter and deleter as parameters.

They can used to treat methods as property and attributes
'''
'''
class diff:
    @property
    def sub(self):
        return self.a - self.b
    
num = diff()
num.a = 12
num.b = 5
print(num.sub) # we can run methods without using brackets by this decorator it will claim it as attribute
'''

# Getters and setters
'''
Getters
-----------------
Getters get or fetch the value when we print then we get the result as getter

Setters
---------------
Setters set or assign the value in a variable then we get result as setter
to write setter use method name and then .setter 
'''
'''
class Name:
    
    @property
    def fullname(self): # getter method
        return f"{self.fname} {self.lname}"
    
    @fullname.setter
    def fullname(self, name): # Setter Method
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]
    
name1 = Name()
name1.fname = "Aryan"
name1.lname = "Tiwari"
print(name1.fullname)

name2 = Name()
name2.fullname = "Ananya Tiwari"
print("After setting")
print(name2.fname, name2.lname)
'''