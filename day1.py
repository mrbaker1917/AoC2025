

data = []

with open("day1_data.txt", 'r') as f:
    data = f.read().splitlines()

# d = 50

# zeros  = 0

# for t in data:
#     if t[0] == 'L':
#         d = (d - int(t[1:])) % 100
#         if d == 0:
#             zeros += 1
#     elif t[0] == 'R':
#         d = (d + int(t[1:])) % 100
#         if d == 0:
#             zeros += 1

# print(zeros)

# for part 2 we need to count each time we pass 0, even in the middle of dialing:
d = 50
zeros  = 0
for t in data:
    if t[0] == 'L':
        steps = int(t[1:])
        for _ in range(steps):
            d = (d - 1) % 100
            if d == 0:
                zeros += 1
    elif t[0] == 'R':
        steps = int(t[1:])
        for _ in range(steps):
            d = (d + 1) % 100
            if d == 0:
                zeros += 1

print(zeros)