# Lets go ahead and just make a simple 2 characters; Hero and Enemy

def create_player():
    return {
        "name": "Hero",
        "hp": 100,
        "attack": 15
    }

def create_enemy():
    return {
        "name": "Amalgam",
        "hp": 30,
        "attack": 25
    }

# Here we will make a function for being alive

def is_alive(character):
    return character ["hp"] > 0

### and now we've created the characters file and we shall head to the main.py