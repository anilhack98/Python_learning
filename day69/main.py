class Employee:
    company="Samsung"
    def show(self):
        print(f"The name is {self.name} and Company is {self.company}")

    @classmethod 
    def changeCompany(cls,newCompany):
        cls.company=newCompany

e1=Employee()
e1.name="Ram"
e1.show()
e1.changeCompany("Apple")
e1.show()
print(Employee.company)