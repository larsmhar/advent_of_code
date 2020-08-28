xss = list(map(lambda x: x.strip(), open('data.txt', 'r')))

i = 0

for xs in xss:
    last_letter = ""
    second_last_letter = ""
    third_last_letter = ""
    pairs = []
    pair, good_string = False, False
    for x in xs:
        #print(f"Second: {second_last_letter}, last: {last_letter}, curr: {x}")
        if last_letter + x != second_last_letter + last_letter:
            if last_letter + x in pairs:
                pair = True
            pairs.append(last_letter+x)
        if last_letter + x == third_last_letter + second_last_letter:
            pair = True

        if second_last_letter == x:
            good_string = True

        third_last_letter = second_last_letter
        second_last_letter = last_letter
        last_letter = x

    if pair and good_string:
        i += 1


        

print(i)
