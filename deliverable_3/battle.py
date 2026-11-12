# task 5: Implement a turn-based combat system

from character import Character
# imports the Character class from the character module to use in the Battle class.

class Battle:
# makes a class that implements a turn based combat system.
    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy
    # defines the hero and the enemy, the two sides in the battle

    def play_round(self) -> None:
        if not self.hero.is_alive or not self.enemy.is_alive:
            return
            
    # plays a round of combat. If either character is dead, the round ends.
        self.hero.attack(self.enemy)
        # hero attacks enemy first.
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
        # checks if the enemy is alive then attacks hero if they are.

    def simulate_battle(self) -> None:
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()
    # starts a loop that continues until either the hero or the enemy is dead.