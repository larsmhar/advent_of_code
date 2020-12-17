data = list(map(lambda x: x.strip(), open("data.txt", "r")))
data = list(map(lambda x: x.strip(), open("input2.txt", "r")))
print(data)

lines = set()
last_lines = set()
line_num = 0
last_acc = 0
acc = 0
checked = set()
check = ""

while True:
    if line_num in lines:
        #print(acc)
        print("Error", line_num)
        checked.add(check)
        line_num = last_line_num
        lines = last_lines
        acc = last_acc
    elif line_num >= len(data):
        print("Reached end:", acc)
        break
    line = data[line_num]
    #print(lines, line_num)
    last_line_num = line_num
    lines.add(line_num)
    if line[0] == "n":
        if line_num not in checked:
            check = line_num
            last_acc = acc
            last_lines = lines
            checked.add(line_num)
            if line.find("-") != -1:
                line_num += int(line[line.find("-"):])
            else:
                line_num += int(line[line.find("+"):])
        else:
            line_num += 1
    elif line[0] == "a":
        line_num += 1
        if line.find("-") != -1:
            acc += int(line[line.find("-"):])
        else:
            acc += int(line[line.find("+"):])
    elif line[0] == "j":
        if line_num not in checked:
            print("chekding jump")
            print(acc)
            last_acc = acc
            last_lines = lines
            check = line_num
            checked.add(line_num)
            line_num += 1
        elif line.find("-") != -1:
            print(line_num)
            line_num += int(line[line.find("-"):])
            print(line_num)
        else:
            print(line_num)
            line_num += int(line[line.find("+"):])
            print(line_num)
    print(line)
    print(checked)
print(checked)
