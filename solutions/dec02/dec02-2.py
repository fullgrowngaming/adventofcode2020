#!/usr/bin/env python

"""dec02-2.py: Solution to Advent of Code December 2nd, part 2

Notes:
    -As it turns out, my more general solution from part 1 was greatly needed since
    it did turn out that part 2 needed a different sort of evaluation of the input

    -Again, a named tuple would have made things cleaner.
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
        #this is an exclusive or test since at most one needs to be true
        if (entry[3][entry[0] - 1] == entry[2]) != (entry[3][entry[1] - 1] == entry[2]):
            good_passwords += 1

    print(good_passwords)
