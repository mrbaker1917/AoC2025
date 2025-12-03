data = []

with open("day3_data.txt", 'r') as f:
    data = f.read().splitlines()

# for each string of digits, find the two highest digits in consecutive order:

def find_highest(s):
    for i in range(9, -1, -1):
        if s.find(str(i)) != -1:
            return i, s.find(str(i))

def find_second_highest(s, highest, index):
    if index != len(s)-1:
        for j in range(9, -1, -1):
            rest = s[index+1:]
            if rest.find(str(j)) != -1:
                return j, (rest.find(str(j)) + index+1)
    else:
        for j in range(highest-1, -1, -1):
            if s.find(str(j)) != -1:
                return j, s.find(str(j))

def find_two_highest(s):
    highest, h_index = find_highest(s)
    second, s_index = find_second_highest(s, highest, h_index)
    # print(f"highest: {highest}, h_index: {h_index}")
    # print(f"second: {second}, s_index: {s_index}")
    if h_index < s_index:
        n = highest * 10 + second
        return n
    else:
        n = second * 10 + highest
        return n

sum = 0

# for r, s in enumerate(data):
#     two_highest = find_two_highest(s)
#     # print(r, two_highest)
#     sum += find_two_highest(s)


def find_12_largest(s):
    while len(s) > 12:
        # Find the leftmost position where s[i] < s[i+1]
        removed = False
        for i in range(len(s) - 1):
            if s[i] < s[i + 1]:
                s = s[:i] + s[i+1:]
                removed = True
                break
        # If no such position exists, remove the last digit
        if not removed:
            s = s[:-1]
    return s


new_data = data
for i, r in enumerate(new_data):
    new_s = find_12_largest(r)
    sum += int(new_s)

print(sum)