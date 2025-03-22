# Functions are helpful to keep track of records and make the work easier

'''
Syntax:
def function_name(parameter):
    body
    
Function Call
---------------------
When we want to call a function we put the function name and the by brackets

func1()
'''
'''

def sum():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    
    print("The sum of the numbers is " + str(a+b+c))

sum() # Calling the function sum
'''
# Functions with parameters or arguments

# In Python, an argument is a value passed to a function during a function call.
'''

def greet(name, ending):
    print("Greet " + name)
    print(ending)
    
greet("Aryan", "Thank you")
'''

# Return keyword
'''
The Python return statement marks the end of a function and specifies the value
or values to pass back from the function.

If the value of a variable is defined as the function call then the value of the
variable is the value that you have put in return.
a = func1()
'''
'''

def avg(a, b, c):
    return (a+b+c)/3

a = avg(12,45,34)
print(a)
'''

# Default arguments in python
'''
Python allows function arguments to have default values. If the function 
is called without the argument, the argument gets its default value entered by
the user.
'''
'''
def diff(a, b=12):
    print(a-b)
    
diff(34)
diff(23, 10) # The user can change also change the default value of the argument.
'''

# Recursions

# Recursion is a function which calls itself

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1

factorial(n) = n X (n-1) X (n-2) X........................X 3 X 2 X 1

Hence we got.

factorial(n) = n * factorial(n-1)
'''

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)

a = factorial(int(input("Enter a number: ")))

print(f'The factorial is {a}' )

# we need a base condition to stop the recursion to go infinitely
