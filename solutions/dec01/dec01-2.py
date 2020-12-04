#!/usr/bin/env python

"""dec01-2.py: Solution to the second Advent of Code problem posted on December 1st."""

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
    input_list.sort()

    left_pointer = 0
    right_pointer = 1

    while input_list[left_pointer] + input_list[right_pointer] < target_number:
        for number in input_list[right_pointer + 1:]:
            if number + input_list[left_pointer] + input_list[right_pointer] == target_number:
                print(number * input_list[left_pointer] * input_list[right_pointer])
            elif number + input_list[left_pointer] + input_list[right_pointer] > target_number:
                right_pointer += 1
                break

        if right_pointer > len(input_list):
            left_pointer += 1
            right_pointer = left_pointer + 1


