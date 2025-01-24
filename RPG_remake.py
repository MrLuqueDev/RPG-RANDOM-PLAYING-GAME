# RPG.py remake because our code was an UNBEARABLE mess.
# TODO: in the classes list add a matrix (matrix haha funni) where there's the class and the stats so if you want a new class you have it more automatically

# Import libraries

import math
import random
import time

# Game Variables

game = True
name = "" # This is the player's name, duh :v
ename = "" # This is the enemy's name (this one is not so obvious)
mode = None # manual mode or random mode used for selecting names classes and etc, 1 = manual, 0 = random

# Item Variables

keys = None # is that a tboi reference
coins = None # is that a tboi reference
bombs = None # is that a tbo- SHUT THE FUCK UP

# stats

HP = None
ATK = None
DEF = None
SPD = None
LCK = None
CRITPROB = None
CRITDMG = None
DODGEPROB = None
flee = False

# okay killing myself im rewriting this whole shit

# this matrix makes me want to google how to shove the barrel of a gun up my mouth and pull the trigger while listening to the backstreet boys.

Class_list = [
    # name, hp, atk, def, spd, lck, critprob, critdmg, dodgeprob
    ["Random", random.randint(75, 150), random.randint(7, 12), random.randint(5, 10), 10, random.randint(-10, 10), 5, 150, 10], # Mode 1 values (class will be selected randomly after)
    ["Warrior", 130, 10, 8, 5, 0, 5, 150, 10], # Mode 0
    ["Archer", 90, 8, 7, 10, 2, 3, 200, 25],
    ["Wizard", 100, 8, 8, 8, 3, 5, 150, 15] # OCHOCIENTOS OCHENTA Y OCHO
    ]

Class = ""
MP = None
ACC = None

level = 1
XP = None
XP_req = None
XP_res = None

# spell stuff

spell_list = ["Fireball","Healing spell","Frozen shield","Thunderbolt","Weakness","Strength","SHADOW WIZARD MONEY GANG"]
spell_DMG = None

# enemy stats

eHP = None
eATK = None
eDEF = None
eSPD = None
eflee = False

elevel = None
isElite = None
isBoss = None

# structure variables

structure_list = [
    ["Village", "Abandoned Village"], # Villages 
    ["Dungeon", "Lava Dungeon"], # Dungeons
    ["Castle", "Floating Castle"],  # Castles
    ["Forest", "Hardwood Forest"], # Forests
    ["Desert", "Crystal Desert"] # Desert
    ]
structure = None
chest = False
enemies = False

# Game functions

def defstats():
    global HP, ATK, DEF, SPD, LCK, CRITPROB, CRITDMG, Class_list, Class, MP
    if mode == 0:
        random_index = random.randint(1, len(Class_list) - 1)
        Class = Class_list[random_index][0]  # Class name
        HP = Class_list[random_index][1]  # Class stats
        ATK = Class_list[random_index][2]
        DEF = Class_list[random_index][3]
        SPD = Class_list[random_index][4]
        LCK = Class_list[random_index][5]
    else: # hey uhh quick note from the future (wow) uhh it wasnt tomorrow it took me like 3 days to get into it and it fucking sucks please kill me
        var = int(input("Type your preferred class type: "))
        Class = Class_list[var][0]
        HP = Class_list[var][1]
        ATK = Class_list[var][2]
        DEF = Class_list[var][3]
        SPD = Class_list[var][4]
        LCK = Class_list[var][5]
def levelup():
    global HP, ATK, DEF, SPD, LCK, CRITPROB, CRITDMG, Class, MP, XP, XP_req, XP_res, level

    level += 1
    
    if Class == "Wizard":
        MP += random.randint(1, 3)
        
    HP += 16
    ATK = round(ATK + (level / 0.75))
    DEF += 1
    SPD = round(SPD + (level / 0.25))
    LCK += None # do we increase with lvl?
    CRITPROB = round(CRITPROB + (level / 0.5))
    CRITDMG += 5

    XP -= XP_req
    XP_req *= 2
    XP_res = XP - XP_req

    if XP_res > 0:
        XP += XP_res
        XP_res = 0
    else:
        XP_res = 0

