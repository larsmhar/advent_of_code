xs = list(map(lambda x: x.strip(), open('data.py', 'r')))

pos = [(0,0), (0, 0)]
visits = [pos[0]]
transforms = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (1, 0),
    'v': (-1, 0)
}

for idx, x in enumerate(xs[0]):
    santa = idx % 2
    pos[santa] = tuple(map(sum, zip(pos[santa], transforms[x])))
    visits.append(pos[santa])

print(len(set(visits)))
