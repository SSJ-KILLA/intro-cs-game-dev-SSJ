def greet_player(name):
    print(f"Hello, {name}")

def calculate_damage(base_damage):
    return base_damage + 2

greet_player("Tester")
damage = calculate_damage(20)
print(damage)