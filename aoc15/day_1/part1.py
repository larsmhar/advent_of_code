xs = list(open('data.txt', 'r'))[0]

i = 0
moves = {'(': 1, ')': -1}

for x in xs:
    #Check because there is trailing whitespace
    if x in moves.keys():
        i += moves[x]

print(i)
