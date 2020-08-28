xss = list(map(lambda x: x.strip(), open('data.txt', 'r')))

i = 0
VOWELS = "aeiou"
bad_substrings = ['ab', 'cd', 'pq', 'xy']

for xs in xss:
    last_letter = ""
    vows = []
    twice, good_string= False, True
    for x in xs:
        # Keeps track of vowels encountered
        if x in VOWELS:
            vows.append(x)
        # Letter happening twice in a row
        if last_letter == x:
            twice = True
        # Checks for bad substrings
        if last_letter + x in bad_substrings:
            good_string = False
            
        last_letter = x

        
    if len(vows) > 2 and twice and good_string:
        i += 1

    

print(i)
