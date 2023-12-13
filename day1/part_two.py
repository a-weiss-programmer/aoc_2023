def solve(puzzle_input: list[str]):
    sum = 0
    number_list = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]
    for line in puzzle_input:
        first_num = ""
        second_num = "" 
        for index, number in enumerate(number_list):
            line = line.replace(number, str(index + 1))
        
        for char in line:
            if char.isnumeric():
                if first_num == "":
                    first_num = char
                    break
    
        
        for char in line[::-1]:
            if char.isnumeric():
                second_num = char
                break

        if second_num == "":
            second_num = first_num

        sum += int(f"{first_num}{second_num}")
    print(sum)
        


with open ("puzzle_input", "r") as puzzle_input:
    solve(puzzle_input)