name = input("What is your name?:")
print(f"Greetings, {name}")

age = int(input("How old are you?:"))

if age < 11:
    print(f"Hello {name}, you are a child.")

elif age < 13:
    print(f"Hello {name}, you are a pre-teen.")

elif age <= 17:
    print(f"Hello {name}, you are a teenager.")

elif age > 18:
    print(f"Hello {name}, you are an adult.")