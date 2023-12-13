# index 0 = row
# index 1 = column
coordinates_move: dict[str, tuple]= {
    "east": (0, 1),
    "west": (0, -1),
    "north": (-1, 0),
    "south": (1, 0),
    "northeast": (-1, 1),
    "northwest": (-1, -1),
    "southeast": (1, 1),
    "southwest": (1, -1)
}
def solve(input: list[str]):
    matrix: list[list[str]] = []
    for line in input:
        line = [char for char in line]
        matrix.append(line)
    row_length = len(matrix) - 1
    col_length = len(matrix[0]) - 1
 
    part_number = 0
    row_num = 0
    while row_num <= row_length:
        row = matrix[row_num]
        col_num = 0
        while col_num < col_length:
            cell = row[col_num]
            cur_index = 0
            if cell.isnumeric():
                is_valid_number = False
                for (row_delta, col_delta) in coordinates_move.values():
                    new_row_num = row_num + row_delta
                    new_col_num = col_num + col_delta
                    # Check if out of bounds
                    if new_row_num < 0 or new_row_num > row_length:
                        continue
                    if new_col_num < 0 or new_col_num > col_length:
                        continue
                    # if not out of bounds, check if valid spot
                    cell_check = matrix[new_row_num][new_col_num]
                    # Valid if not numeric and not a period
                    if not cell_check.isnumeric() and cell_check != ".":
                        is_valid_number = True
                        break
                if is_valid_number:
                    # Loop over next cells until a non-number is hit to construct the number
                    # ..255..
                    # ...../.
                    # cell = matrix[0][2] = 2
                    # col_num = 2
                    # cur_index = 4
                    # col_num = 2 + (4 - 2) = 4
                    # cell = matrix[0][4] = 
                    
                    number_builder = []
                    cur_index = col_num
                    # look forward
                    while row[cur_index].isnumeric() and cur_index < col_length:
                        number_builder.append(row[cur_index])
                        cur_index += 1
                    
                    # look behind
                    #while row[cur_index].isnumeric() and cur_index >= 0:
                    #    pass
            if cur_index != 0:
                col_num += (cur_index - col_num)
            col_num += 1
        row_num += 1

    print(part_number)


    
with open("test_input", "r") as puzzle_input:
    solve(puzzle_input.readlines())