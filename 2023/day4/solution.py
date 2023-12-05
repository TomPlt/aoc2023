from collections import defaultdict
from tqdm import tqdm

with open("data.txt") as f: 
    lines = f.read().splitlines()

def convert_score_to_points(score):
    '''0 -> 0, 1 -> 1, 2 -> 2, 3 -> 4, 4 -> 8, ...'''
    if score == 0: 
        return 0
    else: 
        return 2**(score-1)

def part1():
    total_points = 0
    for line in lines: 
        all_numbers = line.split(":")[1].split("|")
        dict_line = {n: [int(i) for i in e.split()] for n, e in enumerate(all_numbers)}
        line_score = 0
        for value in dict_line[0]: 
            if value in dict_line[1]: 
                line_score += 1
        total_points += convert_score_to_points(line_score)  
    print(total_points)

def part2():
    dict_card_number = defaultdict(int)
    for counter, line in tqdm(enumerate(lines)): 
        all_numbers = line.split(":")[1].split("|")
        dict_line = {n: [int(i) for i in e.split()] for n, e in enumerate(all_numbers)}
        dict_card_number[counter] += 1
        for i in range(dict_card_number[counter]):
            line_score = 0
            for value in dict_line[0]: 
                if value in dict_line[1]: 
                    line_score += 1
                    if counter+line_score < len(lines):
                        dict_card_number[counter+line_score] += 1 
    print(sum(list(dict_card_number.values())))
    
if __name__ == "__main__":
    part1(), part2()
