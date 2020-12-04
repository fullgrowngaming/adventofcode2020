#!/usr/bin/env python

"""dec04-2.py: Solution to Advent of Code December 4th, part 2
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
    total_passports = 0
    bad_passports = 0
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for elem in data:
        if all(field in elem.keys() for field in fields): #check if all fields are present first
            total_passports += 1

            birth_year = int(elem['byr'])
            if birth_year < 1920 or birth_year > 2002:
                bad_passports += 1
                continue
            
            issue_year = int(elem['iyr'])
            if issue_year < 2010 or issue_year > 2020:
                bad_passports += 1
                continue

            exp_year = elem['eyr']
            if len(exp_year) != 4:
                #this does not actually happen in the data set
                bad_passports += 1
                continue
            else:
                try:
                    if int(exp_year) < 2020 or int(exp_year) > 2030:
                        bad_passports += 1
                        continue
                except:
                    #this does not actually happen in the data set - always actually a number, so this check is not needed
                    bad_passports += 1
                    continue

            height_in_cm = True
            height = 0
            if elem['hgt'][-1] == 'm' or elem['hgt'][-1] == 'n':
                if elem['hgt'][-1] == 'n': #if inches
                    height_in_cm = False
                    height = int(elem['hgt'][:-2])

                    if height_in_cm and (height < 150 or height > 193):
                        bad_passports += 1
                        continue
                    elif not height_in_cm and (height < 59 or height > 76):
                        bad_passports += 1
                        continue
                
            else:
                bad_passports += 1
                continue

            hair_color = elem['hcl']
            if hair_color[0] != '#' or len(hair_color) != 7:
                bad_passports += 1
                continue
            else:
                for char in hair_color[1:]:
                    if char not in '0123456789' and char not in 'abcdef':
                        bad_passports += 1
                        continue

            eye_color = elem['ecl']
            valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if eye_color not in valid_colors:
                bad_passports += 1
                continue

            passport_id = elem['pid']
            if len(passport_id) != 9:
                bad_passports += 1
                continue
            else:
                for digit in passport_id:
                    if not digit.isdigit():
                        #this does not actually happen in the data set 
                        bad_passports += 1
                        continue

    print(f'Bad Passports: {total_passports - bad_passports}')

