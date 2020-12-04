#!/usr/bin/env python

"""dec03-1.py: Solution to Advent of Code December 3rd, part 1
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

if __name__ == "__main__":
    row = column = cursor = trees = 0
    TARGET_CHAR = '#'
    RIGHT_STEP = 3
    DOWN_STEP = 1

    data = read_input('input.txt')
    rows = len(data)
    columns = len(data[0])
    
    parsed_data = parse_input(data)

    while row < rows:
        cursor = row * columns + column
        if parsed_data[cursor] == TARGET_CHAR:
            trees += 1
        
        row += DOWN_STEP
        column += RIGHT_STEP
        if column > columns - 1:
            column = column % columns

    print(trees)