from functools import reduce


def count_ones_index(arr, index):
    return reduce(lambda x, y: x + 1 if y == "1" else x ,map(lambda x: x[index], arr), 0)

data = list(map(lambda x: x.strip(), open('data.txt', 'r')))

ones_occurances_high = [1 if count_ones_index(data, 0) >= len(data) / 2 else 0]
high = list(filter(lambda x: int(x[0]) == ones_occurances_high[0], data))

ones_occurances_low = [1 ^ ones_occurances_high[0]]
low = list(filter(lambda x: int(x[0]) == ones_occurances_low[0], data))

for i in range(1, len(data[0])):
    ones_occurances_high.append(1 if count_ones_index(high, i) >= len(high) / 2 else 0)
    for i in range(len(ones_occurances_high)):
        if len(high) == 1:
            break
        high = list(filter(lambda x: int(x[i]) == ones_occurances_high[i], high))
    ones_occurances_low.append(0 if count_ones_index(low, i) >= len(low) / 2 else 1)
    for i in range(len(ones_occurances_low)):
        if len(low) == 1:
            break
        low = list(filter(lambda x: int(x[i]) == ones_occurances_low[i], low))

# 7041258
print(f"Answer is equal to {int(high[0], 2) * int(low[0], 2)}")
