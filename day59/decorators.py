def greet(fx):
    def mfx(*args, **kwargs):  # *args=takes argument as tuples and **kwargs= takes argument as dictionary in key value pair
        print("Good Morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx
@greet
def hello():
    print("Hello World")

def add(a,b):
    print(a+b)
hello()
add(1,4)