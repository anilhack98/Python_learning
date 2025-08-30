# Getters
-> Getter in Python are methods that are used to access the values of an objects properties. They are used to return the value of a specific property and are typically defined using the @property decorator.
E.g:
class MyClass:
    def __init__(self,values):
    self._value=value

    @property
    def value(self):
        return self._value


# Setters
-> It is important to note that the getter don not take any parameter and we cannot set the value through getter method. For that we need setter method which can be added by decorating method with @property_name.setter