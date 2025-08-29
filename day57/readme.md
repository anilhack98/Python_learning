# Python Class and Object

-> A class in Python is a blueprint or a template for creating objects, providing initial values for state and implementation of behavior. The user-defined objects are created using the class keyword.

# Creating a Class:
class Details:
    name:"Ram"
    age=23

# Creating an Object
-> Object is the instance of the class used to access the properties of the class.
e.g:
class Details:
    name="rohan"
    age=33
obj1=Details()
print(obj1.name)
print(obj1.age)

# Self Parameter
-> The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.