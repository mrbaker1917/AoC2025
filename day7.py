data = []

with open("day7_data.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

data = [[c for c in l] for l in data]


entry = data[0].index("S")
i = 0
while i < len(data)-1:
    r = data[i]
    for j, c in enumerate(r):
        if c == "S":
            data[i+1][j] = "|"
        if c == "|" and i != len(data)-1:
            if data[i+1][j] != "^":
                data[i+1][j] = "|"
        if c == "^":
            if data[i-1][j] == "|":
                data[i][j-1] = "|"
                data[i][j+1] = "|"
    if i == len(data)-2 and data[i][0] != "|":
        i = 1
    else:
        i += 1
if data[-1][0] != "|" and data[-2][0] == "|":
    data[-1][0] = "|"

# for r in data:
#     print("".join(r))
splits = 0
for i, r in enumerate(data):
    for k, c in enumerate(r):
        if c == "^":
            if data[i-1][k] == "|":
                splits += 1
# print(splits)

# PART THE SECOND:
# This code moves up the grid from the bottom, turning the "|" in the bottom row
# to "1"; it then moves up the grid, whenever it finds a "|" with a splitter "^"
# right below it, then it adds the numbers or 2 paths to left and right of splitter.
# It worked well, once I figured out how to get the adding to work.

for i in range(len(data)-1, 0, -1):
    for j in range(len(data[i])):
        # print(i, j)
        if i == len(data)-1:
            if data[i][j] == "|":
                data[i][j] = "1"
        if data[i][j] == "|":
            if data[i-1][j] in ["|", "."] and data[i+1][j] != "^":
                data[i][j] = data[i+1][j]
            if data[i+1][j] == "^":
                data[i][j] = str(int(data[i+1][j-1])+int(data[i+1][j+1]))

print(data[1][entry])

