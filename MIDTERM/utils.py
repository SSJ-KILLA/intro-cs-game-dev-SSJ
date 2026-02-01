import random

def get_int_input(min_val, max_val):
    while True:
        try:
            choice = int(input("Choose: "))
            if min_val <= choice <= max_val:
                return choice
            else:
                print("Choice out of range.")
        except ValueError:
            print("Invalid input. Enter a number.")

def random_event(low, high):
    return random.randint(low, high)

def combat(player, enemy_template):
    enemy = enemy_template.copy()
    print(f"Combat started with {enemy['name']}!")

    while enemy["hp"] > 0 and player["hp"] > 0:
        print(f"\nYour HP: {player['hp']} | Enemy HP: {enemy['hp']}")
        print("1) Attack\n2) Heal\n3) Run")

        try:
            action = int(input("Action: "))
        except ValueError:
            print("Invalid input.")
            continue

        if action == 1:
            dmg = random.randint(10, 20)
            enemy["hp"] -= dmg
            print(f"You hit for {dmg} damage!")

        elif action == 2:
            if "Potion" in player["inventory"]:
                player["hp"] = min(player["max_hp"], player["hp"] + 20)
                player["inventory"].remove("Potion")
                print("You healed 20 HP.")
            else:
                print("No potions left!")

        elif action == 3:
            if random.randint(1, 2) == 1:
                print("You escaped!")
                return
            else:
                print("Failed to escape!")

        else:
            print("Invalid action.")
            continue

        if enemy["hp"] > 0:
            player["hp"] -= enemy["damage"]
            print(f"The enemy hits you for {enemy['damage']}!")

    if player["hp"] > 0:
        print(f"You defeated the {enemy['name']}!")
        player["gold"] += 10
