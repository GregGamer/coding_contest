with open(file="advent2020/p03a_data.txt") as file :
    data = file.read().split("\n")

# rulenumber: [steps_right, steps_down, position_y0, position_x0, trees]
slopes = {  1: [1,1,0,0,0], 
            2: [3,1,0,0,0], 
            3: [5,1,0,0,0], 
            4: [7,1,0,0,0], 
            5: [1,2,0,0,0], }

helper = 0
while helper < len(slopes) :
    helper = 0
    for key, value in slopes.items() :
        value[2] += value[1]
        value[3] += value[0]
        if value[2] < len(data) :
           if data[value[2]][value[3]%len(data[0])] == "#":
               value[4] += 1
            #    print(key, value[2],value[3])

        if value[2] > len(data) :
            helper += 1
            # print(key, value[2], helper)
erg = 1
for s in slopes.values() :
    erg *= s[4]

print(erg)
print(slopes[3])