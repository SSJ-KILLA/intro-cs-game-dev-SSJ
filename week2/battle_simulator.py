import random

# This is the health of the fighters
hero_hp = 100
villain_hp = 100

# Possible damage values theyh can fight off
damages = [3, 4, 1, 4, 1, 5, 9, 2, 500]

# Time to code the battle code

while hero_hp > 0 and villain_hp > 0:
    print("Hero HP:", hero_hp)
    print("Villain HP:", villain_hp)

# Yeah heres the damages for the villain
    villain_damage = random.choice(damages)
    hero_hp -= villain_damage
    print(f"The villain attacks for {villain_damage}")

    # And we're onto hero damage

    hero_damage = random.choice(damages)
    villain_hp -= hero_damage
    print(f"You have attacked the villain for {hero_damage}")

# And now we're doing the winning and losing conditions

if hero_hp > 0:
    print("\nYou Win!")

else:
    print("You Lose!")