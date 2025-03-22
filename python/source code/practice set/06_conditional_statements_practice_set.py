#1 Write a python program to find the greatest among four numbers

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = int(input("Enter 3rd number:"))
num4 = int(input("Enter 4th number:"))

greatest = None

if(num1>num2 and num1>num3 and num1>num4):
    greatest = num1
    
elif(num2>num1 and num2>num3 and num2>num4):
    greatest = num2
    
elif(num3>num1 and num3>num2 and num3>num4):
    greatest = num3
    
else:
    greatest = num4
    
print('The greatest number is ', greatest)

#2 Write a python program to check a student is pass or fail in 3 subjects entered by the user
# if he requires 40% to pass and score 33 or more than in every subject

m1 = int(input("Enter marks of subject1: "))
m2 = int(input("Enter marks of subject2: "))
m3 = int(input("Enter marks of subject3: "))

per_age = ((m1+m2+m3)*100)/300

if(per_age >=40 and m1>=33 and m2>=33 and m3>=33):
    print(f"You are pass with {per_age} percentage")
    
else:
    print(f"You are fail with {per_age} percentage")