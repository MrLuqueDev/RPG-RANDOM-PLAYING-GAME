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
tehas_questobject = False

# structure variables

structure_name = ""
has_chest = 0
has_enemies = 0
has_shop = 0
has_item = random.randint(0, 5)
npcname = ""
quest = False
hasquestobject = False
hasnpc = 0

# player variables

name = ""
keys = 100
coins = 0
bombs = 0
level = 1
Class = ""
XP = 0
XP_req = 0
XP_res = 0
HP = 0
RST = 0
ATK = 0
SPD = 0
LCK = 0
MP = 0
ACC = 0
critPROB = 0
critDMG = 0
levelHP = 0
levelRST = 0
levelATK = 0
levelSPD = 0
levelLCK = 0
levelMP = 0
flee = 0

# enemy variables

eName = ""
eHP = 0
eRST = 0
eATK = 0
eSPD = 0
elevel = 0
elevelHP = 0
elevelRST = 0
elevelATK = 0
elevelSPD = 0
eflee = 0
isElite = 0
isBoss = 0

# Wizard spells

spells = ["Fireball", "Healing spell", "Thunderbolt", "SHADOW WIZARD MONEY GANG"]

# item Values

item_list_pot_t1 = [0] * 5  # HP, RST, ATK, SPD, LCK
item_list_pot_t2 = [0] * 5
item_list_pot_t3 = [0] * 5

item_list = [item_list_pot_t1, item_list_pot_t2, item_list_pot_t3]

# Add new global variables at the top with other game variables
days_in_village = 0
max_days_in_village = 0
quest_biome = ""
quest_item = ""
quest_reward = 0

# FUNCTIONS :3


def defstats():

    global HP, RST, ATK, SPD, LCK, MP, level, Class, critPROB, critDMG

    rndClass = random.randint(1, 3)

    if rndClass == 1:
        Class = "Warrior"
    elif rndClass == 2:
        Class = "Archer"
    elif rndClass == 3:
        Class = "Wizard"  # SHADOW WIZARD MONEY GANG

    if Class == "Wizard":  # WE LOVE CASTING SPELLS
        MP = round(math.log(random.randint(5, 15)))

    level = 1
    HP = random.randint(75, 150)
    RST = random.randint(1, 5)
    ATK = round(math.log(random.randint(5, 15)))
    SPD = 10
    LCK = random.randint(-10, 10)
    critPROB = 5
    critDMG = 150  # min is 100 which is base dmg


def criticalhit():

    global critPROB, critDMG, ATK

    critprobrnd = random.randint(1, 100)

    if critprobrnd <= critPROB:
        critprob1 = 1
    else:
        critprob1 = 0

    if critprob1 == 1:
        ATK *= critDMG / 100
    elif critprob1 == 0:
        return


def levelup():

    global HP, RST, ATK, SPD, MP, level, Class, XP, XP_req, XP_res

    level += 1

    if Class == "Wizard":
        MP += random.randint(2, 4)

    HP += random.randint(5, 15)
    RST += random.randint(1, 2)
    ATK += random.randint(1, 2)
    SPD += 1

    XP -= XP_req

    XP_req += XP_req * 0.5

    XP_res = XP - XP_req

    if XP_res < 0:
        XP_res = 0
    elif XP_res >= 0:
        XP += XP_res


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


def defenemystats(elevel, isElite, isBoss):

    global eHP, eRST, eATK, eSPD, elevelHP, elevelRST, elevelATK, elevelSPD

    rndelite = random.randint(1, 20)

    if rndelite == 1:
        isElite = 1

    if isBoss == 1:
        return
    # make the rnd name
    # more stats
    elif isElite == 1:
        elevelHP = elevel * 25
        elevelRST = elevel * 3
        elevelATK = elevel * 3
        elevelSPD = elevel * 1

        eHP = random.randint(100, 175) + elevelHP
        eRST = random.randint(2, 8) + elevelRST
        eATK = round(math.log(random.randint(8, 20))) + elevelATK
        eSPD = 3 + elevelSPD
    elif isBoss == 0 and isElite == 0:
        elevelHP = elevel * 10
        elevelRST = elevel
        elevelATK = elevel
        elevelSPD = elevel * 0.5

        eHP = random.randint(50, 90) + elevelHP
        eRST = random.randint(1, 5) + elevelRST
        eATK = round(math.log(random.randint(4, 10))) + elevelATK
        eSPD = 2 + elevelSPD


