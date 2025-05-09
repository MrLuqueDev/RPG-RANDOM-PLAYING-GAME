"""
____________________  ________
\______   \______   \/  _____/     ______ ___.__.
 |       _/|     ___/   \  ___     \____ <   |  |
 |    |   \|    |   \    \_\  \    |  |_> >___  |
 |____|_  /|____|    \______  / /\ |   __// ____|
        \/                  \/  \/ |__|   \/     
"""

# [TODO]: like, rewrite everything lmfao. okay but like seriously. ("OkAy BuT sErIoUsLy")
# 3rd Rewrite of the code, DO NOT USE AI. enhance visually, and also improve the code, like a lot, the last 2 ones were a mess, the second one was way better though... (shorter, more controllable (add more controllers to the functions) and make sure it controls multiple things at once)
# Based on the day, enemies will get stronger, exponentially as well, and based on the level too. (:skull:)


# [IMPORTS]: because, we need stuff...
import random
from time import sleep as wait

# [ENGINE VARIABLES AND THINGS]: just fucking die.

errors = {
    1:"Structure not found",
    2:"Out of bounds"
}

# [VARIABLES]: your mother and i had a great time bullying you as a kid so you could bring this bullshit to life ( my mom is dead...)

run = True
name = ""
structure = ""
enemy = ""
potions = 0
day = True

# [CLASSES]: cuando yo la vi

class player:
    name = name
    HP = None
    RES = None
    ATK = None
    SPD = None
    LCK = None
    MANA = None
    CLASS = None
    LVL = None
    XP = None
    XPR =None

class inventory:
    keys = 0
    bombs = 0
    coins = 0
    bag = []

class structures:
    structure = ""
    has_chest, has_enemies, chest_type, has_shop = None
    chest_types = [
        # coins, keys, bombs
        [1, 0, 0], # Village chest
        [1, 1 ,0] # Dungeon chest
        [1, 1, 1] # Castle chest
    ]
    list = [ # random.randint(len(chest_types))
        # Name, has chest, chest type, has enemies, has shop, 
        ["Village", has_chest, chest_type, random.randint(0,1), random.randint(0,1)],
        ["Dungeon", has_chest, chest_type, has_enemies, , random.randint(0,1)],
        ["Castle", 1, random.randint(len(chest_types)), random.randint(0,1), random.randint(0,1)],
    ]

inventory.bombs += 1


# [FUNCTIONS]: saving up space lol :money_mouth:

# RANDNAME: creates a randomly generated name :3, this one goes for you, 5 year old kids that call yourselves "Xx_epicgamingmaster446_xX"
def randname(min, max): 
    # create a list of letters, get the min and max and add the randomly picked letter to the name.
    abc = "abcdefghijklmnopqrstuvwxyz"
    name = ""
    for i in range (min, max):
        name += abc[random.randint(0,(len(abc)-1))]
    return name # this returns so you can store it in another varaible

# WAIT: completely useless function actually, but saves bytes instead of typing time.sleep everytime (:nerd:)

# typewrite: Enhanced version of print, but more Fancy :3, (kys)
def typewrite(text, delay, newline):
    # text is the text you want to write, delay is measured in seconds and is the time it takes to write the next letter, newline decides if it should continue the text AFTER or IN THE NEXT line
    for char in text:
        print(char, end='', flush=True)
        wait(delay)
    if newline: # this is supposed to be a boolean, but for some reason you can use 1 and 0 so uhh yeah use that instead!
        print()  # artificial /n

# [OBJECT FUNCTIONS]: the oiled up machines that make this work
def chest_content():
    global coins, bombs, keys, needs_key, structure
    #This function defines the content of the chests that you find in your journey and adds it to the player's inventory
    chest_content = random.randint(1, 2)
    if structure == "Village" and chest_content == 1:
        wait(0.5)
        typewrite("You've found a coin!", .05, 1)
        coins += 1
    elif structure == "Dungeon" and chest_content == 1:
        wait(0.5)
        typewrite("You've found a key!", .05, 1)
        keys += 1
    elif structure == "Castle" and chest_content == 1:
        wait(0.5)
        typewrite("You've found a bomb!", .05, 1)
        bombs += 1

    if needs_key == True:
        wait(0.5)
        typewrite("You've got a key!", .05, 1)
        keys += 1

