data = []

with open("day2_data.txt", 'r') as f:
    data = f.read().split(",")

def isInValid(s):
    if len(s) < 2:
        return False
    if len(s) == 2:
        if s[0] == s[1]:
            return True
    if len(s) == 3:
        if s[0] == s[1] and s[1] == s[2]:
            return True
    if len(s) == 4:
        if s[0] == s[1] == s[2] == s[3]:
            return True
        if s[0:2] == s[2:4]:
            return True
    if len(s) == 5:
        if s[0] == s[1] == s[2] == s[3] == s[4]:
            return True
    if len(s) == 6:
        if s[0] == s[1] == s[2] == s[3] == s[4] == s[5]:
            return True
        if s[0:3] == s[3:6]:
            return True
        if s[0:2] == s[2:4] == s[4:]:
            return True
    if len(s) == 7:
        if s[0] == s[1] == s[2] == s[3] == s[4] == s[5] == s[6]:
            return True
    if len(s) == 8:
        if s[0:4] == s[4:8]:
            return True
        if s[0:2] == s[2:4] == s[4:6] == s[6:8]:
            return True
        if s[0] == s[1] == s[2] == s[3] == s[4] == s[5] == s[6] == s[7]:
            return True
    if len(s) == 9:
        if s[0:3] == s[3:6] == s[6:9]:
            return True
        if s[0] == s[1] == s[2] == s[3] == s[4] == s[5] == s[6] == s[7] == s[8]:
            return True
    if len(s) == 10:
        if s[0:5] == s[5:10]:
            return True
        if s[0:2] == s[2:4] == s[4:6] == s[6:8] == s[8:10]:
            return True
        if s[0] == s[1] == s[2] == s[3] == s[4] == s[5] == s[6] == s[7] == s[8] == s[9]:
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