data = []

with open("day2_data.txt", 'r') as f:
    data = f.read().split(",")

print(data)

def isInValid(s):
    if len(s) < 2:
        return False
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]
    if left == right:
        return True
    
    return False

def make_range(p):
    return list(range(int(p[0]), int(p[1]) + 1))

ranges = [make_range(p.split("-")) for p in data]


sum = 0
for r in ranges:
    for n in r:
        if isInValid(str(n)):
            sum += n
print(sum)