debug = 0

#____________________  ________
#\______   \______   \/  _____/     ______ ___.__.
# |       _/|     ___/   \  ___     \____ <   |  |
# |    |   \|    |   \    \_\  \    |  |_> >___  |
# |____|_  /|____|    \______  / /\ |   __// ____|
#        \/                  \/  \/ |__|   \/     

# 3rd Rewrite of the code, DO NOT USE AI. enhanced visually, and also improved the code, like a lot, the last 2 ones were a mess, the second one was way better though... shorter, more controllable and made sure it controls multiple things at once
# Most of this was done in live share so uhh when you see someone did a commit it's probably fake and someone else did more than the one who made a commit

""" 
[TODO]: 
- detail structures 
- add more structures and types
- day/night cycle (Based on the day, enemies will get stronger, exponentially as well, (enemy leevel done) (:skull:)) 
- shops 
- usage of items FIXME:(i mean sorta done? there's no other items to use but keys and potions and those get used, discuss this later)
- add more items to chests
- Fun names
"""
# [IMPORTS]: because, we need stuff...
import random
from time import sleep as wait
import os

# [VARIABLES]: shit that makes the rest of the code work

run = True
structure = ""
structures = ["Village", "Dungeon", "Castle"] # why -frit
class_list = ["Warrior", "Archer", "Wizard"] # so sad we need to do this -jlf
time = "Day" # FIXME

# [ENEMY NAMES]: for regular mobs and bosses -jlf
enemy_names = ["Goblin", "Skeleton", "Bandit", "Slime", "Zombie"]
boss_names = ["suOmal", "EMO", "Nobita", "SexOffender", "Xx_Francés_xX"] # me cago en vuestros muertos -jlf

# [CLASSES]: variable classes because if we used self and init then i'd just rather jump off a cliff. -frit

# contains the whole player stuff but its bad and stupid and bad and bad and stupid -frit

class player:
    name = None # None because we can't fucking get the function from the bottom here :C -frit
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
    inventory = [] # in memory of our old 50 lines inventory from the first version :3 -frit

# enemy stats, they don't need a lot of things since they're just used in combat

class enemy:
    name = None
    HP = None
    RES = None
    ATK = None
    LCK = None
    MANA = None

# very barebones -frit

class Structure:

    village_chest = {
        "Keys": random.randint(0, 1),
        "Bombs": 0,
        "Coins": random.randint(0, 10),
        "Potion": 0
    }

    dungeon_chest = {
        "Keys": random.randint(0, 1),
        "Bombs": random.randint(0, 3),
        "Coins": random.randint(0, 25),
        "Potion": random.randint(0, 1)
    }

    castle_chest = {
        "Keys": random.randint(0, 1),
        "Bombs": random.randint(0, 3),
        "Coins": random.randint(0, 25),
        "Potion": random.randint(0, 1)
    }

# [DICTIONARIES]: This is bad but i don't care anymore -frit
    
pot_dic = {
    "Potion1":10,
    "Potion2":25,
    "Potion3":50,
    "Potion4":75
}

# [FUNCTIONS]: WARNING!!! THIS SHIT WILL DRIVE YOU INSANE!! -frit
# these are automatizing processes and making everything work

# RANDNAME: creates a randomly generated name with random letters
# this one goes for you, 5 year old kids that call yourselves "Xx_epicgamingmaster446_xX" -frit
def randname(min, max): 
    # create a list of letters, get the min and max and add the randomly picked letter to the name.
    abc = "abcdefghijklmnopqrstuvwxyz"
    name = ""
    for i in range (min, max):
        name += abc[random.randint(0,(len(abc)-1))]
    return name # this returns so you can store it in another varaible

# cleans the fucking terminal... -frit

# cleans the screen for more readability

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# typewrite: prints the letters like undertale dialogues (wow so retro) -frit
def typewrite(text, delay, newline):
    # text is the text you want to write, delay is measured in seconds and is the time it takes to write the next letter, newline decides if it should continue the text AFTER or IN THE NEXT line (BLAHBLAHBLAH) -frit
    for char in text:
        print(char, end='', flush=True)
        wait(delay)
    if newline: # this is supposed to be a boolean, but for some reason you can use 1 and 0 so uhh yeah use that instead! -frit after realizing 0 and 1 are boolean values
        print()  # artificial /n

