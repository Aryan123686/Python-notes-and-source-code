# Arithmetic Operators
'''+ means addition ,- means subtraction,
* means multiplication,/ means division,** means exponentiation
// means floor division(round off to integer)
and %  shows modulus(remainder when two no. are divided)'''
a = 23
b = 12 

print(a + b, a - b, a * b, a / b, a//b, a**b, a%b)

#Assignment Operators
b = 3
a = 34 # 34 is assigned in a

b += 3 # b += 3 is b = b + 3

b_ = 4

b_ -= 3 # b -= 3 is b = b-3

print(b, b_)

# comparison operators
''' > means greater than, < means lower than, == shows equality, >= means greater than or equal to
<= means lower than or equal to, != means not equal to
'''
c = 3 > 5
d = 3 == 6
e = 4 >= 4
f = 2 <= 3
g = 3 != 4

print(c, d, e, f, g)

#Logical operators


'''
and => returns true if both or more operands are true otherwise false
or => returns true if any one operand is true otherwise false
not => converts false to true and vice versa
'''

h = 3 == 5 or 3 != 5
h_ = 3 == 5 or 3 > 5
_h_ = 3 < 5 and 3 != 5 
_1h_ = 3 < 5 and 3 == 5 
hh = not 5 <= 6 #not
print(h, h_, _h_, _1h_ , hh)


#Identity operator

'''
is => returns true if both variables are of the same object otherwise false
is not => returns true if both variable are not of the same object otherwise false
'''

i1 = "String"
i2 = 23
i3 = False
i4 = True
# i1 is a string and i2 is an integer so they are not of same object whereas i3 and i4 are of same object
print(i1 is i2, i1 is not i2, i3 is i4, i3 is not i4)

#Membership operators

'''
in => returns true if a sequence with a specific value is present in the object otherwise false
not in => returns true if a sequence with a specific value is not present in the object otherwise false
'''

m1 = ["banana", 45, "apple"]
# banana, 45 and apple are present in the list
print("banana" in m1, 34 in m1, 45 not in m1, "apple" is not m1)