def FunNames():
    global name, game, HP, DEF, LCK, ATK, SPD

    if name == "hugo":
        wait(1)
        print("hugo used: Suicide!")
        wait(0.5)
        print("It's super effective!")
        wait(0.5)
        print("hugo is now fucking dead!")
        game = False
    elif name == "frisk":
        input(
            "Warning, This name will make your life a literal living nightmare. do you wish to procceed? (y/n): "
        )
        wait(1.5)
        print("well too bad, you already chose it now HAAHAHAHAHAHAHA")
        HP = 50
        ATK = 5
        DEF = 1
        SPD = 5
        LCK = -10
    elif name == "govus":
        HP = 149
        ATK = 2
        DEF = 1
        SPD = 10
        LCK = 10
    elif name == "jester":
        HP = 50
        ATK = 5
        DEF = 1
        SPD = 5
        LCK = 10

def defenemystats(elevel, isBoss):
    global eHP, eATK, eDEF, eSPD, ename

    rndelite = random.randint(1, 20)
    if rndelite == 1:
        isElite = 1
    
    if isBoss:
        ename = "" # Boss name in caps?
        eHP = None
        eATK = None
        eDEF = None
        eSPD = None
    elif isElite:
        ename = "" # Elite name with decoration?
        eHP = None
        eATK = None
        eDEF =  None
        eSPD = None
    else:
        ename = RandName(1, 7)
        eHP = 100 + (elevel * 15)
        eATK = 5 + elevel
        eDEF = round(4 + (elevel / 1.5))
        eSPD = round(2 + (elevel / 2))

def spells():
    global spell_list, spell_DMG

    rndspell = random.choice(spell_list)
    if rndspell == spell_list[0]:
        return
    elif rndspell == spell_list[1]:
        return
    elif rndspell == spell_list[2]:
        return
    elif rndspell == spell_list[3]:
        return
    elif rndspell == spell_list[4]:
        return
    elif rndspell == spell_list[5]:
        return

def crit_hit():
    global CRITPROB, CRITDMG, ATK

    if random.randint(1, 100) < CRITPROB:
        ATK = round(ATK * (CRITDMG / 100))
        print("crit hit")
        return 1
    else:
        return 0

def enemydeath():
    global elevel, isElite, isBoss, keys, coins, bombs, XP

    if isBoss == 1:
        return
    elif isElite == 1:
        return
    else:
        return

def RandName(char_min, char_max):
    for i in range(random.randint(char_min, char_max)):
        global name
        name += random.choice("abcdefghijklmnopqrstuvwxyz")

# Dev functions

def wait(s):
    time.sleep(s)

# functions for structure functionability

def Villages():
    return "Village"

def Dungeon():
    return "Dungeon"

def Castle():
    return "Castle"

def Forest():
    return "Forest"

def Desert():
    return "Dungeon"

# structure generation functions

def getstructure():
    global structure_list, structure
    structure = structure_list[random.randint(0, len(structure_list) - 1)]
    return structure[random.randint(0, len(structure) - 1)]
def genstructure(g_structure):
    print(g_structure)


# main game

wait(1)
print("------------------------------")
wait(0.5)
print("         [Welcome to]         ")
wait(0.5)
print("             [RPG]            ")
wait(0.5)
print("------------------------------")

mode = int(input("Want a random name (0) or your own name (1)?: "))

if mode == 0:
    RandName(1, 10)
elif mode == 1:
    name = input("What is your name?: ")
else:
    print("That's not a valid answer, picking a random name instead")
    mode = 1
    RandName(1, 10)
wait(1)
print("your name is: ", name)
wait(0.5)
defstats()
FunNames()
wait(2.5)
print("These are your stats: ")
wait(1)
print("Your Class is", Class)
wait(0.4)
print("You're level", level)
wait(0.4)
print("HEALTH (HP):", HP)
wait(0.4)
print("ATTACK (ATK):", ATK)
wait(0.4)
print("DEFENCE (DEF):", DEF)
wait(0.4)
print("SPEED (SPD):", SPD)
wait(0.4)
print("LUCK (LCK):", LCK)
wait(2)

while game:
    if HP <= 0:
        break
    # if XP_req <= XP:
        # levelup()
    genstructure(getstructure())
    wait(1)
