class ParentClass:
    def parent_method(self):
        print("This is parent method")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child class method")
        super().parent_method()

child_object=ChildClass()
child_object.child_method()
child_object.parent_method()