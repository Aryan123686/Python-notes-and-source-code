#1 Write a program to find the sum of two numbers

class Sum:
    
    def getSum(self):
        return self.a + self.b
    
sum1 = Sum()

sum1.a= int(input("Enter a number: "))
sum1.b = int(input("Enter a number: "))

print("The sum of two numbers is ", sum1.getSum())


#2 make a calculator capable of finding square, cube, and cube root of the number.
'''
class Calculator:
    
    def square(self):
        print(f"The square of {self.a} is {(self.a)**2}")
        
    def cube(self):
        print(f"The cube of {self.a} is {(self.a)**3}")
        
    def sqrt(self):
        print(f"The square root of {self.a} is {(self.a)**1/2}")


calculator = Calculator()
calculator.a = int(input("Enter a number: "))
calculator.square()
calculator.cube()
calculator.sqrt()
'''

