class Group():
    gid = 1
    def __init__(self, persons) :
        self.gid = Group.gid
        Group.gid += 1
        self.persons = persons
        self.len_persons = len(persons)
        self.sum_answers = "".join([x.data for x in self.persons])
        self.unique_answers = {x for x in self.sum_answers}
        self.len_unique_answers = len(self.unique_answers)
        

    def __repr__(self) :
        return f"\nGroup {self.gid}: {self.len_unique_answers} \t {self.persons}"


class Person() :
    def __init__(self, form_data) :
        self.data = form_data

    def __repr__(self) :
        return f"Data: {self.data}"
    
with open("advent2020/p06a_data.txt") as file :
    data = file.read().split("\n\n")

groups = []
for d in data :
    persons = []
    for person_data in d.split("\n") :
        persons.append(Person(person_data))
    groups.append(Group(persons))

print(sum([x.len_unique_answers for x in groups]))
print(sum([x.len_answer_intersection for x in groups]))