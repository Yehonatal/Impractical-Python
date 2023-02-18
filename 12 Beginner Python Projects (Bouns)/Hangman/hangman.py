""" 
    player 1 = chose a word
    player 2 = guess a letter 

    fixed amount of tries 

 """
import random as r 
from word import words

LIMIT = 5

def get_word():
    return r.choice(words).lower()

    
def main():
    word = get_word()
    
    space = ''
    count = 0
    for _ in word:
        count += 1
        space += "__ "

    print(f"Your available space's are := {count} :- {space} ")
    print(f"Your available tries are {LIMIT}: ")


    

if __name__ == '__main__':
    main()
