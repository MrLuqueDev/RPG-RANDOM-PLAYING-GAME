def Chest(Debug, contentid):
    global content, coins, bombs, keys, structure_name
    randmath = 0
    if Debug == False and contentid == None:
        if keys >= 1 and not structure_name == "Village":
            keys -= 1
            content = random.randint(1,33)
            if content == 1 or 2 or 3:
                item_list_pot_t1[0] += 1
                print("You've gained a tier 1 HP potion")
            elif content == 4 or 5 or 6:
                item_list_pot_t1[1] += 1
                print("You've gained a tier 1 RESISTANCE potion")
            elif content == 7 or 8 or 9:
                item_list_pot_t1[2] += 1
                print("You've gained a tier 1 ATTACK potion")
            elif content == 10 or 11 or 12:
                item_list_pot_t1[3] += 1
                print("You've gained a tier 1 SPEED potion")
            elif content == 13 or 14 or 15:
                item_list_pot_t1[4] += 1
                print("You've gained a tier 1 LUCK potion")
            elif content == 16 or 17:
                item_list_pot_t2[0] += 1
                print("You've gained a tier 2 HP potion")
            elif content == 18 or 19:
                item_list_pot_t2[1] += 1
                print("You've gained a tier 2 RESISTANCE potion")
            elif content == 20 or 21:
                item_list_pot_t2[2] += 1
                print("You've gained a tier 2 ATTACK potion")
            elif content == 22 or 23:
                item_list_pot_t2[3] += 1
                print("You've gained a tier 2 SPEED potion")
            elif content == 24 or 25:
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
                randmath = random.randint(5,12)
                coins += randmath
                print("You found", randmath, "Coins! Total coins: ", coins)
            elif content == 32:
                keys += 2
                print("You got 2 keys!, now you have: ", keys, "keys")
            elif content == 33:
                bombs += 1
                print("You got a bomb!, now you have: ", bombs, "bombs")
        elif structure_name == "Village":
            randmath = random.randint(1,5)
            if randmath == 1:
                coins += 1
                print("you just got a coin, now you have: ", coins, "coins!")
            elif randmath == 2:
                coins += 3
                print("you just got 3 coins!, now you have: ", coins, "coins!")
            elif randmath == 3:
                coins += 5
                print("you just got 5 coins!!, now you have: ", coins, "coins!")
            elif randmath == 4:
                coins += 7
                print("you just got 7 coins!!!, now you have: ", coins, "coins!")
            elif randmath == 5:
                keys += 1
                print("You got a key!, now you have: ", keys, "keys")
            elif keys == 0:
                print("You can't open this chest because you don't have a key to open it")
    else:
        content = contentid
        if content == 1 or 2 or 3:
            item_list_pot_t1[0] += 1
            print("You've gained a tier 1 HP potion")
        elif content == 4 or 5 or 6:
            item_list_pot_t1[1] += 1
            print("You've gained a tier 1 RESISTANCE potion")
        elif content == 7 or 8 or 9:
            item_list_pot_t1[2] += 1
            print("You've gained a tier 1 ATTACK potion")
        elif content == 10 or 11 or 12:
            item_list_pot_t1[3] += 1
            print("You've gained a tier 1 SPEED potion")
        elif content == 13 or 14 or 15:
            item_list_pot_t1[4] += 1
            print("You've gained a tier 1 LUCK potion")
        elif content == 16 or 17:
            item_list_pot_t2[0] += 1
            print("You've gained a tier 2 HP potion")
        elif content == 18 or 19:
            item_list_pot_t2[1] += 1
            print("You've gained a tier 2 RESISTANCE potion")
        elif content == 20 or 21:
            item_list_pot_t2[2] += 1
            print("You've gained a tier 2 ATTACK potion")
        elif content == 22 or 23:
            item_list_pot_t2[3] += 1
            print("You've gained a tier 2 SPEED potion")
        elif content == 24 or 25:
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
            randmath = random.randint(5,12)
            coins += randmath
            print("You found", randmath, "Coins! Total coins: ", coins)
        elif content == 32:
            keys += 2
            print("You got 2 keys!, now you have: ", keys, "keys")
        elif content == 33:
            bombs += 1
            print("You got a bomb!, now you have: ", bombs, "bombs")
        elif content == None:
            print("This chest has no content...")