#!/usr/bin/env python

"""dec02-1.py: Solution to Advent of Code December 2nd, part 1

Notes:
    -I considered using a named tuple to get rid of the indexing ugliness in parse_input,
    but for a question like this, it seems unneeded.
    
    -Technically, parsing the input and verifying the password could be done at the same 
    time, but I separated it just in case we do something else with the data at a later
    point. 
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

def parse_input(input_list: list) -> list:
    parsed_input = list()

    for line in input_list:
        split_line = line.split(' ')

        occurance = split_line[0].split('-')
        least_occurance = occurance[0]
        most_occurance = occurance[1]

        letter = split_line[1][0]

        password = split_line[2].rstrip()

        finalized = (int(least_occurance), int(most_occurance), letter, password)
        parsed_input.append(finalized)

    return parsed_input

if __name__ == "__main__":
    data = read_input('input.txt')
    parsed_data = parse_input(data)

    good_passwords = 0

    for entry in parsed_data:
        letter_counter = 0
        target_letter = entry[2]

        for letter in entry[3]:
            if letter == target_letter:
                letter_counter += 1
        
        if letter_counter >= entry[0] and letter_counter <= entry[1]:
            good_passwords += 1

    print(good_passwords)
