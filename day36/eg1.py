a=input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except:
    print("Invalid Input!")
print("Some lines of code")
print("End of Program") 