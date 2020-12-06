with open("p02a_data.txt", "r") as filedata :
    data = filedata.read().split("\n")

countvalid = 0
for d in data :
    condition = d.split(": ")[0]
    condition_index1 = int(condition.split("-")[0])
    condition_index2 = int(condition.split("-")[1].split(" ")[0])
    condition_letter = condition.split(" ")[1]
    value= d.split(": ")[1]
    
    if value[condition_index1-1] == condition_letter or value[condition_index2-1] == condition_letter :
        if value[condition_index1-1] != value[condition_index2-1] :
            print(f"{d}\t{value[condition_index1-1]} {value[condition_index2-1]}")
            countvalid += 1
            

print(countvalid)