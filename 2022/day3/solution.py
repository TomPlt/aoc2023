from collections import defaultdict
with open("data.txt") as f: 
    lines = f.read().splitlines()

letters = "abcdefghijklmnopqrstuvwxyz"

def part1():
    total = 0
    for line in lines: 
        length = len(line)
        comp1 = line[:length//2]
        comp2 = line[length//2:]
        assert comp1 + comp2 == line   
        for char in comp1: 
            if char in comp2:
                if char.isupper():
                    total += 26
                total += letters.index(char.lower()) + 1
                break
    print(total)         

def part2():
    total = 0
    for i in range(len(lines)//3):
        comp1, comp2, comp3 = lines[i*3], lines[i*3+1], lines[i*3+2]
        for char in comp1: 
            if char in comp2 and char in comp3: 
                if char.isupper():
                    total += 26
                total += letters.index(char.lower()) + 1
                break
    print(total)
                

part2()
part1()