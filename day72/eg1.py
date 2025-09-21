class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programmer:
    def __init__(self,name,id,lang):
        self.name=name
        self.id=id
        # OR
        # super().__init__(name,id) #instead of above two
        self.lang=lang
ram=Employee("Ram sah","3432")
Hari=Programmer("Hari Das","4343","Java")
print(Hari.lang)
        