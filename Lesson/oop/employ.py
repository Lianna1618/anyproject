from faker import Faker


fake = Faker()


class Person:
    def __init__(self, id, name, surname, birth_number, pasport):
        self.id = id
        self.name = name
        self.age = birth_number
        self.surname = surname
        self.pasport = pasport


p1 = Person(
    fake.random_number(digits=3),
    fake.first_name(),
    fake.last_name(),
    fake.random_number(digits=2),
    fake.random_number(digits=9),
)

print(p1.__dict__.values())


class Employee(Person):
    def __init__(
            self, id, name, surname, birth_number,
            pasport, salary, accsess, position
            ):
        super().__init__(id, name, surname, birth_number, pasport)
        self.salary = salary
        self.accsess = accsess
        self.position = position

    def Accouning(self):
        pass

    def HR(self):
        pass

    def Marketing(self):
        pass


p2 = Employee(
    fake.random_number(digits=3),
    fake.first_name(),
    fake.last_name(),
    fake.random_number(digits=2),
    fake.random_number(digits=9),
    fake.random_number(digits=5),
    fake.random_number(digits=1),
    fake.job()
)


print(p2.__dict__.values())
