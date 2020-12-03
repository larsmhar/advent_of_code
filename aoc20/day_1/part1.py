data = sorted(list(map(lambda x: int(x.strip()), open('data.txt', 'r'))))


def solution(data):
    for idx, x in enumerate(data):
        for idy in range(len(data[idx:])):
            y = data[idy + idx]
            test = x + y
            if test == 2020:
                return x * y
            elif test > 2020:
                break
            

# 974304
print(solution(data))
