from functools import reduce

print(reduce(lambda x, prev: int(prev) + int(x), open("data.txt", "r")))
