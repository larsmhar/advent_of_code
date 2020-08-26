data = list(map(lambda x : int(x), list(map(lambda x: x.split(','), open("data.txt", "r")))[0]))
initial_input = list(map(lambda x : int(x), list(map(lambda x: x.split(','), open("input.txt", "r")))[0]))[0]

memory = {}
def intCodeCompute(data, inp = 0):
    i = 0
    while i < len(data):
        print(data[i])
        if data[i] == 1:
            # Addition
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
            i += 4
            continue
        if data[i] == 2:
            # Mutiplication
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
            i += 4
            continue
        if data[i] == 3:
            # Input saved to the position in its paramater
            data[data[i+1]] = inp
            i += 2
            continue
        if data[i] == 4:
            # Output saved to the position in its paramater
            print(data[i+1])
            i += 2
            continue
        break
    return data


print(f"Answer to part 1: {intCodeCompute(data[:], initial_input)[0]}")
