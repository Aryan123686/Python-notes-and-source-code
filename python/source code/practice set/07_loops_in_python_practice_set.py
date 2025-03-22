#1 Write a program to print a multiplication table of ac number
'''
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")'''

#2 Write a program to greet someone in a list of names.The names should start with S and H

'''
l = ["Harry", "Mridul", "Shubham", "Aryan"]

for item in l:
    if(item.startswith("S") or item.startswith("H")):
        print('Hello ' + item)'''

#3 Write a program to find a number is prime or not
'''
n = int(input("Enter a number: "))

if(n <= 1):
    print("The number is not prime nor composite")
    
else:
    for i in range(2,n):
        if(((n%i)==0)):
            print("The number is not prime")
            break
        
    else:
        print("The number is prime")'''

#4  Write a program to find the sum of n naturals numbers
'''
n = int(input("Tell the n natural numbers:"))

i = 1
sum = 0

while(i<=n):
    sum += i
    i+=1
print(sum)'''

# 5 Write a program to find the factorial of the number.
'''
n = int(input("Enter a number:"))

factorial = 1

for i in range(1, n+1):
    factorial = factorial * i


print(f"Factorial of {n} is {factorial}")'''

#6 Write a program to print the following pattern for n = 3
'''
  *
 ***
*****
'''

'''
Observation
------------------
As you can see the no of spaces to the left of the star is decreasing one by
one, so we should write (n-i) for spaces as i goes from 1 to n 

The stars are following the odd series pattern, so as we know that in odd
series the nth term is 2n-1
'''
'''
n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(" "*(n-i),end="")#by default print adds a new line so end stops it
    print("*"*(2*i-1),end="")
    print("")
'''

#7 write a program to print the following star pattern for n = 3

'''
*
**
***
'''
'''
n = int(input("Enter a number: "))

for i in range(1, n+1):
    print("*"*i, end = "")# no of stars in ith line =   i*star
    print("")
'''

#8 Write a program to print the following pattern for n = 3

'''
***
* *
***
'''
'''
n = int(input("Enter a number: "))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")
'''
'''
Explanation
---------------------
In the pattern the first and last line are printed with the n no of stars
(i goes from 1 to n) so when the i is first or last line we should print
the n no of stars.

In the middle line, we see that the first character and last from side 
is filled with one star and the middle from sideways are filled with spaces
that are (n-1-1) = (n-2) this should we put in else as we do not want 
to print the 2 stars and spaces in first and last line.
'''