def Chest(type, needs_key):
    global inventory, structure

# [PLAYER FUNCTIONS]: ITS LIKE THE THINGS FROM FORTNITE

# defclass: Im fucking done if you cant guess
def defclass():
    global player
    randclass = random.randint(1,3)
    if randclass == 1:
        player.CLASS = "Warrior"
    elif randclass == 2:
        player.CLASS = "Archer"
    else: 
        player.CLASS = "Wizard"

# defstats: Fucking. guess. (god im so done)
def defstats():
    global player
    player.HP = 100
    player.RES = 20
    player.ATK = 10
    player.SPD = 5
    player.LCK = 10
    if player.CLASS == "Wizard":
        player.MANA = 100


# lvlup: How about you go fucking kys before i see you again
# TODO: levels must always upgrade your hp and resistance, preferably atk too, each x levels other stats will get a level up too
def lvlup():
    global player
    player.LVL += 1
    player.HP += 5
    player.RES += 1
    if player.LVL % 2 == 0:
        player.ATK += 1
    if player.CLASS == "Wizard":
        player.MANA += 5
    player.XPX = 0
    if player.XPR < player.XP:
        player.XPX = player.XP - player.XPR
    player.XP = 0
    player.XPR *= 1.5
    player.XPR += player.XPX

# [GAME FUNCTIONS]:i uhh idk, fucking geuss

# combat: is a fuckin' combat dude, it's not even that hard to read the code, it is easy to understand
def combat():
    global enemy, potions
    enemy_life = 100
    first_attacking = random.randint(1, 2)
    attack_type = random.randint(1, 4)
    enemy_attack = random.randint(1, 2)
    wait(0.5)
    typewrite(enemy, .05, 0)
    typewrite("wants to fight you", .05, 1)
    if first_attacking == 1:
        if attack_type == 1:
            wait(0.5)
            typewrite("You've done a standart attack!", .05, 1)
            enemy_life -= 15
        elif attack_type == 2:
            wait(0.5)
            typewrite("THAT WAS A CRITICAL ATTACK", .05, 1)
            enemy_life -= 34
        elif attack_type == 4 and potions > 0:
            wait(0.5)
            typewrite("You've used a potion", .05, 1)
            HP += 15
            typewrite("Your HP: ", .05, 0);typewrite(HP, .05, 1)
            potions -= 1
        elif attack_type == 4 and potions <= 0:
            wait(0.5)
            typewrite("You don't have potions", .05, 1)
        else:
            wait(0.5)
            typewrite("You've missed...", .05, 1)
    else:
        if enemy_attack == 1:
            wait(0.5)
            typewrite("You've been hit...", .05, 1)
            pHP -= 16
        else:
            wait(0.5)
            typewrite("The enemy missed...", .05, 1)

# [STRUCTURE FUNCTIONS]: brainfuck the sequel

# defstructure: Work around structures (brainfuck, beyond cooked, undertanding this is an ancient art)
def defstructure(setstructure): 
    # SETSTRUCTURE: 0 = random, any other variable will be a set structture (read dictionary below)
    global structure
    structuredic = {
        1:"Village",
        2:"Dungeon",
        3:"Castle"
        }
    if setstructure in structuredic:
        structure = structuredic[setstructure]
    if not setstructure:
        structure = random.randint(1, len(structuredic)-1)
    else:
        print(f'\033[93mERROR: {errors[1]}\033[0m')
    return

# Village: define village structure, 
def village():
    
    chest_content()

# [MAIN GAME LOOP]: GUESS WHAT THE FUCK THIS DOES!

typewrite("-----------------------------------------", 0.01, 1)
typewrite("-----------",0.01, 0);typewrite("WELCOME, TO RPG.PY!",0.1, 0);typewrite("-----------", 0.01, 1)
typewrite("-----------------------------------------", 0.01, 1)
print()
wait(1)
typewrite("First of all, let's pick your name...", 0.1, 1)
wait(1)
name = randname(0, 10)
typewrite("Your name will be: ", 0.01, 0);wait(0.5);typewrite(name, 0.5, 1)
defclass()
typewrite("Your class will be: ", 0.01, 0);wait(1);typewrite(player.CLASS, 0.07, 1)
defstats()
defstructure(1)
typewrite()

while run:
    defstructure(0, 0)
    

# [Third commit]
