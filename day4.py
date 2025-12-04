
data = []
with open('day4_data.txt') as f:
    data = [line.strip() for line in f.readlines()]

data = [list(l) for l in data]


# print(data)
def is_open(i, j):
    roll_count = 0
    # corner cases:
    if i == 0 and j == 0:
        return True
    elif i == 0 and j == len(data[0])-1:
        return True
    elif i == len(data)-1 and j == 0:
        return True
    elif i == len(data)-1 and j == len(data[0])-1:
        return True
    # top line cases
    elif i == 0:
        if data[i][j-1] == "@":
            roll_count += 1
        if data[i][j+1] == "@":
            roll_count += 1
        if data[i+1][j-1] == "@":
            roll_count += 1
        if data[i+1][j] == "@":
            roll_count += 1
        if data[i+1][j+1] == "@":
            roll_count += 1
        return roll_count < 4
    # first column cases:
    elif j == 0:
        if data[i-1][j] == "@":
            roll_count += 1
        if data[i-1][j+1] == "@":
            roll_count += 1
        if data[i][j+1] == "@":
            roll_count += 1
        if data[i+1][j] == "@":
            roll_count += 1
        if data[i+1][j+1] == "@":
            roll_count += 1
        return roll_count < 4
    # bottom row:
    elif i == len(data)-1:
        if data[i][j-1] == "@":
            roll_count += 1
        if data[i-1][j-1] == "@":
            roll_count += 1
        if data[i-1][j] == "@":
            roll_count += 1
        if data[i-1][j+1] == "@":
            roll_count += 1
        if data[i][j+1] == "@":
            roll_count += 1
        return roll_count < 4
    
    elif j == len(data[0])-1:
        if data[i-1][j] == "@":
            roll_count += 1
        if data[i-1][j-1] == "@":
            roll_count += 1
        if data[i][j-1] == "@":
            roll_count += 1
        if data[i+1][j-1] == "@":
            roll_count += 1
        if data[i+1][j] == "@":
            roll_count += 1
        return roll_count < 4
    # all other cases, not on edges:
    else:
        if data[i-1][j] == "@":
            roll_count += 1
        if data[i-1][j+1] == "@":
            roll_count += 1
        if data[i][j+1] == "@":
            roll_count += 1
        if data[i+1][j+1] == "@":
            roll_count += 1
        if data[i+1][j] == "@":
            roll_count += 1
        if data[i+1][j-1] == "@":
            roll_count += 1
        if data[i][j-1] == "@":
            roll_count += 1
        if data[i-1][j-1] == "@":
            roll_count += 1
        return roll_count < 4

total = 0

def remove_open_rolls(data):
    openings = 0
    global total
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "@" and is_open(i, j):
                openings += 1
                data[i][j] = "."
    total += openings
    if openings == 0:
        return data
    else:
        return remove_open_rolls(data)

remove_open_rolls(data)
print(total)