from functools import reduce


data = [[x.strip() for x in xs] for xs in list(map(lambda x: x.split(","), open("data.txt", "r")))]
#data = [[x.strip() for x in xs] for xs in list(map(lambda x: x.split(","), open("testdata1.txt", "r")))]
#data = [[x.strip() for x in xs] for xs in list(map(lambda x: x.split(","), open("testdata2.txt", "r")))]


conversions = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1],
}

def get_coords(data, ends = None):
    coords = [set(), set()]
    minimums = [[],[]]
    return_minimums = True if ends else False
    if ends:
        ends_copy = ends
    for i, line_data in enumerate(data):
        x, y = 0, 0
        print(i)
        if return_minimums:
            ends = ends_copy
        for datum in line_data: 
            move = list(int(datum[1:]) * x for x in conversions[datum[0]])
            # Original (smart?) idea
            #print(list(map(lambda x, y: x + y, move, [-10, -10])))
            for step in range(max([abs(x) for x in move])):
                if ends and ends & coords[i]:
                    intersect = ends.intersection(coords[i])
                    #minimums.append(ends.intersection(coords[i]))
                    minimums[i].append(len(coords[i]))
                    #print(ends.intersection(coords[i]))
                    #print(len(coords[i]))
                    ends = ends - coords[i]
                x, y = (tuple(list(map(lambda x, y: x + y, conversions[datum[0]], [x, y]))))
                coords[i].add(tuple(list([x, y])))
    if return_minimums:
        return_vals = [0 for i in range(len(minimums[0]))]
        for xs in minimums:
            for i, x in enumerate(xs):
                return_vals[i] += x
    return return_vals if return_minimums else coords[0] & coords[1]


clashes = get_coords(data)
#distances = []
#for coords in clashes:
    #distances.append((manhattan_distance(coords), coords))

#minimum =(reduce(lambda minimum, x: x if (x[0] < minimum[0]) else minimum, distances))
#print("Minimum", minimum[0]) # 245
print("part 1: ", min(abs(x) + abs(y) for (x, y) in clashes))
minimums = get_coords(data, clashes)

#print(minimums)
#print(minimums.sort())
#print(minimums)
        

