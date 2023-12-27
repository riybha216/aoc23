import re

block_max = {"red": 12, "green": 13, "blue": 14}
block_mins = {"red": 0, "blue": 0, "green": 0}

def process_line(line):
    line = re.sub(",|:|;|\n", "", line)    
    line = line.split(" ")
    game_id, is_valid = 0, True

    for i in range(1, len(line), 2):
        if i == 1:
            game_id = int(line[i])
        else:
            color = line[i]
            num = int(line[i-1])
            if num > block_max[color]:
                is_valid = False
    
    return game_id, is_valid

def process_line_part_2(line):
    line = re.sub(",|:|;|\n", "", line)    
    line = line.split(" ")

    for i in range(1, len(line), 2):
        if i != 1:
            color = line[i]
            num = int(line[i-1])
            if num > block_mins[color]:
                block_mins[color] = num
    
    power = block_mins["red"] * block_mins["blue"] * block_mins["green"]
    block_mins["red"], block_mins["green"], block_mins["blue"] = 0, 0, 0
    return power

def get_sum(filename):
    total = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            total += process_line_part_2(line)
    return total

print(get_sum("inp.txt"))