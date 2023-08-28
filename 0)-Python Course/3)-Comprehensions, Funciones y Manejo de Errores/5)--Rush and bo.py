"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Refactor Game
FILE TYPE   : Dictionary and List Comprehention with functions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////   Rush and Bo Game   //////////////////////////////
#///////////////////////////   Rush and Bo Game   //////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
# Dictionary generation
# Generate a rush and bo game using list and dictionary comprehention
#///////////////////////////////////////////


def choose_options():
    options = ("rock","paper","scissors")
    user_option = input("Dude, choose paper, scissors or rock => ")
    user_option = user_option.lower()
    
    if not user_option.lower() in options:
        print("Not a valid option dude...")
        return None, None
    
    computer_option = random.choice(options)
    
    print("Dude = ",user_option)
    print("Machine dude =",computer_option)
    
    return user_option, computer_option


def rule_checker( user_option, computer_option, user_wins, computer_wins ):
    
    if user_option == computer_option:
        print("Tie")
        
    elif user_option == "rock":
        
        if computer_option == "scissors":
            
            print("Stone wins over scissors")
            print("Dude...you win¡¡¡ :V")       
            user_wins += 1
        else:
            
            print("Paper wins over stone")
            print("Dude...you lost :C")       
            computer_wins += 1
            
    elif user_option == "paper":
        
        if computer_option == "stone":
            
            print("Paper wins over Stone")
            print("Dude...you win¡¡¡ :V")       
            user_wins += 1
        else:
            
            print("Scissors wins over paper")
            print("Dude...you lost :C")       
            computer_wins += 1
            
    elif user_option == "Scissors":
        
        if computer_option == "paper":
            
            print("Scissors wins over Paper")
            print("Dude...you win¡¡¡ :V")       
            user_wins += 1
        else:
            
            print("Stone wins over Scissors")
            print("Dude...you lost :C")       
            computer_wins += 1
    
    return user_wins, computer_wins


def rush_and_bo(number_of_rounds=True):
    computer_wins = 0
    user_wins = 0
    rounds = 1
    
    
    while True:
        print("*"*10)
        print("ROUND - ",rounds)
        print("*"*10)
        
        print("Computer Wins = ",computer_wins)
        print("Dude wins = ",user_wins)
        rounds += 1
        
        user_option, computer_option = choose_options()
        user_wins, computer_wins = rule_checker( user_option, computer_option, user_wins, computer_wins )
        
        if computer_wins == 2:
            print("Dude jajaja you lost, computer rules ¡¡")
            break
        
        if user_wins == 2:
            print("Duuuudeee...you win¡¡¡")
            break
    
                        

if __name__ == "__main__":
    rush_and_bo()
    
