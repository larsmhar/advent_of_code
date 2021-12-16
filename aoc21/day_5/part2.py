data = list(map(lambda x: list(map(lambda y: y.split(","), x.strip().split(" -> "))), open("data.txt", "r")))

# This would be easier with numpy
arr = [[0 for i in range(1000)] for _ in range(1000)]


for ite, datum in enumerate(data):
    x_1 = int(datum[0][0])
    y_1 = int(datum[0][1])
    x_2 = int(datum[1][0])
    y_2 = int(datum[1][1])
    if x_1 == x_2:
        for i in range(min(y_1, y_2), max(y_1, y_2) + 1):
            arr[i][x_1] += 1
    elif y_1 == y_2:
        for i in range(min(x_1, x_2), max(x_1, x_2) + 1):
            arr[y_1][i] += 1
    else:
        if y_1 < y_2:
            for x, i in enumerate(range(y_1, y_2 + 1)):
                if x_1 < x_2:
                    arr[i][x_1 + x] += 1
                else:
                    arr[i][x_1 - x] += 1
        else:
            for x, i in enumerate(range(y_2, y_1 + 1)):
                if x_1 < x_2:
                    arr[i][x_2 - x] += 1
                else:
                    arr[i][x_2 + x] += 1
out = 0

for y in arr:
    for x in y:
        if x > 1:
            out += 1
# 21051 too high
print(out)
