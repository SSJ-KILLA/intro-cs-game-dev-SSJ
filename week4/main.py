from player import Player
from enemy import Enemy

# Now we're finalizing the player

player = Player("Hero", 30, 6)

# Finalizing enemies as well

Omen = Enemy("The Omen", 20, 5)
Aberration = Enemy("Aberration", 40, 3)

enemies = [Omen, Aberration]

print("Fight for your life...\n")
# Onto the actual fight, we're gonna let the player attack first cause they're lowkey fried
for enemy in enemies:
    print(f"A wild {enemy.name} appears!")

    while enemy.is_alive() and player.is_alive():
        player.attack_enemy(enemy)
        print(f"{player.name} attacks {enemy.name} HP: {enemy.hp}")

        if enemy.is_alive():
            enemy.attack_player(player)
            print(f"{enemy.name} attacks {player.name}! {player.name} HP: {player.hp}")

        print()

    if not player.is_alive():
        print("You have been defeated. Game Over.")
        break
    else:
        print(f"{enemy.name} defeated!\n")

if player.is_alive():
    print("You defeated all enemies! You win!")