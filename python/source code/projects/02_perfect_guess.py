from random import randint

class mainEngine:
    
    def __init__(self, start, end):
        
        self.start = int(start)
        self.end = int(end)
        
        self.computer = randint(self.start, self.end)
        

start = input("Enter the start value: ")
end = input("Enter the end value: ")

while start.isdigit() == False or end.isdigit() == False:
    print("Please enter an invalid reply!")
    start = input("Enter the start value: ")
    end = input("Enter the end value: ")


game = mainEngine(start, end)

while True:
    
    
    start = input("Enter the start value: ")
    end = input("Enter the end value: ")

    while start.isdigit() == False or end.isdigit() == False:
        print("Please enter an invalid reply!")
        start = input("Enter the start value: ")
        end = input("Enter the end value: ")


    game = mainEngine(start, end)
    
    
    
    # print(game.computer)
    
    
    user = input("Enter a number between the end and start value that you entered: ")
    
            
    while user.isdigit() == False: # is digit checks that a number contains digits or not
        print("Please enter valid number")
        user = input("Enter an number between the end and start value that you entered: ")
        
    else:
        
        while(int(user) < int(start) or int(user) > int(end)):
            print("The number is out of range!")
            user = input("Enter an number between the end and start value that you entered: ")
        
    
    if(int(user) > game.computer):
            print("You have entered greater number!")
            
    elif(int(user) < game.computer):
            print("You have entered lower number!")
            
    else:
        print(f"You have guessed the number in attempts")
            
        play = input("Do you want to play again(yes/no): ").lower()
            
        while play not in ['yes', 'no']:
            print("Invalid reply please enter yes or no")
            play = input("Do you want to play again(yes/no): ").lower()
            
        if(play == 'no'):
            print("Thanks for playing")
            break
        