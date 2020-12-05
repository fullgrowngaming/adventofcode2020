#!/usr/bin/env python

"""dec05-1.py: Solution to Advent of Code December 5th, part 1
"""

def read_input(filename: str) -> list:
    input_list = list()

    try:
        with open(filename) as f:
            for line in f.readlines():
                input_list.append(line)
    except FileNotFoundError:
        print(f'File {filename} not found!')
        
    return input_list

def binary_search(str_to_decode: str, lower_limit: int, upper_limit: int) -> int:
    mid = 0

    for char in str_to_decode[:-1]:
        mid = (upper_limit + lower_limit) // 2
        if char == 'F' or char == 'L':
            upper_limit = mid
        elif char == 'B' or char == 'R':
            lower_limit = mid + 1

    return lower_limit if str_to_decode[-1] == 'F' or str_to_decode[-1] == 'L' else upper_limit

def find_seat_id(str_to_decode: str) -> int:
    row = binary_search(str_to_decode[0:7], 0, 127)
    column = binary_search(str_to_decode[7:], 0, 7)

    return row * 8 + column

if __name__ == "__main__":
    data = read_input('input.txt')
    
    seat_ids = [find_seat_id(seat) for seat in data]
    print(max(seat_ids))



