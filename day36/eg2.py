try:
    num=int(input("Enter an integer:"))
    a=[1,3,4]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index out of range")