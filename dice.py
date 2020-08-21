from random import randint

class Dice():
    """Class presents sinle dice"""

    def __init__(self, num_sides=6):
        """Default dice has 6 sides"""
        self.num_sides = num_sides

    def roll(self):
        """Returns random value from 1 to num_side"""
        return randint(1, self.num_sides)
