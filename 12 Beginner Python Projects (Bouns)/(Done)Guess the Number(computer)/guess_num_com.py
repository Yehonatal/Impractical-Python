import random as r 

def guess(x):
    ran_num = r.randint(1, x)

    guess = 0

    while guess != ran_num:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < ran_num:
            print("Sorry, Guess again, Too low. ")
        elif guess > ran_num:
            print("Sorry, Guess again, Too High. ")
    print(f"Yay, Congrats. You have guessed the right number {ran_num}, Correctly!")


guess(10)