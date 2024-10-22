# TO DO: RANDOMIZE STATS | DONE
# GET RANDOM ATTACK DAMAGE AND SHIT | DONE
# RANDOM GENERATION (get random structures and stuff) | done as well man wtf we're cooking brah
# Random enemies (types and stats and names aswell) | sorta done????
# game items | lmao fuck no
# if you're defending the enemy can't defend (and viceversa?) | WE HAVEN'T EVEN STARTED LLOLOLOLOLOOOLOL
# make enemy types??? | still yet to be aproved
# name codes (put this in the getstats function and if name == "name": stats = value) | not started

# --------------------------------------------------------------------------------

# Import random shit, just like you
# kys

import random
import time
import math

# import pyautogui

# Game variables

game = True
turn = None
battling = None
encounter = None
defending = None
edefending = None
# structure variables

structure_name = ""
has_chest = None
has_enemies = None

# player variables

name = ""
keys = 0
coins = 0
bombs = 0
level = 0
HP = None
RST = None
ATK = None
SPD = None
LCK = None

# enemy variables

eHP = None
eRST = None
eATK = None
eSPD = None
elevel = 0

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

def defenemystats():
    global eHP
    global eRST
    global eATK
    global eSPD
    global elevel

    eHP = random.randint(50, 90) + level
    eRST = random.randint(1,5)
    eATK = round(math.log(random.randint(4,10)))
    eSPD = 2

def RandName(char_min, char_max):
    for i in range(random.randint(char_min, char_max)):
            global name
            name += random.choice('abcdefghijklmnopqrstuvwxyz')

def wait(s):
     time.sleep(s)

def GetStructureInfo():
    global structure_name
    global has_chest
    global has_enemies
    has_enemies = random.randint(0,1)
    encounter = random.randint(0,1)
    has_chest = random.randint(0,1)
    randomstructure = random.randint(1,7)
    if randomstructure == 1:
        structure_name = "Village"
    elif randomstructure == 2:
        structure_name = "Forest"
    elif randomstructure == 3:
        structure_name = "Temple"
    elif randomstructure == 4:
        structure_name = "Plains"
    elif randomstructure == 5:
        structure_name = "Desert"
    elif randomstructure == 6:
        structure_name = "Swamp"
    else:
        structure_name = "Dungeon"

def Structure(s_name, s_chest, s_enemies):

    # when called, the code must specify the name, if it has chests and if it has enemies.
    # here we make it check so if the name is X then it will do this and that

    strname = str(s_name)

    if s_name == "Village":
        print("You are in a village")
        wait(1)
        if s_chest == 1:
            print("This", strname, "has a chest!")
            wait(1)
        else:
            print("This", strname, "doesn't have a chest.")
            wait(1)
    elif s_name == "Forest":
        print("You are in a forest")
        wait(1)
    elif s_name == "Temple":
        print("You are in a temple")
        wait(1)
        if s_chest == 1:
            print("This", strname, "has a chest!")
            wait(1)
        else:
            print("This", strname, "doesn't have a chest.")
            wait(1)
    elif s_name == "Plains":
        print("You are in a plains")
        wait(1)
    elif s_name == "Desert":
        print("You are in a desert")
        wait(1)
    elif s_name == "Swamp":
        print("You are in a swamp")
        wait(1)
    else:
        print("You are in a dungeon ")
        wait(1)
        if s_chest == 1:
            print("This", strname, "has a chest!")
            wait(1)
        else:
            print("This", strname, "doesn't have a chest.")
            wait(1)
    if has_enemies == 1 and encounter == 1:
        battle()
# here we go

def attack():

    # turn 0 is the enemy's turn, 1 is your turn

    global turn

    if turn == 0:
        HP -= eATK + (RST*0.5)
    elif turn == 1:
        eHP -= ATK + (eRST*0.5)
        

def defend():
    global turn

    if turn == 1:
        RST = RST * 2
    elif turn == 0:
        eRST = eRST * 2

def StopDefend():
    global turn
    if turn == 1:
        RST = RST // 2
    elif turn == 0:
        eRST = RST // 2

def item():
    # we need a list with all items
    return

def BattleEnd():
    battling == False

def battle():

    global battling

    while battling == True:
        rnd_action = random.randint(1,3)

        if HP <= 0:
           print(name, "has died\nlife stats")
           game = False
        if eHP <= 0:
            # kills the enemy and gives you (xp) money, bombs & keys
            return

        if eHP <= 10:
            eflee = random.randint(0,1)

        if eflee == 1:
            print("the enemy is fleeing...")

        if HP <= 10:
            flee = random.randint(0,1)

        if flee == 1:
            print(name, "decided to flee")


        if rnd_action == 1:
            print(name, "has decided to attack!")
            attack(1)
        elif rnd_action == 2:
            print(name, "has decided to defend!")
            defend()
        elif rnd_action == 3:
            print(name, "has decided to use an item!")
            item()
        if battling == False:
            BattleEnd()

# Main game code
# hardcode a game loop so whenever the player dies it can break, and also the structures and shit can loop indefinetely

# while run == true:

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
wait(2)
# pyautogui.typewrite("These are your stats: ") --this should do a typewrite effect

# game starts

while game == True:
    if HP <= 0:
        break
    GetStructureInfo()
    Structure(structure_name, has_chest, has_enemies)
    wait(1)
    # game = False (endgame (haha avengers reference))
