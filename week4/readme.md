# Week 4 – OOP Battle Game (Classes and Objects)

## Student Information

Name:  Stephen St Jean
GitHub Username: SSJ_KILLA 

---

## Project Overview

This project is a turn-based battle game written in Python using **classes and objects**.

Instead of using dictionaries, the player and enemies are represented as objects with their own data and behavior.  
This project demonstrates object-oriented programming (OOP) concepts and cleaner program structure.

---

## Programs Included

This project is split across multiple files.

- `main.py` – Runs the game and controls the main loop
- `player.py` – Defines the Player class
- `enemy.py` – Defines the Enemy class

---

## Concepts Used

This project demonstrates the following concepts:

- Classes and objects
- The `__init__` method
- Instance variables
- Methods
- Object interaction
- Importing classes from other files
- Cleaner and more scalable program structure

---

## How to Run the Program

From inside the `week4` folder, run:

`python main.py`
Make sure all files are in the same folder so imports work correctly.

---

## Class Descriptions

### Player Class

Describe the `Player` class:

- What attributes does it have? 
The attributes the player have are Hp, damage, and a name.

- What methods does it include?
It includes f-strings, definitions, and defining functions to keep multiple code in track.

- How does it interact with enemies?
They simply go and attack each other degrading each others health till one of them falls, then continuing onto the next fight with the same health they ended the last fight with.

(3–5 sentences.)

---

### Enemy Class

Describe the `Enemy` class:

- What attributes does it have?
Same as the player has as well. Just simple Health, Name, and attack or damage.

- What methods does it include?
Essentially an exact clone as player as well. F-strings, definitions, defining functions.
- How does it interact with the player?

(3–5 sentences.)

---

## Game Flow Description

Describe how the game works from start to finish:

- How does the game begin?
- How do turns work?
- How does the game end?

(4–6 sentences.)
The game begins by creating the player and enemy objects and displaying an introduction to the player. Turns work by alternating between the player and the enemy, with each turn allowing one character to attack and reduce the other’s health. After each attack, the game checks whether the target is still alive. This loop continues until one character’s health reaches zero. The game ends when either the player defeats the enemy or the player’s health is reduced to zero, and a win or loss message is displayed.

---

## File Responsibility Explanation

Explain what each file is responsible for:

- `main.py`  
- `player.py`  
- `enemy.py`  

(1–2 sentences per file.)
`main.py` is responsible for running the game logic, creating objects, and controlling the overall flow of the program (such as turns, combat, and win/lose conditions).
`player.py` defines the `Player` class and handles everything related to the player’s data and behavior, like health, attacks, and checking if the player is alive.
`enemy.py` defines the `Enemy` class and contains the logic and attributes specific to enemies, keeping enemy behavior separate from the player for cleaner and more organized code.

---

## Design Decisions

Describe any design decisions you made:

- Why did you use classes instead of dictionaries?
- How did OOP improve code clarity?
- Did you reuse logic from earlier weeks?

(3–5 sentences.)
I used classes instead of dictionaries because classes clearly define both the data and the behavior of a player in one place. OOP improved code clarity by making it obvious what actions a player can perform and what data belongs to that player. Methods like `take_damage()` are easier to understand and reuse than standalone functions that pass data around. I reused logic from earlier weeks by applying conditionals and function-style thinking inside class methods.

---

## Known Issues or Limitations

List any bugs, missing features, or improvements you would make with more time.

If none, write:  
`None`

None
---

## Reflection

Answer the following questions:

- What was the hardest concept this week?
- What part of OOP do you feel most confident about?
- How did using classes change how you think about writing programs?

(4–6 sentences total.)

---

The hardest concept this week was understanding how `self` works and why it’s required in every method inside a class. I feel most confident about creating classes and using `__init__()` to set up object attributes. Writing methods like `take_damage()` made sense once I saw how they directly modify an object’s own data. Using classes changed how I think about programs by encouraging me to group related data and behavior together. Instead of writing scattered functions, I now think in terms of objects that represent real things in the program.