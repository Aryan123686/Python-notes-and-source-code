# dictionaries
''' to make a dictionary first put them in square brackets and put comma after every
line except the last line'''

dict1 = { '''The first values before : are called keys and their corresponding terms
are called values'''
    "Harry" : 100,
    "Aryan" : 90,
    "Rowan" : False,
    "list_science": [12,34,50],
}

# print(dict1, type(dict1))

print(dict1["Aryan"]) #prints the corresponding value of the "Aryan" which is 90
print(dict1["Rowan"])
print(dict1["list_science"])

#methods of dictionaries

dict2 = {
    'Name': 'Harry',
    'Age' : 12,
    False : True,
    'Salary' : None
}

print(dict2.items()) #prints all items in dict2


print(dict2.keys()) #print keys
print(dict2.values()) #print values


print(dict2)
dict2.update({'Name' : 'Aryan' , "Salary" : "2.5lakhs"})
#updates the value of key with its corresponding value
print(dict2)

print(dict2.get('Name')) # Gets the value of the corresponding key
print(dict2.get( False))
print(dict2.get('Age'))
print(dict2.get('Salary'))


#Sets in python

# Set is a collection of well-defined objects

A = {1, 'Hello', None, 23, 12.03, "Aryan", 56, "Shushan"}
B = {3, 'Hello', None, 12, 12.03, "Are you fine?"}

# print(A, B, type(A), type(B))

#operations on set

print(len(A), len(B)) #enters the no. of element in a set

A.remove('Hello') # Removes hello from set A
B.remove(12.03) # Removes 12.03 from set B
print(A , B)

A.pop() # removes random element or the element with computer choice
B.pop()
print(A,B)

A.clear() #clears the set
B.clear()
print(A,B)

A.add(123) #adds the element in the set with the corresponding value
B.add('1q')
print(A,B)

# Union and intersection

'''
Union
-------------------------------------
Suppose two sets A and B. The union of A and B read as A union B is the set
containing all items in A and B

Note: the common elements in A and B are only written 1 time

Intersection
-----------------------------------------------
Suppose two sets A and B. The intersection of A and B read as A intersection B is 
the set of the common elements in A and B
'''

s1 = {1,2,-3,3, 34,-102,23,-34}
s2 = {1,2,56,23}

print(s1.union(s2))  # s1 union s2
print(s1.intersection(s2)) # s1 intersection s2