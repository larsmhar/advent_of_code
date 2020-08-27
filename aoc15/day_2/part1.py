xss = list(map(lambda x: x, list(map(lambda x: x.strip().split('x'), open('data.txt', 'r')))))

i = 0
for xs in xss:
    # This looks yucky
    i += 2 * int(xs[0]) * int(xs[1]) +  2 * int(xs[1]) * int(xs[2]) + 2 * int(xs[0]) * int(xs[2]) + (min(int(xs[0]) * int(xs[1]), int(xs[1]) * int(xs[2]), int(xs[0]) * int(xs[2])))

print(i)
