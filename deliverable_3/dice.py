# Task 2: Implement a Dice class 

import random


class Dice:
    def __init__(self, sides: int = 6) -> None:
        """Create at-least-two sides dice""" 
        if sides < 2:
            raise ValueError("Dice must have at least 2 sides.")
        self.sides = sides

    def roll(self) -> int:
        """Roll the dice and return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of dice object"""
        return f"<Dice sides={self.sides}>"

    def __call__(self) -> int:
        return self.roll() 