# FUNnames: Goofy ahh efects when a specific name is entered :3
def FUNnames(name):
    global debug    # in case a special name allows debug like... idk... "Admin"?
    clear()
    match(name):
        case "hugo":
            return


# [OBJECT FUNCTIONS]: Mind torture for those who sinned in the dark ages, however we did not sin, we're just sadomasochistic programmers in search of killing boredom! -frit

def Chest(type, needs_key):
    # FUCK YOU OMAR JAHAAHJASHDJH I MADE YOUR CODE 10 TIMES SHORTER :middle_finger: - frit
    # kys - jlf

    # This fucking sucks but DO NOT TOUCH IT BECAUSE IT WILL FUCK UP SINCE I AM REALLY BADS!!!

    # get the variables

    global player, structure

    # let you know that you found a chest since you don't have eyes in this world

    typewrite(f"{player.name} found a chest", 0.02, 0);wait(0.5);typewrite("...", 0.1, 1)
    wait(1)

    # check if we have a key, if we don't then tell the player and end the function

    if needs_key:
        if player.keys > 0:
            player.keys -= 1
        else:
            typewrite("You don't have a key to open this chest...", 0.01, 1)
            wait(1);clear()
            return

    # TODO (sorta): add more things like potions, weapons, or other kinds 

    # Big brain time moment i had in class which probably is actually a fuckign shit -frit
    # get the dictionaries from the chest type and check the ammount of the item specified in it, give it (if there is), and tell you

    if type["Keys"] != 0:
        player.keys += type["Keys"]
        typewrite(f"{player.name} got {type["Keys"]} Keys!", 0.02, 1)
        wait(1)

    if type["Coins"] != 0:
        player.coins += type["Coins"]
        typewrite(f"{player.name} got {type["Coins"]} Coins!", 0.02, 1)
        wait(1)
    
    if type["Bombs"] != 0:
        player.bombs += type["Bombs"]
        typewrite(f"{player.name} got {type["Bombs"]} Bombs!", 0.02, 1)
        wait(1)
    
    if type["Potion"] != 0:
        rndpot = random.randint(1,4)
        player.inventory.append(("Potion" + str(rndpot)))
        typewrite(f"{player.name} got a tier {type["Potion"]} Potion!", 0.02, 1)
        wait(1)

    # i fucking hate this shit why did you let me write code again fuck im going to kill myself now :3 -frit


def set_chests(): 
    
    # fucking horrible function but it'll work for now... i hate my life. -frit
    # this uh resets the chest values since the value is always the same, for day and night cycle or finding new chests.

    Structure.village_chest = {
        "Keys": random.randint(0, 1),
        "Bombs": 0,
        "Coins": random.randint(0, 10),
        "Potion": 0
    }

    Structure.dungeon_chest = {
        "Keys": random.randint(0, 1),
        "Bombs": random.randint(0, 3),
        "Coins": random.randint(0, 25),
        "Potion": random.randint(0, 1)
    }

    Structure.castle_chest = {
        "Keys": random.randint(0, 1),
        "Bombs": random.randint(0, 3),
        "Coins": random.randint(0, 25),
        "Potion": random.randint(0, 1)
    }

# [PLAYER FUNCTIONS]: this fucking sucks i hate my life martha let me see the kids again -jeremiah
# MARTHA LOOK IM LIVING IN AN ISEKAI WHERE EVERY ACTION I DO IS RANDOM THAT MEANS I NEVER GAAMBLED OUR HOUSE ON PURPOSE -jeremiah
# Who the fuck is jeremiah? -jeremiah

# lvlup: this gets the player's xp, required xp and then raises the player's stats
def lvlup():
    global player
    player.LVL += 1
    player.HP += 5
    player.RES += 1
    if player.LVL % 2 == 0:
        player.ATK += 1
    if player.CLASS == "Wizard": # only wizards can use mana
        player.MANA += 5
    overflow_xp = max(player.XP - player.XPR, 0)
    player.XP = 0 + overflow_xp
    player.XPR = player.XPR * 1.5 

