xs = list(map(lambda x: x.strip(), open('data.txt', 'r')))

values = {}

# Input value for a from part 1
xs[3] = "3176 -> b"

for idx, x in enumerate(xs):
    data = x.split(' ')
    did = False
    """
        Direct
        NOT
        OR
        XOR
        LSHIFT
        RSHIFT
    """
    if data[0].isdigit():
        # Direct assigment
        if len(data) == 3:
            #print("direct", data)
            values[data[2]] = int(data[0])
            did = True
        # And with number
        elif data[2] in values:
            #print("num add", data)
            values[data[4]] = int(data[0]) & int(values[data[2]])
            did = True
            
    elif data[0] in ("NOT"):
        # NOT
        if data[1] in values:
            #print("not", data)
            values[data[3]] = (1 << 16) - 1 - int(values[data[1]])
            did = True

    else:
        if data[0] in values:
            # Direct assigment
            if len(data) == 3 and data[0] in values:
                #print("direct", data)
                values[data[2]] = values[data[0]]
                did = True
            # RSHIFT
            if data[1] in ("RSHIFT"):
                #print("RSHIFT", data)
                values[data[4]] = int(values[data[0]]) >> int(data[2])
                did = True
            #LSHIFT
            if data[1] in ("LSHIFT"):
                #print("LSHIFT", data)
                values[data[4]] = int(values[data[0]]) << int(data[2])
                did = True
            if data[2] in values:
                # AND
                if data[1] in ("AND"):
                    #print("normal AND", data)
                    values[data[4]] = int(values[data[0]]) & int(values[data[2]])
                    did = True
                # OR
                if data[1] in ("OR"):
                    #print("OR", data)
                    values[data[4]] = int(values[data[0]]) | int(values[data[2]])
                    did = True
    if not did:
        xs.append(x)

print(values["a"])
