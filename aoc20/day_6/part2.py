from collections import defaultdict
xs = list(map(lambda x: x.strip(), open("data.txt", "r")))

curr = defaultdict(lambda: 0)
total = 0
length = 0
for x in xs:
    if x == "":
        for i in curr.keys():
            if curr[i] == length:
                total += curr[i]
        curr = defaultdict(lambda x: x)
    else:
        for i in x:
            length += 1
            print(curr)
            print(f"i {i}")
            # Bad naming practice >:(
            for y in i:
                curr[y] += 1
                if curr !== {}:
                    print("No")

total += len(curr)
# 6768
print(total)

