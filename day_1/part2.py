values = set()
value = 0

data = list(map(lambda x: int(x.strip()), open("data.txt", "r")))

duplicate_not_found = True
while duplicate_not_found == True:
    for datum in data:
        value += datum
        if value in values:
            print(value) # 709
            duplicate_not_found = False
            break
        values.add(value)
