debug = 1

#____________________  ________
#\______   \______   \/  _____/     ______ ___.__.
# |       _/|     ___/   \  ___     \____ <   |  |
# |    |   \|    |   \    \_\  \    |  |_> >___  |
# |____|_  /|____|    \______  / /\ |   __// ____|
#        \/                  \/  \/ |__|   \/     

# 3rd Rewrite of the code, DO NOT USE AI. enhanced visually, and also improved the code, like a lot, the last 2 ones were a mess, the second one was way better though... shorter, more controllable and made sure it controls multiple things at once

""" 
[TODO]: 
- detail structures 
- add more structures and types
- day/night cycle (Based on the day, enemies will get stronger, exponentially as well, (enemy leevel done) (:skull:)) 
- shops 
- done! (combat)
- optimize a lot of the code stuff but rn its doing great ngl, maybe a bit mroe of order (ultrakill)
- usage of items
- add more items to chests
- Move chest types to class, or turn structures into classes and then add the type of chest inside of it
"""
# [IMPORTS]: because, we need stuff...
import random
from time import sleep as wait
import os

# [ENGINE VARIABLES AND THINGS]: just fucking die.

# YOU IS A MOTHERFUCKER YOU KNOW THAT

errors = {
    1:"Structure not found",
    2:"Out of bounds"
}

# [VARIABLES]: your mother and i had a great time bullying you as a kid so you could bring this bullshit to life ( my mom is dead...)

run = True
structure = ""
structures = ["Village", "Dungeon", "Castle"] # this little fucker is a rouge us military asset
class_list = ["Warrior", "Archer", "Wizard"] # so sad we need to do this
day = True # what the fuck is this?? can't we make a string variable called time and set it to day/night???? fucking idiot whoever did that

# [ENEMY NAMES]: for regular mobs and bosses
enemy_names = ["Goblin", "Skeleton", "Bandit", "Slime", "Zombie"]
boss_names = ["suOmal", "EMO"]

# [CLASSES]: cuando yo la vi

# this fucker will murderer everyone like hitler on ww2

class player:
    name = None
    HP = 100
    RES = 10
    ATK = 10
    SPD = 5
    LCK = 10
    CLASS = random.choice(class_list)
    if CLASS == "Wizard":
        MANA = 100
    LVL = 1
    XP = 0
    XPR = 100
    keys = 0
    bombs = 0
    coins = 0
    inventory = []
# in memory of our old 50 lines inventory from the first version :3

# structure classes

class enemy:
    name = None
    HP = None
    RES = None
    ATK = None
    LCK = None
    MANA = None

class Village:
    chest = {
        "Keys": random.randint(0, 1),
        "Bombs": 0,
        "Coins": random.randint(0, 10),
        "Potion": 0
    }

class Dungeon:
    chest = {
        "Keys": random.randint(0, 1),
        "Bombs": random.randint(0, 3),
        "Coins": random.randint(0, 25),
        "Potion": random.randint(0, 1)
    }

class Castle:
    chest = {
        "Keys": random.randint(0, 1),
        "Bombs": random.randint(0, 3),
        "Coins": random.randint(0, 25),
        "Potion": random.randint(0, 1)
    }

# [DICTIONARIES]: This is this because i say so fckin betch :( | || || |_
    
