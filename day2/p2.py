from functools import reduce

with open("data.txt", 'r') as f:
    input_lines = [line.strip() for line in f.readlines()]

color_dict = {"red": 12, "green": 13, "blue": 14}
sum_prod_balls = 0
for line in input_lines:
    game_info = line.rsplit(":")[1]
    draws = game_info.split(";")
    min_number_dict = {}   
    for draw in draws:
        counter = 0
        for color, num in color_dict.items():
            if color in draw:
                index = draw.index(color)
                num_balls = int(draw[index-3:index-1].replace(" ", ""))
                if color not in min_number_dict:
                    min_number_dict[color] = num_balls 
                elif num_balls > min_number_dict[color]:
                    min_number_dict[color] = num_balls
                    counter += 1
    sum_prod_balls += reduce(lambda x, y: x*y, min_number_dict.values())
print(sum_prod_balls)

