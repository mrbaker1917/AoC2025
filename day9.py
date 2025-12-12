data = []
with open("day9_test_data.txt") as f:
    data = [p.strip().split(",") for p in f.readlines()]
for i, rt in enumerate(data):
    data[i] = [int(rt[1]), int(rt[0])]
data = sorted(data)
print(data)
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
h = data[-1][0]+2
w = max([i[1] for i in data])+3
grid = [["." for _ in range(w)] for _ in range(h)]

rows = {data[p][0]: [data[p-1][1],data[p][1]] for p in range(1, len(data), 2)}
print(rows)
for r, c in rows.items():
    c1 = c[0]
    c2 = c[1]
    grid[r][c1] = "#"
    grid[r][c2] = "#"
    for j in range(c1+1, c2):
        grid[r][j] = "X"

# for i, row in enumerate(grid[:-1]):
#     for j in range(len(row)-1):
#         if 




for r in grid:
    print("".join(r))