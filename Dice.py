import random


class dice():
    def __init__(self) -> None:
        self.diceface = 1

    def roll_dice(self) -> int:
        self.diceface = random.randint(1,6)
        print(f"Your diceface is: {self.diceface}")
        return self.diceface

    def get_diceface(self) -> int:
        return self.diceface

    def set_diceface(self, set_diceface: int) -> None:
        self.diceface = set_diceface