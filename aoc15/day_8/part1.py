xs = list(map(lambda x: fr"{x.strip()}", open('data.txt', 'r')))

#print(xs)

total = 0
minus = 0

#xs = ["", "abc", 'aaa\\"aaa', fr"\x70"]
#xs = ["abc"]
#xs = ['aaa\\"aaa']
#xs = [fr"\x70"]
for x in xs:
    total += 2 + len(x)
    idx = 0
    while idx < len(x):
        i = x[idx]
        if i == "\\":
            if x[idx + 1] == "x":
                minus += 1
                idx += 4
            elif x[idx + 1] == "\\" or x[idx + 1] == '"':
                idx += 2
                minus += 1
        else:
            idx += 1
            minus += 1
            
    
print(total, minus, total - minus)
