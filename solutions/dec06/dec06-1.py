#!/usr/bin/env python

"""dec06-1.py: Solution to Advent of Code December 6th, part 1
"""

import string

def read_input(filename: str) -> list:
    data = list()
    new_entry = list()

    try:
        with open(filename) as f:
            for line in f.readlines():
                if line != "\n":
                    new_entry.append(set(line.rstrip()))
                else:
                    data.append(new_entry)
                    new_entry = []
            if new_entry:
                data.append(new_entry)
    except FileNotFoundError:
        print(f'File {filename} not found!')
        
    return data

def main():
    data = read_input('input.txt')
    shared = 0
    for elem in data:
        union = set.union(*elem)
        for char in set(string.ascii_lowercase):
            if char in union:
                shared += 1

    print(shared)

if __name__ == "__main__":
    main()