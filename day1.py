

data = []

with open("day1_data.txt", 'r') as f:
    data = f.read().splitlines()



d = 50

zeros  = 0

for t in data:
    if t[0] == 'L':
        d = (d - int(t[1:])) % 100
        if d == 0:
            zeros += 1
    elif t[0] == 'R':
        d = (d + int(t[1:])) % 100
        if d == 0:
            zeros += 1

print(zeros)