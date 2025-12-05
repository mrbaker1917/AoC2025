data = []

with open("day5_data.txt", "r") as f:
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

for id in IDs:
    if isFresh(id):
        count += 1
print(count)