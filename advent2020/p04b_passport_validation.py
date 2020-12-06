import re

class Passport():
    def __init__(self, data):
        self.data = {}
        self.data["byr"] = [x.split(":")[1] for x in data if keys[0] in x]
        self.data["iyr"] = [x.split(":")[1] for x in data if keys[1] in x]
        self.data["eyr"] = [x.split(":")[1] for x in data if keys[2] in x]
        self.data["hgt"] = [x.split(":")[1] for x in data if keys[3] in x]
        self.data["hcl"] = [x.split(":")[1] for x in data if keys[4] in x]
        self.data["ecl"] = [x.split(":")[1] for x in data if keys[5] in x]
        self.data["pid"] = [x.split(":")[1] for x in data if keys[6] in x]
        # self.data["cid"] = [x.split(":")[1] for x in data if keys[7] in x]

    def valid(self):
        help = 0
        for d in self.data.values() :
            if d != [] :
                help += 1

        return help >= 7

    def validation_data(self) :
        help = 0
        if self.valid() :
            if 1920 <= int(self.data["byr"][0]) <= 2002 :
                help += 1
            if 2010 <= int(self.data["iyr"][0]) <= 2020 :
                help += 1
            if 2020 <= int(self.data["eyr"][0]) <= 2030 :
                help += 1
            if "in" in self.data["hgt"][0] or "cm" in self.data["hgt"][0] :
                if "cm" in self.data["hgt"][0] and 150 <= int(self.data["hgt"][0].replace("cm", "")) <= 193 :
                    help += 1   
                if "in" in self.data["hgt"][0] and 59 <= int(self.data["hgt"][0].replace("in", "")) <= 76 :
                    help += 1
            if re.match("#[a-fA-F0-9]{6}", self.data["hcl"][0]) :
                help += 1
            if self.data["ecl"][0] in ["amb","blu","brn","gry","grn","hzl","oth"] :
                help += 1
            if re.match("\d{9}", self.data["pid"][0]) :
                help += 1
                
            # print(help, self.data)
        return help >= 7


    def __str__(self):
        return f"byr: {self.data['byr']}"

with open(file="advent2020/p04a_data.txt", mode="r", encoding="utf-8") as filedata :
    data = filedata.read().split("\n\n")

passport_data = []
for d in data :
    passport_data.extend([d.replace("\n", " ").split(" ")])

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

people = []
for p in passport_data :
    people.append(Passport(p))

help = 0
for p in people :
    if p.validation_data() :
        help += 1
print(help)