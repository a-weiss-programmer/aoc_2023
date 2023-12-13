class Game():
    def __init__(self, game: str):
        parts = game.split(":")[1].split(";")
        self.valid = {
            "red": 12,
            "green": 13,
            "blue": 14,
        }
        self.is_winning = True

        for part in parts:
            part = part.strip()
            num_dice = part.split(",")
            for die in num_dice:
                die = die.strip().split(" ")
                number = int(die[0])
                color = die[1]
                if self.valid[color] < number:
                    self.is_winning = False

from functools import reduce

class GameTwo():
    def __init__(self, game: str):
        rolls = game.split(":")[1].split(";")
        self.color_power = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for roll in rolls:
            roll = roll.strip()
            num_dice = roll.split(",")
            for die in num_dice:
                die = die.strip().split(" ")
                number = int(die[0])
                color = die[1]
                self.color_power[color] = max(self.color_power[color], number)
        
        self.power = reduce((lambda x, y: x * y), self.color_power.values())

def part_one(puzzle_input: list[str]):
    sum = 0
    for index, line in enumerate(puzzle_input):
        game = Game(line)
        if game.is_winning:
            sum += index + 1
    
    print(sum)

def part_two(puzzle_input: list[str]):
    sum = 0
    for line in puzzle_input:
        game = GameTwo(line)
        sum += game.power
    print(sum)


    
with open("puzzle_input", "r") as puzzle_input:
    lines = puzzle_input.readlines()
    part_one(lines)
    part_two(lines)