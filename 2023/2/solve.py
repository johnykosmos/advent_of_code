#!/usr/bin/env python3


#CONTSANTS
MAX_CUBES_QUANTITY = {"red" : 12,
                      "green" : 13,
                      "blue" : 14}

# check if the game is valid
def isGameValid(line: str) -> bool:
    for game_set in line.split("; "):
        cubes_quantity = {cube.split(' ')[1] : int(cube.split(' ')[0]) for cube in game_set.split(", ")}
        print(cubes_quantity)
        for color in cubes_quantity:
            if cubes_quantity[color] > MAX_CUBES_QUANTITY[color]:
                return False
    
    return True

# check the minimum quantity of cubes to be able to play the gane
def minCubeQuantity(line: str) -> dict:
    min_cubes_quantity = {"red" : None,
                          "green" : None,
                          "blue" : None}

    for game_set in line.split("; "):
        cubes_quantity = {cube.split(' ')[1] : int(cube.split(' ')[0]) for cube in game_set.split(", ")}
        for color in min_cubes_quantity:
            if min_cubes_quantity[color] is None and color in cubes_quantity:
                min_cubes_quantity[color] = cubes_quantity[color]
            
            else:
                if color in cubes_quantity and min_cubes_quantity[color] is not None and min_cubes_quantity[color] < cubes_quantity[color]:
                    min_cubes_quantity[color] = cubes_quantity[color]
    
    return min_cubes_quantity 

# calculate the product of every color of cube amounts
def cubesPower(cubes: dict) -> int:
    product = 1
    for color in cubes:
        product *= cubes[color]

    return product


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

def part_two(in_) -> int:
    sum_of_power = 0
    with open(in_, 'r') as file:
        for line in file:
            line = line.strip()
            print(line)
            cubes = minCubeQuantity(line.split(": ")[1]) 
            print(cubes)
            sum_of_power += cubesPower(cubes)
        
        return sum_of_power

def main() -> None: 
    #print(part_one("input.txt")) 
    print(part_two("input.txt"))


if __name__ == '__main__':
    main()





