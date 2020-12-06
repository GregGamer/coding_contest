with open("p01a_data.txt") as file :
    data = list(map(int,file.read().split("\n")))

print(data)

for i,d in enumerate(data) :
    compliment = 2020 - d
    if compliment in data[i:] :
        print(d * compliment)
        break