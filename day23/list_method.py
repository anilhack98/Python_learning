l=[3,4,5,7,5,5,5]
print(l)
l.append(10)
l.sort(reverse=True)
l.reverse()
print(l.index(5))
print(l.count(5))
m=l.copy()
l.insert(1,1005) #Here 1 is index and the 1005 is value to be inserted at index 1.
s=[500,113,433]
l.extend(s)  #This method adds an entire list to the existing list.
print(l)
