#Class is a blueprint for creating object
#Object is an instantiation of class.
'''
class Marks:
    maths = 95 # class attributes bcoz they belong to class
    science = 92
    english = 85
    
Aryan = Marks() #Aryan is object
print(Aryan.maths, Aryan.science, Aryan.english)

rohan = Marks()
print(rohan.maths)
'''
'''
#Object attributes or instance attributes
Instance attributes takes preference over class attributes
means they will show instance attributes ignoring class 
attributes

class Employee:
    harry_salary = 1200
    harry_age = 18
    
harry = Employee()
print(harry.harry_salary, harry.harry_age)

aryan = Employee()

aryan.salary = 14000
aryan.age = 22

print(aryan.salary, aryan.age)
'''

#Self parameter
''' When we run a method it requires a parameter to run it
we can use any parameter but self is popular. 
Harry.course() changes to Job.about(Harry)
'''
# object.method() (Syntax to run a method)
'''
class Job:
    language = "Python"
    course ="BCA"
    
    def about(self): # function name is called method
        print(self.language, self.course)
        
Harry = Job()
Harry.course = "B. Tech"
Harry.about() # It will take instance attributes

'''

# static method

'''
Static method is used to mark that the method below it
does not require self ,property, attributes.It is a decorator
'''
'''
class Toppers:
    students = 3
    marks = [498, 489, 478]
    
    def getInfo(top):
        print(f'{self.students} students topped, The first got {top.marks[0]}, second {top.marks[1]} and third got {top.marks[2]} marks respectively')

    @staticmethod # This method does not require a parameter
    def greet():
        print("Good Morning!")
        
DPS = Toppers()

DPS.greet()
DPS.getInfo()
'''

# INIT constructer

#__init__ is method which run as soon as the object is created

# it is a dunder method as it starts with double underscore

class Form:
    
    def __init__(self, name, age, course):
        self.name = name # dont confuse in self.name name is a attribute and name is a parameter
        self.age = age
        self.course = course
    
    @staticmethod
    def intro():
        print("Your form details are")
        
aryan = Form("Aryan Tiwari", 19, "IIT-JEE")

aryan.intro()
print(f"Your name is {aryan.name} Your age is {aryan.age} and your course is {aryan.course}")