# [ENEMY FUNCTIONS]: | || || |_
# I swear if i fucking see any of you write loss again i am going to LOSE it. -frit

def defenemy(lvl):
    # creates an enemy and gives him stats
    global enemy, enemy_names, boss_names
    boss : int = random.randint(2,10) # random.randint(1, 10) but rn we don't want it to appear -jlf
    if boss == 1:
        enemy.name = random.choice(boss_names) # funi and destructive
        enemy.HP = 200 + (lvl * 15)
        enemy.ATK = 20 + (lvl * 4)
        enemy.RES = 10 + (lvl * 2)
    else:
        enemy.name = random.choice(enemy_names) # not funi but if you're lucky enough (since this whole game is RNG) you can get fucked by a base enemy
        enemy.HP = 50 + (lvl * 5)
        enemy.ATK = 10 + lvl
        enemy.RES = 5 + lvl
    enemy.LCK = 10


# [GAME FUNCTIONS]: functions that are used ingame, as in actions or things that the player directly does -frit

# combat: is a fuckin' combat dude, it's not even that hard to read the code, it is easy to understand -omar
# omar you did not even fucking write the new combat get your comment out of here please :sob: -frit

def combat(): # -jlf
    # combat: he fight -frit 
    global player, enemy, structure, run

    # enemies have different levels depending on the zone
    if structure == "Village":
        elvl = random.randint(1, 3)
    elif structure == "Dungeon":
        elvl = random.randint(2, 4)
    elif structure == "Castle":
        elvl = random.randint(3, 5)

    defenemy(elvl) # creates an enemy -jlf

    clear()
    
    # after creating enemy stats you introduce him to the combat

    typewrite(f"A {enemy.name} appeared!", 0.1, 1) # take a very fucking wild guess -jlf
    wait(1);clear()
    typewrite(f"Enemy stats:", 0.1, 1)
    typewrite(f"HP: {enemy.HP}", 0.1, 1)
    typewrite(f"ATK: {enemy.ATK}", 0.1, 1)
    typewrite(f"RES: {enemy.RES}", 0.1, 1)
    wait(1.5);clear()

    # set the damages -jlf
    player_dmg = max(0, player.ATK - enemy.RES)
    enemy_dmg = max(0, enemy.ATK - player.RES)

    # combat loop -jlf
    while player.HP >= 0 and enemy.HP >= 0: 
        
        wait(1)

        # sets the crit hit -jlf

        player_crit = random.random() < (player.LCK / 100)
        enemy_crit = random.random() < (enemy.LCK / 100)
        
        # player deals a critical hit -jlf

        if player_crit:
            player_dmg *= 1.5
            typewrite(f"{player.name} made a critical hit", 0.05, 0);typewrite("...", 0.07, 1)
            wait(0.1)
            typewrite(f"{player.name} dealt {player_dmg} DMG! Enemy HP: {enemy.HP}", 0.05, 1) 
            wait(0.5)

        # regular damage -jlf

        if not player_crit:
            typewrite(f"{player.name} dealt {player_dmg} DMG! Enemy HP: {enemy.HP}", 0.05, 1)
            wait(0.5)

        # enemy deals a critical hit -jlf

        if enemy_crit:
            enemy_dmg *= 1.5
            typewrite(f"{enemy.name} made a critical hit", 0.05, 0);typewrite("...", 0.07, 1)
            wait(0.1)
            typewrite(f"{enemy.name} dealt {enemy_dmg} DMG! Your HP: {player.HP}", 0.05, 1)
            wait(0.5)

        # REGULAR HURTING AN ENEMY BRO :sob: -frit

        if not enemy_crit:
            typewrite(f"{enemy.name} dealt {enemy_dmg} DMG! Your HP: {player.HP}", 0.05, 1)
            wait(0.5)

        # deal the damage -jlf

        enemy.HP -= player_dmg
        player.HP -= enemy_dmg

        # reseting crits -jlf

        if player_crit:
            player_dmg /= 1.5
        if enemy_crit:
            enemy_dmg /= 1.5
        
        player_crit = False
        enemy_crit = False

        # heal -frit

        if player.HP < 25:
            for item in player.inventory:
                if item.startswith("Potion"):
                    player.inventory.remove(item)
                    typewrite(f"{player.name} drank a potion", 0.05, 0)
                    typewrite("...", 0.07, 1)
                    wait(0.1)
                    typewrite(f"It healed {pot_dic[item]} HP! Your HP: {player.HP}", 0.1, 1)
                    player.HP += pot_dic[item]
                    wait(0.5)
                    break
        
        wait(1.5);clear()
            
    if player.HP <= 0:
        typewrite("you died, skill issue", 0.1, 1)
        typewrite(f"Your maximum reached level was: {player.LVL}", 0.1, 1)
        run = False
    else:
        typewrite(f"you killed {enemy.name}!", 0.1, 1) # the XP var is to print the value of the xp gained. -jlf
        XP = 10 + (elvl * 5)
        typewrite(f"You earned {XP} XP!", 0.1, 1)
        player.XP += XP

