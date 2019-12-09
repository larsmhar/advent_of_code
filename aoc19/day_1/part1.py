from functools import reduce


data = list(map(lambda x: int(x.strip()), open("data.txt", "r")))
print(reduce(lambda x, y: x + y, (list(map(lambda x: int(x / 3) - 2, data)))))

