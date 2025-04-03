"""
____________________  ________
\______   \______   \/  _____/     ______ ___.__.
 |       _/|     ___/   \  ___     \____ <   |  |
 |    |   \|    |   \    \_\  \    |  |_> >___  |
 |____|_  /|____|    \______  / /\ |   __// ____|
        \/                  \/  \/ |__|   \/     
"""

# [TODO]: like, rewrite everything lmfao. okay but like seriously. 
# 3rd Rewrite of the code, DO NOT USE AI. enhance visually, and also improve the code,like a lot, the last 2 ones were a mess, the second one was way better though... (shorter, more controllable (add more controllers to the functions) and make sure it controls multiple things at once)

# [IMPORTS]: because, we need stuff...
import random
import time

# [VARIABLES]: there's literally just one fucking var-
name = ""

# [FUNCTIONS]: saving up space lol :money_mouth:

# RANDNAME: creates a randomly generated name, this one goes for you, 5 year old kids that call yourselves "Xx_epicgamingmaster446_xX"
def randname(min, max): 
    # create a list of letters, get the min and max and add the randomly picked letter to the name.
    abc = "abcdefghijklmnopqrstuvwxyz"
    name = ""
    for i in range (min, max):
        name += abc[random.randint(0,(len(abc)-1))]
    return name # this returns so you can store it in another varaible

# WAIT: completely useless function actually, but saves bytes instead of typing time.sleep everytime
def wait(s):
    time.sleep(s)

# Typewrite: Enhanced version of print, but more Fancy :3, 
def typewrite(text, delay, newline):
    # text is the text you want to write, delay is measured in seconds and is the time it takes to write the next letter, newline decides if it should continue the text AFTER or IN THE NEXT line
    for char in text:
        print(char, end='', flush=True)
        wait(delay)
    if newline: # this is supposed to be a boolean, but for some reason you can use 1 and 0 so uhh yeah use that instead!
        print()  # artificial /n

# Test use (placeholder for the main game)

typewrite("You used your special attack... ", .05, 0)
wait(2)
typewrite("it was super effective!", .05, 1)

# [First commit]: V1
# (holy shit is that an ultrakill reference)