# [STRUCTURE FUNCTIONS]: brainfuck -frit

# defstructure: Work around structures (brainfuck, beyond cooked, undertanding this is an ancient art) -frit
def defstructure(str): 
    # i hate my life i hate my life oh boy i do hate it why did i even force myself to do this
    global structure, structures

    structure = structures[str]
    # nasty ugly fuckface annoying i hate this i fucking hate it -frit
    match(structure):
        case "Village":
            village()
        case "Dungeon":
            dungeon()
        case "Castle":
            castle()
    set_chests()
    return

# fucking lamest comments ever, no shit sherlock -frit

# Village: define village structure, -frit
def village():
    typewrite(structure, 0.1, 1)
    wait(1)
    clear()
    Chest(Structure.village_chest, 0)
# Dungeon: define dungeon structure, -frit
def dungeon():
    typewrite(structure, 0.1, 1)
    wait(1)
    clear()
    Chest(Structure.dungeon_chest, random.randint(0,1))
# Castle: define castle structure, -you guessed it, frit
def castle():
    typewrite(structure, 0.1, 1)
    wait(1)
    clear()
    Chest(Structure.castle_chest, random.randint(0,1))

# i'm sure there's a simpler way to do the chest call, but right now i'm at a loss -frit

"""
 |   | |
| |  | _
"""

# OKAY WHO WAS IT THAT DID LOSS AGAIN

# [MAIN GAME LOOP]: GUESS WHAT THE FUCK THIS DOES! -frit

clear()
if not debug:
    typewrite("-----------------------------------------", 0.01, 1)
    typewrite("-----------",0.01, 0);typewrite("WELCOME, TO RPG.PY!",0.1, 0);typewrite("-----------", 0.01, 1)
    typewrite("-----------------------------------------", 0.01, 1)
    wait(1);clear()
    typewrite("First of all, let's pick your name...", 0.1, 1)
    wait(1)
    typewrite("Would you rather have a random name... ", 0.05, 0);wait(0.5);typewrite("or be able to choose your own? (0, 1): ", 0.05, 0)
    q = int(input(""))
    print()
    wait(0.5);clear()
    match(q):
        case 0:
            player.name = randname(0, 10)
        case 1:
            typewrite("choose your name: ", 0.1, 0)
            player.name = input("")
            print()
            FUNnames(player.name)
    clear()
    typewrite("Very well then.", 0.02, 1)
    wait(1)
    typewrite("Your name will be: ", 0.02, 0);wait(0.5);typewrite(f"{player.name}", 0.5, 1)
    wait(0.5)
    typewrite("Your class will be: ", 0.01, 0);wait(1);typewrite(player.CLASS, 0.07, 1)
    wait(1);clear()



while run:
    defstructure(random.randint(0, (len(structures)-1)))
    wait(1)
    combat()
    if player.XP > player.XPR:  # triggers lvlup
        lvlup()
    if not run:
        break

# [jaCinco commit] kys
