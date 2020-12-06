with open(file="p03a_data.txt") as file :
    data = file.read().split("\n")

trees = 0
left = 0
for d in data[1:] :
    left += 3
    # print(d[left%len(d)], d)
    if d[left%len(d)] == "#" :
        trees += 1

print(trees)        