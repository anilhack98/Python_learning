tup =(1,3,5,6,7,"green","Anil",342)  #if only (1) it shows int but if (1,) it shows tuple
# tup[0]=60  # if we make list [] then we can change the index 0 to 60 but not in case of tuple
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])

if 342 in tup:
    print("Yes 342 is present in the tuple")
else:
    print("It is not present")

tup2=tup[1:5]
print(tup2)