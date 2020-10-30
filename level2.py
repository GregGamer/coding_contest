def minPrice(filename, outputfile) :
    f = open("level2/"+filename, mode="r", encoding="utf-8")
    prices = []
    pricescounter = int(f.readline())
    for index in range(pricescounter) :
        # print(f.readline())
        prices.append(f.readline().replace("\n",""))

    tasks = {}
    taskscounter = int(f.readline())
    for index in range(taskscounter) :
        line = f.readline()
        tasknumber = line.split(" ")[0]
        tasks[tasknumber] = (line.split(" ")[1].replace("\n",""))

    f.close()

    f = open("level2/output/"+outputfile, mode="w", encoding="utf-8")
    f.write(f"{len(tasks)}\n")

    for key, value in tasks.items() :
        minimumPrice = 0
        minimumPriceKey = 0
        for p in range(len(prices)-int(value)+1) :
            tmpPrice = 0
            # helpPrice = []
            for i in range(int(value)) :
                tmpPrice += int(prices[i+p])
            # helpPrice.append(tmpPrice)
            if minimumPrice > tmpPrice or minimumPrice == 0 :
                minimumPriceKey = p
                minimumPrice = tmpPrice

        # print(f"{key} {minimumPriceKey}")

        f.write(f"{key} {minimumPriceKey}\n")
    f.close()




    print(tasks)







def main():

    minPrice("level.in", "output.txt")
    for i in range(1,6):
        minPrice(f"level2_{i}.in", f"ouput_{i}.txt")



if __name__ == "__main__":
    main()