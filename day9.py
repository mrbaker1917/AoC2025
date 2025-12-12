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

# print(largest_area)


# part 2:
widest_row = 0
widest_row_pt = []
second_widest_row = 0
sec_widest_row_pt = []
for i, row in enumerate(data):
    if i < len(data)-2 and row[0] == data[i+1][0]:
        w = data[i+1][1]-row[1] 
        if w > widest_row:
            second_widest_row = widest_row
            sec_widest_row_pt = widest_row_pt
            widest_row = w
            widest_row_pt = [row, data[i+1]]

print(widest_row, widest_row_pt, second_widest_row, sec_widest_row_pt)
print(widest_row * (widest_row_pt[0][0]-sec_widest_row_pt[0][0]))

