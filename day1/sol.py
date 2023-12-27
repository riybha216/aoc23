def convert_str_to_digit_format(line):
    word2num = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    for key, val in word2num.items():
        line = line.replace(key, val)
    return line

def process_line(line):
    line = convert_str_to_digit_format(line)

    nums = []

    for char in line:
        if char.isnumeric():
            nums.append(char)

    if len(nums) >= 2:
        return nums[0] + nums[-1]
    elif len(nums) == 1:
        return nums[0] + nums[0]
    return 0

def get_sum(filename):
    total = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            line_sum = int(process_line(line))
            total += line_sum
    return total

print(get_sum('inp.txt'))