def enemydeath():

    global elevel, isElite, isBoss, XP, XP_req, coins, keys, bombs

    if isBoss == 1:
        return
    elif isElite == 1:
        return
    elif isBoss == 0 and isElite == 0:
        return


def RandName(char_min, char_max):
    for i in range(random.randint(char_min, char_max)):
        global name
        name += random.choice("abcdefghijklmnopqrstuvwxyz")


def wait(s):
    time.sleep(s)


def GiveItems():

    global content, coins, bombs, keys, structure_name

    randmath = 0
    content = random.randint(1, 33)  # kys
    if content in [1, 2, 3]:
        item_list_pot_t1[0] += 1
        print("You've gained a tier 1 HP potion")
    elif content in [4, 5, 6]:
        item_list_pot_t1[1] += 1
        print("You've gained a tier 1 RESISTANCE potion")
    elif content in [7, 8, 9]:
        item_list_pot_t1[2] += 1
        print("You've gained a tier 1 ATTACK potion")
    elif content in [10, 11, 12]:
        item_list_pot_t1[3] += 1
        print("You've gained a tier 1 SPEED potion")
    elif content in [13, 14, 15]:
        item_list_pot_t1[4] += 1
        print("You've gained a tier 1 LUCK potion")
    elif content in [16, 17]:
        item_list_pot_t2[0] += 1
        print("You've gained a tier 2 HP potion")
    elif content in [18, 19]:
        item_list_pot_t2[1] += 1
        print("You've gained a tier 2 RESISTANCE potion")
    elif content in [20, 21]:
        item_list_pot_t2[2] += 1
        print("You've gained a tier 2 ATTACK potion")
    elif content in [22, 23]:
        item_list_pot_t2[3] += 1
        print("You've gained a tier 2 SPEED potion")
    elif content in [24, 25]:
        item_list_pot_t2[4] += 1
        print("You've gained a tier 2 LUCK potion")
    elif content == 26:
        item_list_pot_t3[0] += 1
        print("You've gained a tier 3 HP potion")
    elif content == 27:
        item_list_pot_t3[1] += 1
        print("You've gained a tier 3 RESISTANCE potion")
    elif content == 28:
        item_list_pot_t3[2] += 1
        print("You've gained a tier 3 ATTACK potion")
    elif content == 29:
        item_list_pot_t3[3] += 1
        print("You've gained a tier 3 SPEED potion")
    elif content == 30:
        item_list_pot_t3[4] += 1
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


def GetNormalEvent():

    global event_name

    randomevent = random.randint(1, 3)

    if randomevent == 1:
        event_name = "bro falls"
    elif randomevent == 2:
        event_name = "you got hit by a stone"
    elif randomevent == 3:
        event_name = "alcoholics"


def GetStructureInfo():
    global structure_name, has_enemies, has_chest, has_item, tehas_questobject
    has_enemies = random.randint(0, 1)
    encounter = random.randint(0, 1)
    if structure_name != "Abandoned Village":
        has_chest = random.randint(0, 1)
    else:
        has_chest = random.randint(0, 5)
    randomstructure = random.randint(1, 8)
    tehas_questobject = random.randint(1, 4)
    hasnpc = random.randint(1, 5)
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


