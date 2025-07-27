marks=[12,45,66,35,77,60,89]

index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Anil, awsome!")
#     index +=1

    #Next Method
for index, mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("Anil, awsome!")