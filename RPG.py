"""
____________________  ________
\______   \______   \/  _____/     ______ ___.__.
 |       _/|     ___/   \  ___     \____ <   |  |
 |    |   \|    |   \    \_\  \    |  |_> >___  |
 |____|_  /|____|    \______  / /\ |   __// ____|
        \/                  \/  \/ |__|   \/     
"""

# 3rd Rewrite of the code, DO NOT USE AI. enhanced visually, and also improved the code, like a lot, the last 2 ones were a mess, the second one was way better though... shorter, more controllable and made sure it controls multiple things at once

""" 
[TODO]: 
- detail structures 
- add more structures and types
- day/night cycle (Based on the day, enemies will get stronger, exponentially as well, and based on the level too. (:skull:)) 
- shops 
- redefine combat because SOMEONE IS FUCKING STUPID!!! (im not looking at anyone (omar...)) 
- optimize a lot of the code stuff but rn its doing great ngl, maybe a bit mroe of order (ultrakill)
- usage of items
- add more items to chests
- Move chest types to class, or turn structures into classes and then add the type of chest inside of it
"""
# [IMPORTS]: because, we need stuff...
import random
from time import sleep as wait

# [ENGINE VARIABLES AND THINGS]: just fucking die.

# YOU IS A MOTHERFUCKER YOU KNOW THAT

errors = {
    1:"Structure not found",
    2:"Out of bounds"
}

# [VARIABLES]: your mother and i had a great time bullying you as a kid so you could bring this bullshit to life ( my mom is dead...)

debug = 1
run = True
name = ""
structure = ""
structures = ["Village", "Dungeon", "Castle"] # this little fucker is a rouge us military asset
enemy = ""
potions = 0
day = True # what the fuck is this?? can't we make a string variable called time and set it to day/night???? fucking idiot whoever did that

# [CLASSES]: cuando yo la vi

# this fucker will murderer everyone like hitler on ww2

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

# in memory of our old 50 lines inventory from the first version :3

class inventory:
    keys = 0
    bombs = 0
    coins = 0
    bag = []

# [DICTIONARIES]: this fucking stupid, move to a class after we get it working and feel motivated

village_chest = {
    "Keys":random.randint(0,1),
    "Bombs":0,
    "Coins":random.randint(0,10)
}

dungeon_chest = {
    "Keys":random.randint(0,1),
    "Bombs":random.randint(0,3),
    "Coins":random.randint(0,25),
}

castle_chest = {
    "Keys":random.randint(0,1),
    "Bombs":random.randint(0,3),
    "Coins":random.randint(0,25),
}

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

def Chest(type, needs_key):
    # FUCK YOU OMAR JAHAAHJASHDJH I MADE YOUR CODE 10 TIMES SHORTER :middle_finger: - hugo
    # kys - jordi
    global player, structure, inventory, chestdic

    if needs_key:
        if inventory.keys > 0:
            inventory.keys -= 1
        else:
            typewrite("You don't have a key to open this chest", 0.01, 1)
    else:
        # TODO: add a message with the contents that you found in the chest, and say that you found nothing if you... found... noting....
        # TODO: add more things like potions, weapons, or other kinds

        # Big brain time moment i had in class which probably is actually a fuckign shit 
        inventory.keys += type["Keys"]
        inventory.coins += type["Coins"]
        inventory.bombs += type["Bombs"]
    

# [PLAYER FUNCTIONS]: ITS LIKE THE THINGS FROM FORTNITE

# defclass: Im fucking done if you cant guess
def defclass():
    global player
    classes = ["Warrior", "Archer", "Wizard"] # shouldnt this be outside of the function? isn't it a global thing?
    player.CLASS = random.choice(classes)

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
    # holy fucking shit. mindfuckery!
    global player
    player.LVL += 1
    player.HP += 5
    player.RES += 1
    if player.LVL % 2 == 0:
        player.ATK += 1
    if player.CLASS == "Wizard":
        player.MANA += 5
    XPX = 0
    if player.XPR < player.XP:
        XPX = player.XP - player.XPR
    player.XP = 0
    player.XPR *= 1.5
    player.XPR += XPX
    # what the fuck does any of this mean bro xpx xpr xp bro this sounds like morse code but more advanced


# [GAME FUNCTIONS]:i uhh idk, fucking geuss ("geuss" lol oh wait i wrote that LMAO)

# combat: is a fuckin' combat dude, it's not even that hard to read the code, it is easy to understand
# easy to understand my fucking ass bro, and WHAT IN THE FUCK IS THIS WHY IS THERE SO MANY IFS USE THE AND OPERATOR PLEASE I BEG
def combat():
    global player
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
def defstructure(str): 
    # THY END IS NOW! PREPARE THYSELF! WEAK! CRUSH! 
    global structure, structures

    structure = structures[str]
    if not structure:
        print(f'\033[93mERROR: {errors[1]}\033[0m')
    else:
        # nasty ugly fuckface annoying i hate this i fucking hate it
        match(structure):
            case "Village":
                village()
            case "Dungeon":
                dungeon()
            case "Castle":
                castle()
    return

# fucking lamest comments ever

# Village: define village structure, 
def village():
    Chest(village_chest, 0)
# Dungeon: define dungeon structure,
def dungeon():
    Chest(dungeon_chest, 0)
# Castle: define castle structure,
def castle():
    Chest(castle_chest, 0)

# i'm sure there's a simpler way to do the chest call, but right now i'm at a loss

"""
 |   | |
| |  | _
"""

# [MAIN GAME LOOP]: GUESS WHAT THE FUCK THIS DOES!

# [FIXME]: oh god please forgive me for making this HORRIBLE mess but it is the only way i can think of right now to get rid of the fucking annoying intro
typewrite("-----------------------------------------", 0.01, 1) if not debug else print()
typewrite("-----------",0.01, 0)if not debug else print();typewrite("WELCOME, TO RPG.PY!",0.1, 0) if not debug else print();typewrite("-----------", 0.01, 1) if not debug else print()
typewrite("-----------------------------------------", 0.01, 1) if not debug else print()
wait(1) if not debug else wait(0)
typewrite("First of all, let's pick your name...", 0.1, 1) if not debug else print()
wait(1) if not debug else wait(0)
name = randname(0, 10)
typewrite("Your name will be: ", 0.01, 0)if not debug else print();wait(0.5)if not debug else wait(0);typewrite(name, 0.5, 1) if not debug else print()
defclass()
typewrite("Your class will be: ", 0.01, 0)if not debug else print();wait(1)if not debug else wait(0);typewrite(player.CLASS, 0.07, 1) if not debug else print()
defstats()

while run:
    defstructure(random.randint(0, (len(structures)-1)))
    wait(1)

# [Fourth commit]
