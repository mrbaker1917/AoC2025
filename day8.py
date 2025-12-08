data = []

with open("day8_test_data.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

data = [l.split(",") for l in data]

data = [[int(n) for n in l] for l in data]

print(data)

def closeness(p1, p2):
    total_distance = 0
    for i in range(3):
        total_distance += abs(p1[i] - p2[i])
    return total_distance

for j in range(1, len(data)):
    print(closeness(data[j-1], data[j]))

