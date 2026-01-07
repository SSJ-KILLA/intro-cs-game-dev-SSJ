# So to begin with, we gotta import the characters and (in my words) traits into this file from another file.

from characters import create_enemy, create_player, is_alive

# Now thats done, we go ahead and create the attacks for the characters.

def player_attack(player, enemy):
    enemy["hp"] -= player["attack"]
    print(f"You attacked the {enemy['name']} for {player['attack']} damage!")

def enemy_attack(enemy, player):
    player["hp"] -= enemy["attack"]
    print(f"The {enemy['name']} attacks you for {enemy['attack']} damage!")

# And so now, we go on to the main dish, the battle!. Going to make the battle 

def battle(player, enemy): 
    print("A DEEPWOKEN PATHFINDER APPROACHES")  # Decided to just take a phrase from deepwoken
    print()


    while is_alive(player) and is_alive(enemy):
        print(f"Your HP: {player['hp']}")
        print(f"{enemy['name']} HP: {enemy['hp']}")
        print()

        input("Press Enter to attack...") # Here there isnt a real answer you should give so just pressing enter allows you to continue to fight since its an input module.

        player_attack(player, enemy)

        if is_alive(enemy):
            enemy_attack(enemy, player)


        print("-" * 30)

    if is_alive(player):
        print("You Win!")

    else:
        print("You died...") #from player attack to here, states player attacked enemy whilst  enemy attacked player. Hero's win cause I rigged it.

def main():
    player = create_player()
    enemy = create_enemy()
    battle(player, enemy)

# Now here is the juice. All that code condensed into 4 lines.
main()

# And its all called down here, to begin the fight.