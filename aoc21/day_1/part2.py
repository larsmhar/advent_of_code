data = list(map(lambda x: int(x), open('data.txt', 'r')))



# First input is 700ish
# but like this should just be inifity
last_datum_sum = 3 * 1000
inc = 0

for i in range(0, len(data) - 2):
    datum_sum = data[i] + data[i + 1] + data[i + 2]
    if datum_sum > last_datum_sum:
        inc += 1
    last_datum_sum = datum_sum

print(f"There were {inc} increases")
