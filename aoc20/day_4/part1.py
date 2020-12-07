from collections import defaultdict

class Passport:
    def __init__(self):
        self.pass_data = {
            "byr": None,
            "iyr": None,
            "eyr": None,
            "hgt": None,
            "hcl": None,
            "ecl": None,
            "pid": None
        } 
        #defaultdict(lambda: None)

    def valid(self):
        """
        return self.pass_data["byr"] is not None and \
            self.pass_data["iyr"] is not None and \
            self.pass_data["eyr"] is not None and \
            self.pass_data["hgt"] is not None and \
            self.pass_data["hcl"] is not None and \
            self.pass_data["ecl"] is not None and \
            self.pass_data["pid"] is not None  

        """
        return self.pass_data["byr"] is not None and \
            self.pass_data["iyr"] is not None and \
            self.pass_data["eyr"] is not None and \
            self.pass_data["hgt"] is not None and \
            self.pass_data["hcl"] is not None and \
            self.pass_data["ecl"] is not None and \
            self.pass_data["pid"] is not None  

    def add(self, x):
        field = x[:3]
        field_data = x[3:]
        self.pass_data[field] = field_data

out = 0
passport = Passport()
for line in open('data.txt', 'r'):
    data = line.split(" ")
    for datum in data:
        passport.add(datum)

    if line == "\n":
        if passport.valid():
            out += 1
        passport = Passport()

# The last passport is not checked by the loop
if passport.valid():
    out += 1

# 254
print(out)
