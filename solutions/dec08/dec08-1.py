#!/usr/bin/env python

"""dec08-1.py: Solution to Advent of Code December 8th, part 1
"""

import copy

def read_input(filename: str) -> list:
    input_list = list()

    try:
        with open(filename) as f:
            for line in f.readlines():
                split_line = line.rstrip().split()
                input_list.append([split_line[0], split_line[1]])
    except FileNotFoundError:
        print(f'File {filename} not found!')
        
    return input_list

def run_code(code):
    instruction_pointer = 0
    accumulator = 0
    running = True

    while running:
        if instruction_pointer == len(code):
            print('Completed successfully!')
            return (instruction_pointer, accumulator)
        elif instruction_pointer > len(code) or instruction_pointer < 0:
            print('Jumped out of bounds.')
            return -1

        current_instruction = code[instruction_pointer]
        if current_instruction[0] == 'seen':
            return (instruction_pointer, accumulator)

        if current_instruction[0] == 'acc':
            accumulator += int(current_instruction[1])
            instruction_pointer += 1
        elif current_instruction[0] == 'nop':
            instruction_pointer += 1
        elif current_instruction[0] == 'jmp':
            instruction_pointer += int(current_instruction[1])
        
        current_instruction[0] = 'seen'
  
    return -1

def fix_code(code):
    number_of_instructions = len(code)
    working_memory = copy.deepcopy(code) #working memory is copy of original code
    current_instruction = 0

    while True:
        if current_instruction == number_of_instructions:
            break

        if working_memory[current_instruction][0] == 'jmp':
            working_memory[current_instruction][0] = 'nop'
            
        elif working_memory[current_instruction][0] == 'nop':
            working_memory[current_instruction][0] = 'jmp'

        instruction_pointer, accumulator = run_code(working_memory)
        if instruction_pointer == number_of_instructions:
            return accumulator
            
        current_instruction += 1
        working_memory = copy.deepcopy(code)

    return -1
        
def main():
    code = read_input('input.txt')
    print(run_code(code)[1])

if __name__ == "__main__":
    main()
