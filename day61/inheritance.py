class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print(f"The name of Employee is {self.name} and his id is {self.id}")
class Programmer(Employee):
    def showLanguage(self):
        print("The default Language is Python")

e=Employee("Ram",205)
e.showDetails()
e1=Programmer("Hari",203)
e1.showDetails()
e1.showLanguage()