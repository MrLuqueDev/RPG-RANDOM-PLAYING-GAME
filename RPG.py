# TO DO: RANDOMIZE STATS | DONE
# GET RANDOM ATTACK DAMAGE AND SHIT | DONE
# RANDOM GENERATION (get random structures and stuff) | done as well man wtf we're cooking brah
# Random enemies (types and stats and names aswell) | sorta done????
# game items | lmao fuck no
# if you're defending the enemy can't defend (and viceversa?) | WE HAVEN'T EVEN STARTED LLOLOLOLOLOOOLOL
# make enemy types??? | still yet to be aproved
# name codes (put this in the getstats function and if name == "name": stats = value) | not started
# Make quests (when you go to a village there's a 1/5 probability that you can encounter an npc (math.random (1,5) if random == 5)
# if you encounter the npc it'll tell you that he needs you to find something in a certain biome. once you go to those biomes
# you have a probability of 1/2 to encounter it. when you find it you'll forcedly encounter the npc in the next village you go to and
# he will reward you with something for your actions)
# implement days in villages, you can stay there for 1/3 days (randint). enemies and chests randomize again except the chest probabilities are now 1/4 and shops stay the same

# --------------------------------------------------------------------------------

# Import random shit, just like you
# kys

import random
import time
import math

# import pyautogui

# Game variables

game = True
turn = 0
battling = 0
encounter = 0
defending = 0
edefending = 0
content = None

# structure variables

structure_name = ""
has_chest = 0
has_enemies = 0
has_shop = 0
has_item = random.randint(0,5)

# player variables

name = ""
keys = 100
coins = 0
bombs = 0
level = 0
HP = 0
RST = 0
ATK = 0
SPD = 0
LCK = 0
flee = 0

# enemy variables

eHP = 0
eRST = 0
eATK = 0
eSPD = 0
elevel = 0
eflee = 0

# item Values

HP_pot_t1 = 0
RST_pot_t1 = 0
ATK_pot_t1 = 0
SPD_pot_t1 = 0

HP_pot_t2 = 0
RST_pot_t2 = 0
ATK_pot_t2 = 0
SPD_pot_t2 = 0

HP_pot_t3 = 0
RST_pot_t3 = 0
ATK_pot_t3 = 0
SPD_pot_t3 = 0

LCK_pot_t1 = 0
LCK_pot_t2 = 0
LCK_pot_t3 = 0

item_list_pot = [
    HP_pot_t1, RST_pot_t1, ATK_pot_t1, SPD_pot_t1, LCK_pot_t1,
    HP_pot_t2, RST_pot_t2, ATK_pot_t2, SPD_pot_t2, LCK_pot_t2,
    HP_pot_t3, RST_pot_t3, ATK_pot_t3, SPD_pot_t3, LCK_pot_t3
]

item_list = [item_list_pot, ]

# FUNCTIONS :3

def defstats():
    global HP
    global RST
    global ATK
    global SPD
    global LCK

    HP = random.randint(75, 150)
    RST = random.randint(1, 5)
    ATK = round(math.log(random.randint(5, 15)))
    SPD = 10
    LCK = random.randint(-10, 10)

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
        input("Warning, This name will make your life a literal living nightmare. do you wish to procceed? (y/n): ")
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
    

def defenemystats():
    global eHP
    global eRST
    global eATK
    global eSPD
    global elevel

    eHP = random.randint(50, 90) + level
    eRST = random.randint(1, 5)
    eATK = round(math.log(random.randint(4, 10)))
    eSPD = 2


def RandName(char_min, char_max):
    for i in range(random.randint(char_min, char_max)):
        global name
        name += random.choice('abcdefghijklmnopqrstuvwxyz')


def wait(s):
    time.sleep(s)

