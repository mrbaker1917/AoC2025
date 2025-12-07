data = []
with open("day6_data.txt") as f:
    for line in f.readlines():
        if "\n" in line:
            line = line.replace("\n", "")
            data.append(line)
        else:
            data.append(line)

new_data = []
ops = []
for i in range(len(data[0])-1, -1, -1):
    n = ""
    for row in data:
        if "+" in row[i]:
            ops.append("+")
        elif "*" in row[i]:
            ops.append("*")
        else:
            n += row[i]
    new_data.append(n.strip())    
print(new_data)
print(ops)

new_nums = []
temp = []
for t in new_data:
    if t == '':
        new_nums.append(temp)
        temp = []
    elif t == new_data[-1]:
        temp.append(t)
        new_nums.append(temp)
        temp = []
    else:
        temp.append(t)
print(new_nums)

# print(new_data)
# for r in data:
#     t = []
#     for e in r:
#         if e != '':
#             t.append(e)
#     new_data.append(t)
# # print(new_data)
# turned_data = []

# # for i in range(len(new_data[0])):
# #     t = []
# #     for r in new_data:
# #         t.append(r[i])
# #     turned_data.append(t)

total = 0
for j in range(len(ops)):
    op = ops[j]
    s = ''
    for e in new_nums[j]:
        s += e+op
    total += eval(s[:-1])
print(total)