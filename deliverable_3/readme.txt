task 1 + 4 : character.py 
task 2: dice.py
task 3: items.py
task 5: battle.py

* Hent, opprett en ny .py-fil med følgende innhold for å teste koden:
[from battle import Battle
from character import Mage, Warrior

hero = Warrior(name="Knight")
enemy = Mage(name="Wizard")

battle = Battle(hero=hero, enemy=enemy)
battle.simulate_battle()

if hero.is_alive:
print(f"{hero.name} wins!")
else:
print(f"{enemy.name} wins!")]


* If [import block is unsorted or un-formatted Error] appears, do:

1. Place your cursor on the underlined import.
2. Press Ctrl + .
3. Select Organize imports.
