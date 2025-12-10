data = []
with open("day9_data.txt") as f:
    data = [p.strip().split(",") for p in f.readlines()]
for i, rt in enumerate(data):
    data[i] = [int(rt[1]), int(rt[0])]
data = sorted(data)

def area_rect(p1, p2):
    h = abs(p2[0]-p1[0])+1
    w = abs(p2[1]-p1[1])+1
    return h * w

largest_area = 0
for p1 in data:
    for p2 in data:
        area = area_rect(p1, p2)
        if area > largest_area:
            largest_area = area

print(largest_area)