#!/usr/bin/env python

"""dec09-2.py: Solution to Advent of Code December 9th, part 2
"""

import time

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

def break_encryption(failed_number, data):
    left_pointer = 0
    right_pointer = 1
    cum_total = data[left_pointer] + data[right_pointer]

    while right_pointer < len(data):
        if cum_total > failed_number:        
            cum_total -= data[left_pointer]
            left_pointer += 1
                
        elif cum_total < failed_number:
            right_pointer += 1
            cum_total += data[right_pointer]
        else:
            return data[left_pointer:right_pointer + 1]
    
    return -1

def main():
    data = read_input('input.txt')
    failed_number = find_failure_in_xmas_data(25, data)
    answer = break_encryption(failed_number, data)
    print(min(answer) + max(answer))
    
if __name__ == "__main__":
    main()
