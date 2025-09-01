class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"The name of Employee is {self.name} and his id is {self.id}")

e=Employee("Ram",205)
e.showDetails()