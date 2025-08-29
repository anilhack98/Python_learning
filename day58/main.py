class Person:
    def __init__(self,n,o):
       # print("Hey I am a Person")
        self.name=n
        self.occ=o

    def info(self):
        print(f"{self.name} is a {self.occ}")
a=Person("Ram","Accountant")
b=Person("Rohan","Teacher")
a.info()
b.info()