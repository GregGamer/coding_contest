with open("advent2020/p06a_data.txt") as file :
    data = file.read().split("\n\n")

erg1 = 0
erg2 = 0
for d in data :
    group = d.split("\n")
    intersect1 = set(group[0])
    intersect2 = set(group[0])
    for person in group[1:] :
        # print(len(person), set(person))
        intersect1 = set(person).intersection(intersect1)
        intersect2 = set(person).union(intersect2)
    # print(len(intersect),intersect,"\n")
    erg1 += len(intersect1)
    erg2 += len(intersect2)
print("Ergebnis Beispiel 1:",erg2)
print("Ergebnis Beispiel 2:",erg1)
# print(erg1)