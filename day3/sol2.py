def inp2matrix(filename):
    mat = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line_mat = [char for char in line.strip()]
            mat.append(line_mat)
    return mat

def list2int(list):
    return int("".join(list))

def get_if_valid_part(coord2gears, tracker, mat):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for cx, cy in tracker:
        for x, y in dirs:
            pos_x, pos_y = cx + x, cy + y
            if pos_x >= len(mat[0]) or pos_x < 0 or pos_y >= len(mat) or pos_y < 0:
                pass
            elif (pos_x, pos_y) in coord2gears.keys():
                return (pos_x, pos_y)

    return None

def process_line(mat):
    coord2gears = dict()
    tracker = []
    num = []
    total = 0

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '*':
                coord2gears[(i, j)] = []

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j].isnumeric():
                num.append(mat[i][j])
                tracker.append((i, j))
            else:
                valid_tup = get_if_valid_part(coord2gears, tracker, mat)
                if valid_tup != None:
                    coord2gears[valid_tup].append(list2int(num))
                num.clear()
                tracker.clear()

    for num_list in coord2gears.values():
        if len(num_list) == 2:
            total += num_list[0] * num_list[1]
            
    return total

print(process_line(inp2matrix('inp.txt')))