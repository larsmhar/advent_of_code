data = [[x.strip() for x in xs] for xs in list(map(lambda x: x.split(","), open("data.txt", "r")))]
print(data)

conversions = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1],
}

def get_coords(data):
    coords = [set(), set()]
    for i, line_data in enumerate(data):
        x, y = 0, 0
        for datum in line_data: 
            move = list(int(datum[1:]) * x for x in conversions[datum[0]])
            #print(datum, i, move)
            #print(x, y)
            #print("this thing", (list(map(lambda x, y: x + y, conversions[datum[0]], [x, y]))))
            # Original (smart?) idea
            #print(list(map(lambda x, y: x + y, move, [-10, -10])))
            for step in range(max([abs(x) for x in move])):
                #print(x, y, conversions[datum[0]])
                x, y = (tuple(list(map(lambda x, y: x + y, conversions[datum[0]], [x, y]))))
                #print(x, y, conversions[datum[0]])
                coords[i].add(tuple(list([x, y])))
            """
            print(coords)
            b = set()
            b.add(tuple([1003, 0]))
            print(coords & b)
            """
    return coords[0] & coords[1]
        #print(list(map(lambda x, y: x + y, move, [-10, -10])))
        #for _ in range(int(datum[1:])):


def manhattan_distance(data):
    return abs(data[0]) + abs(data[1])

clashes = get_coords(data)
print(clashes)
print("here")
distances = []

for coords in clashes:
    print(coords)
    distances.append(manhattan_distance(coords))

print(min(distances)) # 1024
