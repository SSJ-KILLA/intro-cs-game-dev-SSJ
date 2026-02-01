from entities import create_player, ENEMIES
from utils import get_int_input, combat, random_event

def main():
    print("=== Dungeon Sprint ===")
    name = input("Enter your name: ")
    player = create_player(name)

    rooms = [
        "Entrance Hall",
        "Spike Trap Room",
        "Goblin Den",
        "Treasure Room",
        "Dark Corridor",
        "Final Exit"
    ]

    room_index = 0

    while True:
        if player["hp"] <= 0:
            print("You have fallen in the dungeon. Game Over.")
            break

        if room_index >= len(rooms):
            print("You escaped the dungeon alive! YOU WIN!")
            break

        print(f"\n--- {rooms[room_index]} ---")
        print(f"HP: {player['hp']}/{player['max_hp']} | Gold: {player['gold']}")

        # ROOM LOGIC
        if room_index == 0:
            print("A cold stone hall lies before you.")
            print("1) Move forward\n2) Quit")
            choice = get_int_input(1, 2)
            if choice == 2:
                print("You quit the dungeon.")
                break

        elif room_index == 1:
            print("You notice suspicious holes in the walls.")
            print("1) Run through\n2) Move carefully")
            choice = get_int_input(1, 2)
            if choice == 1:
                dmg = random_event(5, 15)
                player["hp"] -= dmg
                print(f"You are hit by spikes! Lost {dmg} HP.")
            else:
                print("You pass safely.")

        elif room_index == 2:
            print("A Goblin attacks!")
            combat(player, ENEMIES["goblin"])

        elif room_index == 3:
            print("A chest sits in the center.")
            print("1) Open it\n2) Ignore it")
            choice = get_int_input(1, 2)
            if choice == 1:
                gold = random_event(10, 30)
                player["gold"] += gold
                player["inventory"].append("Potion")
                print(f"You gained {gold} gold and a Potion!")

        elif room_index == 4:
            print("A Skeleton blocks your path!")
            combat(player, ENEMIES["skeleton"])

        elif room_index == 5:
            print("The exit is guarded by an Orc!")
            combat(player, ENEMIES["orc"])

        room_index += 1

if __name__ == "__main__":
    main()
