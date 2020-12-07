from collections import defaultdict
import re

class Passport:
    def __init__(self):
        self.pass_data = defaultdict(lambda: None)

    def valid(self):
        return self.pass_data["byr"] is not None and \
            self.pass_data["iyr"] is not None and \
            self.pass_data["eyr"] is not None and \
            self.pass_data["hgt"] is not None and \
            self.pass_data["hcl"] is not None and \
            self.pass_data["ecl"] is not None and \
            self.pass_data["pid"] is not None  

    def __repr__(self):
        return str(self.pass_data)

    def add(self, x):
        field = x[:3]
        field_data = x[4:].strip()
        if field == "byr":
            if field_data.isnumeric() and int(field_data) >= 1920 and int(field_data) <= 2002:
                self.pass_data[field] = field_data
        if field == "iyr":
            if field_data.isnumeric() and int(field_data) >= 2010 and int(field_data) <= 2020:
                self.pass_data[field] = field_data
        if field == "eyr":
            if field_data.isnumeric() and int(field_data) >= 2020 and int(field_data) <= 2030:
                self.pass_data[field] = field_data
        if field == "hgt":
            if (field_data[:3].isnumeric() and field_data[3:] == "cm" and int(field_data[:3]) >= 150 and int(field_data[:3]) <= 193) or (field_data[:2].isnumeric() and field_data[2:] == "in"  and int(field_data[:2]) >= 59 and int(field_data[:2]) <= 76):
                self.pass_data[field] = field_data
        if field == "hcl":
            p = re.compile("^#[a-f0-9]{6}$")
            if p.match(field_data):
                self.pass_data[field] = field_data
        if field == "ecl":
            if field_data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                self.pass_data[field] = field_data
        if field == "pid":
            p = re.compile("^[0-9]{9}$")
            if p.match(field_data):
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

# not 184
print(out)
