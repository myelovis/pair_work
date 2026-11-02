from character import Character


class Battle:

    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        if not self.hero.is_alive or not self.enemy.is_alive:
            return

        self.hero.attack(self.enemy)

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()