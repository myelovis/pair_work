# Object-oriented game simulator
# Turid Torheim, NMBU, 2026
# Group 7_3, Deliverable 3
from deliverable_3.items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, amount: int = 0) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            amount (int): Amount of damage taken (default = 0)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = max(0, self._hp - max(0, amount))
        self.damage = damage

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    def take_damage(self, amount: int) -> None:
            """Reduces the character's HP by the specified amount, ensuring it doesn't go below 0."""
            self._hp = max(0, self._hp - max(0, amount))
    
    def attack(self, target: "Character") -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage)
        target._hp = max(0, target._hp)  # Target hp cannot end up lower than 0


    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

# task 4
class Warrior(Character):
    def __init__(
            self, 
            name: str, 
            hp_max: int = 100, 
            damage: int = 10, 
            armor: int = 5, 
            weapon: Weapon | None = None ) -> None:
        super().__init__(name, hp_max, damage)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        reduce_damage = max(0, amount - self.armor)
        super().take_damage(reduce_damage)

class Mage(Character):
    def __init__(
            self, 
            name: str, 
            hp_max: int = 100, 
            damage: int = 10, 
            mana: int = 30, 
            weapon: Weapon | None = None,
            mana: int = 30) -> None:
        super().__init__(name, hp_max, damage)
        self.mana = mana
        self.spell_power = spell_power

    def cast_spell(self, target: "Character") -> None:
        if self.mana >= 10:
            target.take_damage(self.spell_power)
            self.mana -= 10
        else:
            print(f"{self.name} does not have enough mana to cast a spell.")