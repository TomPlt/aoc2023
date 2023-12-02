with open("data.txt", 'r') as f:
    input_lines = [line.strip() for line in f.readlines()]

sum_valid_ids = 0
color_dict = {"red": 12, "green": 13, "blue": 14}
for line in input_lines:
    id = int(line.split(":")[1])
    game_info = line.rsplit(":")[1]
    draws = game_info.split(";")
    valid_draw = 0
    for draw in draws:
        counter = 0
        for color, num in color_dict.items():
            if color in draw:
                index = draw.index(color)
                num_balls = int(draw[index-3:index-1].replace(" ", ""))
                if num < num_balls:
                    break
                else: 
                    counter += 1
        if counter == len(draw.split(",")):
            valid_draw += 1
    if valid_draw == len(draws):
        sum_valid_ids += id
print(sum_valid_ids)
