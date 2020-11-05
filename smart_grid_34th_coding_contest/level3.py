LEVEL = 4


def default(filename, outputfile) :
    f = open(f"level{LEVEL}/{filename}", mode="r", encoding="utf-8")
    maxpower = int(f.readline().replace("\n",""))
    maxprice = int(f.readline().replace("\n",""))
    prices = []
    pricescounter = int(f.readline())
    for index in range(pricescounter) :
        # print(f.readline())
        prices.append({"ppm": int(f.readline().replace("\n","")), "usedPower": 0})

    tasks = {}
    taskscounter = int(f.readline())
    for index in range(taskscounter) :
        line = f.readline().replace("\n","")
        tasknumber = int(line.split(" ")[0])
        tasks[tasknumber] = []
        tasks[tasknumber].append(int(line.split(" ")[1]))
        tasks[tasknumber].append(int(line.split(" ")[2]))
        tasks[tasknumber].append(int(line.split(" ")[3]))
    tasks = dict(sorted(tasks.items(), key = lambda x: x[1][2] - x[1][1]))
    f.close()



    maxElectricityBill = 0

    f = open(f"level{LEVEL}/output/{outputfile}", mode="w", encoding="utf-8")
    f.write(f"{len(tasks)}\n")


    
    for key,value in tasks.items() :
        powertoBook = value[0]

        print(minPriceFromRange(prices, value[0], value[1]))
        


  
            
    # f.write(f"{t} {minpricekey} {tasks[str(t)][0]}\n")
    f.close()



    print(tasks)



def minPriceFromRange(prices, minRange, maxRange) :
    liste = prices[minRange:maxRange]
    for l in liste :
        if l['usedPower'] >= 5 :
            liste.remove(l)

    minValue = min(x['ppm'] for x in liste)
    return prices.index(filter(lambda n: n.get('ppm') == minValue, prices)[0])




def main():

    default(f"level{LEVEL}_example.in", "output.txt")
    # for i in range(1,6):
        # minPrice(f"level{LEVEL}_{i}.in", f"ouput_{i}.txt")



if __name__ == "__main__":
    main()