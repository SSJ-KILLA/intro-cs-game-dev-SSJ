def welcoming():
    print(f"Welcome to the void.")

welcoming()

name = input("Greetings... What shall this vessel be called?:")
print(f"I see... {name}. Quite the choice.")

age = int(input("What is the historical value of this vessel?:"))

if age <= 15:
    print(f"{name} shall be too weak.")

elif age >= 15:
    print(f"{name} shall be cultured.")

elif age > 18:
    print(f"{name} shall recieve more privilge than most.")

options = int(input("You see yourself in the mirror. What must be done?\n1.I look into myself \n2.I seek oblivion.\n3.I must find power.\n"))

if options == 1:
    print("You shall recieve an awakening.")

elif options == 2:
    print("You shall achieve nothingness")

elif options == 3:
    print("You shall acquire the strength you seek")

