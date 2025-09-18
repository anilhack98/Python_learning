class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p=Person("Ram",35)
print(p.__dict__)
print(help(Person))