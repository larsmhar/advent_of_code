xs = list(open('data.txt', 'r'))[0]

i = 0
moves = {'(': 1, ')': -1}

for idx, x in enumerate(xs):
    #Check because there is trailing whitespace
    if x in moves.keys():
        i += moves[x]
    if i < 0:
        print(idx + 1)
        break
