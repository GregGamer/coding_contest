from tqdm import tqdm
with open("p01a_data.txt") as file :
    data = list(map(int,file.read().split("\n")))

print(data)


for a in tqdm(data) :
    for b in data :
        for c in data :
            if a+b+c == 2020 :
                sum = a*b*c
                
print(sum)
        