pot_dic = {
    "Potion1":10,
    "Potion2":25,
    "Potion3":50,
    "Potion4":75
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

def clear():
    os.system("cls" if os.name == "nt" else "clear")

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
    global player, structure

    if needs_key:
        if player.keys > 0:
            player.keys -= 1
        else:
            typewrite("You don't have a key to open this chest", 0.01, 1)
            wait(1);clear()
    else:
        # TODO: add a message with the contents that you found in the chest, and say that you found nothing if you... found... nothing....
        # TODO: add more things like potions, weapons, or other kinds

        # Big brain time moment i had in class which probably is actually a fuckign shit 
        if type["Keys"] != 0:
            player.keys += type["Keys"]
            print(f"Player got {type["Keys"]} Keys!")

        if type["Coins"] != 0:
            player.coins += type["Coins"]
            print(f"Player got {type["Coins"]} Coins!")
        
        if type["Bombs"] != 0:
            player.keys += type["Bombs"]
            print(f"Player got {type["Bombs"]} Bombs!")
            
        if type["Potion"] != 0:
            rndpot = random.randint(1,4)
            player.inventory.append(("Potion" + str(rndpot)))
            print(f"Player got a tier {type["Potion"]} Potion!")

# fucking horrible function but it'll work for now... i hate my life.

def set_chests():
    Village.chest = {
        "Keys": random.randint(0, 1),
        "Bombs": 0,
        "Coins": random.randint(0, 10),
        "Potion": 0
    }

    Dungeon.chest = {
        "Keys": random.randint(0, 1),
        "Bombs": random.randint(0, 3),
        "Coins": random.randint(0, 25),
        "Potion": random.randint(0, 1)
    }

    Castle.chest = {
        "Keys": random.randint(0, 1),
        "Bombs": random.randint(0, 3),
        "Coins": random.randint(0, 25),
        "Potion": random.randint(0, 1)
    }

# [PLAYER FUNCTIONS]: this fucking sucks i hate my life martha let me see the kids again

# MARTHA LOOK IM LIVING IN AN ISEKAI WHERE EVERY ACTION I DO IS RANDOM THAT MEANS I NEVER GAAMBLED OUR HOUSE ON PURPOSE

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
    overflow_xp = max(player.XP - player.XPR, 0)
    player.XP = 0 + overflow_xp
    player.XPR = player.XPR * 1.5 
    # what the fuck does any of this mean bro xpx xpr xp bro this sounds like morse code but more advanced - kys

# [ENEMY FUNCTIONS]: | || || |_

def defenemy(lvl):
    global enemy, enemy_names, boss_names
    boss = random.randint(1, 10)
    if boss == 1:
        enemy.name = random.choice(boss_names)
        enemy.HP = 200 + (lvl * 15)
        enemy.ATK = 20 + (lvl * 4)
        enemy.RES = 10 + (lvl * 2)
    else:
        enemy.name = random.choice(enemy_names)
        enemy.HP = 50 + (lvl * 5)
        enemy.ATK = 10 + lvl
        enemy.RES = 5 + lvl
    enemy.LCK = 10


# [GAME FUNCTIONS]:i uhh idk, fucking geuss ("geuss" lol oh wait i wrote that LMAO)

# combat: is a fuckin' combat dude, it's not even that hard to read the code, it is easy to understand
# easy to understand my fucking ass bro, and WHAT IN THE FUCK IS THIS WHY IS THERE SO MANY IFS USE THE AND OPERATOR PLEASE I BEG
def combat():
    global player, enemy, structure, run
    if structure == "Village":
        lvl = random.randint(1, 3)
    elif structure == "Dungeon":
        lvl = random.randint(2, 4)
    elif structure == "Castle":
        lvl = random.randint(3, 5)

    defenemy(lvl) # creates an enemy
    
    typewrite(f"A {enemy.name} appeared!", 0.1, 1) # take a very fucking wild guess
    wait(1);clear()

    # set the damages
    player_dmg = max(0, player.ATK - enemy.RES)
    enemy_dmg = max(0, enemy.ATK - player.RES)

    # combat loop
    while player.HP >= 0 and enemy.HP >= 0: 
        
        wait(1)

        # sets the crit hit

        player_crit = random.random() < (player.LCK / 100)
        enemy_crit = random.random() < (enemy.LCK / 100)
        
        # player deals a critical hit

        if player_crit:
            player_dmg *= 1.5
            typewrite(f"{player.name} made a critical hit", 0.05, 0);typewrite("...", 0.07, 1)
            wait(0.1)
            typewrite(f"{player.name} dealt {player_dmg} DMG!", 0.05, 1) 

        # regular damage

        if not player_crit:
            typewrite(f"{player.name} dealt {player_dmg} DMG!", 0.05, 1)

        # enemy deals a critical hit

        if enemy_crit:
            enemy_dmg *= 1.5
            typewrite(f"{enemy.name} made a critical hit", 0.05, 0);typewrite("...", 0.07, 1)
            wait(0.1)
            typewrite(f"{enemy.name} dealt {enemy_dmg} DMG!", 0.05, 1)

        # REGULAR HURTING AN ENEMY BRO :sob:

        if not enemy_crit:
            typewrite(f"{enemy.name} dealt {enemy_dmg} DMG!", 0.05, 1)

        # deal the damage

        enemy.HP -= player_dmg
        player.HP -= enemy_dmg

        # reseting crits

        if player_crit:
            player_dmg /= 1.5
        if enemy_crit:
            enemy_dmg /= 1.5
        
        player_crit = False
        enemy_crit = False

        # heal

        if player.HP < 25:
            for item in player.inventory:
                if item.startswith("Potion"):
                    player.inventory.remove(item)
                    typewrite(f"{player.name} drank a potion", 0.05, 0)
                    typewrite("...", 0.07, 1)
                    wait(0.1)
                    typewrite(f"It healed {pot_dic[item]} HP!", 0.1, 1)
                    player.HP += pot_dic[item]
                    break
                # espero que sea esto lo que querias?? ns bro me liao xd
        
        wait(1);clear()
            
    if player.HP <= 0:
        typewrite("you died, skill issue", 0.05, 1)
        run = False
    else:
        typewrite(f"you killed {enemy.name}!", 0.05, 1)

# [STRUCTURE FUNCTIONS]: brainfuck the sequel

# defstructure: Work around structures (brainfuck, beyond cooked, undertanding this is an ancient art)
def defstructure(str): 
    # THY END IS NOW! PREPARE THYSELF! WEAK! CRUSH! DIE!
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
    set_chests()
    return

# fucking lamest comments ever

# Village: define village structure, 
def village():
    print(structure)
    Chest(Village.chest, 0)
# Dungeon: define dungeon structure,
def dungeon():
    print(structure)
    Chest(Dungeon.chest, 0)
# Castle: define castle structure,
def castle():
    print(structure)
    Chest(Castle.chest, 0)

# i'm sure there's a simpler way to do the chest call, but right now i'm at a loss

"""
 |   | |
| |  | _
"""

# [MAIN GAME LOOP]: GUESS WHAT THE FUCK THIS DOES!

player.name = randname(0, 10)

if not debug:
    typewrite("-----------------------------------------", 0.01, 1)
    typewrite("-----------",0.01, 0);typewrite("WELCOME, TO RPG.PY!",0.1, 0);typewrite("-----------", 0.01, 1)
    typewrite("-----------------------------------------", 0.01, 1)
    wait(1)
    typewrite("First of all, let's pick your name...", 0.1, 1)
    wait(1)
    typewrite("Your name will be: ", 0.01, 0);wait(0.5);typewrite(player.name, 0.5, 1)
    typewrite("Your class will be: ", 0.01, 0);wait(1);typewrite(player.CLASS, 0.07, 1)
    wait(1);clear()

while run:
    defstructure(random.randint(0, (len(structures)-1)))
    wait(2)
    combat()
    if not run:
        break

# [jaCinco commit] kys
