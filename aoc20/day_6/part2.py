from collections import defaultdict
xs = list(map(lambda x: x.strip(), open("data.txt", "r")))

curr = defaultdict(lambda: 0)
total = 0
length = 0
for x in xs:
    line = []
    if x == "":
        for i in curr.keys():
            if curr[i] == length:
                total += 1
        curr = defaultdict(lambda: 0)
        length = 0
    else:
        length += 1
        for i in x:
            # Bad naming practice >:(
            for y in i:
               curr[y] += 1

for i in curr.keys():
    if curr[i] == length:
        total += 1

# 3489
print(total)

