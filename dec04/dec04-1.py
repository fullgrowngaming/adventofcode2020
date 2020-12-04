#!/usr/bin/env python

"""dec04-1.py: Solution to Advent of Code December 4th, part 1
"""

def read_input(filename: str) -> list:
    data = list()
    new_entry = {}

    try:
        with open(filename) as f:
            for line in f.readlines():
                if line != "\n":
                    split_line = line.split()
                    for entry in split_line:
                        new_entry[entry.split(':')[0]] = entry.split(':')[1]
                else:
                    data.append(new_entry)
                    new_entry = {}
            if new_entry:
                data.append(new_entry)
    except FileNotFoundError:
        print(f'File {filename} not found!')
        
    return data

if __name__ == "__main__":
    data = read_input('input.txt')
    good_passports = 0
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for elem in data:
        if all(field in elem.keys() for field in fields):
            good_passports += 1
    print(good_passports)

