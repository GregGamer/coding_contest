class Passport():
    def __init__(self, data):
        # erstellen und befüllen des data dictionaries 
        self.data = {}
        for i,k in enumerate(keys) :
            self.data[k] = [x.split(":")[1] for x in data if keys[i] in x]

    # check if data is valid, returns bool
    def valid(self):
        help = 0
        # check if field is empty
        for d in self.data.values() :
            if d != [] :
                help += 1

        return help >= 7

    def __str__(self):
        return f"byr: {self.data['byr']}"

    def uselessFunction(self):
        return f"useless"

# Daten laden und aufbereitung
with open(file="advent2020/p04a_data.txt", mode="r", encoding="utf-8") as filedata :
    data = filedata.read().split("\n\n")
passport_data = []
for d in data :
    passport_data.extend([d.replace("\n", " ").split(" ")])


# cid ist optional, also hab ichs auch nicht drinnen
keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# liste mit Passport Objekten
people = []
for p in passport_data :
    people.append(Passport(p))

help = 0
for p in people :
    if p.valid() :
        help += 1
    # print(p.valid())
print(help)

# print(sorted(keys))
