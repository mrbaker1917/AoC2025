data = []

with open("day7_test_data.txt", "r") as f:
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

for r in data:
    print(r)
splits = 0
for i, r in enumerate(data):
    for k, c in enumerate(r):
        if c == "^":
            if data[i-1][k] == "|":
                splits += 1
# print(splits)

# part 2:
paths = 0
for i, r in enumerate(data):
    for j, c in enumerate(r):
        if c == "|":
            paths += 1
print(paths)  # +1 for the starting point