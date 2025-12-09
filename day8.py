import math

data = []

with open("day8_test_data.txt", "r") as f:
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

for k in d_keys[:20]:
    p1, p2 = d[k]
    p1s = "-".join(map(str, p1))
    p2s = "-".join(map(str, p2))
    circuit_pairs.append([p1s, p2s])

print(circuit_pairs)
added = False
circuits = [circuit_pairs[0]]
for i, pair in enumerate(circuit_pairs[1:]):
    for j in range(len(circuits)):
        if pair[0] in circuits[j] and pair[1] in circuits[j]:
            added = True
            circuit_pairs.pop(i)
            break
        elif pair[0] in circuits[j]:
            circuits[j].append(pair[1])
            added = True
            circuit_pairs.pop(i)
            break
            
        elif pair[1] in circuits[j]:
            circuits[j].append(pair[0])
            added = True
            circuit_pairs.pop(i)
            break
        print(f"circuit_pairs: {circuit_pairs}")
    if not added:   
        circuits.append(pair)

print(f"circuits: {circuits}")