data = [[x.strip() for x in xs] for xs in list(map(lambda x: x.split(","), open("data.txt", "r")))]
#data = [[x.strip() for x in xs] for xs in list(map(lambda x: x.split(","), open("testdata1.txt", "r")))]
#data = [[x.strip() for x in xs] for xs in list(map(lambda x: x.split(","), open("testdata2.txt", "r")))]

conversions = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1],
}

def get_coords(data):
    coords = [[], []]
    for i, line_data in enumerate(data):
        x, y = 0, 0
        for datum in line_data: 
            move = list(int(datum[1:]) * x for x in conversions[datum[0]])
            # Original (smart?) idea
            #print(list(map(lambda x, y: x + y, move, [-10, -10])))
            for step in range(max([abs(x) for x in move])):
                x, y = (tuple(list(map(lambda x, y: x + y, conversions[datum[0]], [x, y]))))
                coords[i].append(tuple(list([x, y])))
    # Only one return value, please
    return coords

wires = get_coords(data)
intersections = set(wires[0]) & set(wires[1])
print("part 1: ", min(abs(x) + abs(y) for (x, y) in intersections))
# Sets can't be indexed, but can be foreached through
# Can make most of this into one line. Maybe later
distances = []
for intersection in intersections:
    # Need to add 2 because (0,0) isn't counted by any of them, and
    # moving from (0,0) takes 1 move
    distances.append(2 + sum(wire.index(intersection) for wire in wires))
print("print 2: ", min(distances))
