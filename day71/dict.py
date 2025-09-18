class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.version=1

p=Person("Ram",34)
print(p.__dict__)