import math

data = []

with open("day8_data.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

data = [l.split(",") for l in data]

data = [[int(n) for n in l] for l in data]

# print(data)

def closeness(p1, p2):
    return round(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2), 2)

d = {}

for j in range(len(data)):
    p1 = data[j]
    l = data[:j] + data[j+1:]
    for p in l:
        dist = closeness(p1, p)
        d[dist] = [p1, p]

d_keys = sorted(d.keys())
# for k in d_keys[:10]:
#     print(k, d[k])

circuit_pairs = []

for k in d_keys:
    p1, p2 = d[k]
    p1s = "-".join(map(str, p1))
    p2s = "-".join(map(str, p2))
    circuit_pairs.append([p1s, p2s])

# print(circuit_pairs)
connections = 0
circuits = []
i = 0
while connections < 2000:
    added = False
    pair = circuit_pairs[i]
    for j in range(len(circuits)):
        if pair[0] in circuits[j] and pair[1] in circuits[j]:
            added = True
            circuit_pairs[i] = []
            connections += 1
            break
        elif pair[0] in circuits[j]:
            circuits[j].append(pair[1])
            added = True
            circuit_pairs[i] = []
            connections += 1
            break
            
        elif pair[1] in circuits[j]:
            circuits[j].append(pair[0])
            added = True
            circuit_pairs[i] = []
            connections += 1
            break
    
    if not added:   
        circuits.append(pair)
        connections += 1
    i += 1
    # print(f"connections: {connections}")

circuits = sorted(circuits, key=len, reverse=True)
print(len(circuits))
# for ci in circuits[:10]:
    # print(ci, len(ci))
total_circ = 1
for c in circuits[:3]:
    print(c, len(c))
    total_circ *= len(c)
print(total_circ)