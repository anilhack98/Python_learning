l=[1,2,4,6,4,3]
def filter_function(a):
    return a>2
newl=list(filter(filter_function,l))
print(newl)