class Person:
    name="Ram"
    occupation="Teacher"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person()
b=Person()
a.name="Hari"
a.occupation="Driver"
# print(a.name, a.occupation)

b.name="Rahul"
b.occupation="Accountant"

a.info()
b.info()
