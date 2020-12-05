xs = list(map(lambda x: x.strip(), open('data.txt', 'r')))
print(xs)

def solution(data, coords = (3, 1)):
    right = 0
    down = 0
    out = 0
    print(0, len(data), coords[1])
    for x in range(0, len(data), coords[1]):
        if data[x][right] == "#":
            out += 1
        right = (right + coords[0]) % 31
        down += 1
    return out


checks = [(1,1), (3,1), (5,1), (7,1), (1,2)]
out = 1
for check in checks:
    out = out * solution(xs, check)

# 6708199680
print(out)
