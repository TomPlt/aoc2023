from collections import defaultdict
with open("data.txt") as f: 
    lines = f.read().splitlines()

def part1():
    outcomes_dict = {"A": [1+3, 2+6, 3+0], "B": [1+0, 2+3, 3+6], "C": [1+6, 2+0, 3+3]}
    player_dict = {"X": 0, "Y": 1, "Z": 2}
    points = 0
    for line in lines: 
        temp = outcomes_dict[line[0]]
        idx = player_dict[line[2]]
        points += temp[idx]
    print(points)

def part2():
    choices_dict = {"A": ["X", "Y", "Z"], "B": ["Y", "Z", "X"], "C": ["Z", "X", "Y"]}
    outcomes_dict = {"A": [1+3, 2+6, 3+0], "B": [1+0, 2+3, 3+6], "C": [1+6, 2+0, 3+3]}
    player_dict = {"X": 2, "Y": 0, "Z": 1}
    player_choices = {"X": 0, "Y": 1, "Z": 2}   
    points = 0
    for line in lines: 
        outcomes = outcomes_dict[line[0]]
        temp = choices_dict[line[0]]
        idx = player_dict[line[2]]
        choice = temp[idx]
        points += outcomes[player_choices[choice]]  
    print(points)

part1()
part2()