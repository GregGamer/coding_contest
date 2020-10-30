import re
str_input = "F 1 995 F 2 884 F 3 749 F 4 866 B 1 497 B 2 442 B 3 319 B 3 374 B 4 239 B 4 433 B 5 375 B 6 177"

pattern = "[FB]\s\d*\s\d*"
elemente = re.findall(pattern, str_input)


print(elemente)

franz = []  # [995,884]
bank = []   

dayF = 0
dayB = 0

for i in range(len(elemente)) :
    if "F" in elemente[i]:
        dayF = int(elemente[i].split(" ")[1])
        franz[dayF] += int(elemente[-1])
    if "B" in elemente[i]:
        dayB = int(elemente[i].split(" ")[1])
        bank[dayB] += int(elemente[-1])

print(franz)
print(bank)