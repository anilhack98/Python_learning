class Employee:
    def __init__(self,name):
        self.name=name 
        self.raise_amt=0.03
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount is {self.raise_amt}")

emp1=Employee("Anil")
emp1.raise_amt=0.5
emp1.showDetails()

emp2=Employee("Ram")
emp2.showDetails()
# OR
# Employee.showDetails(emp1)