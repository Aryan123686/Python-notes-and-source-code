from random import choice

class mainGame:
    
    
    def get_user_choice(self):
        
        self.user = input("Enter your choice(rock, paper, scissors)").lower()

        while self.user not in ['rock', 'paper', 'scissors']:
            self.user = input("Invalid Text(please enter rock, paper, scissors)").lower()
            
        
        return self.user
        
    def get_computer_choice(self):
        self.computer = choice(['rock', 'paper', 'scissors'])
        return self.computer
    
    def getWin(self):
        
        if(self.user == self.computer):
            return "Its a draw!"
            
        elif(self.user == 'rock' and self.computer == 'scissors') or (self.user == 'paper' and self.computer == 'rock') or (self.user == 'scissors' and self.computer == 'paper'):
            return "Congrats! You Won"
        
        else:
            return "You lose! Try again next time"
    
    
game = mainGame()

while True:
    
    game.user = game.get_user_choice()
    game.computer = game.get_computer_choice()
    
    print("You Choose ", game.user)
    print("Computer choose ", game.computer)
    
    result = game.getWin()
    
    print(result)
    
    play_again = input("Do you want to play again(yes/no): ").lower()
    
    while play_again not in ['yes', 'no']:
        play_again = input("Invalid Reply! please enter(yes/no)").lower()
        
    if(play_again == 'no'):
        print("Thanks for Playing!")
        break