#!/usr/bin/env python3

def get_input(filename: str) -> list:
    with open(filename, 'r') as file:
        in_ = [line.strip() for line in file]

    return in_

def part_one(in_):
    pass

def part_two(in_):
    pass

def main() -> None:
    in_ = get_input("input2.txt")
    part_one(in_)
    part_two(in_)

if __name__ == '__main__':
    main()





