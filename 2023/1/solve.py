#!/usr/bin/env python3

#CONSTANTS
DIGITS = "123456789"
WORD_TO_DIGIT = {"one":"1",
               "two":"2",
                 "three":"3",
                 "four":"4",
                 "five":'5',
                 "six":'6',
                 "seven":"7",
                 "eight":'8',
                 "nine":'9'}


def getFirstDigit(line: str) -> str:
    for i in range(len(line)):
        if line[i] in DIGITS:
            return line[i]
        '''for part two'''
        for word in WORD_TO_DIGIT:
            if word in line[:i+1]:
                return WORD_TO_DIGIT[word]
    return ""

def getSecondDigit(line: str) -> str:
    for i in range(1, len(line) + 1):
        if line[-i] in DIGITS:
            return line[-i]
        '''for part two'''
        for word in WORD_TO_DIGIT:
            if word in line[-i:]:
                return WORD_TO_DIGIT[word]
    return ""

def part_one(in_) -> int:
    with open(in_) as file:  
        sum = 0
        for line in file:
            line = line.strip()
            number = int(getFirstDigit(line) + getSecondDigit(line))
            sum += number
        return sum

def part_two(in_):
    with open(in_) as file:
        sum = 0
        for line in file:
            line = line.strip()
            print(line, getFirstDigit(line), getSecondDigit(line))
            number = int(getFirstDigit(line) + getSecondDigit(line))
            sum += number
        return sum

def main() -> None:
    #print(part_one("input.txt"))
    print(part_two("input.txt"))


if __name__ == '__main__':
    main()





