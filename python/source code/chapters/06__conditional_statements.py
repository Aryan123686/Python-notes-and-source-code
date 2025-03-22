''' conditional expressions can be used to express conditions like if you want to eat ice cream if day 
is hot if not then eat pasta.'''

#if else syntax

'''indentation is skip of columns when you press tab. It is essential because its help us to know that 
the function like if, else, def content is insie them or not.'''

a = int(input("Enter your age:   "))

if(a>=18):
    print("YOu are eligible to vote")

else:
    print("You can't vote")
    
print("End of program") # this excutes after if else body
#if 'if' condition is true then else is ignored if not then else body is executed.

# if elif else

b = int(input('Enter an number 0 to 100:   '))

    
if(b>=0 and b<=10):
    print("Your number is 0 to 10")

elif(b>=10 and b<=20):
    print("Your number is 10 to 20")
    
elif(b>=20 and b<=30):
    print("Your number is 20 to 30")
    
elif(b>=30 and b<=40):
    print("Your number is 30 to 40")

elif(b>=40 and b<=50):
    print("Your number is 40 to 50")

elif(b>=50 and b<=60):
    print("Your number is 50 to 60")

elif(b>=60 and b<=70):
    print("Your number is 60 to 70")

elif(b>=70 and b<=80):
    print("Your number is 70 to 80")

elif(b>=80 and b<=90):
    print("Your number is 80 to 90")

elif(b>=90 and b<=100):
    print("Your number is 90 to 100")

else:
    print("Your number is out of range")
    
#elif means in english is else if
'''the program will check if function if keyword it is false then it will check first elif program 
if the first elif program is false then continues the second elif program and then it repeats the
same procces till else body ''' 
'''Relational operators.  


== signifies that two values are equal or not.It return false if the values are different they 
return true if they are equal

> greater than
< lower than

>= greater than or equal to
<= lower than or equal to

Logical operators

and => returns true when all operands are true otherwise return false

or => returns true when any one operand is true otherwise false


'''
'''If we put if statement in place of elif then it will check the first if statement if its false
then directly move to else statement without checking the other if staements'''

''' Else statement is executed if all the if and elifs statement are false'''