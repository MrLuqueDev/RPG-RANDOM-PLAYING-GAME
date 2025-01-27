# RPG.py remake because our code was an UNBEARABLE mess.
# TODO: in the classes list add a matrix (matrix haha funni) where there's the class and the stats so if you want a new class you have it more automatically

# Import libraries

import math
import random
import time
import json
import os

# Game Variables

game = True
name = "" # This is the player's name, duh :v
ename = "" # This is the enemy's name (this one is not so obvious)
mode = None # manual mode or random mode used for selecting names classes and etc, 1 = manual, 0 = random

# Item Variables

class Inventory:
    def __init__(self):
        self.keys = 0
        self.coins = 0
        self.bombs = 0
        self.potions = {
            "health": {"small": 0, "medium": 0, "large": 0},
            "mana": {"small": 0, "medium": 0, "large": 0},
            "strength": {"small": 0, "medium": 0, "large": 0},
            "defense": {"small": 0, "medium": 0, "large": 0},
            "speed": {"small": 0, "medium": 0, "large": 0}
        }
        self.equipment = {
            "weapon": None,
            "armor": None,
            "accessory": None
        }

inventory = Inventory()

# Status Effects
class StatusEffect:
    def __init__(self, name, duration, effect_type, magnitude):
        self.name = name
        self.duration = duration
        self.effect_type = effect_type  # "buff" or "debuff"
        self.magnitude = magnitude
        
active_effects = []

# Stats
class Stats:
    def __init__(self):
        self.HP = 0
        self.MAX_HP = 0
        self.MP = 0
        self.MAX_MP = 0
        self.ATK = 0
        self.DEF = 0
        self.SPD = 0
        self.LCK = 0
        self.CRITPROB = 0
        self.CRITDMG = 0
        self.DODGEPROB = 0
        self.level = 1
        self.XP = 0
        self.XP_req = 100  # Base XP required for first level
        
player_stats = Stats()

# this matrix makes me want to google how to shove the barrel of a gun up my mouth and pull the trigger while listening to the backstreet boys.

