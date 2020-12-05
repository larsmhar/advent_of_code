xs = list(map(lambda x: x.strip(), open('data.txt', 'r')))
print(xs)

def solution(data):
    coords = (3, 1)
    right = 0
    out = 0
    for x in data:
        if x[right] == "#":
            out += 1
        right = (right + coords[0]) % 31
    return out

# 216
print(solution(xs))
