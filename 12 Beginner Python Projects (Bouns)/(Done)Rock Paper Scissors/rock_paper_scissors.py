'''
    - create game counter, win tracker
    - Enter while loop
        - get players name and choice from r, p, s
        - get a random choice from r, p, s list and store in in a variable
        - if user's input == variable 
            - add 1 to the game counter
            - print game tied 
        - if (r > s, s > p, p > r) based on this rule
            - add 1 to the winner (computer or user(name))
            - print the game winner
        - ask the user to play again
            - yes
                repeat
            - no
                break out the loop and print out the winner (amount of win per player)
                
    Note:
        must use multiple function's
        
 '''
import random
import sys
            
def game(Player):
    list = ["r", "p", "s"]
    win_counter = 0
    tie = 0
    game_counter = -1

    while True:
        choice = input("Chose your Hand: -Rock(r) -Paper(p) -Scissor(s): -").lower()
        com_choice = random.choice(list)
        
        
        if choice == com_choice:
            winner = f"{Player}: {choice}   Computer: {com_choice}    :) Its a Tie.."
            tie += 1
        elif choice == "r":
            if com_choice == "s":
                winner = f"{Player}: {choice}   Breaks..  Computer: {com_choice}    :) {Player} Wins!.."
                win_counter += 1
            else:
                winner = f"{Player}: {choice}   is Covered..  Computer: {com_choice}    :) {Player} Lost!.."
        elif choice == "p":
            if com_choice == "r":
                winner = f"{Player}: {choice}   Covers..  Computer: {com_choice}    :) {Player} Wins!.."
                win_counter += 1
                
            else:
                winner = f"{Player}: {choice}   Cut by...  Computer: {com_choice}    :) {Player} Lost!.."
        elif choice == "s":
            if com_choice == "p":
                winner = f"{Player}: {choice}   Cut's..  Computer: {com_choice}    :) {Player} Wins!.."
                win_counter += 1
                
            else:
                winner = f"{Player}: {choice}   Braked by..  Computer: {com_choice}    :) {Player} Lost!.."    
        
        
        game_counter += 1    
        print(winner)
        if input("Play Again?(n)(y): ").lower() == "n":
            return win_counter, tie, game_counter

def main():   

    """ Main program for the game"""
    
    try:
        player = input("Player Name: ")
    except ValueError:
        sys.exit("Enter a Proper Name next Time! ") 
    
    
    win_counter, tie, game_counter = game(player)
    
    
    print()
    print("-- Game Result Status: --")
    print("-------------------------")
    print(f"Win's: {win_counter}")
    print(f"Tie: {tie}")
    print(f"Game's Played: {game_counter}")
    print("-------------------------")
    
    
    
    
    
    
if __name__ == "__main__":
    main()