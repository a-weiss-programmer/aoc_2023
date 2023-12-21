import re
from functools import reduce

def is_symbol(character: str):
    return (not character.isnumeric()) and character != "."

def get_numbers(lines: list[str]):
    numbers = []
    for i, line in enumerate(lines):
        line = line.strip()
        for match in re.finditer(r"\d+", line):
            start_index = match.start(0) - 1
            end_index = match.end(0)
            number = int(match.group(0))
            numbers.append((i, line, start_index, end_index, number))
    return numbers

def get_gears(lines: list[str]):
    for i, line in enumerate(lines):
        line = line.strip()
        for match in re.finditer(r"\*+", line):
            index = match.start(0)
            yield i, line, index


def part_one(lines: list[str]):
    total = 0
    for (i, line, start_index, end_index, number) in get_numbers(lines):

        # Check to the left
        if start_index >= 0 and is_symbol(line[start_index]):
            total += number
            continue

        # Check to the right
        if end_index <= len(line) - 1 and is_symbol(line[end_index]):
            total += number
            continue

        line_above = ""
        line_below = ""

        if i - 1 >= 0:
            line_above = lines[i - 1]
        
        if i + 1 < len(lines):
            line_below = lines[i + 1]

        # Check Above and below
        for j in range(start_index + 1, end_index):
            if line_above:
                if is_symbol(line_above[j]):
                    total += number 
                    continue
            if line_below:
                if is_symbol(line_below[j]):
                    total += number
                    continue
        
        # Check Diagonal top right (end index + 1) and top left (start index - 1)
        if line_above:
            if end_index < len(line_above) - 1 and is_symbol(line_above[end_index]):
                total += number 
                continue
            if start_index >= 0 and is_symbol(line_above[start_index]):
                total += number
                continue
        
        # Check Diagonal bottom right (end index + 1) and bottom left (start index - 1)
        if line_below:
            if end_index < len(line_below) - 1 and is_symbol(line_below[end_index]):
                total += number 
                continue
            if start_index >= 0 and is_symbol(line_below[start_index]):
                total += number
                continue

    print(f"PART ONE: {total}")

def part_two(lines: list[str]):
    total = 0
    numbers = get_numbers(lines)

    for (i, line, index) in get_gears(lines):
        numbers_near_gear = []
        # Check to left
        if index - 1 >= 0 and line[index - 1].isnumeric():
            numbers_near_gear.append((i, index - 1))
        
        # Check to the right
        if index + 1 <= len(line) -1 and line[index - 1].isnumeric():
            numbers_near_gear.append((i, index + 1))
        
        if i - 1 >= 0:
            # Check Above
            if lines[i - 1][index].isnumeric():
                numbers_near_gear.append((i - 1, index))
            
            # Check Top Left
            if index - 1 >= 0 and lines[i - 1][index - 1].isnumeric():
                numbers_near_gear.append((i - 1, index - 1))
            
            # Check Top right
            if index + 1 <= len(line) - 1 and lines[i - 1][index + 1].isnumeric():
                numbers_near_gear.append((i - 1, index + 1))

        if i + 1 < len(lines):
            # Check Below
            if lines[i + 1][index].isnumeric():
                numbers_near_gear.append((i + 1, index))

            # Check Bottom Left
            if index - 1 >= 0 and lines[i + 1][index - 1].isnumeric():
                numbers_near_gear.append((i + 1, index - 1))
            
            # Check Bottom Right
            if index + 1 <= len(line) - 1 and lines[i + 1][index + 1].isnumeric():
                numbers_near_gear.append((i + 1, index + 1))
        
        if len(numbers_near_gear) == 2:
            product_array = []
            for (row, column) in numbers_near_gear:
                print(row, column)
                for match in re.finditer(r"\d+", lines[row]):
                    start_index = match.start(0) - 1
                    end_index = match.end(0)

                    if start_index <= column and end_index >= column:
                        product_array.append(int(match.group(0)))

            total += product_array[0] * product_array[1]
    
    print(f"PART TWO: {total}")

with open("puzzle_input", "r") as puzzle_input:
    lines = puzzle_input.readlines()
    part_one(lines)
    part_two(lines)
