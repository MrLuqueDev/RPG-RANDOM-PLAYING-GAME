import math
import random
import time

# RPG.py remake because our code was an UNBEARABLE mess.
# TODO: fucking kys

# Game Variables

game = True
name = ""

# stats

HP = None
ATK = None
DEF = None
SPD = None
LCK = None
CRITPROB = None
CRITDMG = None

Class_list = ["Warrior", "Archer", "Wizard"]
Class = ""
MP = None
ACC = None

level = None
XP = None
XP_req = None
XP_res = None

# structure variables

structure_list = [
    ["Village", "Abandoned Village"], # Village 
    ["Dungeon", "Lava Dungeon"], #
    ["Castle", "Floating Castle"],  
    ["Forest", "Hardwood Forest"],
    ["Desert", "Crystal Desert"]
    ]
structure = None
chest = None # bool
enemies = None # bool

# Game functions

def defstats():
    return "Stats"

def levelup():
    global HP, ATK, DEF, SPD, LCK, CRITPROB, CRITDMG, Class, MP, XP, XP_req, XP_res, level

    level += 1
    
    if Class == "Wizard":
        MP += None
        
    HP += None
    ATK += None
    DEF += None
    SPD += None
    LCK += None
    CRITPROB += None
    CRITDMG += None

    XP -= XP_req
    XP_req *= 2
    XP_res = XP - XP_req

    if XP_res > 0:
        XP += XP_res
        XP_res = 0
    else:
        XP_res = 0

def FunNames():
    global name, game, HP, RST, LCK, ATK, SPD

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
        RST = 1
        ATK = 5
        SPD = 5
        LCK = -10
    elif name == "govus":
        HP = 149
        RST = 1
        ATK = 2
        SPD = 10
        LCK = 10
    elif name == "jester":
        HP = 50
        RST = 1
        ATK = 5
        SPD = 5
        LCK = 10

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
    # return structure_list[structure[random.randint(0, len(structure) - 1)]]
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

question = int(input("Want a random name (0) or your own name (1)?: "))

if question == 0:
    RandName(1, 10)
elif question == 1:
    name = input("What is your name?: ")
else:
    print("That's not a valid answer, picking a random name instead")
    RandName(1, 10)
wait(1)
print("your name is: ", name)
wait(0.5)
defstats()
FunNames()
wait(2.5)

while game:
    if HP <= 0:
        break
    if XP_req <= XP:
        levelup()
    genstructure(getstructure())
    wait(1)
