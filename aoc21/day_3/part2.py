from functools import reduce


def count_ones_index(arr, index):
    return reduce(lambda x, y: x + 1 if y == "1" else x ,map(lambda x: x[index], arr), 0)

data = list(map(lambda x: x.strip(), open('data.txt', 'r')))
#data = list(map(lambda x: x.strip(), open('test.txt', 'r')))

low = []
high = []
# This is beutiful
#ones_occurances_high = list(1 if x >= len(data) / 2 else 0 for x in list(count_ones_index(data, i) for i in range(len(data[0]))))

print(count_ones_index(data, 0))

ones_occurances_high = [1 if count_ones_index(data, 0) >= len(data) / 2 else 0]
high = list(filter(lambda x: int(x[0]) == ones_occurances_high[0], data))

ones_occurances_low = [1 ^ ones_occurances_high[0]]
low = list(filter(lambda x: int(x[0]) == ones_occurances_low[0], data))

print(len(high), len(low))
print(ones_occurances_high)
print(ones_occurances_low)

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

out_high = data.copy()
out_low = data.copy()
old_high_out = out_high.copy()
old_low_out = out_low.copy()

for i, ones in enumerate(ones_occurances_high):
    out_high = []
    for datum in old_high_out:
        if len(old_high_out) == 1:
            out_high = old_high_out
            break
        if ones == int(datum[i]):
            out_high.append(datum)
    old_high_out = out_high.copy()

for i, ones in enumerate(ones_occurances_low):
    out_low= []
    for datum in old_low_out:
        if len(old_low_out) == 1:
            out_low = old_low_out
            break
        if ones == int(datum[i]):
            out_low.append(datum)
    old_low_out = out_low.copy()

# 7022988 too low
# 7041258
print(int(high[0], 2) * int(low[0], 2))
print(high[0], low[0])
# Wrong
print(old_high_out, old_low_out)
print(int(old_high_out[0], 2) * int(old_low_out[0], 2))
print("occurance high", ones_occurances_high)
print("occurance low", ones_occurances_low)
#print(f"Gamma times epsilon is equal to {int(gamma, 2) * int(epsilon, 2)}")
