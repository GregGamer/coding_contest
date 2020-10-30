def minPrice(filename, outputfile) :
    f = open("level1/"+filename, mode="r", encoding="utf-8")
    prices = []
    for line in f :
        prices.append(line.replace("\n", ""))
    f.close()
    prices.pop(0)


    minimumprice = 100000000
    keyminimumprice = -1

    # print(price)

    for i in range(len(prices)) :
        if minimumprice > int(prices[i]) :
            minimumprice = int(prices[i])
            keyminimumprice = i
        


    f = open("level1/output/"+outputfile, mode="w", encoding="utf-8")
    f.write(str(keyminimumprice))
    f.close()


    print(f"{keyminimumprice}: {minimumprice}")



def main():

    for i in range(1,6):
        minPrice(f"level1_{i}.in", f"ouput_{i}.txt")



if __name__ == "__main__":
    main()