#!/usr/bin/env python

"""dec09-1.py: Solution to Advent of Code December 9th, part 1
"""

def read_input(filename: str) -> list:
    input_list = list()

    try:
        with open(filename) as f:
            for line in f.readlines():
                input_list.append(int(line.rstrip()))
    except FileNotFoundError:
        print(f'File {filename} not found!')
        
    return input_list

def does_two_sum_exist(target, data):
    seen = set()

    for element in data:
        if target - element in seen and element != target - element:
            return True
        else:
            seen.add(element)

    return False

def find_failure_in_xmas_data(preamble, data):
    left_pointer = 0
    right_pointer = preamble

    while right_pointer < len(data):
        if not does_two_sum_exist(data[preamble], data[left_pointer:right_pointer]):
            return data[preamble]
        else:
            left_pointer += 1
            right_pointer += 1
            preamble += 1

def main():
    data = read_input('input.txt')
    print(find_failure_in_xmas_data(25, data))

if __name__ == "__main__":
    main()
