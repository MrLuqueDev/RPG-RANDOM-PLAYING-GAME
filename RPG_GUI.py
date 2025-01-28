import tkinter as tk
from tkinter import ttk, messagebox
import json
import random
import os
from RPG_remake import Stats, Inventory, StatusEffect, Enemy, calculate_damage, try_flee

VERSION = "1.0"


class RPGGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(f"RPG Game v{VERSION}")
        self.root.geometry("1024x768")

        # Configure style
        self.style = ttk.Style()
        self.style.configure("Title.TLabel", font=("Arial", 24, "bold"))
        self.style.configure("Subtitle.TLabel", font=("Arial", 16))
        self.style.configure("Stats.TLabel", font=("Arial", 12))
        self.style.configure("Battle.TLabel", font=("Arial", 14, "bold"))
        self.style.configure("Action.TButton", font=("Arial", 12))

        # Game variables
        self.player_stats = Stats()
        self.inventory = Inventory()
        self.active_effects = []
        self.active_quests = []
        self.game = True
        self.name = ""
        self.player_class = ""

        # Stats labels for updating
        self.stat_labels = {}
        self.inventory_labels = {}

        # Create main container
        self.main_container = ttk.Frame(self.root, padding="10")
        self.main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(1, weight=3)

        # Create and show the main menu
        self.show_main_menu()

    def show_main_menu(self):
        # Clear main container
        for widget in self.main_container.winfo_children():
            widget.destroy()

        # Background frame
        menu_frame = ttk.Frame(self.main_container, padding="20")
        menu_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
        menu_frame.grid_columnconfigure(0, weight=1)

        # Title
        title = ttk.Label(menu_frame, text="RPG Game", style="Title.TLabel")
        title.grid(row=0, column=0, pady=20)

        version_label = ttk.Label(
            menu_frame, text=f"Version {VERSION}", style="Subtitle.TLabel"
        )
        version_label.grid(row=1, column=0, pady=5)

        # Buttons frame
        button_frame = ttk.Frame(menu_frame, padding="10")
        button_frame.grid(row=2, column=0, pady=20)

        # Buttons with improved style
        new_game_btn = ttk.Button(
            button_frame,
            text="New Game",
            style="Action.TButton",
            command=self.start_new_game,
            width=20,
        )
        new_game_btn.grid(row=0, column=0, pady=10)

        load_game_btn = ttk.Button(
            button_frame,
            text="Load Game",
            style="Action.TButton",
            command=self.load_game,
            width=20,
        )
        load_game_btn.grid(row=1, column=0, pady=10)

        quit_btn = ttk.Button(
            button_frame,
            text="Quit",
            style="Action.TButton",
            command=self.root.quit,
            width=20,
        )
        quit_btn.grid(row=2, column=0, pady=10)

    def start_new_game(self):
        # Clear main container
        for widget in self.main_container.winfo_children():
            widget.destroy()

        # Character creation frame
        char_frame = ttk.LabelFrame(
            self.main_container, text="Character Creation", padding="10"
        )
        char_frame.grid(
            row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S)
        )

        # Name entry
        ttk.Label(char_frame, text="Character Name:").grid(row=0, column=0, pady=5)
        name_entry = ttk.Entry(char_frame)
        name_entry.grid(row=0, column=1, pady=5)

        # Class selection
        ttk.Label(char_frame, text="Class:").grid(row=1, column=0, pady=5)
        class_var = tk.StringVar()
        class_combo = ttk.Combobox(char_frame, textvariable=class_var)
        class_combo["values"] = ("Warrior", "Archer", "Wizard")
        class_combo.grid(row=1, column=1, pady=5)
        class_combo.set("Warrior")

        # Create character button
        def create_character():
            self.name = name_entry.get()
            self.player_class = class_var.get()
            if self.name and self.player_class:
                self.initialize_character()
                self.show_game_screen()
            else:
                messagebox.showerror("Error", "Please fill in all fields!")

        create_btn = ttk.Button(
            char_frame, text="Create Character", command=create_character
        )
        create_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def initialize_character(self):
        # Set base stats based on class
        if self.player_class == "Warrior":
            self.player_stats.MAX_HP = 130
            self.player_stats.HP = 130
            self.player_stats.MAX_MP = 20
            self.player_stats.MP = 20
            self.player_stats.ATK = 12
            self.player_stats.DEF = 10
            self.player_stats.SPD = 5
        elif self.player_class == "Archer":
            self.player_stats.MAX_HP = 90
            self.player_stats.HP = 90
            self.player_stats.MAX_MP = 20
            self.player_stats.MP = 20
            self.player_stats.ATK = 10
            self.player_stats.DEF = 7
            self.player_stats.SPD = 12
        elif self.player_class == "Wizard":
            self.player_stats.MAX_HP = 100
            self.player_stats.HP = 100
            self.player_stats.MAX_MP = 100
            self.player_stats.MP = 100
            self.player_stats.ATK = 8
            self.player_stats.DEF = 6
            self.player_stats.SPD = 8

    def show_game_screen(self):
        # Clear main container
        for widget in self.main_container.winfo_children():
            widget.destroy()

        # Create game layout with three columns
        # Left panel - Character info (1/4 width)
        left_panel = ttk.Frame(self.main_container, padding="10")
        left_panel.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Character info
        char_info = ttk.LabelFrame(left_panel, text="Character Info", padding="10")
        char_info.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Store labels for updating
        self.stat_labels["name"] = ttk.Label(
            char_info, text=f"Name: {self.name}", style="Stats.TLabel"
        )
        self.stat_labels["name"].grid(row=0, column=0, sticky=tk.W, pady=2)

        self.stat_labels["class"] = ttk.Label(
            char_info, text=f"Class: {self.player_class}", style="Stats.TLabel"
        )
        self.stat_labels["class"].grid(row=1, column=0, sticky=tk.W, pady=2)

        self.stat_labels["level"] = ttk.Label(
            char_info, text=f"Level: {self.player_stats.level}", style="Stats.TLabel"
        )
        self.stat_labels["level"].grid(row=2, column=0, sticky=tk.W, pady=2)

        self.stat_labels["xp"] = ttk.Label(
            char_info,
            text=f"XP: {self.player_stats.XP}/{self.player_stats.XP_req}",
            style="Stats.TLabel",
        )
        self.stat_labels["xp"].grid(row=3, column=0, sticky=tk.W, pady=2)

        # Stats
        stats_frame = ttk.LabelFrame(left_panel, text="Stats", padding="10")
        stats_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        self.stat_labels["hp"] = ttk.Label(
            stats_frame,
            text=f"HP: {self.player_stats.HP}/{self.player_stats.MAX_HP}",
            style="Stats.TLabel",
        )
        self.stat_labels["hp"].grid(row=0, column=0, sticky=tk.W, pady=2)

        self.stat_labels["mp"] = ttk.Label(
            stats_frame,
            text=f"MP: {self.player_stats.MP}/{self.player_stats.MAX_MP}",
            style="Stats.TLabel",
        )
        self.stat_labels["mp"].grid(row=1, column=0, sticky=tk.W, pady=2)

        self.stat_labels["atk"] = ttk.Label(
            stats_frame, text=f"ATK: {self.player_stats.ATK}", style="Stats.TLabel"
        )
        self.stat_labels["atk"].grid(row=2, column=0, sticky=tk.W, pady=2)

        self.stat_labels["def"] = ttk.Label(
            stats_frame, text=f"DEF: {self.player_stats.DEF}", style="Stats.TLabel"
        )
        self.stat_labels["def"].grid(row=3, column=0, sticky=tk.W, pady=2)

        self.stat_labels["spd"] = ttk.Label(
            stats_frame, text=f"SPD: {self.player_stats.SPD}", style="Stats.TLabel"
        )
        self.stat_labels["spd"].grid(row=4, column=0, sticky=tk.W, pady=2)

        # Center panel - Main game area (2/4 width)
        center_panel = ttk.Frame(self.main_container, padding="10")
        center_panel.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        center_panel.grid_columnconfigure(0, weight=1)
        center_panel.grid_rowconfigure(0, weight=1)

        # Game log with scrollbar
        log_frame = ttk.LabelFrame(center_panel, text="Game Log", padding="5")
        log_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        log_frame.grid_columnconfigure(0, weight=1)
        log_frame.grid_rowconfigure(0, weight=1)

        self.game_log = tk.Text(log_frame, height=20, width=50, wrap=tk.WORD)
        self.game_log.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        scrollbar = ttk.Scrollbar(
            log_frame, orient=tk.VERTICAL, command=self.game_log.yview
        )
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.game_log["yscrollcommand"] = scrollbar.set

        self.game_log.insert(tk.END, "Welcome to the game!\n")
        self.game_log.config(state=tk.DISABLED)

        # Action buttons
        action_frame = ttk.LabelFrame(center_panel, text="Actions", padding="10")
        action_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.S), pady=5)

        ttk.Button(
            action_frame, text="Explore", style="Action.TButton", command=self.explore
        ).grid(row=0, column=0, padx=5)
        ttk.Button(
            action_frame,
            text="Inventory",
            style="Action.TButton",
            command=self.show_inventory,
        ).grid(row=0, column=1, padx=5)
        ttk.Button(
            action_frame, text="Save", style="Action.TButton", command=self.save_game
        ).grid(row=0, column=2, padx=5)
        ttk.Button(
            action_frame,
            text="Menu",
            style="Action.TButton",
            command=self.show_main_menu,
        ).grid(row=0, column=3, padx=5)

        # Right panel - Inventory (1/4 width)
        right_panel = ttk.Frame(self.main_container, padding="10")
        right_panel.grid(row=0, column=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        inventory_frame = ttk.LabelFrame(
            right_panel, text="Quick Inventory", padding="10"
        )
        inventory_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.inventory_labels["coins"] = ttk.Label(
            inventory_frame, text=f"Coins: {self.inventory.coins}", style="Stats.TLabel"
        )
        self.inventory_labels["coins"].grid(row=0, column=0, sticky=tk.W, pady=2)

        self.inventory_labels["keys"] = ttk.Label(
            inventory_frame, text=f"Keys: {self.inventory.keys}", style="Stats.TLabel"
        )
        self.inventory_labels["keys"].grid(row=1, column=0, sticky=tk.W, pady=2)

        self.inventory_labels["bombs"] = ttk.Label(
            inventory_frame, text=f"Bombs: {self.inventory.bombs}", style="Stats.TLabel"
        )
        self.inventory_labels["bombs"].grid(row=2, column=0, sticky=tk.W, pady=2)

        # Add potions summary
        potions_frame = ttk.LabelFrame(right_panel, text="Potions", padding="10")
        potions_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        row = 0
        for potion_type, sizes in self.inventory.potions.items():
            for size, count in sizes.items():
                label_key = f"{potion_type}_{size}"
                self.inventory_labels[label_key] = ttk.Label(
                    potions_frame,
                    text=f"{size.title()} {potion_type.title()}: {count}",
                    style="Stats.TLabel",
                )
                self.inventory_labels[label_key].grid(
                    row=row, column=0, sticky=tk.W, pady=2
                )
                row += 1

    def update_stats_display(self):
        """Update all stat and inventory labels"""
        # Update character info
        self.stat_labels["name"].config(text=f"Name: {self.name}")
        self.stat_labels["class"].config(text=f"Class: {self.player_class}")
        self.stat_labels["level"].config(text=f"Level: {self.player_stats.level}")
        self.stat_labels["xp"].config(
            text=f"XP: {self.player_stats.XP}/{self.player_stats.XP_req}"
        )

        # Update stats
        self.stat_labels["hp"].config(
            text=f"HP: {self.player_stats.HP}/{self.player_stats.MAX_HP}"
        )
        self.stat_labels["mp"].config(
            text=f"MP: {self.player_stats.MP}/{self.player_stats.MAX_MP}"
        )
        self.stat_labels["atk"].config(text=f"ATK: {self.player_stats.ATK}")
        self.stat_labels["def"].config(text=f"DEF: {self.player_stats.DEF}")
        self.stat_labels["spd"].config(text=f"SPD: {self.player_stats.SPD}")

        # Update inventory
        self.inventory_labels["coins"].config(text=f"Coins: {self.inventory.coins}")
        self.inventory_labels["keys"].config(text=f"Keys: {self.inventory.keys}")
        self.inventory_labels["bombs"].config(text=f"Bombs: {self.inventory.bombs}")

        # Update potions
        for potion_type, sizes in self.inventory.potions.items():
            for size, count in sizes.items():
                label_key = f"{potion_type}_{size}"
                if label_key in self.inventory_labels:
                    self.inventory_labels[label_key].config(
                        text=f"{size.title()} {potion_type.title()}: {count}"
                    )

    def log_message(self, message):
        """Add message to game log"""
        self.game_log.config(state=tk.NORMAL)
        self.game_log.insert(tk.END, message + "\n")
        self.game_log.see(tk.END)
        self.game_log.config(state=tk.DISABLED)

        # Update stats display after any action
        self.update_stats_display()

    def explore(self):
        # Random encounter chance
        if random.random() < 0.7:  # 70% chance for encounter
            encounter_type = random.random()
            
            if encounter_type < 0.5:  # 50% chance for enemy (reduced from 60%)
                self.start_battle()
            elif encounter_type < 0.7:  # 20% chance for chest
                self.find_chest()
            elif encounter_type < 0.85:  # 15% chance for shop (new)
                self.show_shop()
            else:  # 15% chance for special event
                self.special_event()
        else:
            self.log_message("You found nothing interesting...")

    def start_battle(self):
        enemy_level = max(1, self.player_stats.level + random.randint(-2, 2))
        enemy = Enemy("Goblin", enemy_level)

        self.log_message(f"A level {enemy_level} {enemy.name} appears!")

        # Create battle window with improved style
        battle_window = tk.Toplevel(self.root)
        battle_window.title("Battle!")
        battle_window.geometry("500x400")
        battle_window.protocol("WM_DELETE_WINDOW", lambda: None)  # Disable X button
        battle_window.transient(self.root)  # Make it modal
        battle_window.grab_set()  # Make it modal

        # Battle info
        info_frame = ttk.LabelFrame(battle_window, text="Battle Status", padding="10")
        info_frame.grid(
            row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=5
        )

        enemy_label = ttk.Label(
            info_frame,
            text=f"{enemy.name} HP: {enemy.stats.HP}/{enemy.stats.MAX_HP}",
            style="Battle.TLabel",
        )
        enemy_label.grid(row=0, column=0, pady=5)

        player_label = ttk.Label(
            info_frame,
            text=f"Your HP: {self.player_stats.HP}/{self.player_stats.MAX_HP}",
            style="Battle.TLabel",
        )
        player_label.grid(row=1, column=0, pady=5)

        # Battle log
        battle_log = tk.Text(battle_window, height=10, width=50)
        battle_log.grid(row=1, column=0, padx=10, pady=5)

        # Battle actions
        action_frame = ttk.LabelFrame(battle_window, text="Actions", padding="10")
        action_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.S), padx=10, pady=5)

        def attack():
            damage = calculate_damage(self.player_stats, enemy.stats)
            enemy.stats.HP -= damage
            battle_log.insert(tk.END, f"You deal {damage} damage to {enemy.name}!\n")
            battle_log.see(tk.END)

            if enemy.stats.HP <= 0:
                battle_log.insert(tk.END, f"You defeated {enemy.name}!\n")
                battle_window.after(1000, battle_window.destroy)
                self.give_rewards(enemy)
            else:
                # Enemy turn
                enemy_damage = calculate_damage(enemy.stats, self.player_stats)
                self.player_stats.HP -= enemy_damage
                battle_log.insert(
                    tk.END, f"{enemy.name} deals {enemy_damage} damage to you!\n"
                )

                if self.player_stats.HP <= 0:
                    battle_log.insert(tk.END, "You have been defeated!\n")
                    battle_window.after(1000, battle_window.destroy)
                    self.game_over()

                # Update labels
                enemy_label.config(
                    text=f"{enemy.name} HP: {enemy.stats.HP}/{enemy.stats.MAX_HP}"
                )
                player_label.config(
                    text=f"Your HP: {self.player_stats.HP}/{self.player_stats.MAX_HP}"
                )

            # Update main screen stats
            self.update_stats_display()

        ttk.Button(
            action_frame, text="Attack", style="Action.TButton", command=attack
        ).grid(row=0, column=0, padx=5)
        ttk.Button(
            action_frame,
            text="Use Item",
            style="Action.TButton",
            command=self.show_inventory,
        ).grid(row=0, column=1, padx=5)
        ttk.Button(
            action_frame,
            text="Flee",
            style="Action.TButton",
            command=lambda: self.try_flee(enemy, battle_window),
        ).grid(row=0, column=2, padx=5)

    def find_chest(self):
        if (
            self.inventory.keys > 0 or random.random() < 0.3
        ):  # 30% chance for unlocked chest
            self.log_message("You found a chest!")

            # Random loot
            loot_type = random.random()
            if loot_type < 0.4:  # 40% chance for coins
                coins = random.randint(5, 15)
                self.inventory.coins += coins
                self.log_message(f"You found {coins} coins!")
            elif loot_type < 0.7:  # 30% chance for potion
                potion_type = random.choice(["health", "mana"])
                size = random.choice(["small", "medium", "large"])
                self.inventory.potions[potion_type][size] += 1
                self.log_message(f"You found a {size} {potion_type} potion!")
            else:  # 30% chance for key
                self.inventory.keys += 1
                self.log_message("You found a key!")
        else:
            self.log_message("You found a locked chest but don't have any keys!")

    def special_event(self):
        events = [
            "You find a mysterious shrine",
            "You discover an ancient inscription",
            "You meet a traveling merchant",
            "You find a training dummy",
            "You discover a healing spring",
        ]
        event = random.choice(events)
        self.log_message(event)

        if "healing spring" in event.lower():
            heal_amount = self.player_stats.MAX_HP // 4
            self.player_stats.HP = min(
                self.player_stats.MAX_HP, self.player_stats.HP + heal_amount
            )
            self.log_message(f"You feel refreshed! Recovered {heal_amount} HP!")

    def show_inventory(self):
        inventory_window = tk.Toplevel(self.root)
        inventory_window.title("Inventory")
        inventory_window.geometry("300x400")

        # Potions
        potions_frame = ttk.LabelFrame(inventory_window, text="Potions", padding="5")
        potions_frame.grid(
            row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5
        )

        row = 0
        for potion_type, sizes in self.inventory.potions.items():
            for size, count in sizes.items():
                if count > 0:
                    ttk.Label(
                        potions_frame,
                        text=f"{size.title()} {potion_type.title()}: {count}",
                    ).grid(row=row, column=0, sticky=tk.W)
                    use_btn = ttk.Button(
                        potions_frame,
                        text="Use",
                        command=lambda t=potion_type, s=size: self.use_potion(t, s),
                    )
                    use_btn.grid(row=row, column=1)
                    row += 1

        # Other items
        items_frame = ttk.LabelFrame(inventory_window, text="Items", padding="5")
        items_frame.grid(
            row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5
        )

        ttk.Label(items_frame, text=f"Coins: {self.inventory.coins}").grid(
            row=0, column=0, sticky=tk.W
        )
        ttk.Label(items_frame, text=f"Keys: {self.inventory.keys}").grid(
            row=1, column=0, sticky=tk.W
        )
        ttk.Label(items_frame, text=f"Bombs: {self.inventory.bombs}").grid(
            row=2, column=0, sticky=tk.W
        )

    def use_potion(self, potion_type, size):
        if self.inventory.potions[potion_type][size] > 0:
            self.inventory.potions[potion_type][size] -= 1

            if potion_type == "health":
                heal_amount = {
                    "small": int(self.player_stats.MAX_HP * 0.3),  # 30% of max HP
                    "medium": int(self.player_stats.MAX_HP * 0.6),  # 60% of max HP
                    "large": self.player_stats.MAX_HP  # 100% of max HP
                }[size]
                self.player_stats.HP = min(
                    self.player_stats.MAX_HP, self.player_stats.HP + heal_amount
                )
                self.log_message(f"Restored {heal_amount} HP!")
            elif potion_type == "mana":
                mana_amount = {
                    "small": int(self.player_stats.MAX_MP * 0.3),  # 30% of max MP
                    "medium": int(self.player_stats.MAX_MP * 0.6),  # 60% of max MP
                    "large": self.player_stats.MAX_MP  # 100% of max MP
                }[size]
                self.player_stats.MP = min(
                    self.player_stats.MAX_MP, self.player_stats.MP + mana_amount
                )
                self.log_message(f"Restored {mana_amount} MP!")

    def try_flee(self, enemy, battle_window):
        if try_flee(self.player_stats.SPD, enemy.stats.SPD):
            self.log_message("You successfully fled from battle!")
            battle_window.destroy()
        else:
            # Take damage when failing to flee
            flee_damage = calculate_damage(enemy.stats, self.player_stats) * 1.5  # 50% more damage
            self.player_stats.HP -= int(flee_damage)
            self.log_message(f"Couldn't escape! {enemy.name} catches you and deals {int(flee_damage)} damage!")
            
            if self.player_stats.HP <= 0:
                self.log_message("You have been defeated while trying to flee!")
                battle_window.after(1000, battle_window.destroy)
                self.game_over()
            
            self.update_stats_display()

    def show_shop(self):
        self.log_message("You found a traveling merchant!")
        
        # Create shop window
        shop_window = tk.Toplevel(self.root)
        shop_window.title("Shop")
        shop_window.geometry("600x700")
        shop_window.transient(self.root)  # Make it modal
        
        # Main notebook for tabs
        notebook = ttk.Notebook(shop_window)
        notebook.pack(expand=True, fill='both', padx=10, pady=5)
        
        # Buy tab
        buy_frame = ttk.Frame(notebook, padding="10")
        notebook.add(buy_frame, text="Buy")
        
        # Sell tab
        sell_frame = ttk.Frame(notebook, padding="10")
        notebook.add(sell_frame, text="Sell")
        
        # Configure grid weights for frames
        buy_frame.grid_columnconfigure(0, weight=1)
        sell_frame.grid_columnconfigure(0, weight=1)
        
        # Show current coins in both tabs
        coins_label_buy = ttk.Label(buy_frame, text=f"Your Coins: {self.inventory.coins}", style="Stats.TLabel")
        coins_label_buy.grid(row=0, column=0, columnspan=3, pady=10)
        
        coins_label_sell = ttk.Label(sell_frame, text=f"Your Coins: {self.inventory.coins}", style="Stats.TLabel")
        coins_label_sell.grid(row=0, column=0, columnspan=3, pady=10)
        
        # All possible shop items with descriptions
        all_shop_items = {
            "Small Health Potion": {
                "price": 10,
                "type": "health",
                "size": "small",
                "desc": f"Restores 30% of max HP (Currently: {int(self.player_stats.MAX_HP * 0.3)} HP)"
            },
            "Medium Health Potion": {
                "price": 25,
                "type": "health",
                "size": "medium",
                "desc": f"Restores 60% of max HP (Currently: {int(self.player_stats.MAX_HP * 0.6)} HP)"
            },
            "Large Health Potion": {
                "price": 50,
                "type": "health",
                "size": "large",
                "desc": f"Restores 100% of max HP (Currently: {self.player_stats.MAX_HP} HP)"
            },
            "Small Mana Potion": {
                "price": 8,
                "type": "mana",
                "size": "small",
                "desc": f"Restores 30% of max MP (Currently: {int(self.player_stats.MAX_MP * 0.3)} MP)"
            },
            "Medium Mana Potion": {
                "price": 20,
                "type": "mana",
                "size": "medium",
                "desc": f"Restores 60% of max MP (Currently: {int(self.player_stats.MAX_MP * 0.6)} MP)"
            },
            "Large Mana Potion": {
                "price": 40,
                "type": "mana",
                "size": "large",
                "desc": f"Restores 100% of max MP (Currently: {self.player_stats.MAX_MP} MP)"
            },
            "Key": {
                "price": 15,
                "type": "key",
                "size": None,
                "desc": "Opens locked chests"
            },
            "Bomb": {
                "price": 30,
                "type": "bomb",
                "size": None,
                "desc": "Can be used to deal massive damage in battle"
            }
        }
        
        # Select 3 random items for sale
        shop_items = dict(random.sample(list(all_shop_items.items()), 3))
        
        def buy_item(item_name, item_data):
            if self.inventory.coins >= item_data["price"]:
                self.inventory.coins -= item_data["price"]
                
                if item_data["type"] in ["health", "mana"]:
                    self.inventory.potions[item_data["type"]][item_data["size"]] += 1
                    self.log_message(f"Bought {item_name} for {item_data['price']} coins!")
                elif item_data["type"] == "key":
                    self.inventory.keys += 1
                    self.log_message(f"Bought a key for {item_data['price']} coins!")
                elif item_data["type"] == "bomb":
                    self.inventory.bombs += 1
                    self.log_message(f"Bought a bomb for {item_data['price']} coins!")
                
                coins_label_buy.config(text=f"Your Coins: {self.inventory.coins}")
                coins_label_sell.config(text=f"Your Coins: {self.inventory.coins}")
                self.update_stats_display()
                update_sell_items()
            else:
                messagebox.showerror("Error", "Not enough coins!")
        
        def sell_item(item_name, item_data):
            sell_price = item_data["price"] // 2
            
            if item_data["type"] in ["health", "mana"]:
                if self.inventory.potions[item_data["type"]][item_data["size"]] > 0:
                    self.inventory.potions[item_data["type"]][item_data["size"]] -= 1
                    self.inventory.coins += sell_price
                    self.log_message(f"Sold {item_name} for {sell_price} coins!")
            elif item_data["type"] == "key" and self.inventory.keys > 0:
                self.inventory.keys -= 1
                self.inventory.coins += sell_price
                self.log_message(f"Sold a key for {sell_price} coins!")
            elif item_data["type"] == "bomb" and self.inventory.bombs > 0:
                self.inventory.bombs -= 1
                self.inventory.coins += sell_price
                self.log_message(f"Sold a bomb for {sell_price} coins!")
            else:
                messagebox.showerror("Error", "You don't have this item!")
                return
            
            coins_label_buy.config(text=f"Your Coins: {self.inventory.coins}")
            coins_label_sell.config(text=f"Your Coins: {self.inventory.coins}")
            self.update_stats_display()
            update_sell_items()
        
        # Add items to buy tab
        buy_items_frame = ttk.Frame(buy_frame)
        buy_items_frame.grid(row=1, column=0, sticky="nsew")
        
        for i, (item_name, item_data) in enumerate(shop_items.items(), 1):
            # Item name and price
            ttk.Label(buy_items_frame, text=item_name, style="Stats.TLabel").grid(row=i*2-1, column=0, pady=5, padx=5, sticky=tk.W)
            ttk.Label(buy_items_frame, text=f"{item_data['price']} coins", style="Stats.TLabel").grid(row=i*2-1, column=1, pady=5, padx=5)
            ttk.Button(
                buy_items_frame,
                text="Buy",
                style="Action.TButton",
                command=lambda n=item_name, d=item_data: buy_item(n, d)
            ).grid(row=i*2-1, column=2, pady=5, padx=5)
            
            # Description on next row
            ttk.Label(buy_items_frame, text=item_data['desc'], wraplength=400).grid(row=i*2, column=0, columnspan=3, pady=(0,10), sticky=tk.W)
        
        def update_sell_items():
            # Clear sell frame except coins label
            for widget in sell_frame.winfo_children():
                if widget != coins_label_sell:
                    widget.destroy()
            
            # Create new frame for sell items
            sell_items_frame = ttk.Frame(sell_frame)
            sell_items_frame.grid(row=1, column=0, sticky="nsew")
            
            row = 0
            # Add potions that player has
            for potion_type, sizes in self.inventory.potions.items():
                for size, count in sizes.items():
                    if count > 0:
                        item_name = f"{size.title()} {potion_type.title()} Potion"
                        item_data = all_shop_items[item_name]
                        sell_price = item_data["price"] // 2
                        
                        ttk.Label(sell_items_frame, text=f"{item_name} (x{count})", style="Stats.TLabel").grid(row=row, column=0, pady=5, padx=5, sticky=tk.W)
                        ttk.Label(sell_items_frame, text=f"{sell_price} coins", style="Stats.TLabel").grid(row=row, column=1, pady=5, padx=5)
                        ttk.Button(
                            sell_items_frame,
                            text="Sell",
                            style="Action.TButton",
                            command=lambda n=item_name, d=item_data: sell_item(n, d)
                        ).grid(row=row, column=2, pady=5, padx=5)
                        row += 1
            
            # Add keys if player has any
            if self.inventory.keys > 0:
                sell_price = all_shop_items["Key"]["price"] // 2
                ttk.Label(sell_items_frame, text=f"Key (x{self.inventory.keys})", style="Stats.TLabel").grid(row=row, column=0, pady=5, padx=5, sticky=tk.W)
                ttk.Label(sell_items_frame, text=f"{sell_price} coins", style="Stats.TLabel").grid(row=row, column=1, pady=5, padx=5)
                ttk.Button(
                    sell_items_frame,
                    text="Sell",
                    style="Action.TButton",
                    command=lambda: sell_item("Key", all_shop_items["Key"])
                ).grid(row=row, column=2, pady=5, padx=5)
                row += 1
            
            # Add bombs if player has any
            if self.inventory.bombs > 0:
                sell_price = all_shop_items["Bomb"]["price"] // 2
                ttk.Label(sell_items_frame, text=f"Bomb (x{self.inventory.bombs})", style="Stats.TLabel").grid(row=row, column=0, pady=5, padx=5, sticky=tk.W)
                ttk.Label(sell_items_frame, text=f"{sell_price} coins", style="Stats.TLabel").grid(row=row, column=1, pady=5, padx=5)
                ttk.Button(
                    sell_items_frame,
                    text="Sell",
                    style="Action.TButton",
                    command=lambda: sell_item("Bomb", all_shop_items["Bomb"])
                ).grid(row=row, column=2, pady=5, padx=5)
        
        # Initialize sell tab
        update_sell_items()
        
        # Close button at the bottom
        close_frame = ttk.Frame(shop_window)
        close_frame.pack(side='bottom', pady=10)
        
        ttk.Button(
            close_frame,
            text="Close",
            style="Action.TButton",
            command=shop_window.destroy
        ).pack()

    def give_rewards(self, enemy):
        # Give XP
        xp_gained = 50 + (enemy.level * 10)
        self.player_stats.XP += xp_gained
        self.log_message(f"Gained {xp_gained} XP!")

        # Check for level up
        while self.player_stats.XP >= self.player_stats.XP_req:
            self.level_up()

        # Give coins
        coins_gained = random.randint(5, 15)
        self.inventory.coins += coins_gained
        self.log_message(f"Found {coins_gained} coins!")

    def level_up(self):
        self.player_stats.level += 1
        self.player_stats.XP -= self.player_stats.XP_req
        self.player_stats.XP_req = int(self.player_stats.XP_req * 1.5)

        # Increase stats
        self.player_stats.MAX_HP += 15 + random.randint(1, 6)
        self.player_stats.HP = self.player_stats.MAX_HP
        self.player_stats.ATK += 2 + random.randint(0, 2)
        self.player_stats.DEF += 1 + random.randint(0, 2)
        self.player_stats.SPD += 1 + random.randint(0, 1)

        self.log_message(f"Level Up! You are now level {self.player_stats.level}!")

    def save_game(self):
        save_data = {
            "name": self.name,
            "class": self.player_class,
            "stats": vars(self.player_stats),
            "inventory": vars(self.inventory),
        }

        with open(f"save_{self.name}.json", "w") as f:
            json.dump(save_data, f)

        self.log_message("Game saved successfully!")

    def load_game(self):
        try:
            save_files = [
                f for f in os.listdir() if f.startswith("save_") and f.endswith(".json")
            ]

            if not save_files:
                messagebox.showinfo("No Saves", "No save files found!")
                return

            # Create load game window
            load_window = tk.Toplevel(self.root)
            load_window.title("Load Game")
            load_window.geometry("300x400")

            # List of save files
            for i, save_file in enumerate(save_files):

                def load_save(file=save_file):
                    with open(file, "r") as f:
                        save_data = json.load(f)

                    self.name = save_data["name"]
                    self.player_class = save_data["class"]

                    # Load stats
                    for key, value in save_data["stats"].items():
                        setattr(self.player_stats, key, value)

                    # Load inventory
                    for key, value in save_data["inventory"].items():
                        setattr(self.inventory, key, value)

                    load_window.destroy()
                    self.show_game_screen()

                ttk.Button(load_window, text=save_file, command=load_save).grid(
                    row=i, column=0, pady=5
                )

        except Exception as e:
            messagebox.showerror("Error", f"Error loading save file: {str(e)}")

    def game_over(self):
        self.log_message("Game Over!")
        if messagebox.askyesno("Game Over", "Would you like to load a saved game?"):
            self.load_game()
        else:
            self.show_main_menu()


if __name__ == "__main__":
    root = tk.Tk()
    app = RPGGUI(root)
    root.mainloop()
