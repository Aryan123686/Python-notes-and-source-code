#1 Write a program to find the biggest among three numbers
'''
def biggest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

print("The biggest number among them is ", biggest(a, b, c))
'''

#2 Write a program to convert celsius to fahrenheit
'''
def convert(c):
    return (9/5 * c) + 32

c = int(input("Enter celsius value: "))
celsius = convert(c)
print(f"The fahrenheit value is {round(celsius, 2)}") 
# round function round offs the number from given digit places
'''