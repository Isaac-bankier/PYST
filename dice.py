##############################
#          dice.py           #
#    Simulate a dice roll    #
#      By Isaac Bankier      #
##############################

import random # Import the random library

roll = True # The user wants to roll when they run the program.

while roll:
    print(random.randint(1, int(input("What is the upper bound for your role: ")))) # Get the upper bound and output the random number.

    roll = input("You are on a roll do you want to go again: ") in ["y", "Y", "yes", "Yes", "YES", "yeah", "Yeah", "ok", "Ok"] # Ask the user if they want to roll again and then do that.
