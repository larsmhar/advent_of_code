from functools import reduce


data = list(map(lambda x: int(x.strip()), open("data.txt", "r")))

def maths(x):
    total = 0
    while x / 3 - 2 > 0:
        x = int(x / 3) - 2
        total += x
        print(x)
    print(x)
    return total
print(reduce(lambda x, y : x + y, list(map(lambda x : maths(x), data))))