def Structure(
    s_name, s_chest, s_enemies, s_item, s_questobject, s_npc, has_questobject
):
    # when called, the code must specify the name, if it has chests and if it has enemies.
    # here we make it check so if the name is X then it will do this and that

    strname = str(s_name)
    global quest, hasquestobject, days_in_village, max_days_in_village, quest_biome, quest_item, quest_reward, coins
    
    if s_name == "Village":
        print("You are in a village")
        wait(1)
        
        # Handle days in village
        max_days_in_village = random.randint(1, 3)
        days_in_village = 0
        print(f"You can stay in this village for {max_days_in_village} days")
        
        while days_in_village < max_days_in_village:
            days_in_village += 1
            print(f"\nDay {days_in_village} in the village:")
            
            # Randomize chests and enemies each day
            if random.randint(1, 4) == 1:  # 1/4 chance for chest
                Chest()
            
            # Shop stays the same throughout the days
            if has_shop == 1:
                print("The village shop is open")
                # Shop logic here...
            
            # Quest system
            if not quest and s_npc == 1:
                biomes = ["Forest", "Temple", "Plains", "Desert", "Swamp", "Dungeon"]
                items = ["Ancient Relic", "Lost Ring", "Magic Scroll", "Family Heirloom", "Sacred Gem"]
                
                quest_biome = random.choice(biomes)
                quest_item = random.choice(items)
                quest_reward = random.randint(20, 50)
                
                print(f"\nA villager approaches you...")
                wait(1)
                print(f"Please help! I've lost my {quest_item} somewhere in the {quest_biome}.")
                print(f"If you find it, I'll reward you with {quest_reward} coins!")
                quest = True
            
            # Handle quest completion
            if quest and hasquestobject:
                print(f"\nThe villager spots you with their {quest_item}!")
                wait(1)
                print(f"Thank you so much! Here are your {quest_reward} coins!")
                coins += quest_reward
                hasquestobject = False
                quest = False
            
            # Ask player if they want to stay another day
            if days_in_village < max_days_in_village:
                choice = input("\nDo you want to stay another day? (y/n): ").lower()
                if choice != 'y':
                    break
                
    # For non-village locations that have active quests
    elif quest and not hasquestobject and s_name == quest_biome:
        if random.randint(1, 2) == 1:  # 1/2 chance to find quest item
            print(f"\nYou found the {quest_item}!")
            hasquestobject = True
            
    # Rest of the original Structure function code...


# here we go


def attack():
    # turn 0 is the enemy's turn, 1 is your turn
    # need to add critical system

    global turn, HP, eHP, ATK, eATK, RST, eRST, Class, ACC, MP, critPROB, critDMG

    if turn == 0:
        HP -= eATK + (RST * 0.5)
    elif turn == 1:
        if Class == "Warrior":
            eHP -= ATK + (eRST * 0.5)
        elif Class == "Archer":
            ACC = random.randint(1, 5)
            if ACC in [1, 2, 3, 4]:
                print("your arrow did")
            elif ACC == 5:
                print("critical hit !!")
        elif Class == "Wizard":
            rnd_spell = random.randint(1, 100)
            if rnd_spell <= 33:
                print(name, "has used fireball!")
            elif rnd_spell >= 34 and rnd_spell <= 66:
                print(name, "has used healing!")
            elif rnd_spell >= 67 and rnd_spell <= 99:
                print(name, "has used thunderbolt!")
            elif rnd_spell == 100:
                print("SHADOW WIZARD MONEY GANG")
        return


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


