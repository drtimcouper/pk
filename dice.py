import random

class Dice(object):
    def __init__(self, sides, plus=0):
        self.sides = sides
        self.plus =plus

    def roll(self):
        return min(random.randint(0, self.sides)+self.plus, self.sides)

D4 = Dice(4)
D6 = Dice(6)
D8 = Dice(8)
D10 = Dice(10)
D12 = Dice(12)
D12p1 = Dice(12,1)
