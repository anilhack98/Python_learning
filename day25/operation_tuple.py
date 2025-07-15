countries=("Nepal","India","USA")
countries1=("UK","Japan","Korea")
country=countries+countries1
print(country)

tuple=(0,1,2,3,3,4,5,6,7,8,4,4,6,4,4)
# res=tuple.count(4)
# res=tuple.index(4)
res=tuple.index(4,4,8)
print("4 is:",res)