def GiveItems():
    global content, coins, bombs, keys, structure_name
    randmath = 0
    content = random.randint(1, 33)  # kys
    if content in [1, 2, 3]:
        item_list_pot[0] += 1
        print("You've gained a tier 1 HP potion")
    elif content in [4, 5, 6]:
        item_list_pot[1] += 1
        print("You've gained a tier 1 RESISTANCE potion")
    elif content in [7, 8, 9]:
        item_list_pot[2] += 1
        print("You've gained a tier 1 ATTACK potion")
    elif content in [10, 11, 12]:
        item_list_pot[3] += 1
        print("You've gained a tier 1 SPEED potion")
    elif content in [13, 14, 15]:
        item_list_pot[4] += 1
        print("You've gained a tier 1 LUCK potion")
    elif content in [16, 17]:
        item_list_pot[5] += 1
        print("You've gained a tier 2 HP potion")
    elif content in [18, 19]:
        item_list_pot[6] += 1
        print("You've gained a tier 2 RESISTANCE potion")
    elif content in [20, 21]:
        item_list_pot[7] += 1
        print("You've gained a tier 2 ATTACK potion")
    elif content in [22, 23]:
        item_list_pot[8] += 1
        print("You've gained a tier 2 SPEED potion")
    elif content in [24, 25]:
        item_list_pot[9] += 1
        print("You've gained a tier 2 LUCK potion")
    elif content == 26:
        item_list_pot[10] += 1
        print("You've gained a tier 3 HP potion")
    elif content == 27:
        item_list_pot[11] += 1
        print("You've gained a tier 3 RESISTANCE potion")
    elif content == 28:
        item_list_pot[12] += 1
        print("You've gained a tier 3 ATTACK potion")
    elif content == 29:
        item_list_pot[13] += 1
        print("You've gained a tier 3 SPEED potion")
    elif content == 30:
        item_list_pot[14] += 1
        print("You've gained a tier 3 LUCK potion")
    elif content == 31:
        randmath = random.randint(5, 12)
        coins += randmath
        print("You found", randmath, "Coins! Total coins:", coins)
    elif content == 32:
        keys += 2
        print("You got 2 keys!, now you have:", keys, "keys")
    elif content == 33:
        bombs += 1
        print("You got a bomb!, now you have:", bombs, "bombs")

def Chest():
    global content, coins, bombs, keys, structure_name
    randmath = 0
    print("You found a chest!")
    wait(1)
    print("You look inside...")
    wait(2)
    if keys >= 1 and structure_name != "Village":
        keys -= 1
        GiveItems()
    elif structure_name == "Village":
        randmath = random.randint(1, 5)
        if randmath == 1:
            coins += 1
            print("You just got a coin, now you have:", coins, "coins!")
        elif randmath == 2:
            coins += 3
            print("You just got 3 coins!, now you have:", coins, "coins!")
        elif randmath == 3:
            coins += 5
            print("You just got 5 coins!!, now you have:", coins, "coins!")
        elif randmath == 4:
            coins += 7
            print("You just got 7 coins!!!, now you have:", coins, "coins!")
        elif randmath == 5:
            keys += 1
            print("You got a key!, now you have:", keys, "keys")
    elif keys == 0:
        print("You can't open this chest because you don't have a key to open it")

def GetStructureInfo():
    global structure_name, has_enemies, has_chest, has_item
    has_enemies = random.randint(0, 1)
    encounter = random.randint(0, 1)
    if structure_name != "Abandoned Village":
        has_chest = random.randint(0, 1)
    else:
        has_chest = random.randint(0, 5)
    randomstructure = random.randint(1, 8)
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
    elif randomstructure == 7:
        structure_name = "Dungeon"
    elif randomstructure == 8:
        structure_name = "Abandoned Village"


