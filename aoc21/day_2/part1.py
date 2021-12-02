data = list(map(lambda x: x.split(), open('data.txt', 'r')))

depth = 0
horizontal = 0

for action, i in data:
    # If I had a newer version I coul
    # use that cool matching here
    if action in ('forward'):
        horizontal += int(i)
    else:
        if action in 'up':
            i = -int(i)
        depth += int(i)
        

print(f"Answer is {depth * horizontal}")
