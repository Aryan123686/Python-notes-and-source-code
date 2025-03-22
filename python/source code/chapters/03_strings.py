s1 = 'aryan' #single quoted string
s2 = "Aryan" #double quoted string
s3 = '''harry''' #triple quoted string

# string slicing
'''
Harry 
h = 0 or -5, a = 1 or -4, r = 2 or -3, r = 3 or -2, y = 4 or -1
'''
name = "Aryan"

sliced_name = name[-5:-2]  #start in -5 and go till -2 without taking -2
print(sliced_name)

length_name = len(name) #enter no. of characters
print(length_name)

#triple value slicing

string = "123456789"  
print(string[1:7])
print(string[1:7:2]) #here third no. means skip every (third no. -1) character

#func of strings

my_str = "aryantiwari" 
my_str2 = "ARYANTIWARI"
my_str3 = "This is a time of india"

print(len(my_str))


print(my_str.endswith("tiwari")) # check if string ends with the value(true or false))
print(my_str.endswith("tiwarie"))


print(my_str.startswith("aryan")) # check if string starts with the  given value(true or false)
print(my_str.startswith("ryan"))


print(my_str.capitalize()) #capitalise the first letter

print(my_str.upper()) #capitalize the string
print(my_str2.lower())  #non-capitalize the string


print(my_str3.title()) #capitalize every word first letter

print(my_str3.find("india")) #find the index of first letter of the given value

print(my_str3.count("i")) # count the frequency of given letter

print(my_str3.replace("time", "age")) #replaces the old value with the new one
print(my_str.replace(my_str, my_str2))

# split function
# used to split the words before and after the the value entered by the user and make a list of it

split = "Aryan Tiwari"

print(split.split(" "))
print(split.split("r")) # splits where ever r is present

# escape sequence characters

# /n for new line, \t for tab space and // for quoted marks

sgn = '\tHe is good \n\t,in not he'
print(sgn)

direct = "Ram said, \"I am going to market tonight.\""
indirect = "Ram said that he was going to market that night."
print(direct+ "\n" + indirect)

#input function
# used to take input from user 
name1 = input("Enter your name: ")
print(f"Your name is {name1}")