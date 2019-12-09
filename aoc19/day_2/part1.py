data = list(map(lambda x : int(x), list(map(lambda x: x.split(','), open("data.txt", "r")))[0]))

memory = {}
def intCodeCompute(data):
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            continue
        if data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            continue
        break
    return data


print(intCodeCompute(data[:]))


### Part 2
for noun in range(100):
    for verb in range(100):
        data2 = data[:]
        data2[1] = noun
        data2[2] = verb
        data2 = intCodeCompute(data2)
        if data2[0] == 19690720:
            print(f"Answer is {100*noun + verb}")
            break
