# Object-oriented game simulator
# Turid Torheim, NMBU, 2026
# Group 7_3, Deliverable 3
from deliverable_3.items import Weapon


class Character:
    """Represents a character in the RPG."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
    ) -> None:
        """
        Initialise the Character.

        Args:
            name (str): The name of the character.
            hp_max (int): Maximum hit points (default = 100).
            damage (int): Base attack damage (default = 10).
            weapon (Weapon | None): Equipped weapon (default = None).
        """
        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

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
                # here we have the lower limit of 0, so that the character's HP cannot go below 0.

    def heal(self, amount: int) -> None:
        """Increases the character's HP by the specified amount, up to hp_max."""
        self._hp = min(self.hp_max, self._hp + max(0, amount))
    
    def attack(self, target: "Character") -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage)
        

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Return whether the character is alive."""
        return self._hp > 0

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
            mana: int= 0,  
            weapon: Weapon | None = None,
            mana_max: int = 30) -> None:
                super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
                self.mana_max = mana_max
                self.mana = max(0, min(mana, self.mana_max))

    def attack(self, target: Character) -> None:
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.damage * 2)
        else:
            super().attack(target)
            self.mana = min(self.mana_max, self.mana + 5)