data = []

with open("day5_test_data.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

fresh_ranges = data[:data.index("")]
IDs = data[data.index("")+1:]

count = 0
def isFresh(n):
    for r in fresh_ranges:
        start, end = r.split("-")
        if int(n) >= int(start) and int(n) <= int(end):
            print(r)
            return True
    return False

# for id in IDs:
#     if isFresh(id):
#         count += 1
# print(count)

# part 2 is just how many IDs are fresh:
# print(fresh_ranges)

ranges = sorted([[int(r.split("-")[0]), int(r.split("-")[1])] for r in fresh_ranges])
print(ranges)

# Merge overlapping ranges
merged = []
for start, end in ranges:
    if not merged or merged[-1][1] < start - 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
    print(merged)
total = 0
for r in merged:
    total += (r[1] - r[0] + 1)

print(total)