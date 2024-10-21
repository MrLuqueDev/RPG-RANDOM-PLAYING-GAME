# TO DO: RANDOMIZE STATS
# GET RANDOM ATTACK DAMAGE AND SHIT
# RANDOM GENERATION (get random structures and stuff)
# Random enemies (types and stats and names aswell) 
# game objects

# --------------------------------------------------------------------------------

# Import random shit, just like you
# kys

import random
import time
import math

# import pyautogui

# General variables

name = ""
structure_name = ""
has_chest = None
has_enemies = None
keys = None
coins = None
bombs = None
HP = None
RST = None
ATK = None
SPD = None
LCK = None

# FUNCTIONS :3

def defstats():
    global HP
    global RST
    global ATK
    global SPD
    global LCK

    HP = random.randint(75, 150)
    RST = random.randint(1,5)
    ATK = round(math.log(random.randint(5,15)))
    SPD = 10
    LCK = random.randint(-10, 10)

def RandName(char_min, char_max):
    for i in range(random.randint(char_min, char_max)):
            global name
            name += random.choice('abcdefghijklmnopqrstuvwxyz')

def wait(s):
     time.sleep(s)

def Structure(s_name, s_chest, s_enemies):

    # when called, the code must specify the name, if it has chests and if it has enemies.
    # here we make it check so if the name is X then it will do this and that

    if s_name == "Village":
        print("You are in a village")
        if s_chest == 1:
            print("This Village has a chest!")

    elif s_name == "Forest":
        print("You are in a forest")
    elif s_name == "Temple":
        print("You are in a temple")
    elif s_name == "Plains":
        print("You are in a plains")
    elif s_name == "Desert":
        print("You are in a desert")
    elif s_name == "Swamp":
        print("You are in a swamp")
    else:
        print("You are in a dungeon ")

def GetStructureName():
    # firstly get the name
    global structure_name
    global has_chest
    global has_enemies
    has_enemies = random.randint(0,1)
    has_chest = random.randint(0,1)
    randomstructure = random.randint(1,7)
    if randomstructure == 1:
        return "Village"
    elif randomstructure == 2:
        return "Forest"
    elif randomstructure == 3:
        return "Temple"
    elif randomstructure == 4:
        return "Plains"
    elif randomstructure == 5:
        return "Desert"
    elif randomstructure == 6:
        return "Swamp"
    else:
        return "Dungeon"

def getstructurechests():
        # now set if it should have a chest or not

    if structure_name == "Village":
        return

# Main game code

question = int(input("Want a random name (0) or your own name (1)?: "))

if question == 0:
    RandName(1,10)
elif question == 1:
    name = input("What is your name?: ")
else:
    print("That's not a valid answer, kys fag")

print("your name is: ", name)
wait(2.5)
print("These are your stats:")
defstats()
wait(1)
print("HEALTH (HP):", HP)
wait(0.4)
print("RESISTANCE (RST):", RST)
wait(0.4)
print("ATTACK (ATK):", ATK)
wait(0.4)
print("SPEED (SPD):", SPD)
wait(0.4)
print("LUCK (LCK):", LCK)
# pyautogui.typewrite("These are your stats: ") --this should do a typewrite effect

# game starts


GetStructureName()
# make a function called getstructure that straight up does the 3 get structure functions
Structure("Village", 1, 0)