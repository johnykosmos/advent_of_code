#!/usr/bin/env python3

def get_input(filename: str) -> list:
    with open(filename, 'r') as file:
        in_ = [line.strip() for line in file]

    return in_

def part_one(in_) -> int:
    sum_of_points: int = 0
    for line in in_:
        points: int = 0
        table: list = line.split(": ")[1].split(" | ")
        winning_nums: list = [num for num in table[1].split(" ") if num in table[0].split(" ") and num != ''] 
        
        if winning_nums:
            points = 1
            for i in range(len(winning_nums)-1):
                points *= 2

            sum_of_points += points

    return sum_of_points

def part_two(in_):
    pass

def main() -> None:
    in_ = get_input("input2.txt")
    print(part_one(in_))

if __name__ == '__main__':
    main()





