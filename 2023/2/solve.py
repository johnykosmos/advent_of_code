#!/usr/bin/env python3

MAX_CUBES_QUANTITY = {"red" : 12,
                      "green" : 13,
                      "blue" : 14}


def isGameValid(line: str) -> bool:
    for game_set in line.split("; "):
        cubes_quantity = {cube.split(' ')[1] : int(cube.split(' ')[0]) for cube in game_set.split(", ")}
        print(cubes_quantity)
        for color in cubes_quantity:
            if cubes_quantity[color] > MAX_CUBES_QUANTITY[color]:
                return False
    
    return True
    
def part_one(in_) -> int:
    sum_of_indexes = 0
    with open(in_, 'r') as file:
        for line in file:
            line = line.strip()
            game_index = line.split(": ")[0]
            print(line)
            if isGameValid(line.split(": ")[1]):
                sum_of_indexes += int(game_index.split(' ')[1])
    
    return sum_of_indexes

def part_two(in_):
    pass

def main() -> None:
    #print(part_one("input.txt")) 
    print(part_two("input2.txt"))
if __name__ == '__main__':
    main()





