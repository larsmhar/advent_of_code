xs = list(map(lambda x: fr"{x.strip()}", open('data.txt', 'r')))

#print(xs)

total = 0
new_encode = 0

#xs = ["", "abc", 'aaa\\"aaa', fr"\x70"]
#xs = ["abc"]
#xs = ['aaa\\"aaa']
#xs = [fr"\x70"]
for x in xs:
    total += 2 + len(x)
    idx = 0
    new_encode += 6
    while idx < len(x):
        i = x[idx]
        if i == "\\":
            if x[idx + 1] == "x":
                new_encode += 5
                idx += 4
            elif x[idx + 1] == "\\" or x[idx + 1] == '"':
                idx += 2
                new_encode += 4
        else:
            idx += 1
            new_encode += 1
            
    
print(total, new_encode, new_encode - total)
