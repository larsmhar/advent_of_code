from collections import defaultdict

xs = list(map(lambda x: x.split(), open('data.txt', 'r')))


def check(datum):
    mini, maxi = datum[0].split("-")
    letter = datum[1][0]
    password = datum[2]
    l_num = password.count(letter)
    return True if (password[int(mini)-1] == letter) ^ (password[int(maxi)-1] == letter) else False


def solution(data):
    val = 0
    for x in data:
        val += check(x)
    return val


# 388
print(solution(xs))
