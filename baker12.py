import re
str_input = "F 1 995 F 2 884 F 3 749 F 4 866 B 1 497 B 2 442 B 3 319 B 3 374 B 4 239 B 4 433 B 5 375 B 6 177"


pattern = "[FB]\s\d*\s\d*"










bank = {}
franz = {}

for i in re.findall(pattern, str_input) :
    if "F" in i :
        franz[i] += i.split(" ")[-1]
    if "B" in i :
        bank[i] += i.split(" ")[-1]

print(franz)
print(bank)

betrug = []   # [1, 2]

for i in range(len(franz)) :
    if franz[str(i+1)] != bank[str(i+1)] :
        betrug.append(str(i+1))

print(" ".join(betrug))