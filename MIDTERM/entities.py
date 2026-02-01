def create_player(name):
    return {
        "name": name,
        "hp": 100,
        "max_hp": 100,
        "gold": 0,
        "inventory": [],
        "status_effects": {}
    }

ENEMIES = {
    "goblin": {
        "name": "Goblin",
        "hp": 30,
        "damage": 8
    },
    "skeleton": {
        "name": "Skeleton",
        "hp": 40,
        "damage": 10
    },
    "orc": {
        "name": "Orc",
        "hp": 60,
        "damage": 15
    }
}
