def func():
    try:
        l=[1,2,3,4]
        i=int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Invalid index")
        return 0
    finally:
        print("Function executed")

x=func()
print(x)