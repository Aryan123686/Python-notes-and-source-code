# Sometimes we want to repeat a text or a object many times in this case loops are used

# While loop

'''
While Loop
------------------

Syntax:
while(condition):
    #body of the loop
    
The while loop checks the condition if it is true then it will run the body of the loop and after 
running it, the while loop checks the condition again and then also the condition is true then it will 
execute the body, this process is done till the condition become false.
'''

# A program used to print numbers

i = 0

while (i<6):
    print(i)
    i+=1 #Increment
    

'''
Output:

1 "1 < 6"
2 "2 < 6"
3 "3<6
4 "4<6"
5 "5<6"
'''
#6 "6 is not less than 6, hence the condition will become false and it will exit the loop"

#Write a program to print numbers from 1 to 10

x = 0

while(x<=10):
    print(x)
    x +=1
    
# A program to write items in a list line by line

l = [12, 45, 90, "Apple", "Bannana"]
y = 0
while(y<len(l)):
    print(l[y])
    y = y+1

# For Loop

#  for i in range() : # body

'''
range:

for i in range(n) # i value goes from 0 to n-1

for i in range(x, n) # i value goes x to n-1

for i in range(x, n, m) # i value goes from x to n-1 by directly going to m-1 value after the previous value

'''

# code to print value in list

names = ["Harry", "Aryan", "Shubham", "Shobbhit", "Ananya", "Atharva"]

for result in names:
    print(result)
    
# else with for loop

for s in range(1, 6):
    print(s)
    
else:
    print("The loop have finished") # this executes when the loop exhausts,  means after printing 5
    
    
# break and continue

for i in range(1, 21):
    if(i == 12):
        break # exit the loop when this condition become true
    print(i)
    
for t in range(1, 21):
    if(t == 13):
        continue # Skip this iteration
    print(t)
    

# pass statement 

# sometimes we want to leave the body of class, function, loop or condition
# then we use pass to come here later and we dont get the error

for i in range(1, 3):
    pass