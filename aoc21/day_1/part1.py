data = list(map(lambda x: int(x), open('data.txt', 'r')))



# First input is 700ish
# but like this should just be inifity
last_datum = 1000
inc = 0

for datum in data:
    if datum > last_datum:
        inc += 1
    last_datum = datum

print(f"There were {inc} increases")
