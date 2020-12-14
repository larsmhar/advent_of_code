xs = list(map(lambda x: x.strip(), open("data.txt", "r")))

curr = set()
total = 0
for x in xs:
    if x == "":
        total += len(curr)
        curr = set()
    else:
        for i in x:
            curr.add(i)
6768
total += len(curr)
# 6768
print(total)

