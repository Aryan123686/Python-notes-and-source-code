list1 = ["Aryan", 34, None, False, 12.39]
print(list1)
print(list1[2])  # prints the item of given index in list1
print(list1[0] + "\t" +  str(list1[1]) + "\t" +  str(list1[4]))
#functions of lists 

a = [1,2,3,4,5,6,8,9,10,11,12]
print(a[0:8], a[0:8:2]) # same as string slicing but it will take the last index

a.append(13)  # adds new element at the end of list
print(a)
a.sort() # ascending order 
print(a)
# a.reverse()    # reverses the list
# print(a)
a.insert(6, 7) #insert the second parameter at index of the first parameter by taking one more value
print(a)
a.pop(9) #removes element of index 9
print(a)
a.remove(10) # remove the element of value 10
print(a)


#tuples

tur1 = (12, 34, False, None, "Aryan")
print(tur1[1])

tur2 = (1,2,3,4,5,6,7,8,9,10,12,5,5,55,5,5,5,5,5,5,5,5)
print(tur2.count(5)) # no. of 5s in tur2
print(tur2.index(12)) # tells that what is at index 12 
print(tur2[1:12:3]) # same as list slicing
print(len(tur2)) # length of tuple