import math
import random
import time

# RPG.py remake because our code was an UNBEARABLE mess.
# TODO: fucking kys

structure_list = ["Village", "Dungeon", "Castle", "Abandoned Village"]
structure = None

# functions for structure functionability

def Village():
    return "Village"

# structure generation functions

def getstructure():
    global structure_list, structure
    return structure_list[random.randint(0, len(structure_list) - 1)]

def genstructure(g_structure):
    print(g_structure)


# main game

genstructure(getstructure())