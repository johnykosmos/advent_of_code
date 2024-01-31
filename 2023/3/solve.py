#!/usr/bin/env python3

# CONTSANTS
DIGITS = ('0','1','2','3','4','5','6','7','8','9')


def get_input(filename: str) -> list:
    with open(filename) as file:
        in_ = [line.strip() for line in file]

    return in_

def get_nums_cords(line: str, y_cord: int) -> list[list[tuple]]:
    num = list()
    nums_positions = list()
    for index in range(len(line)):
        if line[index] in DIGITS:
            num.append((y_cord, index))

        elif line[index] not in DIGITS and len(num) != 0:
            nums_positions.append(num)
            num = []

    if num: # checking if the last index was a digit
        nums_positions.append(num)

    return nums_positions

def is_part_number(schematic: list[str], cords: list[tuple],
                   length: int, height: int) -> tuple:
    for digit in cords:
        for i in range(digit[0] - 1, digit[0] + 2):
            for j in range(digit[1] - 1, digit[1] + 2):
                if i >= 0 and i < height and j >= 0 and j < length and schematic[i][j] != '.' and schematic[i][j] not in DIGITS:
                    return (i, j)
    
    return ()

def cords_to_num(line: str, cords: list) -> int:
    num: str = ''
    for digit in cords:
        num += line[digit[1]]
    
    return int(num)

def part_one(in_) -> int:
    length: int = len(in_[0])
    height: int = len(in_)
    sum_of_nums: int = 0

    for y_cord, line in enumerate(in_):
        for element in get_nums_cords(line, y_cord):
            if is_part_number(in_, element, length, height):
                sum_of_nums += cords_to_num(line, element)
    return sum_of_nums

def part_two(in_) -> int:
    length: int = len(in_[0])
    height: int = len(in_)
    gears = dict()
    sum_of_ratios: int = 0

    for y_cord, line in enumerate(in_):
        for element in get_nums_cords(line, y_cord):
            gear_cords = is_part_number(in_, element, length, height)
            if gear_cords and in_[gear_cords[0]][gear_cords[1]] == '*':
                if gears.get(gear_cords) is None:
                     gears[gear_cords] = list()
                gears[gear_cords].append(cords_to_num(line, element))

    for cords, nums in gears.items():
        if len(nums) == 2:
            sum_of_ratios += nums[0] * nums[1]
    
    return sum_of_ratios

def main() -> None:
    in_: list = get_input("input.txt")
    print(part_one(in_))
    print(part_two(in_))

if __name__ == '__main__':
    main()