def Structure(s_name, s_chest, s_enemies, s_item):
    # when called, the code must specify the name, if it has chests and if it has enemies.
    # here we make it check so if the name is X then it will do this and that

    strname = str(s_name)

    if s_name == "Village":
        print("You are in a village")
        wait(1)

        if s_chest == 1:
            print("This", strname, "has a chest!")
            wait(1)
            Chest()
            wait(1)  
        else:
            print("This", strname, "doesn't have a chest.")
            wait(1)

        has_shop = random.randint(0,1)
        if has_shop == 0:
            print("This Village doesn't have a shop")
        elif has_shop == 1:
            print("This Village has a shop!")
            shop = random.randint(1,3)
            if has_shop == 1:
                wait(1)
                if shop == 1:
                    print(name, "has decided to go to a potion shop")
                elif shop == 2:
                    print(name, "has decided to go to a armor shop")
                elif shop == 3:
                    print(name, "has decided to go to a general shop")
    elif s_name == "Forest":
        print("You are in a forest")
        wait(1)
    elif s_name == "Temple":
        print("You are in a temple")
        wait(1)
        if s_chest == 1:
            print("This", strname, "has a chest!")
            wait(1)
            Chest()
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
    elif s_name == "Dungeon":
        print("You are in a dungeon ")
        wait(1)
        if s_chest == 1:
            print("This", strname, "has a chest!")
            wait(1)
            Chest()
            wait(1)
        else:
            print("This", strname, "doesn't have a chest.")
            wait(1)
    elif s_name == "Abandoned Village":
        print("You are in an abandoned village")
        wait(1)
        if s_chest == 5:
            print("This", strname, "has a chest!")
            wait(1)
            Chest()
            wait(1)
        else:
            print("This", strname, "doesn't have a chest.")
            wait(1)
    hitem = random.randint(0,2)
    if hitem == 2:
        print("You look around, searching for anything you can use...")
        if s_item != 5:
            wait(1.5)
            print("You did not find any items")
        else:
            print("You see something in the ground...")
            wait(1.5)
            GiveItems()

    if has_enemies == 1 and encounter == 1:
        battle()
# here we go

def attack():
    # turn 0 is the enemy's turn, 1 is your turn

    global turn, HP, eHP

    if turn == 0:
        HP -= eATK + (RST * 0.5)
    elif turn == 1:
        eHP -= ATK + (eRST * 0.5)


def defend():
    global turn, RST, eRST

    if turn == 1:
        RST *= 2
    elif turn == 0:
        eRST *= 2


def StopDefend():
    global turn, RST, eRST

    if turn == 1:
        RST //= 2
    elif turn == 0:
        eRST //= 2


def item():
    # we need a list with all items
    return


def BattleEnd():
    global battling

    battling = False


def battle():
    global battling, flee, eflee

    while battling:
        rnd_action = random.randint(1, 3)

        if HP <= 0:
            print(name, "has died\nlife stats")
            game = False
        if eHP <= 0:
            # kills the enemy and gives you (xp) money, bombs & keys
            return

        if eHP <= 10:
            eflee = random.randint(0, 1)

        if eflee == 1:
            print("the enemy is fleeing...")

        if HP <= 10:
            flee = random.randint(0, 1)

        if flee == 1:
            print(name, "decided to flee")

        if rnd_action == 1:
            print(name, "has decided to attack!")
            attack()
        elif rnd_action == 2:
            print(name, "has decided to defend!")
            defend()
        elif rnd_action == 3:
            print(name, "has decided to use an item!")
            item()
        if not battling:
            BattleEnd()


# Main game code
# hardcode a game loop so whenever the player dies it can break, and also the structures and shit can loop indefinetely

# while run == true:

question = int(input("Want a random name (0) or your own name (1)?: "))

if question == 0:
    RandName(1, 10)
elif question == 1:
    name = input("What is your name?: ")
else:
    print("That's not a valid answer, picking a random name instead")
    RandName(1,10)
wait(1)
print("your name is: ", name)
wait(0.5)
defstats()
FunNames()
wait(2.5)
print("These are your stats: ")
wait(1)
print("HEALTH (HP):", HP)
wait(.4)
print("RESISTANCE (RST):", RST)
wait(.4)
print("ATTACK (ATK):", ATK)
wait(.4)
print("SPEED (SPD):", SPD)
wait(.4)
print("LUCK (LCK):", LCK)
wait(2)

# game starts

while game:
    if HP <= 0:
        break
    GetStructureInfo()
    Structure(structure_name, has_chest, has_enemies, has_item)
    wait(1)
    # game = False (endgame (haha avengers reference))
