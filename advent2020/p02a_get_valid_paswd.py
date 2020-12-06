with open("p02a_data.txt", "r") as filedata :
    data = filedata.read().split("\n")

countvalid = 0
for d in data :
    condition = d.split(": ")[0]
    condition_min = int(condition.split("-")[0])
    condition_max = int(condition.split("-")[1].split(" ")[0])
    condition_letter = condition.split(" ")[1]
    value= d.split(": ")[1]
    
    if condition_min <= value.count(condition_letter) <= condition_max :
        countvalid += 1
        print(d)


print(countvalid)