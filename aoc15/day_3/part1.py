xs = list(map(lambda x: x.strip(), open('data.py', 'r')))

pos = (0, 0)
visits = [pos]
transforms = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (1, 0),
    'v': (-1, 0)
}

for x in xs[0]:
    pos = tuple(map(sum, zip(pos, transforms[x])))
    visits.append(pos)

print(len(set(visits)))
