data = sorted(list(map(lambda x: int(x.strip()), open('data.txt', 'r'))))


def solution(data):
    for idx, x in enumerate(data):
        for idy in range(len(data[idx:])):
            for idz in range(len(data[idx + idy:])):
                y = data[idy + idx]
                z = data[idy + idx + idz]
                test = x + y + z
                if test == 2020:
                    return x * y * z
                elif test > 2020:
                    break
            

# 974304
print(solution(data))
