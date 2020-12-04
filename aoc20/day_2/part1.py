from collections import defaultdict

xs = list(map(lambda x: x.split(), open('data.txt', 'r')))


def check(datum):
    mini, maxi = datum[0].split("-")
    letter = datum[1][0]
    password = datum[2]
    l_num = password.count(letter)
    return True if int(mini) <= l_num and l_num <= int(maxi) else False


def solution(data):
    val = 0
    for x in data:
        # True == 1, so int + True = int + 1...
        val += check(x)
    return val

# 643
print(solution(xs))