def use_items():

    global HP, RST, ATK, SPD, LCK
    # Maybe a boss fight?
    # day night circle, and 50/50 to stay in the same place

    rnd_use_items = random.randint(1, 15)

    if max_HP / 2 >= HP:  # type: ignore
        more_prob_hp_pot = random.randint(1, 4)

    if more_prob_hp_pot == 1 or more_prob_hp_pot == 2 or more_prob_hp_pot == 3:
        # more probs to get hp pots (t1, t2 & t3)
        return
    else:
        # go back to the function
        return

    if rnd_use_items == 1 and item_list_pot_t1[0] >= 1:
        item_list_pot_t1[0] -= 1
        HP += 20
        print(name, " used a tier 1 HP potion")
    elif rnd_use_items == 2 and item_list_pot_t1[1] >= 1:
        item_list_pot_t1[1] -= 1
        RST += 5
        print(name, " used a tier 1 RST potion")
    elif rnd_use_items == 3 and item_list_pot_t1[2] >= 1:
        item_list_pot_t1[2] -= 1
        ATK += 5
        print(name, " used a tier 1 ATK potion")
    elif rnd_use_items == 4 and item_list_pot_t1[3] >= 1:
        item_list_pot_t1[3] -= 1
        SPD += 5
        print(name, " used a tier 1 SPD potion")
    elif rnd_use_items == 5 and item_list_pot_t1[4] >= 1:
        item_list_pot_t1[4] -= 1
        LCK += 5
        print(name, " used a tier 1 LCK potion")
    elif rnd_use_items == 6 and item_list_pot_t2[0] >= 1:
        item_list_pot_t2[0] -= 1
        HP += max_HP / 2
        print(name, " used a tier 2 HP potion")
    elif rnd_use_items == 7 and item_list_pot_t2[1] >= 1:
        item_list_pot_t2[1] -= 1
        RST += 10
        print(name, " used a tier 2 RST potion")
    elif rnd_use_items == 8 and item_list_pot_t2[2] >= 1:
        item_list_pot_t2[2] -= 1
        ATK += 10
        print(name, " used a tier 2 ATK potion")
    elif rnd_use_items == 9 and item_list_pot_t2[3] >= 1:
        item_list_pot_t2[3] -= 1
        SPD += 10
        print(name, " used a tier 2 SPD potion")
    elif rnd_use_items == 10 and item_list_pot_t2[4] >= 1:
        item_list_pot_t2[4] -= 1
        LCK += 10
        print(name, " used a tier 2 LCK potion")
    elif rnd_use_items == 11 and item_list_pot_t3[0] >= 1:
        item_list_pot_t3[0] -= 1
        HP = max_HP
        print(name, " used a tier 3 HP potion")
    elif rnd_use_items == 12 and item_list_pot_t3[1] >= 1:
        item_list_pot_t3[1] -= 1
        RST += 20
        print(name, " used a tier 3 HP potion")
    elif rnd_use_items == 13 and item_list_pot_t3[2] >= 1:
        item_list_pot_t3[2] -= 1
        ATK += 20
        print(name, " used a tier 3 ATK potion")
    elif rnd_use_items == 14 and item_list_pot_t3[3] >= 1:
        item_list_pot_t3[3] -= 1
        SPD += 20
        print(name, " used a tier 3 SPD potion")
    elif rnd_use_items == 15 and item_list_pot_t3[4] >= 1:
        item_list_pot_t3[4] -= 1
        LCK += 20
        print(name, " used a tier 3 LCK potion")
    else:
        print("bro doesnt have items")


def BattleEnd():

    global battling

    battling = False


def battle():
    global battling, flee, eflee, turn, HP, eHP

    battling = True
    while battling:
        # Show battle status
        print(f"\nYour HP: {HP}")
        print(f"Enemy HP: {eHP}\n")

        # Player turn
        turn = 1
        if not handle_turn():
            return

        # Enemy turn
        turn = 0
        if not handle_turn():
            return


def handle_turn():
    """Handle a single turn in battle. Returns False if battle should end."""
    global HP, eHP, flee, eflee

    if HP <= 0:
        print(f"{name} has died\nGame Over")
        return False

    if eHP <= 0:
        print("Enemy defeated!")
        enemydeath()
        return False

    # Handle fleeing
    if HP <= 10:
        flee = random.randint(0, 1)
        if flee == 1:
            print(f"{name} fled from battle!")
            return False

    if eHP <= 10:
        eflee = random.randint(0, 1)
        if eflee == 1:
            print("Enemy fled from battle!")
            return False

    # Handle actions
    if turn == 1:
        action = input("What will you do? (attack/defend/item): ").lower()
        if action == "attack":
            attack()
        elif action == "defend":
            defend()
        elif action == "item":
            use_items()
    else:
        # Enemy AI
        rnd_action = random.randint(1, 3)
        if rnd_action == 1:
            print("Enemy attacks!")
            attack()
        elif rnd_action == 2:
            print("Enemy defends!")
            defend()

    return True


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
print("RESISTANCE (RST):", RST)
wait(0.4)
print("ATTACK (ATK):", ATK)
wait(0.4)
print("SPEED (SPD):", SPD)
wait(0.4)
print("LUCK (LCK):", LCK)
wait(2)

# game starts

while game:
    if HP <= 0:
        break
    if XP_req <= XP:
        levelup()
    GetStructureInfo()
    Structure(
        structure_name,
        has_chest,
        has_enemies,
        has_item,
        hasquestobject,
        hasnpc,
        tehas_questobject,
    )
    wait(1)
    # game = False (endgame (haha avengers reference))
