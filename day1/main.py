def solve(puzzle_input: list[str]):
    sum = 0
    for line in puzzle_input:
        first_num = ""
        second_num = "" 
        for char in line:
            if char.isnumeric():
                if first_num == "":
                    first_num = char
                else:
                    second_num = char
        if second_num == "":
            second_num = first_num
        sum += int(f"{first_num}{second_num}")
    print(sum)
        


with open ("puzzle_input", "r") as puzzle_input:
    solve(puzzle_input)