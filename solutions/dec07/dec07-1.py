#!/usr/bin/env python

"""dec07-1.py: Solution to Advent of Code December 7th, part 1
"""

import string
import re

def read_input(filename: str) -> list:
    data = dict()
    
    try:
        with open(filename) as f:
            for line in f.readlines():
                split_line = line.split()
                build_dict = {}
                for match in re.findall(r'(\d) (\w+ \w+)', line):
                    build_dict[match[1]] = int(match[0])
                data[split_line[0] + " " + split_line[1]] = build_dict
                    
    except FileNotFoundError:
        print(f'File {filename} not found!')
        
    return data
                       
def main():
    data = read_input('input.txt')
    target_bag = 'shiny gold'

    print(data)
    
if __name__ == "__main__":
    main()