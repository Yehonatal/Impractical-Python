import sys
import random

""" The Function that returns the first and last name after generating them using the random module."""
def random_name_generator():
    
    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'BeenieWeenie'",
        "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
        'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
        'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
        'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
        'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
        'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
        'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"',
        'Mergatroid', '"Mr Peabody"', 'OilCan', 'Oinks', 'Old Scratch',
        'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
        'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scunt',
        "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
        'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
        'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
        "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
        'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
        'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
        'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
        'Hootkins', 'Jefferson', 'Jenkins', 'JingleySchmidt', 'Johnson',
        'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
        'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
        'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
        'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
        'Stevens', 'Stroganoff', 'SugarGold', 'Swackhamer', 'Tippins',
        'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
        'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
        'Woolysocks')
    
    # First name selected at radom
    first_name = random.choice(first)

    # Second name selected at radom
    last_name = random.choice(last)
    return first_name, last_name


""" main funtion"""
def main():
    """ Welcome massge to the User"""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")



    """ The code """
    chose = True
    while chose:
      
        first_name, last_name = random_name_generator()
        
        print("======================================")
        print(f"Full Name: {first_name} {last_name}")   
        

        # Ask the user to quit or try again
        try_again = input("Try again? (y/n): ").lower()
        if try_again == "n":
            sys.exit()
        
        

if __name__ == "__main__":
    main()