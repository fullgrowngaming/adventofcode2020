#!/usr/bin/env python

"""dec03-1.py: Solution to Advent of Code December 3rd, part 2
"""

def read_input(filename: str) -> list:
    input_list = list()

    try:
        with open(filename) as f:
            for line in f.readlines():
                input_list.append(line.rstrip())
    except FileNotFoundError:
        print(f'File {filename} not found!')
        
    return input_list

def parse_input(input_list: list) -> str:
    parsed_input = ''

    for line in input_list:
        parsed_input += line

    return parsed_input

def solver(rows: int, columns: int, target_char: str, right_step: int, down_step: int, parsed_data: str) -> int:
    row = column = cursor = trees = 0
    while row < rows:
        cursor = row * columns + column
        if parsed_data[cursor] == target_char:
            trees += 1
        
        row += down_step
        column += right_step
        if column > columns - 1:
            column = column % columns

    return trees

if __name__ == "__main__":
    data = read_input('input.txt')
    rows = len(data)
    columns = len(data[0])
    parsed_data = parse_input(data)
    
    answer = solver(rows, columns, '#', 1, 1, parsed_data)
    answer2 = solver(rows, columns, '#', 3, 1, parsed_data)
    answer3 = solver(rows, columns, '#', 5, 1, parsed_data)
    answer4 = solver(rows, columns, '#', 7, 1, parsed_data)
    answer5 = solver(rows, columns, '#', 1, 2, parsed_data)
    print(answer * answer2 * answer3 * answer4 * answer5)
    