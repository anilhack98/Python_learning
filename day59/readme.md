# Python Decorators
-> Python decorators are a powerful and versatile that allows you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying it's source code.

-> A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often refereed to as "decorated" function. The basic syntax for using a decorator is the following:
 @decorator_function
 def my_function():
    pass                  
Note: @decorator_function notation is just a shorthand for the following code:
def my_function():
    pass
my_function=decorator_function(my_function)

Note: Decorator are often used to add functionality to function and methods, such as logging, memoization and access control.