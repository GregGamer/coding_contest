with open("advent2020/p06a_data.txt") as file :
    data = file.read().split("\n\n")

erg = 0
for d in data :
    group = d.split("\n")
    intersect = set(group[0])
    for person in group[1:] :
        print(len(person), set(person))
        intersect = set(person).intersection(intersect)
    print(len(intersect),intersect,"\n")
    erg += len(intersect)
print(erg)