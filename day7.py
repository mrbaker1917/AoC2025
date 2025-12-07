data = []

with open("day7_test_data.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

data = [[c for c in l] for l in data]

print(data)

entry = data[0].index("S")
for i, r in enumerate(data):
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

for r in data:
    print(r)