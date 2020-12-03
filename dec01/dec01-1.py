#!/usr/bin/env python

"""dec01-1.py: Solution to the first Advent of Code problem posted on December 1st."""

import sys

def parse_input(filename: str) -> list:
    input_list = list()

    try:
        with open(filename) as f:
            for line in f.readlines():
                input_list.append(int(line.rstrip()))
    except FileNotFoundError:
        print(f'File {filename} not found!')
        
    return input_list

if __name__ == "__main__":
    target_number = 2020
    input_list = parse_input('input.txt')
    seen_nums = set()

    for num in input_list:
        if (target_number - num) in seen_nums:
            print((target_number - num) * num)
            sys.exit()
        else:
            seen_nums.add(num)

