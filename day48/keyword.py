x=10  # Global variable

def my_function():
    global x
    x=4
    y=5  #local variable
    print(y)

my_function()
print(x)
# print(y)   #this will throw cause an error because y is a local variable and is not accessible outside the function.