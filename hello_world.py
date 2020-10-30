class Person():
    def __init__(self, name, bday):
        self.name = name
        self.bday = bday

    def getAge(self):
        return self.bday

    def __repr__(self):
        return f"Name: {self.name}, bday: {self.bday}"


p1 = Person("Gregor", "15.11.1998")

print(type(p1.bday))


personen = []

for p in range(12) :  # [0,1,2,3,4,5,6,7,8,...,11]
    personen.append(Person(f"person{p}",f"12.{p+1}.2000"))

print(personen)