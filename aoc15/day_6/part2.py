xs = list(map(lambda x: x.strip().split(' '), open('data.txt', 'r')))

mat = [[0 for i in range(1000)] for x in range(1000)]
transforms = {
    'off': -1,
    'on': 1
}

for x in xs:
    #print(x)
    if x[0] == 'turn':
        #print(x)
        coords = x[2].split(',') + x[4].split(',')
        coords = list(map(lambda x: int(x), coords))
        #print(coords)
        for xc in range(coords[0], coords[2] + 1):
            for yc in range(coords[1], coords[3] + 1):
                if mat[xc][yc] + transforms[x[1]] >= 0:
                    mat[xc][yc] += transforms[x[1]]
                #if transforms[x[1]] == -1:
                #    print(f"b{mat[xc][yc]}-{mat[xc][yc] + transforms[x[1]]}", end=",")
        pass
    elif x[0] == 'toggle':
        #print(x)
        coords = x[1].split(',') + x[3].split(',')
        coords = list(map(lambda x: int(x), coords))
        for xc in range(coords[0], coords[2] + 1):
            for yc in range(coords[1], coords[3] + 1):
                mat[xc][yc] += 2
        pass

#print(mat)

i = 0

for idx, x in enumerate(mat):
    for idy, y in enumerate(x):
        if y >= 1:
            #print(idx, idy)
            #print(mat[idx][idy])
            i += mat[idx][idy]
print(i)
