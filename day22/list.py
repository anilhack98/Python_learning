list=[45,34,50,"Anil",True,67.89,41,55,67,78,90]
print(list)
print(type(list))
print(list[0])  # Accessing the first element of the list
print(list[1])  # Accessing the second element of the list
print(list[2])  # Accessing the third element of the list
print(list[3])  # Accessing the fourth element of the list
print(list[4])  # Accessing the fifth element of the list
print(list[5])  # Accessing the sixth element of the list
print(list[6])  # Accessing the seventh element of the list
print(list[7])  # Accessing the eighth element of the list
print(list[8])  # Accessing the ninth element of the list
print(list[9])  # Accessing the tenth element of the list

# Negative Indexing
print(list[-3])
print(len(list)-3)  # This will give the same result as list[-3]

print(list)
print(list[1:8])
print(list[1:8:2])  # Slicing the list from index 1 to 7 with a step of 2

lst=[i*i for i in range(10)]
print(lst)

lst1=[i*i for i in range(10) if i%2==0]
print(lst1)