Class_list = [
    # name,  hp,   mp,   atk,  def,  spd,  lck, critprob, critdmg, dodgeprob
    ["Random", random.randint(75, 150), random.randint(20, 40), random.randint(7, 12), random.randint(5, 10), 10, random.randint(-10, 10), 5, 150, 10],
    ["Warrior", 130, 20, 12, 10, 5, 0, 5, 150, 10],
    ["Archer", 90, 20, 10, 7, 12, 2, 15, 200, 25],
    ["Wizard", 100, 100, 8, 6, 8, 3, 5, 150, 15]
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

# Quest system
class Quest:
    def __init__(self, name, description, reward, target_type, target_amount):
        self.name = name
        self.description = description
        self.reward = reward
        self.target_type = target_type  # "kill", "collect", "explore"
        self.target_amount = target_amount
        self.progress = 0
        self.completed = False

# Lista de misiones disponibles
available_quests = [
    Quest("Monster Hunter", "Defeat monsters in the area", 100, "kill", 5),
    Quest("Treasure Hunter", "Find treasure chests", 150, "collect", 3),
    Quest("Explorer", "Discover new locations", 200, "explore", 4),
    Quest("Potion Collector", "Collect health potions", 120, "collect", 3),
    Quest("Elite Slayer", "Defeat elite enemies", 300, "kill", 2)
]

# Lista de misiones activas
active_quests = []

# Game functions

def defstats():
    global player_stats, Class_list, Class
    if mode == 0:
        random_index = random.randint(1, len(Class_list) - 1)
        Class = Class_list[random_index][0]  # nombre
        player_stats.MAX_HP = Class_list[random_index][1]  # hp
        player_stats.HP = player_stats.MAX_HP
        player_stats.MAX_MP = Class_list[random_index][2]  # mp
        player_stats.MP = player_stats.MAX_MP
        player_stats.ATK = Class_list[random_index][3]  # atk
        player_stats.DEF = Class_list[random_index][4]  # def
        player_stats.SPD = Class_list[random_index][5]  # spd
        player_stats.LCK = Class_list[random_index][6]  # lck
        player_stats.CRITPROB = Class_list[random_index][7]  # critprob
        player_stats.CRITDMG = Class_list[random_index][8]  # critdmg
        player_stats.DODGEPROB = Class_list[random_index][9]  # dodgeprob
    else:
        print("\nAvailable Classes:")
        for i, class_data in enumerate(Class_list):
            print(f"{i}: {class_data[0]}")
        var = int(input("\nType your preferred class number: "))
        if 0 <= var < len(Class_list):
            Class = Class_list[var][0]
            player_stats.MAX_HP = Class_list[var][1]
            player_stats.HP = player_stats.MAX_HP
            player_stats.MAX_MP = Class_list[var][2]
            player_stats.MP = player_stats.MAX_MP
            player_stats.ATK = Class_list[var][3]
            player_stats.DEF = Class_list[var][4]
            player_stats.SPD = Class_list[var][5]
            player_stats.LCK = Class_list[var][6]
            player_stats.CRITPROB = Class_list[var][7]
            player_stats.CRITDMG = Class_list[var][8]
            player_stats.DODGEPROB = Class_list[var][9]
        else:
            print("Invalid class selection. Choosing Random class.")
            defstats()

def levelup():
    global player_stats, Class
    
    player_stats.level += 1
    
    # Base stat increases
    player_stats.MAX_HP += 15 + random.randint(1, 6)
    player_stats.HP = player_stats.MAX_HP
    player_stats.ATK += 2 + random.randint(0, 2)
    player_stats.DEF += 1 + random.randint(0, 2)
    player_stats.SPD += 1 + random.randint(0, 1)
    player_stats.LCK += random.randint(0, 2)
    
    # Class-specific bonuses
    if Class == "Warrior":
        player_stats.MAX_HP += 5
        player_stats.ATK += 1
        player_stats.DEF += 1
    elif Class == "Archer":
        player_stats.SPD += 2
        player_stats.CRITPROB += 1
        player_stats.DODGEPROB += 1
    elif Class == "Wizard":
        player_stats.MAX_MP += 10 + random.randint(1, 5)
        player_stats.MP = player_stats.MAX_MP
        
    # Update XP requirements
    player_stats.XP -= player_stats.XP_req
    player_stats.XP_req = int(player_stats.XP_req * 1.5)  # 50% increase per level

def cast_spell(spell_name):
    global player_stats, active_effects
    
    if spell_name not in spell_list:
        print("Invalid spell!")
        return False
        
    spell = spell_list[spell_name]
    
    if player_stats.MP < spell.mp_cost:
        print("Not enough MP!")
        return False
        
    player_stats.MP -= spell.mp_cost
    
    if spell.effect:
        active_effects.append(spell.effect)
        print(f"Applied {spell.effect.name} effect!")
        
    return spell.damage

def update_effects():
    global active_effects, player_stats
    
    for effect in active_effects[:]:  # Copy list to safely remove while iterating
        effect.duration -= 1
        
        if effect.effect_type == "buff":
            if effect.name == "Protected":
                player_stats.DEF += effect.magnitude
            elif effect.name == "Quickened":
                player_stats.SPD += effect.magnitude
        elif effect.effect_type == "debuff":
            if effect.name == "Burn":
                player_stats.HP -= effect.magnitude
            elif effect.name == "Frozen":
                player_stats.SPD -= effect.magnitude
            elif effect.name == "Paralyzed":
                player_stats.ATK -= effect.magnitude
                
        if effect.duration <= 0:
            active_effects.remove(effect)
            # Revert stat changes
            if effect.effect_type == "buff":
                if effect.name == "Protected":
                    player_stats.DEF -= effect.magnitude
                elif effect.name == "Quickened":
                    player_stats.SPD -= effect.magnitude

def save_game():
    global name, Class, player_stats, inventory, active_effects, active_quests
    
    save_data = {
        "player_name": name,
        "class": Class,
        "stats": vars(player_stats),
        "inventory": vars(inventory),
        "active_effects": [(e.name, e.duration, e.effect_type, e.magnitude) for e in active_effects],
        "active_quests": [(q.name, q.progress, q.completed) for q in active_quests] if active_quests else []
    }
    
    with open(f"save_{name}.json", "w") as f:
        json.dump(save_data, f)
    print("Game saved successfully!")

def load_game(save_file):
    global name, Class, player_stats, inventory, active_effects, active_quests
    
    try:
        with open(save_file, "r") as f:
            save_data = json.load(f)
            
        name = save_data["player_name"]
        Class = save_data["class"]
        
        # Load stats
        for key, value in save_data["stats"].items():
            setattr(player_stats, key, value)
            
        # Load inventory
        for key, value in save_data["inventory"].items():
            setattr(inventory, key, value)
            
        # Load effects
        active_effects = [StatusEffect(name, dur, type_, mag) 
                         for name, dur, type_, mag in save_data["active_effects"]]
                         
        # Load quests
        active_quests = []
        for quest_name, progress, completed in save_data["active_quests"]:
            for quest in available_quests:
                if quest.name == quest_name:
                    quest.progress = progress
                    quest.completed = completed
                    active_quests.append(quest)
                    
        print("Game loaded successfully!")
        return True
    except:
        print("Error loading save file!")
        return False

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

class Enemy:
    def __init__(self, name, level, is_elite=False, is_boss=False):
        self.name = name
        self.level = level
        self.is_elite = is_elite
        self.is_boss = is_boss
        self.stats = Stats()
        self.active_effects = []
        self.loot_table = {}
        self.initialize_stats()
        
    def initialize_stats(self):
        if self.is_boss:
            self.stats.MAX_HP = 200 + (self.level * 25)
            self.stats.HP = self.stats.MAX_HP
            self.stats.ATK = 15 + (self.level * 2)
            self.stats.DEF = 12 + (self.level * 1.5)
            self.stats.SPD = 8 + (self.level)
            self.setup_boss_loot()
        elif self.is_elite:
            self.stats.MAX_HP = 150 + (self.level * 20)
            self.stats.HP = self.stats.MAX_HP
            self.stats.ATK = 12 + (self.level * 1.5)
            self.stats.DEF = 10 + (self.level)
            self.stats.SPD = 7 + (self.level * 0.5)
            self.setup_elite_loot()
        else:
            self.stats.MAX_HP = 100 + (self.level * 15)
            self.stats.HP = self.stats.MAX_HP
            self.stats.ATK = 8 + self.level
            self.stats.DEF = 6 + (self.level * 0.5)
            self.stats.SPD = 5 + (self.level * 0.5)
            self.setup_normal_loot()
            
    def setup_normal_loot(self):
        self.loot_table = {
            "coins": (5, 15),  # (min, max)
            "xp": 50 + (self.level * 10),
            "items": {
                "health_potion_small": 0.3,  # 30% chance
                "mana_potion_small": 0.2
            }
        }
        
    def setup_elite_loot(self):
        self.loot_table = {
            "coins": (15, 30),
            "xp": 100 + (self.level * 20),
            "items": {
                "health_potion_medium": 0.4,
                "mana_potion_medium": 0.3,
                "key": 0.5
            }
        }
        
    def setup_boss_loot(self):
        self.loot_table = {
            "coins": (50, 100),
            "xp": 200 + (self.level * 30),
            "items": {
                "health_potion_large": 1.0,  # Guaranteed
                "mana_potion_large": 0.8,
                "key": 1.0,
                "special_item": 0.5
            }
        }

def battle(enemy):
    global player_stats, inventory, active_effects
    
    print(f"\nBattle start! You encounter {enemy.name}")
    print(f"Enemy Level: {enemy.level}")
    print(f"Enemy HP: {enemy.stats.HP}/{enemy.stats.MAX_HP}")
    
    turn = 0  # 0 for player, 1 for enemy
    
    while True:
        # Update status effects
        update_effects()
        
        # Show current status
        print(f"\nYour HP: {player_stats.HP}/{player_stats.MAX_HP}")
        print(f"Your MP: {player_stats.MP}/{player_stats.MAX_MP}")
        print(f"Enemy HP: {enemy.stats.HP}/{enemy.stats.MAX_HP}")
        
        if turn == 0:  # Player turn
            print("\nYour turn! What will you do?")
            print("1. Attack")
            print("2. Cast Spell")
            print("3. Use Item")
            print("4. Defend")
            print("5. Try to Flee")
            
            choice = input("Choose your action (1-5): ")
            
            if choice == "1":  # Attack
                damage = calculate_damage(player_stats, enemy.stats)
                enemy.stats.HP -= damage
                print(f"You deal {damage} damage!")
                
            elif choice == "2" and Class == "Wizard":  # Cast Spell
                print("\nAvailable Spells:")
                for i, spell in enumerate(spell_list.keys(), 1):
                    print(f"{i}. {spell}")
                spell_choice = input("Choose a spell (or 0 to go back): ")
                if spell_choice.isdigit() and 0 < int(spell_choice) <= len(spell_list):
                    spell_name = list(spell_list.keys())[int(spell_choice)-1]
                    damage = cast_spell(spell_name)
                    if damage:
                        if damage < 0:  # Healing spell
                            player_stats.HP = min(player_stats.MAX_HP, player_stats.HP - damage)
                            print(f"You heal for {-damage} HP!")
                        else:
                            enemy.stats.HP -= damage
                            print(f"Your spell deals {damage} damage!")
                            
            elif choice == "3":  # Use Item
                use_item()
                
            elif choice == "4":  # Defend
                player_stats.DEF *= 1.5  # Temporary defense boost
                print("You take a defensive stance!")
                
            elif choice == "5":  # Flee
                if try_flee(player_stats.SPD, enemy.stats.SPD):
                    print("You successfully fled from battle!")
                    return "fled"
                else:
                    print("Couldn't escape!")
        
        else:  # Enemy turn
            # Simple enemy AI
            if enemy.stats.HP < enemy.stats.MAX_HP * 0.3:  # Low HP
                if random.random() < 0.7:  # 70% chance to defend
                    enemy.stats.DEF *= 1.5
                    print(f"{enemy.name} takes a defensive stance!")
                else:
                    damage = calculate_damage(enemy.stats, player_stats)
                    player_stats.HP -= damage
                    print(f"{enemy.name} attacks for {damage} damage!")
            else:
                damage = calculate_damage(enemy.stats, player_stats)
                player_stats.HP -= damage
                print(f"{enemy.name} attacks for {damage} damage!")
        
        # Check battle end conditions
        if player_stats.HP <= 0:
            print("You have been defeated!")
            return "defeat"
        elif enemy.stats.HP <= 0:
            print(f"You defeated {enemy.name}!")
            give_loot(enemy.loot_table)
            return "victory"
            
        # Reset temporary effects
        if turn == 0:
            player_stats.DEF = player_stats.DEF / 1.5 if player_stats.DEF > player_stats.ATK else player_stats.DEF
        else:
            enemy.stats.DEF = enemy.stats.DEF / 1.5 if enemy.stats.DEF > enemy.stats.ATK else enemy.stats.DEF
            
        # Switch turns
        turn = 1 - turn

def calculate_damage(attacker_stats, defender_stats):
    base_damage = attacker_stats.ATK - (defender_stats.DEF * 0.5)
    
    # Critical hit check
    if random.random() * 100 < attacker_stats.CRITPROB:
        base_damage *= attacker_stats.CRITDMG / 100
        print("Critical hit!")
        
    # Dodge check
    if random.random() * 100 < defender_stats.DODGEPROB:
        print("Attack dodged!")
        return 0
        
    # Add some randomness
    damage = max(1, base_damage * random.uniform(0.9, 1.1))
    return round(damage)

def try_flee(player_speed, enemy_speed):
    flee_chance = 0.4 + ((player_speed - enemy_speed) * 0.1)
    return random.random() < min(0.8, max(0.2, flee_chance))

def give_loot(loot_table):
    # Give coins
    coins_min, coins_max = loot_table["coins"]
    coins_gained = random.randint(coins_min, coins_max)
    inventory.coins += coins_gained
    print(f"You gained {coins_gained} coins!")
    
    # Give XP
    player_stats.XP += loot_table["xp"]
    print(f"You gained {loot_table['xp']} XP!")
    
    # Check for level up
    while player_stats.XP >= player_stats.XP_req:
        levelup()
        print(f"Level up! You are now level {player_stats.level}!")
    
    # Give items based on probabilities
    for item, chance in loot_table["items"].items():
        if random.random() < chance:
            if "health_potion" in item:
                size = item.split("_")[-1]
                inventory.potions["health"][size] += 1
                print(f"You found a {size} health potion!")
            elif "mana_potion" in item:
                size = item.split("_")[-1]
                inventory.potions["mana"][size] += 1
                print(f"You found a {size} mana potion!")
            elif item == "key":
                inventory.keys += 1
                print("You found a key!")
            elif item == "special_item":
                # TODO: Implement special item drops
                print("You found a special item!")

def use_item():
    print("\nAvailable Items:")
    items_available = False
    
    # Show health potions
    for size, count in inventory.potions["health"].items():
        if count > 0:
            items_available = True
            print(f"Health Potion ({size}): {count}")
            
    # Show mana potions
    for size, count in inventory.potions["mana"].items():
        if count > 0:
            items_available = True
            print(f"Mana Potion ({size}): {count}")
            
    if not items_available:
        print("No items available!")
        return
        
    item_choice = input("\nWhat item would you like to use? (or press Enter to cancel): ").lower()
    
    if not item_choice:
        return
        
    potion_type = None
    size = None
    
    if "health" in item_choice:
        potion_type = "health"
        for s in ["small", "medium", "large"]:
            if s in item_choice:
                size = s
                break
    elif "mana" in item_choice:
        potion_type = "mana"
        for s in ["small", "medium", "large"]:
            if s in item_choice:
                size = s
                break
                
    if potion_type and size and inventory.potions[potion_type][size] > 0:
        inventory.potions[potion_type][size] -= 1
        
        if potion_type == "health":
            heal_amount = {"small": 30, "medium": 60, "large": 120}[size]
            player_stats.HP = min(player_stats.MAX_HP, player_stats.HP + heal_amount)
            print(f"Restored {heal_amount} HP!")
        else:  # mana
            mana_amount = {"small": 20, "medium": 40, "large": 80}[size]
            player_stats.MP = min(player_stats.MAX_MP, player_stats.MP + mana_amount)
            print(f"Restored {mana_amount} MP!")
    else:
        print("Invalid item selection!")

def main():
    global name, Class, player_stats, inventory, active_effects, active_quests, game
    
    print("------------------------------")
    print("         [Welcome to]         ")
    print("             [RPG]            ")
    print("------------------------------")
    
    # Check for save file
    save_files = [f for f in os.listdir() if f.startswith("save_") and f.endswith(".json")]
    if save_files:
        print("\nSave files found:")
        for i, save_file in enumerate(save_files, 1):
            print(f"{i}. {save_file}")
        choice = input("\nWould you like to load a save file? (number or n): ")
        if choice.isdigit() and 1 <= int(choice) <= len(save_files):
            if load_game(save_files[int(choice)-1]):
                print(f"\nWelcome back, {name}!")
    
    if not name:  # New game
        mode = int(input("\nWant a random name (0) or your own name (1)?: "))
        
        if mode == 0:
            RandName(1, 10)
        elif mode == 1:
            name = input("What is your name?: ")
        else:
            print("That's not a valid answer, picking a random name instead")
            RandName(1, 10)
            
        print(f"\nYour name is: {name}")
        defstats()
        FunNames()
        
        print("\nThese are your stats:")
        print(f"Your Class is {Class}")
        print(f"Level: {player_stats.level}")
        print(f"HEALTH (HP): {player_stats.HP}/{player_stats.MAX_HP}")
        if player_stats.MAX_MP > 0:
            print(f"MANA (MP): {player_stats.MP}/{player_stats.MAX_MP}")
        print(f"ATTACK (ATK): {player_stats.ATK}")
        print(f"DEFENSE (DEF): {player_stats.DEF}")
        print(f"SPEED (SPD): {player_stats.SPD}")
        print(f"LUCK (LCK): {player_stats.LCK}")
        print(f"CRIT CHANCE: {player_stats.CRITPROB}%")
        print(f"CRIT DAMAGE: {player_stats.CRITDMG}%")
        print(f"DODGE CHANCE: {player_stats.DODGEPROB}%")
    
    # Main game loop
    while game and player_stats.HP > 0:
        # Auto-save every few actions
        if random.random() < 0.2:  # 20% chance each loop
            save_game()
            
        # Get current location
        structure = getstructure()
        print(f"\nYou are in a {structure}")
        
        # Location options
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Check Stats")
        print("3. View Inventory")
        print("4. View Quests")
        print("5. Save Game")
        print("6. Quit Game")
        
        choice = input("\nChoose an action (1-6): ")
        
        if choice == "1":  # Explore
            # Random encounter check
            if random.random() < 0.7:  # 70% chance for encounter
                encounter_type = random.random()
                
                if encounter_type < 0.6:  # 60% chance for enemy
                    # Create enemy based on location and player level
                    enemy_level = max(1, player_stats.level + random.randint(-2, 2))
                    is_elite = random.random() < 0.1  # 10% chance for elite
                    is_boss = random.random() < 0.05  # 5% chance for boss
                    
                    enemy_name = RandName(3, 8)  # Generate random enemy name
                    enemy = Enemy(enemy_name, enemy_level, is_elite, is_boss)
                    
                    result = battle(enemy)
                    if result == "defeat":
                        game = False
                        print("\nGame Over!")
                        break
                        
                elif encounter_type < 0.8:  # 20% chance for chest
                    if structure != "Village":
                        if inventory.keys > 0:
                            print("\nYou found a chest!")
                            if input("Would you like to open it? (y/n): ").lower() == 'y':
                                inventory.keys -= 1
                                give_loot({
                                    "coins": (10, 25),
                                    "xp": 30,
                                    "items": {
                                        "health_potion_small": 0.5,
                                        "mana_potion_small": 0.3,
                                        "key": 0.2
                                    }
                                })
                        else:
                            print("\nYou found a chest but don't have any keys!")
                    else:
                        # Village chests don't need keys
                        give_loot({
                            "coins": (5, 15),
                            "items": {
                                "health_potion_small": 0.3,
                                "key": 0.2
                            }
                        })
                        
                else:  # 20% chance for special event
                    events = [
                        "You find a mysterious shrine",
                        "You discover an ancient inscription",
                        "You meet a traveling merchant",
                        "You find a training dummy",
                        "You discover a healing spring"
                    ]
                    event = random.choice(events)
                    print(f"\n{event}")
                    # TODO: Implement special event effects
            
        elif choice == "2":  # Check Stats
            print(f"\nLevel: {player_stats.level}")
            print(f"XP: {player_stats.XP}/{player_stats.XP_req}")
            print(f"HP: {player_stats.HP}/{player_stats.MAX_HP}")
            if player_stats.MAX_MP > 0:
                print(f"MP: {player_stats.MP}/{player_stats.MAX_MP}")
            print(f"ATK: {player_stats.ATK}")
            print(f"DEF: {player_stats.DEF}")
            print(f"SPD: {player_stats.SPD}")
            print(f"LCK: {player_stats.LCK}")
            print(f"CRIT CHANCE: {player_stats.CRITPROB}%")
            print(f"CRIT DAMAGE: {player_stats.CRITDMG}%")
            print(f"DODGE CHANCE: {player_stats.DODGEPROB}%")
            
            if active_effects:
                print("\nActive Effects:")
                for effect in active_effects:
                    print(f"{effect.name} ({effect.duration} turns remaining)")
            
        elif choice == "3":  # View Inventory
            print(f"\nCoins: {inventory.coins}")
            print(f"Keys: {inventory.keys}")
            print(f"Bombs: {inventory.bombs}")
            
            print("\nPotions:")
            for potion_type, sizes in inventory.potions.items():
                for size, count in sizes.items():
                    if count > 0:
                        print(f"{potion_type.title()} Potion ({size}): {count}")
            
            print("\nEquipment:")
            for slot, item in inventory.equipment.items():
                print(f"{slot.title()}: {item if item else 'Empty'}")
            
        elif choice == "4":  # View Quests
            if active_quests:
                print("\nActive Quests:")
                for quest in active_quests:
                    print(f"\n{quest.name}")
                    print(f"Description: {quest.description}")
                    print(f"Progress: {quest.progress}/{quest.target_amount}")
                    print(f"Reward: {quest.reward}")
            else:
                print("\nNo active quests!")
            
        elif choice == "5":  # Save Game
            save_game()
            
        elif choice == "6":  # Quit Game
            if input("\nWould you like to save before quitting? (y/n): ").lower() == 'y':
                save_game()
            print("\nThanks for playing!")
            game = False
            
        else:
            print("\nInvalid choice!")

if __name__ == "__main__":
    main()
