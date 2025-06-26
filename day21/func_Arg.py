# Default arguments in functions
def average(a=10,b=10):
    print("Average is", (a+b)/2)
average()

#keyword arguments in functions
average(b=20,a=30)  #In this case, the order of arguments does not matter because we are using keyword arguments.

#Required arguments in functions
def add(c,d=45):
    print("Sum is", c+d)
add(10)

# Another example
def average(*numbers):  # The asterisk * before numbers means that all the arguments passed will be collected into a tuple named numbers.
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is", sum/len(numbers))
average(10,20,30,40)  # Here we can pass any number

# example
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)  # The return statement is used to return the value of the expression  back to the calling function.
c=average(10,20,30,40)
print(c)