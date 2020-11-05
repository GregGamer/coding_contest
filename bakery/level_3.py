inputstring = "F 1 200 F 2 170 B 1 100 B 2 80 B 2 15 B 2 100 B 3 70"

class Konto() :
    def __init__(self) :
        self.kontostand_on_day = {}
        self.money = 0

    def addMoney(self, day, money) :
        self.money += money
        self.kontostand_on_day[day] = (money, self.money)

    def einzahlen(self, day, money, other) :
        self.money -= money
        other.kontostand_on_day[day] = (money, self.money)
        self.kontostand_on_day[day] = (money, self.money)



def main() :
    f = Konto()
    b = Konto()



    print(f.kontostand_on_day)


    print(f.kontostand_on_day)
    


if __name__ == "__main__":
    main()