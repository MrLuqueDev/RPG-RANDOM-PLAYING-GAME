import math
import random
import time

# RPG.py remake because our code was an UNBEARABLE mess.
# TODO: fucking kys

structure_list = [["Village", "Abandoned Village"], 
                ["Dungeon", "Lava Dungeon"], 
                ["Castle", "Floating Castle"],  
                ["Forest", "Hardwood Forest"],
                ["Desert", "Crystal Desert"]]
structure = None

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
    return structure_list[random.randint(0, len(structure_list) - 1), random.randint(0,1)]

def genstructure(g_structure):
    print(g_structure)


# main game

while True:
    break
